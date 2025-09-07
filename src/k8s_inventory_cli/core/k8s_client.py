"""Kubernetes client wrapper for cluster operations."""

from typing import Optional, Dict, Any, List
import os
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import logging

logger = logging.getLogger(__name__)


class K8sClient:
    """Kubernetes client wrapper with cluster connection management."""

    def __init__(self, kubeconfig_path: Optional[str] = None, context: Optional[str] = None):
        """Initialize Kubernetes client.
        
        Args:
            kubeconfig_path: Path to kubeconfig file (optional)
            context: Kubernetes context to use (optional)
        """
        self.kubeconfig_path = kubeconfig_path
        self.context = context
        self._api_client = None
        self._custom_objects_api = None
        self._apps_v1_api = None
        self._core_v1_api = None
        self._extensions_v1_api = None
        
        self._load_config()

    def _load_config(self) -> None:
        """Load Kubernetes configuration."""
        try:
            if self.kubeconfig_path and os.path.exists(self.kubeconfig_path):
                config.load_kube_config(config_file=self.kubeconfig_path, context=self.context)
            else:
                # Try in-cluster config first, then default kubeconfig
                try:
                    config.load_incluster_config()
                    logger.info("Using in-cluster configuration")
                except config.ConfigException:
                    config.load_kube_config(context=self.context)
                    logger.info(f"Using kubeconfig with context: {self.context or 'default'}")
            
            self._api_client = client.ApiClient()
            self._custom_objects_api = client.CustomObjectsApi(self._api_client)
            self._apps_v1_api = client.AppsV1Api(self._api_client)
            self._core_v1_api = client.CoreV1Api(self._api_client)
            self._extensions_v1_api = client.ApiextensionsV1Api(self._api_client)
            
        except Exception as e:
            logger.error(f"Failed to load Kubernetes configuration: {e}")
            raise

    @property
    def custom_objects_api(self) -> client.CustomObjectsApi:
        """Get CustomObjectsApi instance."""
        return self._custom_objects_api

    @property
    def apps_v1_api(self) -> client.AppsV1Api:
        """Get AppsV1Api instance."""
        return self._apps_v1_api

    @property
    def core_v1_api(self) -> client.CoreV1Api:
        """Get CoreV1Api instance."""
        return self._core_v1_api

    @property
    def extensions_v1_api(self) -> client.ApiextensionsV1Api:
        """Get ApiextensionsV1Api instance."""
        return self._extensions_v1_api

    def test_connection(self) -> bool:
        """Test the Kubernetes cluster connection.
        
        Returns:
            True if connection is successful, False otherwise
        """
        try:
            # Try to list namespaces as a simple connection test
            self._core_v1_api.list_namespace(limit=1)
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            return False

    def get_cluster_info(self) -> Dict[str, Any]:
        """Get basic cluster information.
        
        Returns:
            Dictionary containing cluster information
        """
        try:
            # Get nodes
            nodes = self._core_v1_api.list_node()
            
            # Try to get version info (simplified)
            version_info = "unknown"
            try:
                import subprocess
                result = subprocess.run(['kubectl', 'version', '--client=false', '--short=true'], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    version_info = result.stdout.strip()
            except Exception:
                pass
            
            return {
                'version': [version_info],
                'node_count': len(nodes.items),
                'nodes': [node.metadata.name for node in nodes.items]
            }
        except ApiException as e:
            logger.error(f"Failed to get cluster info: {e}")
            raise
