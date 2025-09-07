"""Main CLI entry point for k8s-inventory-cli."""

import click
from typing import Optional

from .commands.crd import crd_commands
from .commands.operators import operator_commands
from .commands.cluster import cluster_commands
from .commands.olm import olm_commands
from .commands.database import database_commands


@click.group()
@click.option('--kubeconfig', '-k', help='Path to kubeconfig file')
@click.option('--context', '-c', help='Kubernetes context to use')
@click.option('--namespace', '-n', help='Namespace to focus on (default: all)')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.pass_context
def cli(ctx: click.Context, kubeconfig: Optional[str], context: Optional[str], 
        namespace: Optional[str], verbose: bool) -> None:
    """K8s Inventory CLI - Inventory CRDs and operators in Kubernetes clusters."""
    ctx.ensure_object(dict)
    ctx.obj['kubeconfig'] = kubeconfig
    ctx.obj['context'] = context
    ctx.obj['namespace'] = namespace
    ctx.obj['verbose'] = verbose


# Add command groups
cli.add_command(crd_commands)
cli.add_command(operator_commands)
cli.add_command(cluster_commands)
cli.add_command(olm_commands)
cli.add_command(database_commands)


if __name__ == '__main__':
    cli()
