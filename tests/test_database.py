"""Unit tests for database functionality."""

import pytest
import tempfile
import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

from k8s_inventory_cli.core.database import DatabaseManager, InventorySnapshot
from k8s_inventory_cli.core.models import CRD, Operator, ClusterServiceVersion


class TestDatabaseManager:
    """Test cases for DatabaseManager."""

    def test_init_creates_database(self):
        """Test that DatabaseManager creates database and tables."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            assert os.path.exists(db_path)
            
            # Check that tables exist
            with db_manager.get_connection() as conn:
                cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = [row[0] for row in cursor.fetchall()]
            
            expected_tables = {'inventory_snapshots', 'crds', 'operators', 'csvs'}
            assert expected_tables.issubset(set(tables))

    def test_init_with_none_path_uses_default(self):
        """Test that DatabaseManager uses default path when None is provided."""
        with patch('k8s_inventory_cli.core.database.Path.home') as mock_home:
            mock_home.return_value = Path("/mock/home")
            
            with patch('os.makedirs') as mock_makedirs:
                with patch('sqlite3.connect') as mock_connect:
                    mock_connect.return_value.cursor.return_value.fetchone.return_value = None
                    
                    db_manager = DatabaseManager(None)
                    
                    expected_path = "/mock/home/.k8s-inventory/inventory.db"
                    mock_makedirs.assert_called_once_with("/mock/home/.k8s-inventory", exist_ok=True)
                    mock_connect.assert_called_once_with(expected_path)

    def test_store_inventory_snapshot(self):
        """Test storing an inventory snapshot."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Create test data
            crd = CRD(
                name="test-crd.example.com",
                group="example.com",
                version="v1",
                kind="TestResource",
                plural="testresources",
                singular="testresource",
                scope="Namespaced"
            )
            
            operator = Operator(
                name="test-operator",
                namespace="test-namespace",
                operator_framework="CustomFramework"
            )
            
            csv = ClusterServiceVersion(
                name="test-csv",
                namespace="test-namespace",
                display_name="Test CSV",
                version="1.0.0",
                phase="Succeeded"
            )
            
            # Store snapshot
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[crd],
                operators=[operator],
                csvs=[csv],
                namespace_filter="test-namespace",
                notes="Test snapshot"
            )
            
            assert snapshot_id is not None
            assert snapshot_id > 0
            
            # Verify data was stored
            with db_manager.get_connection() as conn:
                cursor = conn.execute("SELECT COUNT(*) FROM inventory_snapshots WHERE id = ?", (snapshot_id,))
                assert cursor.fetchone()[0] == 1
                
                cursor = conn.execute("SELECT COUNT(*) FROM crds WHERE snapshot_id = ?", (snapshot_id,))
                assert cursor.fetchone()[0] == 1
                
                cursor = conn.execute("SELECT COUNT(*) FROM operators WHERE snapshot_id = ?", (snapshot_id,))
                assert cursor.fetchone()[0] == 1
                
                cursor = conn.execute("SELECT COUNT(*) FROM csvs WHERE snapshot_id = ?", (snapshot_id,))
                assert cursor.fetchone()[0] == 1

    def test_list_snapshots(self):
        """Test listing inventory snapshots."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Store multiple snapshots
            snapshot1_id = db_manager.store_inventory_snapshot(
                cluster_context="context1",
                cluster_info={"version": "1.21.0"},
                crds=[],
                operators=[],
                csvs=[],
                notes="First snapshot"
            )
            
            snapshot2_id = db_manager.store_inventory_snapshot(
                cluster_context="context2",
                cluster_info={"version": "1.22.0"},
                crds=[],
                operators=[],
                csvs=[],
                notes="Second snapshot"
            )
            
            # List all snapshots
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 2
            
            # List with cluster context filter
            snapshots = db_manager.list_snapshots(cluster_context="context1")
            assert len(snapshots) == 1
            assert snapshots[0].cluster_context == "context1"
            
            # List with limit
            snapshots = db_manager.list_snapshots(limit=1)
            assert len(snapshots) == 1

    def test_get_snapshot_data(self):
        """Test retrieving snapshot data."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Create test data
            crd = CRD(
                name="test-crd.example.com",
                group="example.com",
                version="v1",
                kind="TestResource",
                plural="testresources",
                singular="testresource",
                scope="Namespaced"
            )
            
            # Store snapshot
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[crd],
                operators=[],
                csvs=[],
                notes="Test snapshot"
            )
            
            # Retrieve snapshot data
            data = db_manager.get_snapshot_data(snapshot_id)
            
            assert data['snapshot']['id'] == snapshot_id
            assert data['snapshot']['cluster_context'] == "test-context"
            assert data['snapshot']['notes'] == "Test snapshot"
            assert len(data['crds']) == 1
            assert data['crds'][0]['name'] == "test-crd.example.com"
            assert len(data['operators']) == 0
            assert len(data['csvs']) == 0

    def test_get_snapshot_data_nonexistent(self):
        """Test retrieving data for non-existent snapshot."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            with pytest.raises(ValueError, match="Snapshot 999 not found"):
                db_manager.get_snapshot_data(999)

    def test_delete_snapshot(self):
        """Test deleting a snapshot."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Store snapshot
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[],
                operators=[],
                csvs=[],
                notes="Test snapshot"
            )
            
            # Delete snapshot
            result = db_manager.delete_snapshot(snapshot_id)
            assert result is True
            
            # Verify deletion
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 0
            
            # Try to delete non-existent snapshot
            result = db_manager.delete_snapshot(999)
            assert result is False

    def test_get_database_stats(self):
        """Test getting database statistics."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Store some test data
            crd = CRD(
                name="test-crd.example.com",
                group="example.com",
                version="v1",
                kind="TestResource",
                plural="testresources",
                singular="testresource",
                scope="Namespaced"
            )
            
            operator = Operator(
                name="test-operator",
                namespace="test-namespace",
                operator_framework="CustomFramework"
            )
            
            db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[crd],
                operators=[operator],
                csvs=[],
                notes="Test snapshot"
            )
            
            # Get stats
            stats = db_manager.get_database_stats()
            
            assert stats['db_path'] == db_path
            assert stats['db_file_size'] > 0
            assert stats['total_snapshots'] == 1
            assert stats['total_crds'] == 1
            assert stats['total_operators'] == 1
            assert stats['total_csvs'] == 0
            assert 'test-context' in stats['cluster_contexts']
            assert stats['oldest_snapshot'] is not None
            assert stats['newest_snapshot'] is not None

    def test_cleanup_old_snapshots(self):
        """Test cleaning up old snapshots."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Store multiple snapshots
            for i in range(5):
                db_manager.store_inventory_snapshot(
                    cluster_context="test-context",
                    cluster_info={"version": "1.21.0"},
                    crds=[],
                    operators=[],
                    csvs=[],
                    notes=f"Snapshot {i}"
                )
            
            # Cleanup keeping only 2 most recent
            deleted_count = db_manager.cleanup_old_snapshots(keep_count=2)
            
            assert deleted_count == 3
            
            # Verify only 2 snapshots remain
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 2

    def test_cleanup_old_snapshots_with_context_filter(self):
        """Test cleaning up old snapshots with cluster context filter."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Store snapshots for different contexts
            for i in range(3):
                db_manager.store_inventory_snapshot(
                    cluster_context="context1",
                    cluster_info={"version": "1.21.0"},
                    crds=[],
                    operators=[],
                    csvs=[],
                    notes=f"Context1 Snapshot {i}"
                )
            
            for i in range(2):
                db_manager.store_inventory_snapshot(
                    cluster_context="context2",
                    cluster_info={"version": "1.21.0"},
                    crds=[],
                    operators=[],
                    csvs=[],
                    notes=f"Context2 Snapshot {i}"
                )
            
            # Cleanup context1 keeping only 1
            deleted_count = db_manager.cleanup_old_snapshots(
                keep_count=1, 
                cluster_context="context1"
            )
            
            assert deleted_count == 2
            
            # Verify total snapshots (1 from context1 + 2 from context2)
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 3
            
            # Verify context1 has only 1 snapshot
            context1_snapshots = db_manager.list_snapshots(cluster_context="context1")
            assert len(context1_snapshots) == 1

    def test_context_manager(self):
        """Test using DatabaseManager as a context manager."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            with DatabaseManager(db_path) as db_manager:
                snapshot_id = db_manager.store_inventory_snapshot(
                    cluster_context="test-context",
                    cluster_info={"version": "1.21.0"},
                    crds=[],
                    operators=[],
                    csvs=[],
                    notes="Test snapshot"
                )
                
                assert snapshot_id is not None
            
            # Verify manager is still functional (connection handling is per-operation)
            assert hasattr(db_manager, 'db_path')


