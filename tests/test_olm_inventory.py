"""Tests for OLM inventory functionality."""

import pytest
from unittest.mock import Mock, MagicMock
from kubernetes.client.rest import ApiException

from src.k8s_inventory_cli.core.olm_inventory import OLMInventory, CSVInfo
from src.k8s_inventory_cli.core.k8s_client import K8sClient


class TestOLMInventory:
    """Test OLM inventory functionality."""

    @pytest.fixture
    def mock_k8s_client(self):
        """Create a mock Kubernetes client."""
        return Mock(spec=K8sClient)

    @pytest.fixture
    def olm_inventory(self, mock_k8s_client):
        """Create an OLM inventory instance with mock client."""
        return OLMInventory(mock_k8s_client)

    @pytest.fixture
    def mock_csv_response(self):
        """Create mock CSV API response."""
        return {
            'items': [{
                'metadata': {
                    'name': 'test-operator.v1.0.0',
                    'namespace': 'test-namespace',
                    'creationTimestamp': '2023-01-01T00:00:00Z',
                    'labels': {'app': 'test-operator'},
                    'annotations': {'description': 'Test operator'}
                },
                'spec': {
                    'displayName': 'Test Operator',
                    'version': '1.0.0',
                    'description': 'A test operator for unit tests',
                    'provider': {'name': 'Test Company'},
                    'installModes': [{'type': 'OwnNamespace'}],
                    'customresourcedefinitions': {
                        'owned': [{'name': 'testresources.test.io'}],
                        'required': []
                    },
                    'install': {
                        'strategy': 'deployment',
                        'spec': {
                            'permissions': [{'serviceAccountName': 'test-operator'}],
                            'clusterPermissions': []
                        }
                    },
                    'replaces': 'test-operator.v0.9.0',
                    'skips': ['test-operator.v0.8.0'],
                    'minKubeVersion': '1.20.0'
                },
                'status': {
                    'phase': 'Succeeded'
                }
            }]
        }

    def test_list_csvs_success(self, olm_inventory, mock_k8s_client, mock_csv_response):
        """Test successful CSV listing."""
        # Setup
        mock_k8s_client.custom_objects_api.list_cluster_custom_object.return_value = mock_csv_response

        # Execute
        csvs = olm_inventory.list_csvs()

        # Verify
        assert len(csvs) == 1
        csv = csvs[0]
        assert isinstance(csv, CSVInfo)
        assert csv.name == "test-operator.v1.0.0"
        assert csv.namespace == "test-namespace"
        assert csv.display_name == "Test Operator"
        assert csv.version == "1.0.0"
        assert csv.phase == "Succeeded"
        assert csv.provider == "Test Company"
        assert "testresources.test.io" in csv.owned_crds

    def test_list_csvs_olm_not_installed(self, olm_inventory, mock_k8s_client):
        """Test CSV listing when OLM is not installed."""
        # Setup - 404 error indicates OLM CRDs don't exist
        mock_k8s_client.custom_objects_api.list_cluster_custom_object.side_effect = ApiException(
            status=404, reason="Not Found"
        )

        # Execute
        csvs = olm_inventory.list_csvs()

        # Verify
        assert len(csvs) == 0

    def test_list_csvs_api_exception(self, olm_inventory, mock_k8s_client):
        """Test CSV listing with non-404 API exception."""
        # Setup
        mock_k8s_client.custom_objects_api.list_cluster_custom_object.side_effect = ApiException(
            status=500, reason="Internal Server Error"
        )

        # Execute & Verify
        with pytest.raises(ApiException):
            olm_inventory.list_csvs()

    def test_get_csv_details_success(self, olm_inventory, mock_k8s_client):
        """Test successful CSV details retrieval."""
        # Setup
        csv_data = {
            'metadata': {
                'name': 'test-operator.v1.0.0',
                'namespace': 'test-namespace',
                'creationTimestamp': '2023-01-01T00:00:00Z',
                'labels': {},
                'annotations': {}
            },
            'spec': {
                'displayName': 'Test Operator',
                'version': '1.0.0',
                'description': 'Test operator',
                'provider': {'name': 'Test Company'},
                'customresourcedefinitions': {'owned': [], 'required': []},
                'install': {'strategy': 'deployment', 'spec': {}},
                'replaces': '',
                'skips': [],
                'minKubeVersion': ''
            },
            'status': {'phase': 'Succeeded'}
        }
        mock_k8s_client.custom_objects_api.get_namespaced_custom_object.return_value = csv_data

        # Execute
        csv = olm_inventory.get_csv_details("test-operator.v1.0.0", "test-namespace")

        # Verify
        assert csv is not None
        assert csv.name == "test-operator.v1.0.0"
        assert csv.phase == "Succeeded"

    def test_get_csv_details_not_found(self, olm_inventory, mock_k8s_client):
        """Test CSV details retrieval when CSV not found."""
        # Setup
        mock_k8s_client.custom_objects_api.get_namespaced_custom_object.side_effect = ApiException(
            status=404, reason="Not Found"
        )

        # Execute
        csv = olm_inventory.get_csv_details("nonexistent-csv", "test-namespace")

        # Verify
        assert csv is None

    def test_filter_csvs(self, olm_inventory):
        """Test CSV filtering functionality."""
        # Setup
        csvs = [
            CSVInfo(
                name="csv1", namespace="ns1", display_name="CSV 1", version="1.0.0",
                phase="Succeeded", description="", provider="Company A", install_strategy="",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                owned_crds=[], required_crds=[], permissions=[], cluster_permissions=[],
                replaces="", skips=[], min_kube_version=""
            ),
            CSVInfo(
                name="csv2", namespace="ns2", display_name="CSV 2", version="2.0.0",
                phase="Failed", description="", provider="Company B", install_strategy="",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                owned_crds=[], required_crds=[], permissions=[], cluster_permissions=[],
                replaces="", skips=[], min_kube_version=""
            )
        ]

        # Test namespace filter
        filtered = olm_inventory.filter_csvs(csvs, namespace_filter="ns1")
        assert len(filtered) == 1
        assert filtered[0].namespace == "ns1"

        # Test phase filter
        filtered = olm_inventory.filter_csvs(csvs, phase_filter="Succeeded")
        assert len(filtered) == 1
        assert filtered[0].phase == "Succeeded"

        # Test provider filter
        filtered = olm_inventory.filter_csvs(csvs, provider_filter="Company A")
        assert len(filtered) == 1
        assert filtered[0].provider == "Company A"

    def test_get_csv_statistics(self, olm_inventory):
        """Test CSV statistics generation."""
        # Setup
        csvs = [
            CSVInfo(
                name="csv1", namespace="ns1", display_name="CSV 1", version="1.0.0",
                phase="Succeeded", description="", provider="Company A", install_strategy="",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                owned_crds=["crd1.test.io", "crd2.test.io"], required_crds=[], 
                permissions=[], cluster_permissions=[], replaces="", skips=[], min_kube_version=""
            ),
            CSVInfo(
                name="csv2", namespace="ns1", display_name="CSV 2", version="2.0.0",
                phase="Failed", description="", provider="Company B", install_strategy="",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                owned_crds=["crd3.test.io"], required_crds=[], permissions=[], 
                cluster_permissions=[], replaces="", skips=[], min_kube_version=""
            )
        ]

        # Execute
        stats = olm_inventory.get_csv_statistics(csvs)

        # Verify
        assert stats["total_csvs"] == 2
        assert stats["by_phase"]["Succeeded"] == 1
        assert stats["by_phase"]["Failed"] == 1
        assert stats["by_provider"]["Company A"] == 1
        assert stats["by_provider"]["Company B"] == 1
        assert stats["by_namespace"]["ns1"] == 2
        assert stats["total_owned_crds"] == 3
        assert stats["successful_csvs"] == 1

    def test_csv_info_to_dict(self):
        """Test CSVInfo to_dict conversion."""
        csv_info = CSVInfo(
            name="test-csv", namespace="test-ns", display_name="Test CSV", version="1.0.0",
            phase="Succeeded", description="Test", provider="Test Co", install_strategy="deployment",
            creation_timestamp="2023-01-01T00:00:00Z", labels={"app": "test"}, 
            annotations={"desc": "test"}, owned_crds=["test.crd.io"], required_crds=[],
            permissions=[], cluster_permissions=[], replaces="", skips=[], min_kube_version="1.20.0"
        )

        result = csv_info.to_dict()
        
        assert isinstance(result, dict)
        assert result["name"] == "test-csv"
        assert result["phase"] == "Succeeded"
        assert result["owned_crds"] == ["test.crd.io"]
