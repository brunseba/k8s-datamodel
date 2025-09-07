"""OLM-related CLI commands for ClusterServiceVersions."""

import click
import logging
from typing import Optional

from ..core.k8s_client import K8sClient
from ..core.olm_inventory import OLMInventory
from ..core.database import DatabaseManager
from ..utils.formatters import OutputFormatter

logger = logging.getLogger(__name__)


@click.group(name='olm')
@click.pass_context
def olm_commands(ctx: click.Context) -> None:
    """Commands for managing OLM (Operator Lifecycle Manager) inventory."""
    pass


@olm_commands.command(name='list')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='table', help='Output format')
@click.option('--namespace', '-n', help='Filter by namespace')
@click.option('--phase', '-p', help='Filter by phase (partial match)')
@click.option('--provider', help='Filter by provider (partial match)')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.option('--store-db', '--db', is_flag=True, help='Store results in database')
@click.option('--db-path', help='Path to SQLite database file')
@click.option('--notes', help='Optional notes for database snapshot')
@click.pass_context
def list_csvs(ctx: click.Context, output: str, namespace: Optional[str],
              phase: Optional[str], provider: Optional[str], no_color: bool,
              store_db: bool, db_path: Optional[str], notes: Optional[str]) -> None:
    """List all OLM ClusterServiceVersions in the cluster."""
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
        
        # Get CSVs
        if ctx.obj.get('verbose'):
            click.echo("Fetching OLM ClusterServiceVersions from cluster...")
        
        inventory = OLMInventory(k8s_client)
        csvs = inventory.list_csvs(namespace=target_namespace)
        
        if not csvs:
            click.echo("No OLM ClusterServiceVersions found (OLM may not be installed)")
            return
        
        # Apply filters
        if namespace or phase or provider:
            csvs = inventory.filter_csvs(
                csvs, 
                namespace_filter=namespace,
                phase_filter=phase,
                provider_filter=provider
            )
        
        # Store in database if requested
        if store_db:
            if ctx.obj.get('verbose'):
                click.echo("Storing OLM CSVs in database...")
            
            db_manager = DatabaseManager(db_path)
            cluster_context = ctx.obj.get('context') or 'default'
            cluster_info = k8s_client.get_cluster_info()
            
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context=cluster_context,
                cluster_info=cluster_info,
                crds=[],
                operators=[],
                csvs=csvs,
                namespace_filter=target_namespace,
                notes=notes
            )
            
            click.echo(f"✓ Stored OLM CSVs inventory snapshot #{snapshot_id} ({len(csvs)} CSVs)")
        
        # Format and display output
        formatter = CSVOutputFormatter(use_color=not no_color)
        output_text = formatter.format_csvs(csvs, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to list OLM ClusterServiceVersions: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@olm_commands.command(name='get')
@click.argument('csv_name')
@click.option('--namespace', '-n', required=True, help='CSV namespace')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='yaml', help='Output format')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def get_csv(ctx: click.Context, csv_name: str, namespace: str, output: str, no_color: bool) -> None:
    """Get detailed information about a specific OLM ClusterServiceVersion."""
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
        
        # Get CSV details
        inventory = OLMInventory(k8s_client)
        csv = inventory.get_csv_details(csv_name, namespace)
        
        if not csv:
            click.echo(f"ClusterServiceVersion '{csv_name}' not found in namespace '{namespace}'", err=True)
            ctx.exit(1)
        
        # Format and display output
        formatter = CSVOutputFormatter(use_color=not no_color)
        output_text = formatter.format_csvs([csv], output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to get CSV {csv_name}: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@olm_commands.command(name='count')
@click.option('--namespace', '-n', help='Filter by namespace')
@click.option('--phase', '-p', help='Filter by phase (partial match)')
@click.pass_context
def count_csvs(ctx: click.Context, namespace: Optional[str], phase: Optional[str]) -> None:
    """Count OLM ClusterServiceVersions, optionally with filters."""
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
        
        # Get CSVs
        inventory = OLMInventory(k8s_client)
        csvs = inventory.list_csvs(namespace=target_namespace)
        
        # Apply filters
        if namespace or phase:
            csvs = inventory.filter_csvs(csvs, namespace_filter=namespace, phase_filter=phase)
        
        # Display count
        click.echo(f"Total OLM ClusterServiceVersions: {len(csvs)}")
        
        if ctx.obj.get('verbose') and csvs:
            # Show statistics
            stats = inventory.get_csv_statistics(csvs)
            
            click.echo("\\nBreakdown by phase:")
            for phase_name, count in sorted(stats['by_phase'].items()):
                click.echo(f"  {phase_name}: {count}")
            
            click.echo("\\nBreakdown by provider:")
            for provider_name, count in sorted(stats['by_provider'].items()):
                click.echo(f"  {provider_name}: {count}")
            
            if not target_namespace:
                click.echo("\\nBreakdown by namespace:")
                for ns, count in sorted(stats['by_namespace'].items()):
                    click.echo(f"  {ns}: {count}")
        
    except Exception as e:
        logger.error(f"Failed to count CSVs: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@olm_commands.command(name='status')
@click.option('--namespace', '-n', help='Filter by namespace')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='rich', help='Output format')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def olm_status(ctx: click.Context, namespace: Optional[str], output: str, no_color: bool) -> None:
    """Show OLM status and statistics."""
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
        
        # Get CSVs
        if ctx.obj.get('verbose'):
            click.echo("Analyzing OLM status...")
        
        inventory = OLMInventory(k8s_client)
        csvs = inventory.list_csvs(namespace=target_namespace)
        
        if not csvs:
            click.echo("No OLM ClusterServiceVersions found (OLM may not be installed)")
            return
        
        # Get statistics
        stats = inventory.get_csv_statistics(csvs)
        
        # Format and display output
        formatter = CSVOutputFormatter(use_color=not no_color)
        output_text = formatter.format_olm_status(stats, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to get OLM status: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


class CSVOutputFormatter(OutputFormatter):
    """Extended formatter for ClusterServiceVersions."""

    def format_csvs(self, csvs, output_format: str = "table") -> str:
        """Format CSV list for output."""
        if output_format.lower() == "json":
            return self._format_csvs_json(csvs)
        elif output_format.lower() == "yaml":
            return self._format_csvs_yaml(csvs)
        elif output_format.lower() == "rich":
            return self._format_csvs_rich(csvs)
        else:  # table
            return self._format_csvs_table(csvs)

    def _format_csvs_json(self, csvs) -> str:
        """Format CSVs as JSON."""
        import json
        data = {
            "csvs": [csv.to_dict() for csv in csvs],
            "total_count": len(csvs)
        }
        return json.dumps(data, indent=2, default=str)

    def _format_csvs_yaml(self, csvs) -> str:
        """Format CSVs as YAML."""
        import yaml
        data = {
            "csvs": [csv.to_dict() for csv in csvs],
            "total_count": len(csvs)
        }
        return yaml.dump(data, default_flow_style=False)

    def _format_csvs_table(self, csvs) -> str:
        """Format CSVs as a table."""
        if not csvs:
            return "No OLM ClusterServiceVersions found."

        from tabulate import tabulate

        headers = [
            "Name", "Namespace", "Display Name", "Version", "Phase", 
            "Provider", "Owned CRDs", "Age"
        ]

        rows = []
        for csv in csvs:
            age = self._calculate_age(csv.creation_timestamp)
            owned_crds_count = len(csv.owned_crds)
            
            rows.append([
                csv.name,
                csv.namespace,
                csv.display_name[:40] + "..." if len(csv.display_name) > 40 else csv.display_name,
                csv.version,
                csv.phase,
                csv.provider,
                str(owned_crds_count) if owned_crds_count > 0 else "-",
                age
            ])

        return tabulate(rows, headers=headers, tablefmt="grid")

    def _format_csvs_rich(self, csvs) -> str:
        """Format CSVs using rich formatting."""
        if not csvs:
            return "No OLM ClusterServiceVersions found."

        from rich.table import Table
        from rich.console import Console

        table = Table(title="OLM ClusterServiceVersions")
        table.add_column("Name", style="cyan")
        table.add_column("Namespace", style="magenta")
        table.add_column("Display Name", style="white")
        table.add_column("Version", style="green")
        table.add_column("Phase", style="yellow")
        table.add_column("Provider", style="blue")
        table.add_column("Owned CRDs", justify="right", style="red")
        table.add_column("Age", style="dim")

        for csv in csvs:
            age = self._calculate_age(csv.creation_timestamp)
            owned_crds_count = len(csv.owned_crds)
            
            # Phase with color
            phase_color = {
                'Succeeded': '[green]',
                'Failed': '[red]',
                'Installing': '[yellow]',
                'Pending': '[dim]'
            }
            colored_phase = f"{phase_color.get(csv.phase, '')} {csv.phase}[/]"
            
            table.add_row(
                csv.name,
                csv.namespace,
                csv.display_name[:30] + "..." if len(csv.display_name) > 30 else csv.display_name,
                csv.version,
                colored_phase,
                csv.provider,
                str(owned_crds_count) if owned_crds_count > 0 else "-",
                age
            )

        with self.console.capture() as capture:
            self.console.print(table)
        
        return capture.get()

    def format_olm_status(self, stats: dict, output_format: str = "rich") -> str:
        """Format OLM status statistics."""
        if output_format.lower() == "json":
            import json
            return json.dumps(stats, indent=2)
        elif output_format.lower() == "yaml":
            import yaml
            return yaml.dump(stats, default_flow_style=False)
        elif output_format.lower() == "rich":
            return self._format_olm_status_rich(stats)
        else:  # table
            return self._format_olm_status_table(stats)

    def _format_olm_status_rich(self, stats: dict) -> str:
        """Format OLM status using rich formatting."""
        from rich.panel import Panel

        # Overall status
        status_text = f"Total CSVs: {stats['total_csvs']}\\n"
        status_text += f"Successful: {stats['successful_csvs']}\\n"
        status_text += f"Failed: {stats['failed_csvs']}\\n"
        status_text += f"Total Owned CRDs: {stats['total_owned_crds']}"

        # Phase breakdown
        phase_text = ""
        for phase, count in sorted(stats['by_phase'].items()):
            phase_text += f"{phase}: {count}\\n"

        # Provider breakdown  
        provider_text = ""
        for provider, count in sorted(stats['by_provider'].items()):
            provider_text += f"{provider}: {count}\\n"

        with self.console.capture() as capture:
            self.console.print(Panel(status_text.strip(), title="OLM Status", style="cyan"))
            if phase_text:
                self.console.print(Panel(phase_text.strip(), title="By Phase", style="yellow"))
            if provider_text:
                self.console.print(Panel(provider_text.strip(), title="By Provider", style="green"))
        
        return capture.get()

    def _format_olm_status_table(self, stats: dict) -> str:
        """Format OLM status as simple text."""
        result = f"OLM Status Summary:\\n"
        result += f"  Total CSVs: {stats['total_csvs']}\\n"
        result += f"  Successful: {stats['successful_csvs']}\\n"
        result += f"  Failed: {stats['failed_csvs']}\\n"
        result += f"  Total Owned CRDs: {stats['total_owned_crds']}\\n"
        
        return result