class TestInventorySnapshot:
    """Test cases for InventorySnapshot model."""

    def test_inventory_snapshot_creation(self):
        """Test creating an InventorySnapshot object."""
        snapshot = InventorySnapshot(
            id=1,
            timestamp="2024-01-01T12:00:00Z",
            cluster_context="test-context",
            cluster_info='{"version": "1.21.0"}',
            crd_count=5,
            operator_count=3,
            csv_count=2,
            namespace_filter="test-namespace",
            notes="Test snapshot"
        )
        
        assert snapshot.id == 1
        assert snapshot.cluster_context == "test-context"
        assert snapshot.crd_count == 5
        assert snapshot.operator_count == 3
        assert snapshot.csv_count == 2
        assert snapshot.namespace_filter == "test-namespace"
        assert snapshot.notes == "Test snapshot"

    def test_inventory_snapshot_to_dict(self):
        """Test converting InventorySnapshot to dictionary."""
        snapshot = InventorySnapshot(
            id=1,
            timestamp="2024-01-01T12:00:00Z",
            cluster_context="test-context",
            cluster_info='{"version": "1.21.0"}',
            crd_count=5,
            operator_count=3,
            csv_count=2,
            namespace_filter=None,
            notes=None
        )
        
        data = snapshot.to_dict()
        
        expected_keys = {
            'id', 'timestamp', 'cluster_context', 'cluster_info',
            'crd_count', 'operator_count', 'csv_count', 
            'namespace_filter', 'notes'
        }
        
        assert set(data.keys()) == expected_keys
        assert data['id'] == 1
        assert data['cluster_context'] == "test-context"
        assert data['crd_count'] == 5


