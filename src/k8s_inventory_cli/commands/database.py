"""Database-related CLI commands for persistent storage."""

import click
import logging
from typing import Optional
from pathlib import Path
import json

from ..core.k8s_client import K8sClient
from ..core.crd_inventory import CRDInventory
from ..core.operator_inventory import OperatorInventory
from ..core.olm_inventory import OLMInventory
from ..core.database import DatabaseManager
from ..utils.formatters import OutputFormatter

logger = logging.getLogger(__name__)


@click.group(name='database')
@click.option('--db-path', help='Path to SQLite database file')
@click.pass_context
def database_commands(ctx: click.Context, db_path: Optional[str]) -> None:
    """Commands for database operations and persistent storage."""
    ctx.ensure_object(dict)
    ctx.obj['db_path'] = db_path


@database_commands.command(name='store')
@click.option('--notes', help='Optional notes for this snapshot')
@click.option('--include-crds/--no-crds', default=True, help='Include CRDs in snapshot')
@click.option('--include-operators/--no-operators', default=True, help='Include operators in snapshot')
@click.option('--include-olm/--no-olm', default=True, help='Include OLM CSVs in snapshot')
@click.pass_context
def store_snapshot(ctx: click.Context, notes: Optional[str], include_crds: bool, 
                  include_operators: bool, include_olm: bool) -> None:
    """Store current cluster inventory as a database snapshot."""
    try:
        # Initialize components
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        k8s_client = K8sClient(
            kubeconfig_path=ctx.obj.get('kubeconfig'),
            context=ctx.obj.get('context')
        )
        
        # Test connection
        if not k8s_client.test_connection():
            click.echo("Failed to connect to Kubernetes cluster", err=True)
            ctx.exit(1)
        
        if ctx.obj.get('verbose'):
            click.echo("Gathering cluster inventory for database storage...")
        
        # Get cluster information
        cluster_context = ctx.obj.get('context') or 'default'
        cluster_info = k8s_client.get_cluster_info()
        namespace_filter = ctx.obj.get('namespace')
        
        # Collect inventory data based on options
        crds = []
        operators = []
        csvs = []
        
        if include_crds:
            if ctx.obj.get('verbose'):
                click.echo("  Collecting CRDs...")
            crd_inventory = CRDInventory(k8s_client)
            crds = crd_inventory.list_crds()
            if namespace_filter:
                # Filter CRDs if needed (though most CRDs are cluster-scoped)
                pass
        
        if include_operators:
            if ctx.obj.get('verbose'):
                click.echo("  Collecting operators...")
            operator_inventory = OperatorInventory(k8s_client)
            operators = operator_inventory.list_operators(namespace=namespace_filter)
        
        if include_olm:
            if ctx.obj.get('verbose'):
                click.echo("  Collecting OLM CSVs...")
            olm_inventory = OLMInventory(k8s_client)
            csvs = olm_inventory.list_csvs(namespace=namespace_filter)
        
        # Store snapshot
        snapshot_id = db_manager.store_inventory_snapshot(
            cluster_context=cluster_context,
            cluster_info=cluster_info,
            crds=crds,
            operators=operators,
            csvs=csvs,
            namespace_filter=namespace_filter,
            notes=notes
        )
        
        click.echo(f"✓ Stored inventory snapshot #{snapshot_id}")
        click.echo(f"  CRDs: {len(crds)}, Operators: {len(operators)}, CSVs: {len(csvs)}")
        if namespace_filter:
            click.echo(f"  Namespace filter: {namespace_filter}")
        if notes:
            click.echo(f"  Notes: {notes}")
        
    except Exception as e:
        logger.error(f"Failed to store snapshot: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='list')
@click.option('--cluster-context', help='Filter by cluster context')
@click.option('--limit', type=int, help='Maximum number of snapshots to show')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='table', help='Output format')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def list_snapshots(ctx: click.Context, cluster_context: Optional[str], limit: Optional[int],
                  output: str, no_color: bool) -> None:
    """List stored inventory snapshots."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        snapshots = db_manager.list_snapshots(
            cluster_context=cluster_context, 
            limit=limit
        )
        
        if not snapshots:
            click.echo("No snapshots found.")
            return
        
        # Format output
        formatter = DatabaseOutputFormatter(use_color=not no_color)
        output_text = formatter.format_snapshots(snapshots, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to list snapshots: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='show')
@click.argument('snapshot_id', type=int)
@click.option('--output', '-o', type=click.Choice(['json', 'yaml']), 
              default='yaml', help='Output format')
@click.pass_context
def show_snapshot(ctx: click.Context, snapshot_id: int, output: str) -> None:
    """Show detailed information about a specific snapshot."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        snapshot_data = db_manager.get_snapshot_data(snapshot_id)
        
        if output == 'json':
            click.echo(json.dumps(snapshot_data, indent=2, default=str))
        else:  # yaml
            import yaml
            click.echo(yaml.dump(snapshot_data, default_flow_style=False, default=str))
        
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)
    except Exception as e:
        logger.error(f"Failed to show snapshot: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='delete')
@click.argument('snapshot_id', type=int)
@click.option('--yes', '-y', is_flag=True, help='Skip confirmation prompt')
@click.pass_context
def delete_snapshot(ctx: click.Context, snapshot_id: int, yes: bool) -> None:
    """Delete a stored snapshot."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        
        if not yes:
            if not click.confirm(f"Are you sure you want to delete snapshot #{snapshot_id}?"):
                click.echo("Aborted.")
                return
        
        if db_manager.delete_snapshot(snapshot_id):
            click.echo(f"✓ Deleted snapshot #{snapshot_id}")
        else:
            click.echo(f"Snapshot #{snapshot_id} not found", err=True)
            ctx.exit(1)
        
    except Exception as e:
        logger.error(f"Failed to delete snapshot: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='stats')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='rich', help='Output format')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def database_stats(ctx: click.Context, output: str, no_color: bool) -> None:
    """Show database statistics."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        stats = db_manager.get_database_stats()
        
        formatter = DatabaseOutputFormatter(use_color=not no_color)
        output_text = formatter.format_database_stats(stats, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to get database stats: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='cleanup')
@click.option('--keep', type=int, default=10, help='Number of snapshots to keep per cluster')
@click.option('--cluster-context', help='Specific cluster context to clean')
@click.option('--yes', '-y', is_flag=True, help='Skip confirmation prompt')
@click.pass_context
def cleanup_snapshots(ctx: click.Context, keep: int, cluster_context: Optional[str], yes: bool) -> None:
    """Clean up old snapshots, keeping only the most recent ones."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        
        if not yes:
            context_msg = f" for context '{cluster_context}'" if cluster_context else ""
            if not click.confirm(f"Clean up old snapshots{context_msg}, keeping {keep} most recent?"):
                click.echo("Aborted.")
                return
        
        deleted_count = db_manager.cleanup_old_snapshots(
            keep_count=keep, 
            cluster_context=cluster_context
        )
        
        if deleted_count > 0:
            click.echo(f"✓ Cleaned up {deleted_count} old snapshots")
        else:
            click.echo("No snapshots to clean up")
        
    except Exception as e:
        logger.error(f"Failed to cleanup snapshots: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@database_commands.command(name='export')
@click.argument('snapshot_id', type=int)
@click.option('--file', '-f', help='Output file (default: stdout)')
@click.option('--output', '-o', type=click.Choice(['json', 'yaml']), 
              default='json', help='Export format')
@click.pass_context
def export_snapshot(ctx: click.Context, snapshot_id: int, file: Optional[str], output: str) -> None:
    """Export a snapshot to file or stdout."""
    try:
        db_manager = DatabaseManager(ctx.obj.get('db_path'))
        snapshot_data = db_manager.get_snapshot_data(snapshot_id)
        
        # Format output
        if output == 'yaml':
            import yaml
            output_text = yaml.dump(snapshot_data, default_flow_style=False, default=str)
        else:  # json
            output_text = json.dumps(snapshot_data, indent=2, default=str)
        
        # Write to file or stdout
        if file:
            with open(file, 'w') as f:
                f.write(output_text)
            click.echo(f"Snapshot #{snapshot_id} exported to {file}")
        else:
            click.echo(output_text)
        
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)
    except Exception as e:
        logger.error(f"Failed to export snapshot: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


class DatabaseOutputFormatter(OutputFormatter):
    """Extended formatter for database-related outputs."""

    def format_snapshots(self, snapshots, output_format: str = "table") -> str:
        """Format snapshots list for output."""
        if output_format.lower() == "json":
            return self._format_snapshots_json(snapshots)
        elif output_format.lower() == "yaml":
            return self._format_snapshots_yaml(snapshots)
        elif output_format.lower() == "rich":
            return self._format_snapshots_rich(snapshots)
        else:  # table
            return self._format_snapshots_table(snapshots)

    def _format_snapshots_json(self, snapshots) -> str:
        """Format snapshots as JSON."""
        data = {
            "snapshots": [snapshot.to_dict() for snapshot in snapshots],
            "total_count": len(snapshots)
        }
        return json.dumps(data, indent=2, default=str)

    def _format_snapshots_yaml(self, snapshots) -> str:
        """Format snapshots as YAML."""
        import yaml
        data = {
            "snapshots": [snapshot.to_dict() for snapshot in snapshots],
            "total_count": len(snapshots)
        }
        return yaml.dump(data, default_flow_style=False)

    def _format_snapshots_table(self, snapshots) -> str:
        """Format snapshots as a table."""
        if not snapshots:
            return "No snapshots found."

        from tabulate import tabulate

        headers = [
            "ID", "Timestamp", "Context", "CRDs", "Operators", 
            "CSVs", "Namespace", "Notes"
        ]

        rows = []
        for snapshot in snapshots:
            # Parse timestamp for better display
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(snapshot.timestamp.replace('Z', '+00:00'))
                timestamp_display = dt.strftime('%Y-%m-%d %H:%M')
            except:
                timestamp_display = snapshot.timestamp[:16]
            
            notes_display = (snapshot.notes[:30] + "...") if snapshot.notes and len(snapshot.notes) > 30 else (snapshot.notes or "")
            
            rows.append([
                snapshot.id,
                timestamp_display,
                snapshot.cluster_context,
                snapshot.crd_count,
                snapshot.operator_count,
                snapshot.csv_count,
                snapshot.namespace_filter or "all",
                notes_display
            ])

        return tabulate(rows, headers=headers, tablefmt="grid")

    def _format_snapshots_rich(self, snapshots) -> str:
        """Format snapshots using rich formatting."""
        if not snapshots:
            return "No snapshots found."

        from rich.table import Table

        table = Table(title="Stored Inventory Snapshots")
        table.add_column("ID", style="cyan", width=6)
        table.add_column("Timestamp", style="dim")
        table.add_column("Context", style="magenta")
        table.add_column("CRDs", justify="right", style="green")
        table.add_column("Operators", justify="right", style="blue")
        table.add_column("CSVs", justify="right", style="yellow")
        table.add_column("Namespace", style="white")
        table.add_column("Notes", style="dim", max_width=30)

        for snapshot in snapshots:
            # Parse timestamp for better display
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(snapshot.timestamp.replace('Z', '+00:00'))
                timestamp_display = dt.strftime('%Y-%m-%d %H:%M')
            except:
                timestamp_display = snapshot.timestamp[:16]

            table.add_row(
                str(snapshot.id),
                timestamp_display,
                snapshot.cluster_context,
                str(snapshot.crd_count),
                str(snapshot.operator_count),
                str(snapshot.csv_count),
                snapshot.namespace_filter or "all",
                (snapshot.notes[:25] + "...") if snapshot.notes and len(snapshot.notes) > 25 else (snapshot.notes or "")
            )

        with self.console.capture() as capture:
            self.console.print(table)
        
        return capture.get()

    def format_database_stats(self, stats: dict, output_format: str = "rich") -> str:
        """Format database statistics."""
        if output_format.lower() == "json":
            return json.dumps(stats, indent=2, default=str)
        elif output_format.lower() == "yaml":
            import yaml
            return yaml.dump(stats, default_flow_style=False)
        elif output_format.lower() == "rich":
            return self._format_database_stats_rich(stats)
        else:  # table
            return self._format_database_stats_table(stats)

    def _format_database_stats_rich(self, stats: dict) -> str:
        """Format database stats using rich formatting."""
        from rich.panel import Panel

        # General stats
        general_stats = f"Database Path: {stats['db_path']}\\n"
        general_stats += f"File Size: {self._format_bytes(stats['db_file_size'])}\\n"
        general_stats += f"Total Snapshots: {stats['total_snapshots']}"

        # Data counts
        data_stats = f"Total CRDs: {stats['total_crds']}\\n"
        data_stats += f"Total Operators: {stats['total_operators']}\\n"
        data_stats += f"Total CSVs: {stats['total_csvs']}"

        # Cluster contexts
        contexts_stats = "\\n".join(stats['cluster_contexts']) if stats['cluster_contexts'] else "None"

        # Date range
        date_stats = ""
        if stats['oldest_snapshot'] and stats['newest_snapshot']:
            date_stats = f"Oldest: {stats['oldest_snapshot'][:16]}\\n"
            date_stats += f"Newest: {stats['newest_snapshot'][:16]}"
        else:
            date_stats = "No snapshots"

        with self.console.capture() as capture:
            self.console.print(Panel(general_stats.strip(), title="Database Info", style="cyan"))
            self.console.print(Panel(data_stats.strip(), title="Data Counts", style="green"))
            if stats['cluster_contexts']:
                self.console.print(Panel(contexts_stats.strip(), title="Cluster Contexts", style="magenta"))
            self.console.print(Panel(date_stats.strip(), title="Date Range", style="yellow"))
        
        return capture.get()

    def _format_database_stats_table(self, stats: dict) -> str:
        """Format database stats as simple text."""
        result = "Database Statistics:\\n"
        result += f"  Path: {stats['db_path']}\\n"
        result += f"  File Size: {self._format_bytes(stats['db_file_size'])}\\n"
        result += f"  Total Snapshots: {stats['total_snapshots']}\\n"
        result += f"  Total CRDs: {stats['total_crds']}\\n"
        result += f"  Total Operators: {stats['total_operators']}\\n"
        result += f"  Total CSVs: {stats['total_csvs']}\\n"
        
        if stats['cluster_contexts']:
            result += f"  Cluster Contexts: {', '.join(stats['cluster_contexts'])}\\n"
        
        return result

    def _format_bytes(self, size_bytes: int) -> str:
        """Format bytes to human readable size."""
        if size_bytes == 0:
            return "0B"
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        return f"{size_bytes:.1f}{size_names[i]}"
