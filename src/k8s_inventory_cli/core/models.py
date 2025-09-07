"""Data models for Kubernetes inventory components."""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class CRDProperty:
    """Information about a property in a CRD schema."""
    name: str
    type: str
    description: Optional[str] = None
    required: bool = False
    format: Optional[str] = None
    enum: Optional[List[str]] = None
    properties: Optional[Dict[str, 'CRDProperty']] = None  # For nested objects
    items: Optional['CRDProperty'] = None  # For arrays
    
    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.enum is None:
            self.enum = []
        if self.properties is None:
            self.properties = {}


@dataclass
class CRDSchema:
    """Schema information for a CRD version."""
    version: str
    properties: Dict[str, CRDProperty]
    required: List[str] = None
    
    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.required is None:
            self.required = []


@dataclass
class CRD:
    """Information about a Custom Resource Definition."""
    name: str
    group: str
    version: str
    kind: str
    plural: str
    singular: str
    scope: str  # Namespaced or Cluster
    creation_timestamp: str = ""
    labels: Dict[str, str] = None
    annotations: Dict[str, str] = None
    served_versions: List[str] = None
    stored_version: str = ""
    categories: List[str] = None
    short_names: List[str] = None
    description: Optional[str] = None
    instance_count: int = 0
    schemas: Dict[str, CRDSchema] = None  # Schema for each version

    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.labels is None:
            self.labels = {}
        if self.annotations is None:
            self.annotations = {}
        if self.served_versions is None:
            self.served_versions = []
        if self.categories is None:
            self.categories = []
        if self.short_names is None:
            self.short_names = []
        if self.schemas is None:
            self.schemas = {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


@dataclass
class Operator:
    """Information about a Kubernetes operator."""
    name: str
    namespace: str
    operator_type: str = "deployment"  # deployment, statefulset, etc.
    image: str = ""
    version: Optional[str] = None
    creation_timestamp: str = ""
    labels: Dict[str, str] = None
    annotations: Dict[str, str] = None
    replicas: int = 0
    ready_replicas: int = 0
    conditions: List[Dict[str, Any]] = None
    managed_crds: List[str] = None  # CRDs this operator manages
    managed_resources: List[str] = None  # Other resources this operator manages
    operator_framework: Optional[str] = None  # OLM, Helm, manual, etc.

    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.labels is None:
            self.labels = {}
        if self.annotations is None:
            self.annotations = {}
        if self.conditions is None:
            self.conditions = []
        if self.managed_crds is None:
            self.managed_crds = []
        if self.managed_resources is None:
            self.managed_resources = []

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


@dataclass
class ClusterServiceVersion:
    """Information about a ClusterServiceVersion (OLM operator)."""
    name: str
    namespace: str
    display_name: str = ""
    version: str = "unknown"
    phase: str = "Unknown"  # Succeeded, Installing, Failed, etc.
    description: Optional[str] = None
    provider: str = "Unknown"
    install_strategy: str = "Unknown"
    creation_timestamp: str = ""
    labels: Dict[str, str] = None
    annotations: Dict[str, str] = None
    owned_crds: List[str] = None  # CRDs owned by this operator
    required_crds: List[str] = None  # CRDs required by this operator
    permissions: List[Dict[str, Any]] = None
    cluster_permissions: List[Dict[str, Any]] = None
    replaces: Optional[str] = None  # Previous version replaced
    skips: List[str] = None  # Versions skipped
    min_kube_version: Optional[str] = None

    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.labels is None:
            self.labels = {}
        if self.annotations is None:
            self.annotations = {}
        if self.owned_crds is None:
            self.owned_crds = []
        if self.required_crds is None:
            self.required_crds = []
        if self.permissions is None:
            self.permissions = []
        if self.cluster_permissions is None:
            self.cluster_permissions = []
        if self.skips is None:
            self.skips = []

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


# Legacy aliases for backward compatibility
CRDInfo = CRD
OperatorInfo = Operator
CSVInfo = ClusterServiceVersion
