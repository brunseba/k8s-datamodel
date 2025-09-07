"""Unit tests for database CLI commands."""

import pytest
import tempfile
import os
from unittest.mock import Mock, patch
from click.testing import CliRunner

from k8s_inventory_cli.commands.database import (
    store_snapshot, list_snapshots, show_snapshot,
    delete_snapshot, database_stats, cleanup_snapshots, export_snapshot
)
from k8s_inventory_cli.core.database import DatabaseManager
from k8s_inventory_cli.core.models import CRD, Operator, ClusterServiceVersion


class TestDatabaseCommands:
    """Test cases for database CLI commands."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_store_snapshot_command(self):
        """Test the store snapshot command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            with patch('k8s_inventory_cli.commands.database.K8sClient') as mock_k8s_client, \
                 patch('k8s_inventory_cli.commands.database.CRDInventory') as mock_crd_inventory, \
                 patch('k8s_inventory_cli.commands.database.OperatorInventory') as mock_operator_inventory, \
                 patch('k8s_inventory_cli.commands.database.OLMInventory') as mock_olm_inventory:
                
                # Mock K8s client
                mock_client_instance = Mock()
                mock_client_instance.test_connection.return_value = True
                mock_client_instance.get_cluster_info.return_value = {"version": "1.21.0"}
                mock_k8s_client.return_value = mock_client_instance
                
                # Mock inventories
                mock_crd_inventory.return_value.list_crds.return_value = []
                mock_operator_inventory.return_value.list_operators.return_value = []
                mock_olm_inventory.return_value.list_csvs.return_value = []
                
                # Create context
                ctx = {'db_path': db_path, 'verbose': False}
                
                result = self.runner.invoke(store_snapshot, ['--notes', 'Test snapshot'], obj=ctx)
                
                assert result.exit_code == 0
                assert "Stored inventory snapshot" in result.output

    def test_list_snapshots_command(self):
        """Test the list snapshots command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create some test snapshots
            db_manager = DatabaseManager(db_path)
            db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[], operators=[], csvs=[],
                notes="Test snapshot 1"
            )
            db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[], operators=[], csvs=[],
                notes="Test snapshot 2"
            )
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(list_snapshots, [], obj=ctx)
            
            assert result.exit_code == 0
            assert "Test snapshot 1" in result.output
            assert "Test snapshot 2" in result.output

    def test_list_snapshots_empty_database(self):
        """Test list snapshots command on empty database."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create empty database
            DatabaseManager(db_path)
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(list_snapshots, [], obj=ctx)
            
            assert result.exit_code == 0
            assert "No snapshots found" in result.output

    def test_show_snapshot_command(self):
        """Test the show snapshot command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create test snapshot
            crd = CRD(
                name="test-crd.example.com",
                group="example.com",
                version="v1",
                kind="TestResource",
                plural="testresources",
                singular="testresource",
                scope="Namespaced"
            )
            
            db_manager = DatabaseManager(db_path)
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[crd], operators=[], csvs=[],
                notes="Test snapshot"
            )
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(
                show_snapshot, 
                [str(snapshot_id)], 
                obj=ctx
            )
            
            assert result.exit_code == 0
            assert "test-context" in result.output
            assert "test-crd.example.com" in result.output

    def test_delete_snapshot_command(self):
        """Test the delete snapshot command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create test snapshot
            db_manager = DatabaseManager(db_path)
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[], operators=[], csvs=[],
                notes="Test snapshot"
            )
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(
                delete_snapshot, 
                [str(snapshot_id), '--yes'], 
                obj=ctx
            )
            
            assert result.exit_code == 0
            assert f"Deleted snapshot #{snapshot_id}" in result.output
            
            # Verify deletion
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 0

    def test_database_stats_command(self):
        """Test the database stats command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create test data
            db_manager = DatabaseManager(db_path)
            db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[], operators=[], csvs=[],
                notes="Test snapshot"
            )
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(database_stats, [], obj=ctx)
            
            assert result.exit_code == 0
            # Should contain database info in some form
            assert (db_path in result.output or 
                    "total_snapshots" in result.output or
                    "Total Snapshots" in result.output)

    def test_cleanup_snapshots_command(self):
        """Test the cleanup snapshots command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create multiple test snapshots
            db_manager = DatabaseManager(db_path)
            for i in range(5):
                db_manager.store_inventory_snapshot(
                    cluster_context="test-context",
                    cluster_info={"version": "1.21.0"},
                    crds=[], operators=[], csvs=[],
                    notes=f"Test snapshot {i}"
                )
            
            ctx = {'db_path': db_path}
            
            result = self.runner.invoke(
                cleanup_snapshots, 
                ['--keep', '2', '--yes'], 
                obj=ctx
            )
            
            assert result.exit_code == 0
            assert "Cleaned up 3 old snapshots" in result.output
            
            # Verify only 2 snapshots remain
            snapshots = db_manager.list_snapshots()
            assert len(snapshots) == 2

    def test_export_snapshot_command(self):
        """Test the export snapshot command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = os.path.join(temp_dir, "test.db")
            
            # Create test snapshot
            crd = CRD(
                name="test-crd.example.com",
                group="example.com",
                version="v1",
                kind="TestResource",
                plural="testresources",
                singular="testresource",
                scope="Namespaced"
            )
            
            db_manager = DatabaseManager(db_path)
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context="test-context",
                cluster_info={"version": "1.21.0"},
                crds=[crd], operators=[], csvs=[],
                notes="Test snapshot"
            )
            
            ctx = {'db_path': db_path}
            
            # Export to stdout
            result = self.runner.invoke(
                export_snapshot, 
                [str(snapshot_id)], 
                obj=ctx
            )
            
            assert result.exit_code == 0
            assert "test-context" in result.output
            assert "test-crd.example.com" in result.output
