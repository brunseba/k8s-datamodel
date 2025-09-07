"""Operators-related CLI commands."""

import click
import logging
from typing import Optional

from ..core.k8s_client import K8sClient
from ..core.operator_inventory import OperatorInventory
from ..core.database import DatabaseManager
from ..utils.formatters import OutputFormatter

logger = logging.getLogger(__name__)


@click.group(name='operators')
@click.pass_context
def operator_commands(ctx: click.Context) -> None:
    """Commands for managing operators inventory."""
    pass


@operator_commands.command(name='list')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='table', help='Output format')
@click.option('--namespace', '-n', help='Filter by namespace')
@click.option('--framework', '-f', help='Filter by framework (partial match)')
@click.option('--name', help='Filter by name (partial match)')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.option('--store-db', '--db', is_flag=True, help='Store results in database')
@click.option('--db-path', help='Path to SQLite database file')
@click.option('--notes', help='Optional notes for database snapshot')
@click.pass_context
def list_operators(ctx: click.Context, output: str, namespace: Optional[str],
                   framework: Optional[str], name: Optional[str], no_color: bool,
                   store_db: bool, db_path: Optional[str], notes: Optional[str]) -> None:
    """List all operators in the cluster."""
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
        
        # Get operators
        if ctx.obj.get('verbose'):
            click.echo("Fetching operators from cluster...")
        
        inventory = OperatorInventory(k8s_client)
        operators = inventory.list_operators(namespace=target_namespace)
        
        # Apply filters
        if namespace or framework or name:
            operators = inventory.filter_operators(
                operators, 
                namespace_filter=namespace,
                framework_filter=framework,
                name_filter=name
            )
        
        # Store in database if requested
        if store_db:
            if ctx.obj.get('verbose'):
                click.echo("Storing operators in database...")
            
            db_manager = DatabaseManager(db_path)
            cluster_context = ctx.obj.get('context') or 'default'
            cluster_info = k8s_client.get_cluster_info()
            
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context=cluster_context,
                cluster_info=cluster_info,
                crds=[],
                operators=operators,
                csvs=[],
                namespace_filter=target_namespace,
                notes=notes
            )
            
            click.echo(f"✓ Stored operators inventory snapshot #{snapshot_id} ({len(operators)} operators)")
        
        # Format and display output
        formatter = OutputFormatter(use_color=not no_color)
        output_text = formatter.format_operators(operators, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to list operators: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@operator_commands.command(name='get')
@click.argument('operator_name')
@click.option('--namespace', '-n', help='Operator namespace (required if operator is namespaced)')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='yaml', help='Output format')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def get_operator(ctx: click.Context, operator_name: str, namespace: Optional[str], 
                 output: str, no_color: bool) -> None:
    """Get detailed information about a specific operator."""
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
        
        # Get all operators and find the one we want
        inventory = OperatorInventory(k8s_client)
        operators = inventory.list_operators(namespace=target_namespace)
        
        # Find the specific operator
        operator = None
        for op in operators:
            if op.name == operator_name:
                if not target_namespace or op.namespace == target_namespace:
                    operator = op
                    break
        
        if not operator:
            if target_namespace:
                click.echo(f"Operator '{operator_name}' not found in namespace '{target_namespace}'", err=True)
            else:
                click.echo(f"Operator '{operator_name}' not found", err=True)
            ctx.exit(1)
        
        # Format and display output
        formatter = OutputFormatter(use_color=not no_color)
        output_text = formatter.format_operators([operator], output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to get operator {operator_name}: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@operator_commands.command(name='count')
@click.option('--namespace', '-n', help='Filter by namespace')
@click.option('--framework', '-f', help='Filter by framework (partial match)')
@click.pass_context
def count_operators(ctx: click.Context, namespace: Optional[str], 
                    framework: Optional[str]) -> None:
    """Count operators, optionally with filters."""
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
        
        # Get operators
        inventory = OperatorInventory(k8s_client)
        operators = inventory.list_operators(namespace=target_namespace)
        
        # Apply filters
        if namespace or framework:
            operators = inventory.filter_operators(
                operators, 
                namespace_filter=namespace,
                framework_filter=framework
            )
        
        # Display count
        click.echo(f"Total Operators: {len(operators)}")
        
        if ctx.obj.get('verbose'):
            # Show breakdown by namespace and framework
            namespaces = {}
            frameworks = {}
            
            for op in operators:
                namespaces[op.namespace] = namespaces.get(op.namespace, 0) + 1
                framework_name = op.operator_framework or "Unknown"
                frameworks[framework_name] = frameworks.get(framework_name, 0) + 1
            
            if not target_namespace:
                click.echo("\\nBreakdown by namespace:")
                for ns, count in sorted(namespaces.items()):
                    click.echo(f"  {ns}: {count}")
            
            click.echo("\\nBreakdown by framework:")
            for framework_name, count in sorted(frameworks.items()):
                click.echo(f"  {framework_name}: {count}")
        
    except Exception as e:
        logger.error(f"Failed to count operators: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@operator_commands.command(name='managed-crds')
@click.argument('operator_name')
@click.option('--namespace', '-n', help='Operator namespace')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'list']), 
              default='list', help='Output format')
@click.pass_context
def list_managed_crds(ctx: click.Context, operator_name: str, namespace: Optional[str], 
                      output: str) -> None:
    """List CRDs managed by a specific operator."""
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
        
        # Get operators and find the one we want
        inventory = OperatorInventory(k8s_client)
        operators = inventory.list_operators(namespace=target_namespace)
        
        # Find the specific operator
        operator = None
        for op in operators:
            if op.name == operator_name:
                if not target_namespace or op.namespace == target_namespace:
                    operator = op
                    break
        
        if not operator:
            if target_namespace:
                click.echo(f"Operator '{operator_name}' not found in namespace '{target_namespace}'", err=True)
            else:
                click.echo(f"Operator '{operator_name}' not found", err=True)
            ctx.exit(1)
        
        # Display managed CRDs
        if not operator.managed_crds:
            click.echo(f"Operator '{operator_name}' manages no CRDs")
            return
        
        if output == 'list':
            click.echo(f"CRDs managed by '{operator_name}':")
            for crd_name in sorted(operator.managed_crds):
                click.echo(f"  - {crd_name}")
        elif output == 'json':
            import json
            data = {
                "operator": operator_name,
                "namespace": operator.namespace,
                "managed_crds": sorted(operator.managed_crds)
            }
            click.echo(json.dumps(data, indent=2))
        elif output == 'yaml':
            import yaml
            data = {
                "operator": operator_name,
                "namespace": operator.namespace,
                "managed_crds": sorted(operator.managed_crds)
            }
            click.echo(yaml.dump(data, default_flow_style=False))
        else:  # table
            from tabulate import tabulate
            headers = ["CRD Name"]
            rows = [[crd_name] for crd_name in sorted(operator.managed_crds)]
            click.echo(tabulate(rows, headers=headers, tablefmt="grid"))
        
    except Exception as e:
        logger.error(f"Failed to list managed CRDs for {operator_name}: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)