class TestDatabaseIntegration:
    """Integration tests for database functionality."""

    def test_full_workflow(self):
        """Test a complete workflow with database operations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # Create test data with various types
            crd1 = CRD(
                name="crd1.example.com",
                group="example.com",
                version="v1",
                kind="Resource1",
                plural="resource1s",
                singular="resource1",
                scope="Namespaced"
            )
            
            crd2 = CRD(
                name="crd2.example.com",
                group="example.com",
                version="v1beta1",
                kind="Resource2",
                plural="resource2s",
                singular="resource2",
                scope="Cluster"
            )
            
            operator1 = Operator(
                name="operator1",
                namespace="namespace1",
                operator_framework="OLM"
            )
            
            csv1 = ClusterServiceVersion(
                name="csv1",
                namespace="namespace1",
                display_name="Test CSV 1",
                version="1.0.0",
                phase="Succeeded"
            )
            
            # Store initial snapshot
            snapshot1_id = db_manager.store_inventory_snapshot(
                cluster_context="prod-cluster",
                cluster_info={"version": "1.21.0", "nodes": 3},
                crds=[crd1, crd2],
                operators=[operator1],
                csvs=[csv1],
                namespace_filter="namespace1",
                notes="Production cluster snapshot"
            )
            
            # Store second snapshot (simulating cluster evolution)
            operator2 = Operator(
                name="operator2",
                namespace="namespace2",
                operator_framework="Helm"
            )
            
            snapshot2_id = db_manager.store_inventory_snapshot(
                cluster_context="prod-cluster",
                cluster_info={"version": "1.21.0", "nodes": 3},
                crds=[crd1, crd2],
                operators=[operator1, operator2],
                csvs=[csv1],
                namespace_filter=None,
                notes="Updated production cluster snapshot"
            )
            
            # List snapshots and verify
            all_snapshots = db_manager.list_snapshots()
            assert len(all_snapshots) == 2
            
            prod_snapshots = db_manager.list_snapshots(cluster_context="prod-cluster")
            assert len(prod_snapshots) == 2
            
            # Get detailed data for each snapshot
            snapshot1_data = db_manager.get_snapshot_data(snapshot1_id)
            snapshot2_data = db_manager.get_snapshot_data(snapshot2_id)
            
            # Verify snapshot 1
            assert len(snapshot1_data['crds']) == 2
            assert len(snapshot1_data['operators']) == 1
            assert len(snapshot1_data['csvs']) == 1
            assert snapshot1_data['snapshot']['namespace_filter'] == "namespace1"
            
            # Verify snapshot 2
            assert len(snapshot2_data['crds']) == 2
            assert len(snapshot2_data['operators']) == 2  # Added operator2
            assert len(snapshot2_data['csvs']) == 1
            assert snapshot2_data['snapshot']['namespace_filter'] is None
            
            # Test statistics
            stats = db_manager.get_database_stats()
            assert stats['total_snapshots'] == 2
            assert stats['total_crds'] == 4  # 2 CRDs per snapshot × 2 snapshots
            assert stats['total_operators'] == 3  # 1 in snapshot1 + 2 in snapshot2
            assert stats['total_csvs'] == 2  # 1 CSV per snapshot × 2 snapshots
            assert "prod-cluster" in stats['cluster_contexts']
            
            # Test cleanup
            deleted_count = db_manager.cleanup_old_snapshots(keep_count=1)
            assert deleted_count == 1
            
            remaining_snapshots = db_manager.list_snapshots()
            assert len(remaining_snapshots) == 1
            assert remaining_snapshots[0].id == snapshot2_id  # Most recent should remain

    def test_empty_database_operations(self):
        """Test operations on empty database."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            db_manager = DatabaseManager(db_path)
            
            # List snapshots on empty database
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 0
            
            # Get stats on empty database
            stats = db_manager.get_database_stats()
            assert stats['total_snapshots'] == 0
            assert stats['total_crds'] == 0
            assert stats['total_operators'] == 0
            assert stats['total_csvs'] == 0
            assert len(stats['cluster_contexts']) == 0
            assert stats['oldest_snapshot'] is None
            assert stats['newest_snapshot'] is None
            
            # Cleanup on empty database
            deleted_count = db_manager.cleanup_old_snapshots(keep_count=5)
            assert deleted_count == 0
            
            # Delete non-existent snapshot
            result = db_manager.delete_snapshot(1)
            assert result is False
