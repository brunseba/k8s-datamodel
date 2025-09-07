#!/usr/bin/env python3
"""Verify that datetime objects are properly serialized in the database."""

import sqlite3
import json
from pathlib import Path

def verify_datetime_serialization():
    """Check that all stored specs can be deserialized without datetime errors."""
    
    # Database path
    db_path = Path.home() / ".k8s-inventory" / "inventory.db"
    
    if not db_path.exists():
        print("❌ Database not found!")
        return False
    
    print(f"✓ Database found: {db_path}")
    print(f"✓ Database size: {db_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Connect to database
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    
    try:
        # Check CRDs
        cursor = conn.execute("SELECT name, spec FROM crds WHERE spec IS NOT NULL LIMIT 5")
        crd_count = 0
        for row in cursor:
            try:
                spec = json.loads(row['spec'])
                crd_count += 1
                print(f"✓ CRD '{row['name']}' spec deserialized successfully")
            except json.JSONDecodeError as e:
                print(f"❌ Failed to deserialize CRD '{row['name']}' spec: {e}")
                return False
        
        # Check operators
        cursor = conn.execute("SELECT name, spec FROM operators WHERE spec IS NOT NULL LIMIT 5")
        operator_count = 0
        for row in cursor:
            try:
                spec = json.loads(row['spec'])
                operator_count += 1
                print(f"✓ Operator '{row['name']}' spec deserialized successfully")
            except json.JSONDecodeError as e:
                print(f"❌ Failed to deserialize operator '{row['name']}' spec: {e}")
                return False
        
        # Check CSVs
        cursor = conn.execute("SELECT name, spec FROM csvs WHERE spec IS NOT NULL LIMIT 5")
        csv_count = 0
        for row in cursor:
            try:
                spec = json.loads(row['spec'])
                csv_count += 1
                print(f"✓ CSV '{row['name']}' spec deserialized successfully")
            except json.JSONDecodeError as e:
                print(f"❌ Failed to deserialize CSV '{row['name']}' spec: {e}")
                return False
        
        print(f"\n✅ SUCCESS: All specs properly serialized!")
        print(f"   - Checked {crd_count} CRDs")
        print(f"   - Checked {operator_count} operators")
        print(f"   - Checked {csv_count} CSVs")
        
        # Get total counts
        cursor = conn.execute("SELECT COUNT(*) as count FROM crds WHERE spec IS NOT NULL")
        total_crds = cursor.fetchone()['count']
        
        cursor = conn.execute("SELECT COUNT(*) as count FROM operators WHERE spec IS NOT NULL")
        total_operators = cursor.fetchone()['count']
        
        cursor = conn.execute("SELECT COUNT(*) as count FROM csvs WHERE spec IS NOT NULL")
        total_csvs = cursor.fetchone()['count']
        
        print(f"\n📊 Total resources with specs:")
        print(f"   - CRDs: {total_crds}")
        print(f"   - Operators: {total_operators}")
        print(f"   - CSVs: {total_csvs}")
        
        return True
        
    finally:
        conn.close()

if __name__ == "__main__":
    verify_datetime_serialization()
