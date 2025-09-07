"""Unit tests for CRD group synthesis functionality."""

import pytest
from datetime import datetime
from unittest.mock import Mock

from k8s_inventory_cli.core.crd_inventory import CRDInventory
from k8s_inventory_cli.core.models import CRD as CRDInfo
from k8s_inventory_cli.core.k8s_client import K8sClient


class TestCRDGroupSynthesis:
    """Test cases for CRD group synthesis functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_k8s_client = Mock(spec=K8sClient)
        self.inventory = CRDInventory(self.mock_k8s_client)

    def test_empty_crd_list_synthesis(self):
        """Test group synthesis with empty CRD list."""
        synthesis = self.inventory.get_group_synthesis([])
        
        assert synthesis['total_groups'] == 0
        assert synthesis['total_crds'] == 0
        assert synthesis['total_instances'] == 0
        assert synthesis['groups'] == {}
        assert synthesis['summary']['by_scope'] == {'Namespaced': 0, 'Cluster': 0}
        assert synthesis['summary']['by_category'] == {}
        assert synthesis['summary']['most_active_groups'] == []

    def test_single_group_synthesis(self):
        """Test group synthesis with CRDs from a single group."""
        crds = [
            CRDInfo(
                name="certificates.cert-manager.io",
                group="cert-manager.io",
                version="v1",
                kind="Certificate",
                plural="certificates",
                singular="certificate",
                scope="Namespaced",
                creation_timestamp="2024-01-01T10:00:00Z",
                labels={"app": "cert-manager"},
                annotations={},
                served_versions=["v1"],
                stored_version="v1",
                categories=["cert-manager"],
                short_names=["cert"],
                instance_count=5
            ),
            CRDInfo(
                name="issuers.cert-manager.io",
                group="cert-manager.io",
                version="v1",
                kind="Issuer",
                plural="issuers",
                singular="issuer",
                scope="Namespaced",
                creation_timestamp="2024-01-01T10:05:00Z",
                labels={"app": "cert-manager"},
                annotations={},
                served_versions=["v1"],
                stored_version="v1",
                categories=["cert-manager"],
                short_names=["issuer"],
                instance_count=3
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        
        # Basic counts
        assert synthesis['total_groups'] == 1
        assert synthesis['total_crds'] == 2
        assert synthesis['total_instances'] == 8
        
        # Group details
        assert "cert-manager.io" in synthesis['groups']
        group_data = synthesis['groups']['cert-manager.io']
        
        assert group_data['name'] == "cert-manager.io"
        assert group_data['crd_count'] == 2
        assert group_data['total_instances'] == 8
        assert len(group_data['crds']) == 2
        assert group_data['scopes'] == {'Namespaced': 2, 'Cluster': 0}
        assert group_data['versions'] == ['v1']
        assert group_data['categories'] == ['cert-manager']
        assert group_data['latest_creation'] == "2024-01-01T10:05:00Z"
        assert group_data['oldest_creation'] == "2024-01-01T10:00:00Z"
        
        # Summary statistics
        assert synthesis['summary']['by_scope'] == {'Namespaced': 2, 'Cluster': 0}
        assert synthesis['summary']['by_category'] == {'cert-manager': 2}
        assert synthesis['summary']['by_version'] == {'v1': 2}
        
        # Most active groups
        assert len(synthesis['summary']['most_active_groups']) == 1
        assert synthesis['summary']['most_active_groups'][0] == ('cert-manager.io', 8, 2)
        
        # Diversity metrics
        diversity = synthesis['summary']['diversity']
        assert diversity['single_crd_groups'] == 0
        assert diversity['multi_crd_groups'] == 1
        assert diversity['largest_group'] == 'cert-manager.io'
        assert diversity['average_crds_per_group'] == 2.0

    def test_multiple_groups_synthesis(self):
        """Test group synthesis with CRDs from multiple groups."""
        crds = [
            # cert-manager group
            CRDInfo(
                name="certificates.cert-manager.io",
                group="cert-manager.io",
                version="v1",
                kind="Certificate",
                plural="certificates",
                singular="certificate",
                scope="Namespaced",
                creation_timestamp="2024-01-01T10:00:00Z",
                labels={},
                annotations={},
                served_versions=["v1"],
                stored_version="v1",
                categories=[],
                short_names=[],
                instance_count=5
            ),
            CRDInfo(
                name="issuers.cert-manager.io",
                group="cert-manager.io",
                version="v1",
                kind="Issuer",
                plural="issuers",
                singular="issuer",
                scope="Namespaced",
                creation_timestamp="2024-01-01T10:05:00Z",
                instance_count=3
            ),
            # networking group
            CRDInfo(
                name="ingresses.networking.k8s.io",
                group="networking.k8s.io",
                version="v1",
                kind="Ingress",
                plural="ingresses",
                singular="ingress",
                scope="Namespaced",
                creation_timestamp="2024-01-01T09:00:00Z",
                instance_count=10
            ),
            # monitoring group
            CRDInfo(
                name="prometheuses.monitoring.coreos.com",
                group="monitoring.coreos.com",
                version="v1",
                kind="Prometheus",
                plural="prometheuses",
                singular="prometheus",
                scope="Namespaced",
                creation_timestamp="2024-01-01T11:00:00Z",
                instance_count=2
            ),
            # cluster-scoped CRD
            CRDInfo(
                name="clusterroles.rbac.authorization.k8s.io",
                group="rbac.authorization.k8s.io",
                version="v1",
                kind="ClusterRole",
                plural="clusterroles",
                singular="clusterrole",
                scope="Cluster",
                creation_timestamp="2024-01-01T08:00:00Z",
                instance_count=15
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        
        # Basic counts
        assert synthesis['total_groups'] == 4
        assert synthesis['total_crds'] == 5
        assert synthesis['total_instances'] == 35  # 5 + 3 + 10 + 2 + 15
        
        # Verify all groups are present
        expected_groups = {
            'cert-manager.io', 'networking.k8s.io', 
            'monitoring.coreos.com', 'rbac.authorization.k8s.io'
        }
        assert set(synthesis['groups'].keys()) == expected_groups
        
        # Check group details
        cert_manager_group = synthesis['groups']['cert-manager.io']
        assert cert_manager_group['crd_count'] == 2
        assert cert_manager_group['total_instances'] == 8
        assert cert_manager_group['scopes'] == {'Namespaced': 2, 'Cluster': 0}
        
        rbac_group = synthesis['groups']['rbac.authorization.k8s.io']
        assert rbac_group['crd_count'] == 1
        assert rbac_group['total_instances'] == 15
        assert rbac_group['scopes'] == {'Namespaced': 0, 'Cluster': 1}
        
        # Summary statistics
        assert synthesis['summary']['by_scope'] == {'Namespaced': 4, 'Cluster': 1}
        
        # Most active groups (sorted by instances)
        most_active = synthesis['summary']['most_active_groups']
        assert len(most_active) == 4
        assert most_active[0] == ('rbac.authorization.k8s.io', 15, 1)  # Most instances
        assert most_active[1] == ('networking.k8s.io', 10, 1)
        assert most_active[2] == ('cert-manager.io', 8, 2)
        assert most_active[3] == ('monitoring.coreos.com', 2, 1)
        
        # Diversity metrics
        diversity = synthesis['summary']['diversity']
        assert diversity['single_crd_groups'] == 3  # networking, monitoring, rbac
        assert diversity['multi_crd_groups'] == 1   # cert-manager
        assert diversity['largest_group'] == 'cert-manager.io'
        assert diversity['average_crds_per_group'] == 1.25  # 5 CRDs / 4 groups

    def test_core_group_handling(self):
        """Test handling of CRDs with empty/null group (core group)."""
        crds = [
            CRDInfo(
                name="pods",
                group="",  # Empty group (core)
                version="v1",
                kind="Pod",
                plural="pods",
                singular="pod",
                scope="Namespaced",
                instance_count=100
            ),
            CRDInfo(
                name="services",
                group=None,  # None group (core)
                version="v1",
                kind="Service", 
                plural="services",
                singular="service",
                scope="Namespaced",
                instance_count=50
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        
        assert synthesis['total_groups'] == 1
        assert 'core' in synthesis['groups']
        
        core_group = synthesis['groups']['core']
        assert core_group['crd_count'] == 2
        assert core_group['total_instances'] == 150

    def test_version_and_category_aggregation(self):
        """Test aggregation of versions and categories across groups."""
        crds = [
            CRDInfo(
                name="crd1.example.com",
                group="example.com",
                version="v1",
                kind="Resource1",
                plural="resource1s",
                singular="resource1",
                scope="Namespaced",
                categories=["storage", "database"],
                instance_count=5
            ),
            CRDInfo(
                name="crd2.example.com",
                group="example.com",
                version="v1beta1",
                kind="Resource2",
                plural="resource2s",
                singular="resource2",
                scope="Cluster",
                categories=["storage", "networking"],
                instance_count=3
            ),
            CRDInfo(
                name="crd3.example.com",
                group="example.com",
                version="v2",
                kind="Resource3",
                plural="resource3s",
                singular="resource3",
                scope="Namespaced",
                categories=["compute"],
                instance_count=2
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        
        group_data = synthesis['groups']['example.com']
        
        # Check version aggregation (should be sorted)
        assert set(group_data['versions']) == {'v1', 'v1beta1', 'v2'}
        assert group_data['versions'] == ['v1', 'v1beta1', 'v2']  # sorted
        
        # Check category aggregation (should be sorted)
        assert set(group_data['categories']) == {'compute', 'database', 'networking', 'storage'}
        assert group_data['categories'] == ['compute', 'database', 'networking', 'storage']  # sorted
        
        # Check scope distribution
        assert group_data['scopes'] == {'Namespaced': 2, 'Cluster': 1}
        
        # Check summary statistics
        expected_categories = {'storage': 2, 'database': 1, 'networking': 1, 'compute': 1}
        assert synthesis['summary']['by_category'] == expected_categories
        
        expected_versions = {'v1': 1, 'v1beta1': 1, 'v2': 1}
        assert synthesis['summary']['by_version'] == expected_versions

    def test_creation_timestamp_tracking(self):
        """Test tracking of oldest and newest creation timestamps per group."""
        crds = [
            CRDInfo(
                name="crd1.example.com",
                group="example.com",
                version="v1",
                kind="Resource1",
                plural="resource1s",
                singular="resource1",
                scope="Namespaced",
                creation_timestamp="2024-01-01T10:00:00Z",
                instance_count=1
            ),
            CRDInfo(
                name="crd2.example.com",
                group="example.com",
                version="v1",
                kind="Resource2",
                plural="resource2s",
                singular="resource2",
                scope="Namespaced",
                creation_timestamp="2024-01-01T12:00:00Z",  # Newest
                instance_count=1
            ),
            CRDInfo(
                name="crd3.example.com",
                group="example.com",
                version="v1",
                kind="Resource3",
                plural="resource3s",
                singular="resource3",
                scope="Namespaced",
                creation_timestamp="2024-01-01T08:00:00Z",  # Oldest
                instance_count=1
            ),
            CRDInfo(
                name="crd4.example.com",
                group="example.com",
                version="v1",
                kind="Resource4",
                plural="resource4s",
                singular="resource4",
                scope="Namespaced",
                creation_timestamp="",  # Empty timestamp
                instance_count=1
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        group_data = synthesis['groups']['example.com']
        
        assert group_data['oldest_creation'] == "2024-01-01T08:00:00Z"
        assert group_data['latest_creation'] == "2024-01-01T12:00:00Z"

    def test_zero_instances_handling(self):
        """Test handling of CRDs with zero instances."""
        crds = [
            CRDInfo(
                name="unused.example.com",
                group="example.com",
                version="v1",
                kind="UnusedResource",
                plural="unusedresources",
                singular="unusedresource",
                scope="Namespaced",
                instance_count=0  # No instances
            ),
            CRDInfo(
                name="active.example.com",
                group="example.com",
                version="v1",
                kind="ActiveResource",
                plural="activeresources",
                singular="activeresource",
                scope="Namespaced",
                instance_count=5
            )
        ]
        
        synthesis = self.inventory.get_group_synthesis(crds)
        
        assert synthesis['total_crds'] == 2
        assert synthesis['total_instances'] == 5  # Only active CRD instances
        
        group_data = synthesis['groups']['example.com']
        assert group_data['crd_count'] == 2
        assert group_data['total_instances'] == 5
        assert len(group_data['crds']) == 2
