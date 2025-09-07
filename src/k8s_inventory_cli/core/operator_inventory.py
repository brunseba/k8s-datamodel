"""Operators inventory service for Kubernetes clusters."""

from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass, asdict
from kubernetes.client.rest import ApiException
import logging
import re

from .k8s_client import K8sClient
from .olm_inventory import OLMInventory

logger = logging.getLogger(__name__)


@dataclass
class OperatorInfo:
    """Information about a Kubernetes operator."""
    name: str
    namespace: str
    operator_type: str  # deployment, statefulset, etc.
    image: str
    version: Optional[str]
    creation_timestamp: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    replicas: int
    ready_replicas: int
    conditions: List[Dict[str, Any]]
    managed_crds: List[str]  # CRDs this operator manages
    managed_resources: List[str]  # Other resources this operator manages
    operator_framework: Optional[str]  # OLM, Helm, manual, etc.

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class OperatorInventory:
    """Service for inventorying operators in Kubernetes clusters."""

    def __init__(self, k8s_client: K8sClient):
        """Initialize operator inventory service.
        
        Args:
            k8s_client: Kubernetes client instance
        """
        self.k8s_client = k8s_client

    def list_operators(self, namespace: Optional[str] = None) -> List[OperatorInfo]:
        """List all operators in the cluster or specific namespace.
        
        Args:
            namespace: Specific namespace to search (None for all namespaces)
        
        Returns:
            List of OperatorInfo objects
        """
        operators = []
        
        # Get deployments that look like operators
        operators.extend(self._get_operator_deployments(namespace))
        
        # Get statefulsets that look like operators
        operators.extend(self._get_operator_statefulsets(namespace))
        
        # Enhance with CRD ownership information
        self._enhance_with_crd_ownership(operators)
        
        # Enhance with OLM information
        self._enhance_with_olm_info(operators)
        
        return sorted(operators, key=lambda x: (x.namespace, x.name))

    def _get_operator_deployments(self, namespace: Optional[str] = None) -> List[OperatorInfo]:
        """Get deployments that appear to be operators.
        
        Args:
            namespace: Specific namespace to search
        
        Returns:
            List of OperatorInfo objects from deployments
        """
        operators = []
        
        try:
            if namespace:
                deployments = self.k8s_client.apps_v1_api.list_namespaced_deployment(namespace)
            else:
                deployments = self.k8s_client.apps_v1_api.list_deployment_for_all_namespaces()
            
            for deployment in deployments.items:
                if self._is_operator_deployment(deployment):
                    operator_info = self._deployment_to_operator_info(deployment)
                    operators.append(operator_info)
                    
        except ApiException as e:
            logger.error(f"Failed to list deployments: {e}")
            
        return operators

    def _get_operator_statefulsets(self, namespace: Optional[str] = None) -> List[OperatorInfo]:
        """Get statefulsets that appear to be operators.
        
        Args:
            namespace: Specific namespace to search
        
        Returns:
            List of OperatorInfo objects from statefulsets
        """
        operators = []
        
        try:
            if namespace:
                statefulsets = self.k8s_client.apps_v1_api.list_namespaced_stateful_set(namespace)
            else:
                statefulsets = self.k8s_client.apps_v1_api.list_stateful_set_for_all_namespaces()
            
            for statefulset in statefulsets.items:
                if self._is_operator_statefulset(statefulset):
                    operator_info = self._statefulset_to_operator_info(statefulset)
                    operators.append(operator_info)
                    
        except ApiException as e:
            logger.error(f"Failed to list statefulsets: {e}")
            
        return operators

    def _is_operator_deployment(self, deployment) -> bool:
        """Check if a deployment appears to be an operator.
        
        Args:
            deployment: Kubernetes deployment object
        
        Returns:
            True if deployment appears to be an operator
        """
        name = deployment.metadata.name.lower()
        labels = deployment.metadata.labels or {}
        annotations = deployment.metadata.annotations or {}
        
        # Common operator indicators
        operator_indicators = [
            'operator' in name,
            'controller' in name,
            'manager' in name,
            any('operator' in k.lower() or 'operator' in v.lower() for k, v in labels.items()),
            any('olm' in k.lower() for k in annotations.keys()),
            'app.kubernetes.io/name' in labels and 'operator' in labels['app.kubernetes.io/name'].lower(),
            'control-plane' in labels.get('app.kubernetes.io/component', '').lower(),
        ]
        
        return any(operator_indicators)

    def _is_operator_statefulset(self, statefulset) -> bool:
        """Check if a statefulset appears to be an operator.
        
        Args:
            statefulset: Kubernetes statefulset object
        
        Returns:
            True if statefulset appears to be an operator
        """
        name = statefulset.metadata.name.lower()
        labels = statefulset.metadata.labels or {}
        
        operator_indicators = [
            'operator' in name,
            'controller' in name,
            'manager' in name,
            any('operator' in k.lower() or 'operator' in v.lower() for k, v in labels.items()),
            'control-plane' in labels.get('app.kubernetes.io/component', '').lower(),
        ]
        
        return any(operator_indicators)

    def _deployment_to_operator_info(self, deployment) -> OperatorInfo:
        """Convert deployment to OperatorInfo.
        
        Args:
            deployment: Kubernetes deployment object
        
        Returns:
            OperatorInfo object
        """
        # Extract image information
        image = ""
        version = None
        
        if deployment.spec.template.spec.containers:
            container = deployment.spec.template.spec.containers[0]
            image = container.image
            # Try to extract version from image tag
            if ':' in image:
                tag = image.split(':')[-1]
                if tag != 'latest' and not tag.startswith('sha256:'):
                    version = tag

        # Extract framework information
        framework = self._detect_operator_framework(deployment.metadata.labels or {}, 
                                                   deployment.metadata.annotations or {})

        # Build conditions
        conditions = []
        if deployment.status and deployment.status.conditions:
            conditions = [
                {
                    'type': condition.type,
                    'status': condition.status,
                    'reason': condition.reason,
                    'message': condition.message
                }
                for condition in deployment.status.conditions
            ]

        return OperatorInfo(
            name=deployment.metadata.name,
            namespace=deployment.metadata.namespace,
            operator_type="deployment",
            image=image,
            version=version,
            creation_timestamp=deployment.metadata.creation_timestamp.isoformat() if deployment.metadata.creation_timestamp else "",
            labels=deployment.metadata.labels or {},
            annotations=deployment.metadata.annotations or {},
            replicas=deployment.spec.replicas or 0,
            ready_replicas=deployment.status.ready_replicas or 0 if deployment.status else 0,
            conditions=conditions,
            managed_crds=[],
            managed_resources=[],
            operator_framework=framework
        )

    def _statefulset_to_operator_info(self, statefulset) -> OperatorInfo:
        """Convert statefulset to OperatorInfo.
        
        Args:
            statefulset: Kubernetes statefulset object
        
        Returns:
            OperatorInfo object
        """
        # Extract image information
        image = ""
        version = None
        
        if statefulset.spec.template.spec.containers:
            container = statefulset.spec.template.spec.containers[0]
            image = container.image
            if ':' in image:
                tag = image.split(':')[-1]
                if tag != 'latest' and not tag.startswith('sha256:'):
                    version = tag

        framework = self._detect_operator_framework(statefulset.metadata.labels or {}, 
                                                   statefulset.metadata.annotations or {})

        conditions = []
        if statefulset.status and statefulset.status.conditions:
            conditions = [
                {
                    'type': condition.type,
                    'status': condition.status,
                    'reason': condition.reason,
                    'message': condition.message
                }
                for condition in statefulset.status.conditions
            ]

        return OperatorInfo(
            name=statefulset.metadata.name,
            namespace=statefulset.metadata.namespace,
            operator_type="statefulset",
            image=image,
            version=version,
            creation_timestamp=statefulset.metadata.creation_timestamp.isoformat() if statefulset.metadata.creation_timestamp else "",
            labels=statefulset.metadata.labels or {},
            annotations=statefulset.metadata.annotations or {},
            replicas=statefulset.spec.replicas or 0,
            ready_replicas=statefulset.status.ready_replicas or 0 if statefulset.status else 0,
            conditions=conditions,
            managed_crds=[],
            managed_resources=[],
            operator_framework=framework
        )

    def _detect_operator_framework(self, labels: Dict[str, str], annotations: Dict[str, str]) -> Optional[str]:
        """Detect the operator framework being used.
        
        Args:
            labels: Resource labels
            annotations: Resource annotations
        
        Returns:
            Framework name or None
        """
        # Check for OLM (Operator Lifecycle Manager)
        if any('olm' in k.lower() for k in annotations.keys()):
            return "OLM"
        
        # Check for Helm
        if 'app.kubernetes.io/managed-by' in labels:
            if 'helm' in labels['app.kubernetes.io/managed-by'].lower():
                return "Helm"
        
        # Check for common operator annotations
        if 'operators.coreos.com' in str(annotations):
            return "OLM"
            
        if 'helm.sh/chart' in annotations:
            return "Helm"
        
        return "Manual"

    def _enhance_with_crd_ownership(self, operators: List[OperatorInfo]) -> None:
        """Enhance operator info with CRD ownership information.
        
        Args:
            operators: List of OperatorInfo objects to enhance
        """
        try:
            # Get all CRDs
            crds = self.k8s_client.extensions_v1_api.list_custom_resource_definition()
            
            for operator in operators:
                managed_crds = []
                
                for crd in crds.items:
                    # Check if operator name is mentioned in CRD labels or annotations
                    crd_labels = crd.metadata.labels or {}
                    crd_annotations = crd.metadata.annotations or {}
                    
                    # Common patterns for operator ownership
                    if (operator.name.lower() in str(crd_labels).lower() or
                        operator.name.lower() in str(crd_annotations).lower() or
                        any(operator.name.lower() in label.lower() for label in crd_labels.values()) or
                        self._check_image_ownership(operator.image, crd_annotations)):
                        managed_crds.append(crd.metadata.name)
                
                operator.managed_crds = managed_crds
                
        except ApiException as e:
            logger.debug(f"Could not enhance with CRD ownership: {e}")

    def _check_image_ownership(self, operator_image: str, crd_annotations: Dict[str, str]) -> bool:
        """Check if operator image suggests CRD ownership.
        
        Args:
            operator_image: Operator container image
            crd_annotations: CRD annotations
        
        Returns:
            True if ownership is suggested
        """
        if not operator_image:
            return False
            
        # Extract image name without registry and tag
        image_parts = operator_image.split('/')
        image_name = image_parts[-1].split(':')[0]
        
        # Check if image name appears in annotations
        return any(image_name.lower() in value.lower() for value in crd_annotations.values())

    def filter_operators(self, operators: List[OperatorInfo], 
                        namespace_filter: Optional[str] = None,
                        framework_filter: Optional[str] = None,
                        name_filter: Optional[str] = None) -> List[OperatorInfo]:
        """Filter operators based on criteria.
        
        Args:
            operators: List of OperatorInfo objects to filter
            namespace_filter: Filter by namespace (exact match)
            framework_filter: Filter by framework (partial match)
            name_filter: Filter by name (partial match)
        
        Returns:
            Filtered list of OperatorInfo objects
        """
        filtered = operators
        
        if namespace_filter:
            filtered = [op for op in filtered if op.namespace == namespace_filter]
        
        if framework_filter:
            filtered = [op for op in filtered if op.operator_framework and 
                       framework_filter.lower() in op.operator_framework.lower()]
        
        if name_filter:
            filtered = [op for op in filtered if name_filter.lower() in op.name.lower()]
        
        return filtered

    def _enhance_with_olm_info(self, operators: List[OperatorInfo]) -> None:
        """Enhance operator info with OLM ClusterServiceVersion data.
        
        Args:
            operators: List of OperatorInfo objects to enhance
        """
        try:
            # Get OLM CSVs
            olm_inventory = OLMInventory(self.k8s_client)
            csvs = olm_inventory.list_csvs()
            
            # Create mapping of CSV display names to CSV info
            csv_by_display_name = {}
            csv_by_name = {}
            for csv in csvs:
                csv_by_display_name[csv.display_name.lower()] = csv
                csv_by_name[csv.name.lower()] = csv
            
            for operator in operators:
                # Try to match operator with CSV by name similarity
                operator_name_lower = operator.name.lower()
                
                # Look for exact matches or partial matches
                matching_csv = None
                
                # First try exact name match
                if operator_name_lower in csv_by_name:
                    matching_csv = csv_by_name[operator_name_lower]
                elif operator_name_lower in csv_by_display_name:
                    matching_csv = csv_by_display_name[operator_name_lower]
                else:
                    # Try partial matches
                    for csv_name, csv in csv_by_name.items():
                        if operator_name_lower in csv_name or csv_name in operator_name_lower:
                            matching_csv = csv
                            break
                    
                    if not matching_csv:
                        for display_name, csv in csv_by_display_name.items():
                            if operator_name_lower in display_name or display_name in operator_name_lower:
                                matching_csv = csv
                                break
                
                # If we found a matching CSV, update operator info
                if matching_csv:
                    operator.operator_framework = "OLM"
                    # Add CSV-owned CRDs to managed CRDs
                    if matching_csv.owned_crds:
                        existing_crds = set(operator.managed_crds)
                        existing_crds.update(matching_csv.owned_crds)
                        operator.managed_crds = list(existing_crds)
                
        except Exception as e:
            logger.debug(f"Could not enhance with OLM info: {e}")
