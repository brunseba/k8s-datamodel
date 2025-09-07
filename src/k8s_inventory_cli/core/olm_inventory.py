"""OLM (Operator Lifecycle Manager) inventory service."""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from kubernetes.client.rest import ApiException
import logging

from .k8s_client import K8sClient

logger = logging.getLogger(__name__)


@dataclass
class CSVInfo:
    """Information about a ClusterServiceVersion (OLM operator)."""
    name: str
    namespace: str
    display_name: str
    version: str
    phase: str  # Succeeded, Installing, Failed, etc.
    description: Optional[str]
    provider: str
    install_strategy: str
    creation_timestamp: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    owned_crds: List[str]  # CRDs owned by this operator
    required_crds: List[str]  # CRDs required by this operator
    permissions: List[Dict[str, Any]]
    cluster_permissions: List[Dict[str, Any]]
    replaces: Optional[str]  # Previous version replaced
    skips: List[str]  # Versions skipped
    min_kube_version: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class OLMInventory:
    """Service for inventorying OLM-managed operators via ClusterServiceVersions."""

    def __init__(self, k8s_client: K8sClient):
        """Initialize OLM inventory service.
        
        Args:
            k8s_client: Kubernetes client instance
        """
        self.k8s_client = k8s_client

    def list_csvs(self, namespace: Optional[str] = None) -> List[CSVInfo]:
        """List all ClusterServiceVersions in the cluster or specific namespace.
        
        Args:
            namespace: Specific namespace to search (None for all namespaces)
        
        Returns:
            List of CSVInfo objects
        """
        try:
            if namespace:
                csvs = self.k8s_client.custom_objects_api.list_namespaced_custom_object(
                    group="operators.coreos.com",
                    version="v1alpha1", 
                    namespace=namespace,
                    plural="clusterserviceversions"
                )
            else:
                csvs = self.k8s_client.custom_objects_api.list_cluster_custom_object(
                    group="operators.coreos.com",
                    version="v1alpha1",
                    plural="clusterserviceversions"
                )
            
            csv_list = []
            
            for csv in csvs.get('items', []):
                csv_info = self._csv_to_info(csv)
                if csv_info:
                    csv_list.append(csv_info)
            
            return sorted(csv_list, key=lambda x: (x.namespace, x.name))
        
        except ApiException as e:
            if e.status == 404:
                logger.info("OLM ClusterServiceVersions not found (OLM may not be installed)")
                return []
            logger.error(f"Failed to list ClusterServiceVersions: {e}")
            raise

    def get_csv_details(self, csv_name: str, namespace: str) -> Optional[CSVInfo]:
        """Get detailed information about a specific ClusterServiceVersion.
        
        Args:
            csv_name: Name of the CSV
            namespace: Namespace of the CSV
        
        Returns:
            CSVInfo object or None if not found
        """
        try:
            csv = self.k8s_client.custom_objects_api.get_namespaced_custom_object(
                group="operators.coreos.com",
                version="v1alpha1",
                namespace=namespace,
                plural="clusterserviceversions",
                name=csv_name
            )
            
            return self._csv_to_info(csv)
        
        except ApiException as e:
            if e.status == 404:
                return None
            logger.error(f"Failed to get CSV details for {csv_name}: {e}")
            raise

    def _csv_to_info(self, csv: Dict[str, Any]) -> Optional[CSVInfo]:
        """Convert CSV resource to CSVInfo object.
        
        Args:
            csv: CSV resource dictionary
        
        Returns:
            CSVInfo object or None if conversion fails
        """
        try:
            metadata = csv.get('metadata', {})
            spec = csv.get('spec', {})
            status = csv.get('status', {})
            
            # Basic information
            name = metadata.get('name', '')
            namespace = metadata.get('namespace', '')
            display_name = spec.get('displayName', name)
            version = spec.get('version', 'unknown')
            phase = status.get('phase', 'Unknown')
            description = spec.get('description', '')
            
            # Provider information
            provider_spec = spec.get('provider', {})
            provider = provider_spec.get('name', 'Unknown') if provider_spec else 'Unknown'
            
            # Install strategy
            install_strategy = spec.get('installModes', [{}])[0].get('type', 'Unknown') if spec.get('installModes') else 'Unknown'
            
            # Timestamps
            creation_timestamp = metadata.get('creationTimestamp', '')
            
            # Labels and annotations
            labels = metadata.get('labels', {})
            annotations = metadata.get('annotations', {})
            
            # Owned CRDs
            owned_crds = []
            custom_resource_definitions = spec.get('customresourcedefinitions', {})
            if 'owned' in custom_resource_definitions:
                owned_crds = [crd.get('name', '') for crd in custom_resource_definitions['owned']]
            
            # Required CRDs
            required_crds = []
            if 'required' in custom_resource_definitions:
                required_crds = [crd.get('name', '') for crd in custom_resource_definitions['required']]
            
            # Permissions
            permissions = []
            cluster_permissions = []
            install_spec = spec.get('install', {})
            if install_spec.get('strategy') == 'deployment':
                deploy_spec = install_spec.get('spec', {})
                permissions = deploy_spec.get('permissions', [])
                cluster_permissions = deploy_spec.get('clusterPermissions', [])
            
            # Version management
            replaces = spec.get('replaces', '')
            skips = spec.get('skips', [])
            min_kube_version = spec.get('minKubeVersion', '')
            
            return CSVInfo(
                name=name,
                namespace=namespace,
                display_name=display_name,
                version=version,
                phase=phase,
                description=description,
                provider=provider,
                install_strategy=install_strategy,
                creation_timestamp=creation_timestamp,
                labels=labels,
                annotations=annotations,
                owned_crds=owned_crds,
                required_crds=required_crds,
                permissions=permissions,
                cluster_permissions=cluster_permissions,
                replaces=replaces,
                skips=skips,
                min_kube_version=min_kube_version
            )
        
        except Exception as e:
            logger.error(f"Failed to convert CSV to CSVInfo: {e}")
            return None

    def filter_csvs(self, csvs: List[CSVInfo], 
                    namespace_filter: Optional[str] = None,
                    phase_filter: Optional[str] = None,
                    provider_filter: Optional[str] = None) -> List[CSVInfo]:
        """Filter CSVs based on criteria.
        
        Args:
            csvs: List of CSVInfo objects to filter
            namespace_filter: Filter by namespace (exact match)
            phase_filter: Filter by phase (partial match)
            provider_filter: Filter by provider (partial match)
        
        Returns:
            Filtered list of CSVInfo objects
        """
        filtered = csvs
        
        if namespace_filter:
            filtered = [csv for csv in filtered if csv.namespace == namespace_filter]
        
        if phase_filter:
            filtered = [csv for csv in filtered if phase_filter.lower() in csv.phase.lower()]
        
        if provider_filter:
            filtered = [csv for csv in filtered if provider_filter.lower() in csv.provider.lower()]
        
        return filtered

    def get_csv_statistics(self, csvs: List[CSVInfo]) -> Dict[str, Any]:
        """Get statistics about ClusterServiceVersions.
        
        Args:
            csvs: List of CSVInfo objects
        
        Returns:
            Dictionary with statistics
        """
        total = len(csvs)
        
        # Group by phase
        phases = {}
        for csv in csvs:
            phases[csv.phase] = phases.get(csv.phase, 0) + 1
        
        # Group by provider
        providers = {}
        for csv in csvs:
            providers[csv.provider] = providers.get(csv.provider, 0) + 1
        
        # Group by namespace
        namespaces = {}
        for csv in csvs:
            namespaces[csv.namespace] = namespaces.get(csv.namespace, 0) + 1
        
        # Count total owned CRDs
        total_owned_crds = sum(len(csv.owned_crds) for csv in csvs)
        
        return {
            'total_csvs': total,
            'by_phase': phases,
            'by_provider': providers,
            'by_namespace': namespaces,
            'total_owned_crds': total_owned_crds,
            'successful_csvs': phases.get('Succeeded', 0),
            'failed_csvs': phases.get('Failed', 0) + phases.get('InstallReady', 0)
        }
