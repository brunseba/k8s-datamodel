"""Tests for CRD inventory functionality."""

import pytest
from unittest.mock import Mock, MagicMock
from kubernetes.client.rest import ApiException

from src.k8s_inventory_cli.core.crd_inventory import CRDInventory
from src.k8s_inventory_cli.core.models import CRD
from src.k8s_inventory_cli.core.k8s_client import K8sClient

# For backward compatibility
CRDInfo = CRD


class TestCRDInventory:
    """Test CRD inventory functionality."""

    @pytest.fixture
    def mock_k8s_client(self):
        """Create a mock Kubernetes client."""
        return Mock(spec=K8sClient)

    @pytest.fixture
    def crd_inventory(self, mock_k8s_client):
        """Create a CRD inventory instance with mock client."""
        return CRDInventory(mock_k8s_client)

    @pytest.fixture
    def mock_crd_response(self):
        """Create mock CRD API response."""
        mock_crd = Mock()
        mock_crd.metadata.name = "test-crd.example.com"
        mock_crd.metadata.creation_timestamp.isoformat.return_value = "2023-01-01T00:00:00Z"
        mock_crd.metadata.labels = {"app": "test"}
        mock_crd.metadata.annotations = {"description": "Test CRD"}
        mock_crd.spec.group = "example.com"
        mock_crd.spec.names.kind = "TestResource"
        mock_crd.spec.names.plural = "testresources"
        mock_crd.spec.names.singular = "testresource"
        mock_crd.spec.names.categories = ["all"]
        mock_crd.spec.names.short_names = ["tr"]
        mock_crd.spec.scope = "Namespaced"
        
        # Mock versions
        mock_version = Mock()
        mock_version.name = "v1"
        mock_version.storage = True
        mock_crd.spec.versions = [mock_version]
        
        mock_response = Mock()
        mock_response.items = [mock_crd]
        return mock_response

    def test_list_crds_success(self, crd_inventory, mock_k8s_client, mock_crd_response):
        """Test successful CRD listing."""
        # Setup
        mock_k8s_client.extensions_v1_api.list_custom_resource_definition.return_value = mock_crd_response
        mock_k8s_client.custom_objects_api.list_cluster_custom_object.return_value = {"items": []}

        # Execute
        crds = crd_inventory.list_crds()

        # Verify
        assert len(crds) == 1
        crd = crds[0]
        assert isinstance(crd, CRD)
        assert crd.name == "test-crd.example.com"
        assert crd.group == "example.com"
        assert crd.kind == "TestResource"
        assert crd.scope == "Namespaced"
        assert crd.stored_version == "v1"

    def test_list_crds_api_exception(self, crd_inventory, mock_k8s_client):
        """Test CRD listing with API exception."""
        # Setup
        mock_k8s_client.extensions_v1_api.list_custom_resource_definition.side_effect = ApiException("API Error")

        # Execute & Verify
        with pytest.raises(ApiException):
            crd_inventory.list_crds()

    def test_get_crd_details_success(self, crd_inventory, mock_k8s_client):
        """Test successful CRD details retrieval."""
        # Setup
        mock_crd = Mock()
        mock_crd.metadata.name = "test-crd.example.com"
        mock_crd.metadata.creation_timestamp.isoformat.return_value = "2023-01-01T00:00:00Z"
        mock_crd.metadata.labels = {}
        mock_crd.metadata.annotations = {}
        mock_crd.spec.group = "example.com"
        mock_crd.spec.names.kind = "TestResource"
        mock_crd.spec.names.plural = "testresources"
        mock_crd.spec.names.singular = "testresource"
        mock_crd.spec.names.categories = []
        mock_crd.spec.names.short_names = []
        mock_crd.spec.scope = "Cluster"
        
        mock_version = Mock()
        mock_version.name = "v1"
        mock_version.storage = True
        mock_crd.spec.versions = [mock_version]
        
        mock_k8s_client.extensions_v1_api.read_custom_resource_definition.return_value = mock_crd
        mock_k8s_client.custom_objects_api.list_cluster_custom_object.return_value = {"items": []}

        # Execute
        crd = crd_inventory.get_crd_details("test-crd.example.com")

        # Verify
        assert crd is not None
        assert crd.name == "test-crd.example.com"
        assert crd.scope == "Cluster"

    def test_get_crd_details_not_found(self, crd_inventory, mock_k8s_client):
        """Test CRD details retrieval when CRD not found."""
        # Setup
        mock_k8s_client.extensions_v1_api.read_custom_resource_definition.side_effect = ApiException(
            status=404, reason="Not Found"
        )

        # Execute
        crd = crd_inventory.get_crd_details("nonexistent-crd")

        # Verify
        assert crd is None

    def test_filter_crds(self, crd_inventory):
        """Test CRD filtering functionality."""
        # Setup
        crds = [
            CRDInfo(
                name="crd1.example.com", group="example.com", version="v1", kind="Resource1",
                plural="resource1s", singular="resource1", scope="Namespaced",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                served_versions=["v1"], stored_version="v1", categories=[], short_names=[],
                instance_count=0
            ),
            CRDInfo(
                name="crd2.test.com", group="test.com", version="v1", kind="Resource2",
                plural="resource2s", singular="resource2", scope="Cluster",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                served_versions=["v1"], stored_version="v1", categories=[], short_names=[],
                instance_count=0
            )
        ]

        # Test group filter
        filtered = crd_inventory.filter_crds(crds, group_filter="example")
        assert len(filtered) == 1
        assert filtered[0].group == "example.com"

        # Test kind filter
        filtered = crd_inventory.filter_crds(crds, kind_filter="Resource2")
        assert len(filtered) == 1
        assert filtered[0].kind == "Resource2"

        # Test scope filter
        filtered = crd_inventory.filter_crds(crds, scope_filter="Cluster")
        assert len(filtered) == 1
        assert filtered[0].scope == "Cluster"

    def test_crd_info_to_dict(self):
        """Test CRDInfo to_dict conversion."""
        crd_info = CRDInfo(
            name="test-crd", group="example.com", version="v1", kind="TestResource",
            plural="testresources", singular="testresource", scope="Namespaced",
            creation_timestamp="2023-01-01T00:00:00Z", labels={"app": "test"}, 
            annotations={"desc": "test"}, served_versions=["v1"], stored_version="v1",
            categories=["all"], short_names=["tr"], instance_count=5
        )

        result = crd_info.to_dict()
        
        assert isinstance(result, dict)
        assert result["name"] == "test-crd"
        assert result["group"] == "example.com"
        assert result["instance_count"] == 5
