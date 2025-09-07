"""Database models and operations for k8s inventory storage."""

import sqlite3
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from contextlib import contextmanager

class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder that handles datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def convert_datetime_in_dict(obj, depth=0, max_depth=10):
    """Recursively convert datetime objects to strings in nested data structures.
    
    Args:
        obj: The object to convert datetime objects in
        depth: Current recursion depth
        max_depth: Maximum recursion depth to prevent infinite loops
    
    Returns:
        Object with all datetime objects converted to ISO format strings
    """
    if depth > max_depth:
        return obj
    
    if isinstance(obj, datetime):
        return obj.isoformat()
    
    if isinstance(obj, dict):
        return {k: convert_datetime_in_dict(v, depth + 1, max_depth) for k, v in obj.items()}
    
    if isinstance(obj, list):
        return [convert_datetime_in_dict(item, depth + 1, max_depth) for item in obj]
    
    return obj

from .models import CRD, Operator, ClusterServiceVersion

logger = logging.getLogger(__name__)


@dataclass
class InventorySnapshot:
    """Represents a complete inventory snapshot."""
    id: Optional[int]
    timestamp: str
    cluster_context: str
    cluster_info: str  # JSON
    crd_count: int
    operator_count: int
    csv_count: int
    namespace_filter: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class DatabaseManager:
    """Manages SQLite database operations for k8s inventory data."""
    
    # Database schema version for migrations
    SCHEMA_VERSION = 2
    
    def __init__(self, db_path: Optional[str] = None):
        """Initialize database manager.
        
        Args:
            db_path: Path to SQLite database file. If None, uses default location.
        """
        if db_path:
            self.db_path = Path(db_path)
        else:
            # Default to user's home directory
            home = Path.home()
            self.db_path = home / ".k8s-inventory" / "inventory.db"
        
        # Ensure directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self._initialize_database()
        
        # Handle migrations if needed
        self._handle_migrations()

    @contextmanager
    def get_connection(self):
        """Get database connection with proper error handling."""
        conn = None
        try:
            conn = sqlite3.connect(str(self.db_path))
            conn.row_factory = sqlite3.Row  # Enable dict-like access
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def _initialize_database(self):
        """Initialize database with required tables."""
        with self.get_connection() as conn:
            # Create metadata table for schema versioning
            conn.execute("""
                CREATE TABLE IF NOT EXISTS db_metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            """)
            
            # Create snapshots table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS inventory_snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    cluster_context TEXT NOT NULL,
                    cluster_info TEXT,
                    crd_count INTEGER DEFAULT 0,
                    operator_count INTEGER DEFAULT 0,
                    csv_count INTEGER DEFAULT 0,
                    namespace_filter TEXT,
                    notes TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create CRDs table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS crds (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    snapshot_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    group_name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    plural TEXT NOT NULL,
                    singular TEXT NOT NULL,
                    scope TEXT NOT NULL,
                    creation_timestamp TEXT,
                    labels TEXT,
                    annotations TEXT,
                    served_versions TEXT,
                    stored_version TEXT,
                    categories TEXT,
                    short_names TEXT,
                    instance_count INTEGER DEFAULT 0,
                    spec TEXT,
                    FOREIGN KEY (snapshot_id) REFERENCES inventory_snapshots (id)
                )
            """)
            
            # Create operators table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS operators (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    snapshot_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    namespace TEXT NOT NULL,
                    operator_type TEXT NOT NULL,
                    image TEXT,
                    version TEXT,
                    creation_timestamp TEXT,
                    labels TEXT,
                    annotations TEXT,
                    replicas INTEGER DEFAULT 0,
                    ready_replicas INTEGER DEFAULT 0,
                    conditions TEXT,
                    managed_crds TEXT,
                    managed_resources TEXT,
                    operator_framework TEXT,
                    spec TEXT,
                    FOREIGN KEY (snapshot_id) REFERENCES inventory_snapshots (id)
                )
            """)
            
            # Create CSVs table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS csvs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    snapshot_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    namespace TEXT NOT NULL,
                    display_name TEXT,
                    version TEXT,
                    phase TEXT,
                    description TEXT,
                    provider TEXT,
                    install_strategy TEXT,
                    creation_timestamp TEXT,
                    labels TEXT,
                    annotations TEXT,
                    owned_crds TEXT,
                    required_crds TEXT,
                    permissions TEXT,
                    cluster_permissions TEXT,
                    replaces TEXT,
                    skips TEXT,
                    min_kube_version TEXT,
                    spec TEXT,
                    FOREIGN KEY (snapshot_id) REFERENCES inventory_snapshots (id)
                )
            """)
            
            # Create indexes for better query performance
            conn.execute("CREATE INDEX IF NOT EXISTS idx_snapshots_timestamp ON inventory_snapshots (timestamp)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_snapshots_context ON inventory_snapshots (cluster_context)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_crds_snapshot ON crds (snapshot_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_crds_name ON crds (name)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_operators_snapshot ON operators (snapshot_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_operators_name ON operators (name)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_csvs_snapshot ON csvs (snapshot_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_csvs_name ON csvs (name)")
            
            # Set schema version
            conn.execute("INSERT OR REPLACE INTO db_metadata (key, value) VALUES (?, ?)",
                        ("schema_version", str(self.SCHEMA_VERSION)))
            
            conn.commit()

    def _handle_migrations(self):
        """Handle database schema migrations."""
        with self.get_connection() as conn:
            # Get current schema version
            cursor = conn.execute(
                "SELECT value FROM db_metadata WHERE key = 'schema_version'"
            )
            result = cursor.fetchone()
            current_version = int(result['value']) if result else 1
            
            # Apply migrations if needed
            if current_version < 2:
                self._migrate_to_version_2(conn)
                logger.info("Database migrated to schema version 2")
            
            # Update schema version
            conn.execute(
                "INSERT OR REPLACE INTO db_metadata (key, value) VALUES (?, ?)",
                ("schema_version", str(self.SCHEMA_VERSION))
            )
            conn.commit()
    
    def _migrate_to_version_2(self, conn):
        """Migrate database from version 1 to version 2 (add spec columns)."""
        try:
            # Add spec column to crds table if it doesn't exist
            conn.execute("ALTER TABLE crds ADD COLUMN spec TEXT")
        except sqlite3.OperationalError:
            # Column already exists, ignore
            pass
        
        try:
            # Add spec column to operators table if it doesn't exist
            conn.execute("ALTER TABLE operators ADD COLUMN spec TEXT")
        except sqlite3.OperationalError:
            # Column already exists, ignore
            pass
        
        try:
            # Add spec column to csvs table if it doesn't exist
            conn.execute("ALTER TABLE csvs ADD COLUMN spec TEXT")
        except sqlite3.OperationalError:
            # Column already exists, ignore
            pass

    def store_inventory_snapshot(self,
                                cluster_context: str,
                                cluster_info: Dict[str, Any],
                                crds: List[CRD] = None,
                                operators: List[Operator] = None,
                                csvs: List[ClusterServiceVersion] = None,
                                namespace_filter: Optional[str] = None,
                                notes: Optional[str] = None) -> int:
        """Store a complete inventory snapshot.
        
        Args:
            cluster_context: Kubernetes context name
            cluster_info: Cluster information dictionary
            crds: List of CRD information
            operators: List of operator information
            csvs: List of CSV information
            namespace_filter: Namespace filter used (if any)
            notes: Optional notes for this snapshot
            
        Returns:
            Snapshot ID
        """
        crds = crds or []
        operators = operators or []
        csvs = csvs or []
        
        with self.get_connection() as conn:
            # Create snapshot record
            cursor = conn.execute("""
                INSERT INTO inventory_snapshots 
                (timestamp, cluster_context, cluster_info, crd_count, operator_count, csv_count, namespace_filter, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                datetime.utcnow().isoformat(),
                cluster_context,
                json.dumps(cluster_info, cls=DateTimeEncoder),
                len(crds),
                len(operators),
                len(csvs),
                namespace_filter,
                notes
            ))
            
            snapshot_id = cursor.lastrowid
            
            # Store CRDs
            for crd in crds:
                try:
                    # Convert datetime objects in spec before JSON serialization
                    crd_spec_converted = convert_datetime_in_dict(crd.spec) if crd.spec else None
                    
                    conn.execute("""
                        INSERT INTO crds (
                            snapshot_id, name, group_name, version, kind, plural, singular, scope,
                            creation_timestamp, labels, annotations, served_versions, stored_version,
                            categories, short_names, instance_count, spec
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        snapshot_id, crd.name, crd.group, crd.version, crd.kind, crd.plural,
                        crd.singular, crd.scope, crd.creation_timestamp,
                        json.dumps(crd.labels, cls=DateTimeEncoder), json.dumps(crd.annotations, cls=DateTimeEncoder),
                        json.dumps(crd.served_versions, cls=DateTimeEncoder), crd.stored_version,
                        json.dumps(crd.categories, cls=DateTimeEncoder), json.dumps(crd.short_names, cls=DateTimeEncoder),
                        crd.instance_count, json.dumps(crd_spec_converted, cls=DateTimeEncoder)
                    ))
                except Exception as e:
                    logger.error(f"Failed to store CRD {crd.name}: {e}")
                    logger.debug(f"CRD spec type: {type(crd.spec)}, content: {str(crd.spec)[:200]}...")
                    raise
            
            # Store Operators
            for operator in operators:
                try:
                    # Convert datetime objects in spec and conditions before JSON serialization
                    operator_spec_converted = convert_datetime_in_dict(operator.spec) if operator.spec else None
                    operator_conditions_converted = convert_datetime_in_dict(operator.conditions) if operator.conditions else []
                    
                    conn.execute("""
                        INSERT INTO operators (
                            snapshot_id, name, namespace, operator_type, image, version,
                            creation_timestamp, labels, annotations, replicas, ready_replicas,
                            conditions, managed_crds, managed_resources, operator_framework, spec
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        snapshot_id, operator.name, operator.namespace, operator.operator_type,
                        operator.image, operator.version, operator.creation_timestamp,
                        json.dumps(operator.labels, cls=DateTimeEncoder), json.dumps(operator.annotations, cls=DateTimeEncoder),
                        operator.replicas, operator.ready_replicas,
                        json.dumps(operator_conditions_converted, cls=DateTimeEncoder), json.dumps(operator.managed_crds, cls=DateTimeEncoder),
                        json.dumps(operator.managed_resources, cls=DateTimeEncoder), operator.operator_framework,
                        json.dumps(operator_spec_converted, cls=DateTimeEncoder)
                    ))
                except Exception as e:
                    logger.error(f"Failed to store operator {operator.name}: {e}")
                    logger.debug(f"Operator spec type: {type(operator.spec)}, content: {str(operator.spec)[:200]}...")
                    raise
            
            # Store CSVs
            for csv in csvs:
                try:
                    # Convert datetime objects in spec before JSON serialization
                    csv_spec_converted = convert_datetime_in_dict(csv.spec) if csv.spec else None
                    
                    conn.execute("""
                        INSERT INTO csvs (
                            snapshot_id, name, namespace, display_name, version, phase, description,
                            provider, install_strategy, creation_timestamp, labels, annotations,
                            owned_crds, required_crds, permissions, cluster_permissions,
                            replaces, skips, min_kube_version, spec
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        snapshot_id, csv.name, csv.namespace, csv.display_name, csv.version,
                        csv.phase, csv.description, csv.provider, csv.install_strategy,
                        csv.creation_timestamp, json.dumps(csv.labels, cls=DateTimeEncoder), json.dumps(csv.annotations, cls=DateTimeEncoder),
                        json.dumps(csv.owned_crds, cls=DateTimeEncoder), json.dumps(csv.required_crds, cls=DateTimeEncoder),
                        json.dumps(csv.permissions, cls=DateTimeEncoder), json.dumps(csv.cluster_permissions, cls=DateTimeEncoder),
                        csv.replaces, json.dumps(csv.skips, cls=DateTimeEncoder), csv.min_kube_version,
                        json.dumps(csv_spec_converted, cls=DateTimeEncoder)
                    ))
                except Exception as e:
                    logger.error(f"Failed to store CSV {csv.name}: {e}")
                    logger.debug(f"CSV spec type: {type(csv.spec)}, content: {str(csv.spec)[:200]}...")
                    raise
            
            conn.commit()
            logger.info(f"Stored inventory snapshot {snapshot_id} with {len(crds)} CRDs, "
                       f"{len(operators)} operators, {len(csvs)} CSVs")
            
            return snapshot_id

    def list_snapshots(self, 
                      cluster_context: Optional[str] = None,
                      limit: Optional[int] = None) -> List[InventorySnapshot]:
        """List inventory snapshots.
        
        Args:
            cluster_context: Filter by cluster context
            limit: Maximum number of snapshots to return
            
        Returns:
            List of inventory snapshots
        """
        with self.get_connection() as conn:
            query = "SELECT * FROM inventory_snapshots"
            params = []
            
            if cluster_context:
                query += " WHERE cluster_context = ?"
                params.append(cluster_context)
            
            query += " ORDER BY timestamp DESC"
            
            if limit:
                query += " LIMIT ?"
                params.append(limit)
            
            cursor = conn.execute(query, params)
            snapshots = []
            
            for row in cursor.fetchall():
                snapshot = InventorySnapshot(
                    id=row['id'],
                    timestamp=row['timestamp'],
                    cluster_context=row['cluster_context'],
                    cluster_info=row['cluster_info'],
                    crd_count=row['crd_count'],
                    operator_count=row['operator_count'],
                    csv_count=row['csv_count'],
                    namespace_filter=row['namespace_filter'],
                    notes=row['notes']
                )
                snapshots.append(snapshot)
            
            return snapshots

    def get_snapshot_data(self, snapshot_id: int) -> Dict[str, Any]:
        """Get complete data for a specific snapshot.
        
        Args:
            snapshot_id: Snapshot ID
            
        Returns:
            Dictionary containing all snapshot data
        """
        with self.get_connection() as conn:
            # Get snapshot info
            cursor = conn.execute("SELECT * FROM inventory_snapshots WHERE id = ?", (snapshot_id,))
            snapshot_row = cursor.fetchone()
            
            if not snapshot_row:
                raise ValueError(f"Snapshot {snapshot_id} not found")
            
            # Get CRDs
            cursor = conn.execute("SELECT * FROM crds WHERE snapshot_id = ?", (snapshot_id,))
            crds = [dict(row) for row in cursor.fetchall()]
            
            # Get Operators
            cursor = conn.execute("SELECT * FROM operators WHERE snapshot_id = ?", (snapshot_id,))
            operators = [dict(row) for row in cursor.fetchall()]
            
            # Get CSVs
            cursor = conn.execute("SELECT * FROM csvs WHERE snapshot_id = ?", (snapshot_id,))
            csvs = [dict(row) for row in cursor.fetchall()]
            
            return {
                'snapshot': dict(snapshot_row),
                'crds': crds,
                'operators': operators,
                'csvs': csvs
            }

    def delete_snapshot(self, snapshot_id: int) -> bool:
        """Delete a snapshot and all its associated data.
        
        Args:
            snapshot_id: Snapshot ID to delete
            
        Returns:
            True if snapshot was deleted, False if not found
        """
        with self.get_connection() as conn:
            # Check if snapshot exists
            cursor = conn.execute("SELECT COUNT(*) FROM inventory_snapshots WHERE id = ?", (snapshot_id,))
            if cursor.fetchone()[0] == 0:
                return False
            
            # Delete associated data (foreign key constraints should handle this)
            conn.execute("DELETE FROM csvs WHERE snapshot_id = ?", (snapshot_id,))
            conn.execute("DELETE FROM operators WHERE snapshot_id = ?", (snapshot_id,))
            conn.execute("DELETE FROM crds WHERE snapshot_id = ?", (snapshot_id,))
            conn.execute("DELETE FROM inventory_snapshots WHERE id = ?", (snapshot_id,))
            
            conn.commit()
            logger.info(f"Deleted snapshot {snapshot_id}")
            return True

    def get_database_stats(self) -> Dict[str, Any]:
        """Get database statistics.
        
        Returns:
            Dictionary with database statistics
        """
        with self.get_connection() as conn:
            stats = {}
            
            # Count tables
            cursor = conn.execute("SELECT COUNT(*) FROM inventory_snapshots")
            stats['total_snapshots'] = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT COUNT(*) FROM crds")
            stats['total_crds'] = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT COUNT(*) FROM operators")
            stats['total_operators'] = cursor.fetchone()[0]
            
            cursor = conn.execute("SELECT COUNT(*) FROM csvs")
            stats['total_csvs'] = cursor.fetchone()[0]
            
            # Get unique cluster contexts
            cursor = conn.execute("SELECT DISTINCT cluster_context FROM inventory_snapshots")
            stats['cluster_contexts'] = [row[0] for row in cursor.fetchall()]
            
            # Get date range
            cursor = conn.execute("""
                SELECT MIN(timestamp) as oldest, MAX(timestamp) as newest 
                FROM inventory_snapshots
            """)
            date_row = cursor.fetchone()
            stats['oldest_snapshot'] = date_row[0]
            stats['newest_snapshot'] = date_row[1]
            
            # Database file size
            stats['db_file_size'] = self.db_path.stat().st_size if self.db_path.exists() else 0
            stats['db_path'] = str(self.db_path)
            
            return stats

    def cleanup_old_snapshots(self, keep_count: int = 10, cluster_context: Optional[str] = None) -> int:
        """Clean up old snapshots, keeping only the most recent ones.
        
        Args:
            keep_count: Number of snapshots to keep per cluster
            cluster_context: Specific cluster context to clean (None for all)
            
        Returns:
            Number of snapshots deleted
        """
        deleted_count = 0
        
        with self.get_connection() as conn:
            if cluster_context:
                contexts = [cluster_context]
            else:
                cursor = conn.execute("SELECT DISTINCT cluster_context FROM inventory_snapshots")
                contexts = [row[0] for row in cursor.fetchall()]
            
            for context in contexts:
                # Get snapshots to delete (keeping the most recent ones)
                cursor = conn.execute("""
                    SELECT id FROM inventory_snapshots 
                    WHERE cluster_context = ?
                    ORDER BY timestamp DESC 
                    LIMIT -1 OFFSET ?
                """, (context, keep_count))
                
                snapshot_ids = [row[0] for row in cursor.fetchall()]
                
                for snapshot_id in snapshot_ids:
                    if self.delete_snapshot(snapshot_id):
                        deleted_count += 1
        
        logger.info(f"Cleaned up {deleted_count} old snapshots")
        return deleted_count
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        # Nothing to do as we use connection contexts per operation
        pass
