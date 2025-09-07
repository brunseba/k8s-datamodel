"""CRD-related CLI commands."""

import click
from typing import Optional, Dict, Any
import logging
import os
from pathlib import Path

from ..core.k8s_client import K8sClient
from ..core.crd_inventory import CRDInventory
from ..utils.formatters import OutputFormatter

logger = logging.getLogger(__name__)


@click.group(name='crd')
@click.pass_context
def crd_commands(ctx: click.Context) -> None:
    """Commands for managing Custom Resource Definitions inventory."""
    pass


@crd_commands.command(name='list')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='table', help='Output format')
@click.option('--group', '-g', help='Filter by API group (partial match)')
@click.option('--kind', '-k', help='Filter by kind (partial match)')
@click.option('--scope', '-s', type=click.Choice(['Namespaced', 'Cluster']), 
              help='Filter by scope')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.option('--store-db', '--db', is_flag=True, help='Store results in database')
@click.option('--db-path', help='Path to SQLite database file')
@click.option('--notes', help='Optional notes for database snapshot')
@click.pass_context
def list_crds(ctx: click.Context, output: str, group: Optional[str], 
              kind: Optional[str], scope: Optional[str], no_color: bool,
              store_db: bool, db_path: Optional[str], notes: Optional[str]) -> None:
    """List all Custom Resource Definitions in the cluster."""
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
        
        # Get CRDs
        if ctx.obj.get('verbose'):
            click.echo("Fetching CRDs from cluster...")
        
        inventory = CRDInventory(k8s_client)
        crds = inventory.list_crds()
        
        # Apply filters
        if group or kind or scope:
            crds = inventory.filter_crds(crds, group_filter=group, 
                                       kind_filter=kind, scope_filter=scope)
        
        # Store in database if requested
        if store_db:
            if ctx.obj.get('verbose'):
                click.echo("Storing CRDs in database...")
            
            db_manager = DatabaseManager(db_path)
            cluster_context = ctx.obj.get('context') or 'default'
            cluster_info = k8s_client.get_cluster_info()
            namespace_filter = ctx.obj.get('namespace')
            
            snapshot_id = db_manager.store_inventory_snapshot(
                cluster_context=cluster_context,
                cluster_info=cluster_info,
                crds=crds,
                operators=[],
                csvs=[],
                namespace_filter=namespace_filter,
                notes=notes
            )
            
            click.echo(f"✓ Stored CRD inventory snapshot #{snapshot_id} ({len(crds)} CRDs)")
        
        # Format and display output
        formatter = OutputFormatter(use_color=not no_color)
        output_text = formatter.format_crds(crds, output_format=output)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to list CRDs: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@crd_commands.command(name='get')
@click.argument('crd_name')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='rich', help='Output format')
@click.option('--properties', '--props', is_flag=True, 
              help='Show schema properties for the CRD')
@click.option('--version', '-v', help='Specific version to show properties for (default: stored version)')
@click.option('--max-depth', type=int, default=3, 
              help='Maximum depth for nested properties (default: 3)')
@click.option('--required-only', is_flag=True, 
              help='Show only required properties')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.pass_context
def get_crd(ctx: click.Context, crd_name: str, output: str, properties: bool, 
           version: Optional[str], max_depth: int, required_only: bool, no_color: bool) -> None:
    """Get detailed information about a specific CRD."""
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
        
        # Get CRD details
        inventory = CRDInventory(k8s_client)
        crd = inventory.get_crd_details(crd_name)
        
        if not crd:
            click.echo(f"CRD '{crd_name}' not found", err=True)
            ctx.exit(1)
        
        # Format and display output
        formatter = OutputFormatter(use_color=not no_color)
        
        if properties:
            # Show properties information
            output_text = formatter.format_crd_properties(
                crd, 
                output_format=output,
                version=version,
                max_depth=max_depth,
                required_only=required_only
            )
        else:
            # Show basic CRD information
            output_text = formatter.format_crds([crd], output_format=output)
        
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to get CRD {crd_name}: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@crd_commands.command(name='count')
@click.option('--group', '-g', help='Filter by API group (partial match)')
@click.option('--scope', '-s', type=click.Choice(['Namespaced', 'Cluster']), 
              help='Filter by scope')
