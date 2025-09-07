"""Cluster-related CLI commands."""

import click
import logging
from typing import Optional

from ..core.k8s_client import K8sClient
from ..core.crd_inventory import CRDInventory
from ..core.operator_inventory import OperatorInventory
from ..core.olm_inventory import OLMInventory
from ..utils.formatters import OutputFormatter

logger = logging.getLogger(__name__)


@click.group(name='cluster')
@click.pass_context
def cluster_commands(ctx: click.Context) -> None:
    """Commands for cluster-wide operations."""
    pass


@cluster_commands.command(name='info')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml']), 
              default='table', help='Output format')
@click.pass_context
def cluster_info(ctx: click.Context, output: str) -> None:
    """Show basic cluster information."""
    try:
        # Initialize Kubernetes client
        k8s_client = K8sClient(
            kubeconfig_path=ctx.obj.get('kubeconfig'),
            context=ctx.obj.get('context')
        )
        
        # Test connection
        if not k8s_client.test_connection():
            click.echo("Failed to connect to Kubernetes cluster", err=True)
            ctx.exit(1)
        
        # Get cluster info
        info = k8s_client.get_cluster_info()
        
        if output == 'json':
            import json
            click.echo(json.dumps(info, indent=2, default=str))
        elif output == 'yaml':
            import yaml
            click.echo(yaml.dump(info, default_flow_style=False))
        else:  # table
            click.echo("Cluster Information:")
            click.echo(f"  API Versions: {', '.join(info['version'])}")
            click.echo(f"  Node Count: {info['node_count']}")
            click.echo(f"  Nodes: {', '.join(info['nodes'])}")
        
    except Exception as e:
        logger.error(f"Failed to get cluster info: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@cluster_commands.command(name='summary')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='rich', help='Output format')
@click.option('--namespace', '-n', help='Focus on specific namespace')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def cluster_summary(ctx: click.Context, output: str, namespace: Optional[str], no_color: bool) -> None:
    """Show a comprehensive summary of CRDs and operators."""
    try:
        # Use namespace from context if not provided as option
        target_namespace = namespace or ctx.obj.get('namespace')
        
        # Initialize Kubernetes client
        k8s_client = K8sClient(
            kubeconfig_path=ctx.obj.get('kubeconfig'),
            context=ctx.obj.get('context')
        )
        
        # Test connection
        if not k8s_client.test_connection():
            click.echo("Failed to connect to Kubernetes cluster", err=True)
            ctx.exit(1)
        
        # Get CRDs and operators
        if ctx.obj.get('verbose'):
            click.echo("Gathering cluster inventory...")
        
        crd_inventory = CRDInventory(k8s_client)
        operator_inventory = OperatorInventory(k8s_client)
        olm_inventory = OLMInventory(k8s_client)
        
        crds = crd_inventory.list_crds()
        operators = operator_inventory.list_operators(namespace=target_namespace)
        csvs = olm_inventory.list_csvs(namespace=target_namespace)
        
        # Filter operators by namespace if specified
        if target_namespace:
            operators = [op for op in operators if op.namespace == target_namespace]
        
        # Format and display summary
        formatter = OutputFormatter(use_color=not no_color)
        output_text = formatter.format_summary(crds, operators, csvs, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to generate cluster summary: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@cluster_commands.command(name='test-connection')
@click.pass_context
def test_connection(ctx: click.Context) -> None:
    """Test connection to the Kubernetes cluster."""
    try:
        # Initialize Kubernetes client
        k8s_client = K8sClient(
            kubeconfig_path=ctx.obj.get('kubeconfig'),
            context=ctx.obj.get('context')
        )
        
        # Test connection
        if k8s_client.test_connection():
            click.echo("✓ Successfully connected to Kubernetes cluster")
            
            if ctx.obj.get('verbose'):
                info = k8s_client.get_cluster_info()
                click.echo(f"  Context: {ctx.obj.get('context') or 'default'}")
                click.echo(f"  Nodes: {info['node_count']}")
        else:
            click.echo("✗ Failed to connect to Kubernetes cluster", err=True)
            ctx.exit(1)
        
    except Exception as e:
        logger.error(f"Connection test failed: {e}")
        click.echo(f"✗ Connection test failed: {e}", err=True)
        ctx.exit(1)


@cluster_commands.command(name='export')
@click.option('--output', '-o', type=click.Choice(['json', 'yaml']), 
              default='json', help='Export format')
@click.option('--file', '-f', help='Output file (default: stdout)')
@click.option('--namespace', '-n', help='Focus on specific namespace for operators')
@click.option('--include-crds/--no-crds', default=True, help='Include CRDs in export')
@click.option('--include-operators/--no-operators', default=True, help='Include operators in export')
@click.option('--include-olm/--no-olm', default=True, help='Include OLM ClusterServiceVersions in export')
@click.pass_context
def export_inventory(ctx: click.Context, output: str, file: Optional[str], 
                     namespace: Optional[str], include_crds: bool, include_operators: bool, include_olm: bool) -> None:
    """Export complete inventory to file or stdout."""
    try:
        # Use namespace from context if not provided as option
        target_namespace = namespace or ctx.obj.get('namespace')
        
        # Initialize Kubernetes client
        k8s_client = K8sClient(
            kubeconfig_path=ctx.obj.get('kubeconfig'),
            context=ctx.obj.get('context')
        )
        
        # Test connection
        if not k8s_client.test_connection():
            click.echo("Failed to connect to Kubernetes cluster", err=True)
            ctx.exit(1)
        
        # Prepare export data
        export_data = {
            "cluster_info": k8s_client.get_cluster_info(),
            "export_timestamp": None,
            "namespace_filter": target_namespace
        }
        
        # Add timestamp
        from datetime import datetime, timezone
        export_data["export_timestamp"] = datetime.now(timezone.utc).isoformat()
        
        # Get CRDs if requested
        if include_crds:
            if ctx.obj.get('verbose'):
                click.echo("Gathering CRDs...")
            crd_inventory = CRDInventory(k8s_client)
            crds = crd_inventory.list_crds()
            export_data["crds"] = [crd.to_dict() for crd in crds]
        
        # Get operators if requested
        if include_operators:
            if ctx.obj.get('verbose'):
                click.echo("Gathering operators...")
            operator_inventory = OperatorInventory(k8s_client)
            operators = operator_inventory.list_operators(namespace=target_namespace)
            export_data["operators"] = [op.to_dict() for op in operators]
        
        # Get OLM CSVs if requested
        if include_olm:
            if ctx.obj.get('verbose'):
                click.echo("Gathering OLM ClusterServiceVersions...")
            olm_inventory = OLMInventory(k8s_client)
            csvs = olm_inventory.list_csvs(namespace=target_namespace)
            export_data["olm_csvs"] = [csv.to_dict() for csv in csvs]
        
        # Format output
        if output == 'yaml':
            import yaml
            output_text = yaml.dump(export_data, default_flow_style=False, default=str)
        else:  # json
            import json
            output_text = json.dumps(export_data, indent=2, default=str)
        
        # Write to file or stdout
        if file:
            with open(file, 'w') as f:
                f.write(output_text)
            click.echo(f"Inventory exported to {file}")
        else:
            click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to export inventory: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)
