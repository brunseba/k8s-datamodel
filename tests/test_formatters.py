"""Tests for output formatters."""

import json
import yaml
import pytest
from unittest.mock import patch

from src.k8s_inventory_cli.utils.formatters import OutputFormatter
from src.k8s_inventory_cli.core.crd_inventory import CRDInfo
from src.k8s_inventory_cli.core.operator_inventory import OperatorInfo


class TestOutputFormatter:
    """Test output formatting functionality."""

    @pytest.fixture
    def formatter(self):
        """Create output formatter instance."""
        return OutputFormatter(use_color=False)  # Disable color for testing

    @pytest.fixture
    def sample_crds(self):
        """Create sample CRD data."""
        return [
            CRDInfo(
                name="test1.example.com", group="example.com", version="v1", kind="Test1",
                plural="test1s", singular="test1", scope="Namespaced",
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                served_versions=["v1"], stored_version="v1", categories=[], short_names=[],
                instance_count=3
            ),
            CRDInfo(
                name="test2.example.com", group="example.com", version="v1", kind="Test2",
                plural="test2s", singular="test2", scope="Cluster",
                creation_timestamp="2023-01-02T00:00:00Z", labels={}, annotations={},
                served_versions=["v1"], stored_version="v1", categories=[], short_names=[],
                instance_count=0
            )
        ]

    @pytest.fixture
    def sample_operators(self):
        """Create sample operator data."""
        return [
            OperatorInfo(
                name="test-operator", namespace="test-ns", operator_type="deployment",
                image="test/operator:v1.0.0", version="v1.0.0", 
                creation_timestamp="2023-01-01T00:00:00Z", labels={}, annotations={},
                replicas=1, ready_replicas=1, conditions=[], managed_crds=["test1.example.com"],
                managed_resources=[], operator_framework="Manual"
            )
        ]

    def test_format_crds_json(self, formatter, sample_crds):
        """Test CRD JSON formatting."""
        result = formatter.format_crds(sample_crds, output_format="json")
        
        # Parse JSON to verify structure
        data = json.loads(result)
        assert "crds" in data
        assert "total_count" in data
        assert data["total_count"] == 2
        assert len(data["crds"]) == 2
        assert data["crds"][0]["name"] == "test1.example.com"

    def test_format_crds_yaml(self, formatter, sample_crds):
        """Test CRD YAML formatting."""
        result = formatter.format_crds(sample_crds, output_format="yaml")
        
        # Parse YAML to verify structure
        data = yaml.safe_load(result)
        assert "crds" in data
        assert "total_count" in data
        assert data["total_count"] == 2

    def test_format_crds_table(self, formatter, sample_crds):
        """Test CRD table formatting."""
        result = formatter.format_crds(sample_crds, output_format="table")
        
        # Verify table contains expected content
        assert "test1.example.com" in result
        assert "test2.example.com" in result
        assert "example.com" in result
        assert "Namespaced" in result
        assert "Cluster" in result

    def test_format_crds_empty_list(self, formatter):
        """Test formatting empty CRD list."""
        result = formatter.format_crds([], output_format="table")
        assert "No CRDs found" in result

    def test_format_operators_json(self, formatter, sample_operators):
        """Test operator JSON formatting."""
        result = formatter.format_operators(sample_operators, output_format="json")
        
        data = json.loads(result)
        assert "operators" in data
        assert "total_count" in data
        assert data["total_count"] == 1
        assert data["operators"][0]["name"] == "test-operator"

    def test_format_operators_table(self, formatter, sample_operators):
        """Test operator table formatting."""
        result = formatter.format_operators(sample_operators, output_format="table")
        
        assert "test-operator" in result
        assert "test-ns" in result
        assert "deployment" in result
        assert "Manual" in result

    def test_calculate_age(self, formatter):
        """Test age calculation."""
        # Test with invalid timestamp returns Unknown
        age = formatter._calculate_age("invalid-timestamp")
        assert age == "Unknown"
        
        # Test with valid timestamp format (basic check)
        age = formatter._calculate_age("2023-01-01T00:00:00Z")
        assert isinstance(age, str)
        assert age != "Unknown"

    def test_calculate_age_empty_timestamp(self, formatter):
        """Test age calculation with empty timestamp."""
        age = formatter._calculate_age("")
        assert age == "Unknown"

    def test_truncate_image(self, formatter):
        """Test image name truncation."""
        # Short image should not be truncated
        short_image = "nginx:latest"
        result = formatter._truncate_image(short_image)
        assert result == short_image
        
        # Long image should be truncated
        long_image = "registry.example.com/very/long/path/to/image:v1.2.3-build.123"
        result = formatter._truncate_image(long_image, max_length=20)
        assert len(result) <= 20
        assert "..." in result

    def test_truncate_image_empty(self, formatter):
        """Test image truncation with empty string."""
        result = formatter._truncate_image("")
        assert result == "-"

    def test_detect_crd_framework(self, formatter):
        """Test CRD framework detection."""
        # Test OLM detection
        labels = {}
        annotations = {"operators.coreos.com/operator": "test-operator"}
        framework = formatter._detect_crd_framework(labels, annotations)
        assert framework == "OLM"
        
        # Test Helm detection
        labels = {"app.kubernetes.io/managed-by": "Helm"}
        annotations = {}
        framework = formatter._detect_crd_framework(labels, annotations)
        assert framework == "Helm"
        
        # Test unknown framework
        labels = {}
        annotations = {}
        framework = formatter._detect_crd_framework(labels, annotations)
        assert framework is None

    def test_format_summary_json(self, formatter, sample_crds, sample_operators):
        """Test summary JSON formatting."""
        result = formatter.format_summary(sample_crds, sample_operators, output_format="json")
        
        data = json.loads(result)
        assert "summary" in data
        assert "crds" in data["summary"]
        assert "operators" in data["summary"]
        assert data["summary"]["crds"]["total"] == 2
        assert data["summary"]["operators"]["total"] == 1

    def test_format_summary_yaml(self, formatter, sample_crds, sample_operators):
        """Test summary YAML formatting."""
        result = formatter.format_summary(sample_crds, sample_operators, output_format="yaml")
        
        data = yaml.safe_load(result)
        assert "summary" in data
        assert data["summary"]["crds"]["total"] == 2