@click.pass_context
def count_crds(ctx: click.Context, group: Optional[str], scope: Optional[str]) -> None:
    """Count CRDs, optionally with filters."""
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
        
        # Get CRDs
        inventory = CRDInventory(k8s_client)
        crds = inventory.list_crds()
        
        # Apply filters
        if group or scope:
            crds = inventory.filter_crds(crds, group_filter=group, scope_filter=scope)
        
        # Display count
        click.echo(f"Total CRDs: {len(crds)}")
        
        if ctx.obj.get('verbose'):
            # Show breakdown by group
            groups = {}
            for crd in crds:
                groups[crd.group] = groups.get(crd.group, 0) + 1
            
            click.echo("\nBreakdown by group:")
            for group_name, count in sorted(groups.items()):
                click.echo(f"  {group_name}: {count}")
        
    except Exception as e:
        logger.error(f"Failed to count CRDs: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@crd_commands.command(name='export-all')
@click.option('--output-file', '-f', default='exports/crd-export.md', 
              help='Output markdown file name (default: exports/crd-export.md)')
@click.option('--max-depth', type=int, default=3, 
              help='Maximum depth for nested properties (default: 3)')
@click.option('--required-only', is_flag=True, 
              help='Show only required properties')
@click.option('--group', '-g', help='Filter by API group (partial match)')
@click.option('--scope', '-s', type=click.Choice(['Namespaced', 'Cluster']), 
              help='Filter by scope')
@click.option('--include-toc', is_flag=True, default=True, 
              help='Include table of contents (default: true)')
@click.pass_context
def export_all_crds(ctx: click.Context, output_file: str, max_depth: int, 
                   required_only: bool, group: Optional[str], scope: Optional[str], 
                   include_toc: bool) -> None:
    """Export all CRDs with their properties to a Markdown file."""
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
        
        # Get CRDs with schemas (use include_schemas=True for comprehensive export)
        if ctx.obj.get('verbose'):
            click.echo("Fetching CRDs from cluster with schema information...")
        
        inventory = CRDInventory(k8s_client)
        crds = inventory.list_crds()
        
        # Apply filters
        if group or scope:
            crds = inventory.filter_crds(crds, group_filter=group, scope_filter=scope)
        
        if not crds:
            click.echo("No CRDs found matching the specified criteria.")
            return
        
        if ctx.obj.get('verbose'):
            click.echo(f"Found {len(crds)} CRDs to export...")
        
        # Generate comprehensive markdown with relationship matrices
        markdown_content = inventory.generate_comprehensive_markdown(crds, group_filter=group)
        
        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        click.echo(f"✓ Exported {len(crds)} CRDs to '{output_file}'")
        
        # Show summary
        total_properties = sum(len(crd.schemas.get(crd.stored_version, crd.schemas[list(crd.schemas.keys())[0]] if crd.schemas else {}).properties or {}) 
                              for crd in crds if crd.schemas)
        click.echo(f"  Total properties documented: {total_properties}")
        
    except Exception as e:
        logger.error(f"Failed to export CRDs: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@crd_commands.command(name='groups')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'yaml', 'rich']), 
              default='rich', help='Output format')
@click.option('--group', '-g', help='Filter by API group (partial match)')
@click.option('--scope', '-s', type=click.Choice(['Namespaced', 'Cluster']), 
              help='Filter by scope')
@click.option('--no-color', is_flag=True, help='Disable colored output')
@click.option('--sort-by', type=click.Choice(['name', 'count', 'instances']), 
              default='count', help='Sort groups by criteria')
@click.pass_context
def analyze_groups(ctx: click.Context, output: str, group: Optional[str], 
                  scope: Optional[str], no_color: bool, sort_by: str) -> None:
    """Analyze and synthesize CRDs by API groups."""
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
        
        # Get CRDs
        if ctx.obj.get('verbose'):
            click.echo("Analyzing CRDs by API groups...")
        
        inventory = CRDInventory(k8s_client)
        crds = inventory.list_crds()
        
        # Apply filters
        if group or scope:
            crds = inventory.filter_crds(crds, group_filter=group, scope_filter=scope)
        
        # Get group synthesis
        synthesis = inventory.get_group_synthesis(crds)
        
        # Format and display output
        formatter = CRDGroupFormatter(use_color=not no_color)
        output_text = formatter.format_group_synthesis(synthesis, output_format=output, sort_by=sort_by)
        click.echo(output_text)
        
    except Exception as e:
        logger.error(f"Failed to analyze CRD groups: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@crd_commands.command(name='diagram')
@click.option('--group', '-g', help='Filter by API group (partial match)')
@click.option('--scope', '-s', type=click.Choice(['Namespaced', 'Cluster']), 
              help='Filter by scope')
@click.option('--file', '-f', help='Output file for diagram (default: stdout)')
@click.option('--format', type=click.Choice(['mermaid', 'markdown', 'pdf']), 
              default='mermaid', help='Output format')
@click.pass_context
def generate_diagram(ctx: click.Context, group: Optional[str], scope: Optional[str], 
                    file: Optional[str], format: str) -> None:
    """Generate Mermaid class diagrams showing CRD schemas by API groups.
    
    Creates one schema diagram per API group, displaying CRD properties,
    types, relationships, and structure based on OpenAPI schema definitions.
    """
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
        
        # Get CRDs
        if ctx.obj.get('verbose'):
            click.echo("Generating Mermaid schema diagrams for CRDs...")
        
        inventory = CRDInventory(k8s_client)
        crds = inventory.list_crds()
        
        # Apply filters
        if group or scope:
            crds = inventory.filter_crds(crds, group_filter=group, scope_filter=scope)
        
        # Generate diagram
        if format == 'markdown':
            # Generate comprehensive markdown documentation
            diagram = inventory.generate_comprehensive_markdown(crds, group_filter=group)
        elif format == 'pdf':
            # Generate comprehensive markdown then convert to PDF
            markdown_content = inventory.generate_comprehensive_markdown(crds, group_filter=group)
            diagram = inventory.convert_markdown_to_pdf(markdown_content, file or 'exports/crd-documentation.pdf')
        else:
            # Generate mermaid diagrams only
            diagram = inventory.generate_mermaid_diagram(crds, group_filter=group)
        
        # Output to file or stdout
        if format == 'pdf':
            # PDF format already creates the file directly
            pdf_file = file or 'exports/crd-documentation.pdf'
            click.echo(f"CRD schema documentation (PDF) written to {pdf_file}")
        elif file:
            # Ensure output directory exists
            output_path = Path(file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file, 'w') as f:
                f.write(diagram)
            if format == 'markdown':
                click.echo(f"CRD schema documentation written to {file}")
            else:
                click.echo(f"CRD schema diagrams written to {file}")
        else:
            click.echo(diagram)
        
    except Exception as e:
        logger.error(f"Failed to generate diagram: {e}")
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


class CRDGroupFormatter(OutputFormatter):
    """Extended formatter for CRD group synthesis."""

    def format_group_synthesis(self, synthesis: Dict[str, Any], 
                              output_format: str = "rich", sort_by: str = "count") -> str:
        """Format group synthesis for output."""
        if output_format.lower() == "json":
            return self._format_synthesis_json(synthesis)
        elif output_format.lower() == "yaml":
            return self._format_synthesis_yaml(synthesis)
        elif output_format.lower() == "rich":
            return self._format_synthesis_rich(synthesis, sort_by)
        else:  # table
            return self._format_synthesis_table(synthesis, sort_by)

    def _format_synthesis_json(self, synthesis: Dict[str, Any]) -> str:
        """Format synthesis as JSON."""
        import json
        return json.dumps(synthesis, indent=2, default=str)

    def _format_synthesis_yaml(self, synthesis: Dict[str, Any]) -> str:
        """Format synthesis as YAML."""
        import yaml
        return yaml.dump(synthesis, default_flow_style=False, default=str)

    def _format_synthesis_table(self, synthesis: Dict[str, Any], sort_by: str = "count") -> str:
        """Format synthesis as a table."""
        if not synthesis['groups']:
            return "No API groups found."
        
        from tabulate import tabulate
        
        # Sort groups
        groups_list = list(synthesis['groups'].items())
        if sort_by == "name":
            groups_list.sort(key=lambda x: x[0])
        elif sort_by == "instances":
            groups_list.sort(key=lambda x: x[1]['total_instances'], reverse=True)
        else:  # count
            groups_list.sort(key=lambda x: x[1]['crd_count'], reverse=True)
        
        # Summary section
        summary_data = [
            ["Total API Groups", synthesis['total_groups']],
            ["Total CRDs", synthesis['total_crds']],
            ["Total Instances", synthesis['total_instances']],
            ["Namespaced CRDs", synthesis['summary']['by_scope']['Namespaced']],
            ["Cluster-scoped CRDs", synthesis['summary']['by_scope']['Cluster']]
        ]
        
        result = "\n=== CRD Groups Summary ===\n"
        result += tabulate(summary_data, headers=["Metric", "Value"], tablefmt="grid")
        
        # Groups breakdown
        headers = ["API Group", "CRDs", "Instances", "Namespaced", "Cluster-scoped", "Versions"]
        rows = []
        
        for group_name, group_data in groups_list:
            versions_str = ", ".join(group_data['versions'][:3])
            if len(group_data['versions']) > 3:
                versions_str += f" (+{len(group_data['versions']) - 3} more)"
            
            rows.append([
                group_name,
                group_data['crd_count'],
                group_data['total_instances'],
                group_data['scopes']['Namespaced'],
                group_data['scopes']['Cluster'],
                versions_str
            ])
        
        result += "\n\n=== API Groups Breakdown ===\n"
        result += tabulate(rows, headers=headers, tablefmt="grid")
        
        # Top active groups
        if synthesis['summary']['most_active_groups']:
            result += "\n\n=== Most Active Groups (by instances) ===\n"
            active_rows = [[name, instances, crds] for name, instances, crds in synthesis['summary']['most_active_groups'][:5]]
            result += tabulate(active_rows, headers=["Group", "Instances", "CRDs"], tablefmt="grid")
        
        return result

    def _format_synthesis_rich(self, synthesis: Dict[str, Any], sort_by: str = "count") -> str:
        """Format synthesis using rich formatting."""
        if not synthesis['groups']:
            return "No API groups found."
        
        from rich.table import Table
        from rich.panel import Panel
        from rich.columns import Columns
        from rich.console import Group
        from rich.text import Text
        
        output_parts = []
        
        # Summary statistics panel
        summary_text = f"""Total API Groups: [bold cyan]{synthesis['total_groups']}[/]
Total CRDs: [bold green]{synthesis['total_crds']}[/]
Total Instances: [bold yellow]{synthesis['total_instances']}[/]

Scope Distribution:
├─ Namespaced: [green]{synthesis['summary']['by_scope']['Namespaced']}[/]
└─ Cluster-scoped: [blue]{synthesis['summary']['by_scope']['Cluster']}[/]

Diversity Metrics:
├─ Single-CRD Groups: {synthesis['summary']['diversity']['single_crd_groups']}
├─ Multi-CRD Groups: {synthesis['summary']['diversity']['multi_crd_groups']}
├─ Largest Group: [bold]{synthesis['summary']['diversity']['largest_group']}[/]
└─ Avg CRDs/Group: {synthesis['summary']['diversity']['average_crds_per_group']:.1f}"""
        
        summary_panel = Panel(summary_text, title="📊 CRD Groups Overview", style="cyan")
        
        # Groups table
        table = Table(title="🗂️ API Groups Analysis")
        table.add_column("API Group", style="magenta")
        table.add_column("CRDs", justify="right", style="green")
        table.add_column("Instances", justify="right", style="yellow")
        table.add_column("Scope Mix", style="blue")
        table.add_column("Versions", style="dim")
        table.add_column("Categories", style="cyan")
        
        # Sort groups
        groups_list = list(synthesis['groups'].items())
        if sort_by == "name":
            groups_list.sort(key=lambda x: x[0])
        elif sort_by == "instances":
            groups_list.sort(key=lambda x: x[1]['total_instances'], reverse=True)
        else:  # count
            groups_list.sort(key=lambda x: x[1]['crd_count'], reverse=True)
        
        for group_name, group_data in groups_list:
            # Scope mix visualization
            ns_count = group_data['scopes']['Namespaced']
            cluster_count = group_data['scopes']['Cluster']
            if ns_count > 0 and cluster_count > 0:
                scope_mix = f"N:{ns_count} C:{cluster_count}"
            elif ns_count > 0:
                scope_mix = f"Namespaced ({ns_count})"
            else:
                scope_mix = f"Cluster ({cluster_count})"
            
            # Versions (show up to 3)
            versions_str = ", ".join(group_data['versions'][:3])
            if len(group_data['versions']) > 3:
                versions_str += f" +{len(group_data['versions']) - 3}"
            
            # Categories (show up to 2)
            categories_str = ", ".join(group_data['categories'][:2])
            if len(group_data['categories']) > 2:
                categories_str += f" +{len(group_data['categories']) - 2}"
            
            table.add_row(
                group_name,
                str(group_data['crd_count']),
                str(group_data['total_instances']),
                scope_mix,
                versions_str or "N/A",
                categories_str or "None"
            )
        
        # Most active groups
        if synthesis['summary']['most_active_groups']:
            active_table = Table(title="🚀 Most Active Groups")
            active_table.add_column("Rank", style="dim", width=4)
            active_table.add_column("Group", style="magenta")
            active_table.add_column("Instances", justify="right", style="yellow")
            active_table.add_column("CRDs", justify="right", style="green")
            
            for i, (name, instances, crds) in enumerate(synthesis['summary']['most_active_groups'][:5], 1):
                rank_style = "gold1" if i == 1 else "silver" if i == 2 else "color(94)" if i == 3 else "dim"
                active_table.add_row(
                    f"[{rank_style}]{i}[/]",
                    name,
                    str(instances),
                    str(crds)
                )
        
        with self.console.capture() as capture:
            self.console.print(summary_panel)
            self.console.print("")
            self.console.print(table)
            if synthesis['summary']['most_active_groups']:
                self.console.print("")
                self.console.print(active_table)
        
        return capture.get()
