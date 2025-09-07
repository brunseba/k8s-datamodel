"""Output formatting utilities for k8s-datamodel."""

import json
import yaml
from typing import List, Dict, Any, Optional
from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rich_print

from ..core.crd_inventory import CRDInfo
from ..core.operator_inventory import OperatorInfo


class OutputFormatter:
    """Handles different output formats for inventory data."""

    def __init__(self, use_color: bool = True):
        """Initialize formatter.
        
        Args:
            use_color: Whether to use colored output
        """
        self.use_color = use_color
        self.console = Console() if use_color else Console(color_system=None)

    def format_crds(self, crds: List[CRDInfo], output_format: str = "table") -> str:
        """Format CRD list for output.
        
        Args:
            crds: List of CRDInfo objects
            output_format: Output format (table, json, yaml, rich)
        
        Returns:
            Formatted string
        """
        if output_format.lower() == "json":
            return self._format_crds_json(crds)
        elif output_format.lower() == "yaml":
            return self._format_crds_yaml(crds)
        elif output_format.lower() == "rich":
            return self._format_crds_rich(crds)
        else:  # table
            return self._format_crds_table(crds)

    def format_operators(self, operators: List[OperatorInfo], output_format: str = "table") -> str:
        """Format operators list for output.
        
        Args:
            operators: List of OperatorInfo objects
            output_format: Output format (table, json, yaml, rich)
        
        Returns:
            Formatted string
        """
        if output_format.lower() == "json":
            return self._format_operators_json(operators)
        elif output_format.lower() == "yaml":
            return self._format_operators_yaml(operators)
        elif output_format.lower() == "rich":
            return self._format_operators_rich(operators)
        else:  # table
            return self._format_operators_table(operators)

    def _format_crds_json(self, crds: List[CRDInfo]) -> str:
        """Format CRDs as JSON."""
        data = {
            "crds": [crd.to_dict() for crd in crds],
            "total_count": len(crds)
        }
        return json.dumps(data, indent=2, default=str)

    def _format_crds_yaml(self, crds: List[CRDInfo]) -> str:
        """Format CRDs as YAML."""
        data = {
            "crds": [crd.to_dict() for crd in crds],
            "total_count": len(crds)
        }
        return yaml.dump(data, default_flow_style=False)

    def _format_crds_table(self, crds: List[CRDInfo]) -> str:
        """Format CRDs as a table."""
        if not crds:
            return "No CRDs found."

        headers = [
            "Name", "Group", "Version", "Kind", "Scope", 
            "Instances", "Age", "Framework"
        ]

        rows = []
        for crd in crds:
            # Calculate age (simplified)
            age = self._calculate_age(crd.creation_timestamp)
            
            # Detect framework from labels/annotations
            framework = self._detect_crd_framework(crd.labels, crd.annotations)
            
            rows.append([
                crd.name,
                crd.group,
                crd.stored_version,
                crd.kind,
                crd.scope,
                str(crd.instance_count),
                age,
                framework or "Unknown"
            ])

        return tabulate(rows, headers=headers, tablefmt="grid")

    def _format_crds_rich(self, crds: List[CRDInfo]) -> str:
        """Format CRDs using rich formatting."""
        if not crds:
            return "No CRDs found."

        table = Table(title="Custom Resource Definitions")
        table.add_column("Name", style="cyan")
        table.add_column("Group", style="magenta")
        table.add_column("Version", style="yellow")
        table.add_column("Kind", style="green")
        table.add_column("Scope", style="blue")
        table.add_column("Instances", justify="right", style="red")
        table.add_column("Age", style="dim")
        table.add_column("Framework", style="bright_green")

        for crd in crds:
            age = self._calculate_age(crd.creation_timestamp)
            framework = self._detect_crd_framework(crd.labels, crd.annotations)
            
            table.add_row(
                crd.name,
                crd.group,
                crd.stored_version,
                crd.kind,
                crd.scope,
                str(crd.instance_count),
                age,
                framework or "Unknown"
            )

        # Capture table as string
        with self.console.capture() as capture:
            self.console.print(table)
        
        return capture.get()

    def _format_operators_json(self, operators: List[OperatorInfo]) -> str:
        """Format operators as JSON."""
        data = {
            "operators": [op.to_dict() for op in operators],
            "total_count": len(operators)
        }
        return json.dumps(data, indent=2, default=str)

    def _format_operators_yaml(self, operators: List[OperatorInfo]) -> str:
        """Format operators as YAML."""
        data = {
            "operators": [op.to_dict() for op in operators],
            "total_count": len(operators)
        }
        return yaml.dump(data, default_flow_style=False)

    def _format_operators_table(self, operators: List[OperatorInfo]) -> str:
        """Format operators as a table."""
        if not operators:
            return "No operators found."

        headers = [
            "Name", "Namespace", "Type", "Image", "Version", 
            "Replicas", "Ready", "Framework", "Managed CRDs", "Age"
        ]

        rows = []
        for op in operators:
            age = self._calculate_age(op.creation_timestamp)
            
            # Truncate image name for display
            image_display = self._truncate_image(op.image)
            
            # Show count of managed CRDs
            managed_crds_count = len(op.managed_crds)
            managed_crds_display = f"{managed_crds_count}" if managed_crds_count > 0 else "-"
            
            rows.append([
                op.name,
                op.namespace,
                op.operator_type,
                image_display,
                op.version or "-",
                f"{op.ready_replicas}/{op.replicas}",
                "✓" if op.ready_replicas == op.replicas else "✗",
                op.operator_framework or "Unknown",
                managed_crds_display,
                age
            ])

        return tabulate(rows, headers=headers, tablefmt="grid")

    def _format_operators_rich(self, operators: List[OperatorInfo]) -> str:
        """Format operators using rich formatting."""
        if not operators:
            return "No operators found."

        table = Table(title="Kubernetes Operators")
        table.add_column("Name", style="cyan")
        table.add_column("Namespace", style="magenta")
        table.add_column("Type", style="yellow")
        table.add_column("Image", style="blue")
        table.add_column("Version", style="green")
        table.add_column("Replicas", justify="center", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Framework", style="bright_green")
        table.add_column("CRDs", justify="right", style="red")
        table.add_column("Age", style="dim")

        for op in operators:
            age = self._calculate_age(op.creation_timestamp)
            image_display = self._truncate_image(op.image)
            managed_crds_count = len(op.managed_crds)
            
            # Status with color
            if op.ready_replicas == op.replicas:
                status = "[green]✓[/green]"
            else:
                status = "[red]✗[/red]"
            
            table.add_row(
                op.name,
                op.namespace,
                op.operator_type,
                image_display,
                op.version or "-",
                f"{op.ready_replicas}/{op.replicas}",
                status,
                op.operator_framework or "Unknown",
                str(managed_crds_count) if managed_crds_count > 0 else "-",
                age
            )

        with self.console.capture() as capture:
            self.console.print(table)
        
        return capture.get()

    def _calculate_age(self, timestamp: str) -> str:
        """Calculate age from timestamp.
        
        Args:
            timestamp: ISO format timestamp string
        
        Returns:
            Human readable age string
        """
        if not timestamp:
            return "Unknown"
        
        try:
            from datetime import datetime, timezone
            
            # Parse ISO timestamp
            created = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            now = datetime.now(timezone.utc)
            
            diff = now - created
            days = diff.days
            
            if days == 0:
                hours = diff.seconds // 3600
                if hours == 0:
                    minutes = diff.seconds // 60
                    return f"{minutes}m"
                else:
                    return f"{hours}h"
            elif days < 30:
                return f"{days}d"
            elif days < 365:
                months = days // 30
                return f"{months}mo"
            else:
                years = days // 365
                return f"{years}y"
                
        except Exception:
            return "Unknown"

    def _truncate_image(self, image: str, max_length: int = 40) -> str:
        """Truncate image name for display.
        
        Args:
            image: Full image name
            max_length: Maximum length for display
        
        Returns:
            Truncated image name
        """
        if not image:
            return "-"
        
        if len(image) <= max_length:
            return image
        
        # Try to keep the important part (image:tag)
        parts = image.split('/')
        if len(parts) > 1:
            # Keep last part (image:tag) and add ellipsis
            last_part = parts[-1]
            if len(last_part) <= max_length - 3:
                return f".../{last_part}"
        
        # If still too long, just truncate
        return image[:max_length-3] + "..."

    def _detect_crd_framework(self, labels: Dict[str, str], annotations: Dict[str, str]) -> Optional[str]:
        """Detect framework that created the CRD.
        
        Args:
            labels: CRD labels
            annotations: CRD annotations
        
        Returns:
            Framework name or None
        """
        # Check for OLM
        if any('olm' in k.lower() for k in annotations.keys()):
            return "OLM"
        
        if 'operators.coreos.com' in str(annotations):
            return "OLM"
        
        # Check for Helm
        if 'helm.sh/chart' in annotations:
            return "Helm"
        
        if 'app.kubernetes.io/managed-by' in labels:
            if 'helm' in labels['app.kubernetes.io/managed-by'].lower():
                return "Helm"
        
        return None

    def format_crds_markdown(self, crds: List['CRD'], max_depth: int = 3, 
                           required_only: bool = False, include_toc: bool = True) -> str:
        """Format CRDs with their properties as a Markdown document.
        
        Args:
            crds: List of CRD objects with schema information
            max_depth: Maximum depth for nested properties
            required_only: Show only required properties
            include_toc: Include table of contents
        
        Returns:
            Formatted Markdown string
        """
        from datetime import datetime
        
        lines = []
        
        # Header
        lines.append("# Kubernetes Custom Resource Definitions (CRDs)")
        lines.append("")
        lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Total CRDs: {len(crds)}")
        
        # Summary statistics
        total_properties = 0
        total_required = 0
        by_group = {}
        
        for crd in crds:
            if crd.schemas and crd.stored_version in crd.schemas:
                schema = crd.schemas[crd.stored_version]
                prop_count = len(schema.properties) if schema.properties else 0
                req_count = len([p for p in (schema.properties or {}).values() if p.required])
                total_properties += prop_count
                total_required += req_count
                
                group = crd.group
                if group not in by_group:
                    by_group[group] = {'count': 0, 'properties': 0}
                by_group[group]['count'] += 1
                by_group[group]['properties'] += prop_count
        
        lines.append(f"Total properties: {total_properties}")
        lines.append(f"Total required properties: {total_required}")
        lines.append("")
        
        # Table of contents
        if include_toc:
            lines.append("## Table of Contents")
            lines.append("")
            
            # Group by API group for TOC
            sorted_groups = sorted(by_group.keys())
            for group in sorted_groups:
                lines.append(f"### {group}")
                lines.append("")
                group_crds = [crd for crd in crds if crd.group == group]
                group_crds.sort(key=lambda x: x.name)
                
                for crd in group_crds:
                    # Create anchor link (replace dots and special chars with hyphens)
                    anchor = crd.name.lower().replace('.', '-').replace('_', '-')
                    lines.append(f"- [{crd.kind} ({crd.name})](#{anchor})")
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        # CRD Details
        lines.append("## CRD Details")
        lines.append("")
        
        # Sort CRDs by group then by name
        sorted_crds = sorted(crds, key=lambda x: (x.group, x.name))
        
        current_group = None
        for crd in sorted_crds:
            # Group header
            if crd.group != current_group:
                current_group = crd.group
                lines.append(f"### {current_group}")
                lines.append("")
            
            # CRD header
            anchor_name = crd.name.lower().replace('.', '-').replace('_', '-')
            lines.append(f"#### {crd.kind} ({crd.name}) {{#{anchor_name}}}")
            lines.append("")
            
            # Basic info table
            lines.append("| Property | Value |")
            lines.append("|----------|-------|")
            lines.append(f"| **API Group** | `{crd.group}` |")
            lines.append(f"| **Version** | `{crd.stored_version}` |")
            lines.append(f"| **Kind** | `{crd.kind}` |")
            lines.append(f"| **Scope** | {crd.scope} |")
            lines.append(f"| **Instances** | {crd.instance_count} |")
            
            if crd.served_versions and len(crd.served_versions) > 1:
                versions_str = ", ".join(f"`{v}`" for v in crd.served_versions)
                lines.append(f"| **All Versions** | {versions_str} |")
            
            lines.append("")
            
            # Schema properties
            if crd.schemas and crd.stored_version in crd.schemas:
                schema = crd.schemas[crd.stored_version]
                if schema.properties:
                    lines.append("##### Properties")
                    lines.append("")
                    
                    # Properties statistics
                    all_props = schema.properties
                    required_props = [p for p in all_props.values() if p.required]
                    
                    lines.append(f"**Total properties**: {len(all_props)} | "
                                f"**Required**: {len(required_props)}")
                    lines.append("")
                    
                    # Property details
                    prop_lines = self._format_properties_markdown(
                        all_props, schema.required or [], max_depth, required_only, 0
                    )
                    lines.extend(prop_lines)
                else:
                    lines.append("*No properties defined.*")
                    lines.append("")
            else:
                lines.append("*No schema information available.*")
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        return "\n".join(lines)
    
    def _format_properties_markdown(self, properties: Dict[str, 'CRDProperty'], 
                                   required_list: List[str], max_depth: int, 
                                   required_only: bool, current_depth: int) -> List[str]:
        """Format properties as Markdown list.
        
        Args:
            properties: Dictionary of properties
            required_list: List of required property names
            max_depth: Maximum depth to traverse
            required_only: Only show required properties
            current_depth: Current nesting depth
        
        Returns:
            List of formatted lines
        """
        lines = []
        
        if current_depth >= max_depth:
            return lines
        
        # Sort properties: required first, then alphabetical
        sorted_props = sorted(properties.items(), key=lambda x: (not x[1].required, x[0]))
        
        for prop_name, prop in sorted_props:
            if required_only and not prop.required:
                continue
            
            # Indentation for nested properties
            indent = "  " * current_depth
            
            # Property name with type and required marker
            required_marker = " ***(required)***" if prop.required else ""
            type_info = f"`{prop.type}`"
            
            if prop.enum:
                enum_values = "|".join(prop.enum[:5])  # Limit enum display
                if len(prop.enum) > 5:
                    enum_values += "|..."
                type_info += f" (enum: {enum_values})"
            
            lines.append(f"{indent}- **{prop_name}** ({type_info}){required_marker}")
            
            # Description
            if prop.description:
                # Clean and truncate description
                desc = prop.description.replace('\n', ' ').strip()
                if len(desc) > 150:
                    desc = desc[:147] + "..."
                lines.append(f"{indent}  • {desc}")
            
            # Nested properties
            if prop.properties and current_depth < max_depth - 1:
                nested_lines = self._format_properties_markdown(
                    prop.properties, required_list, max_depth, required_only, current_depth + 1
                )
                lines.extend(nested_lines)
            
            # Array items
            elif prop.items and prop.items.properties and current_depth < max_depth - 1:
                lines.append(f"{indent}  • **Array items:**")
                nested_lines = self._format_properties_markdown(
                    prop.items.properties, required_list, max_depth, required_only, current_depth + 1
                )
                lines.extend(nested_lines)
        
        return lines

    def format_crd_properties(self, crd: 'CRD', output_format: str = "rich", 
                            version: Optional[str] = None, max_depth: int = 3,
                            required_only: bool = False) -> str:
        """Format CRD schema properties.
        
        Args:
            crd: CRD object with schema information
            output_format: Output format (table, json, yaml, rich)
            version: Specific version to show (default: stored version)
            max_depth: Maximum depth for nested properties
            required_only: Show only required properties
        
        Returns:
            Formatted properties string
        """
        if output_format.lower() == "json":
            return self._format_properties_json(crd, version, max_depth, required_only)
        elif output_format.lower() == "yaml":
            return self._format_properties_yaml(crd, version, max_depth, required_only)
        elif output_format.lower() == "rich":
            return self._format_properties_rich(crd, version, max_depth, required_only)
        else:  # table
            return self._format_properties_table(crd, version, max_depth, required_only)

    def _get_schema_for_version(self, crd: 'CRD', version: Optional[str]):
        """Get schema for specified version or default to stored version."""
        from ..core.models import CRDSchema
        
        if not crd.schemas:
            return None, "No schema information available"
        
        target_version = version or crd.stored_version
        
        if target_version in crd.schemas:
            return crd.schemas[target_version], target_version
        
        # Fallback to first available schema
        if crd.schemas:
            first_version = next(iter(crd.schemas.keys()))
            return crd.schemas[first_version], first_version
        
        return None, target_version

    def _format_properties_json(self, crd: 'CRD', version: Optional[str], 
                               max_depth: int, required_only: bool) -> str:
        """Format properties as JSON."""
        import json
        
        schema, actual_version = self._get_schema_for_version(crd, version)
        if not schema:
            return json.dumps({
                "crd": crd.name,
                "version": actual_version,
                "error": "No schema information available"
            }, indent=2)
        
        properties_data = self._extract_properties_data(
            schema.properties, schema.required, max_depth, required_only
        )
        
        return json.dumps({
            "crd": {
                "name": crd.name,
                "group": crd.group,
                "version": actual_version,
                "kind": crd.kind,
                "scope": crd.scope,
                "properties": properties_data
            }
        }, indent=2)

    def _format_properties_yaml(self, crd: 'CRD', version: Optional[str], 
                               max_depth: int, required_only: bool) -> str:
        """Format properties as YAML."""
        import yaml
        import json
        
        json_data = json.loads(self._format_properties_json(crd, version, max_depth, required_only))
        return yaml.dump(json_data, default_flow_style=False)

    def _format_properties_table(self, crd: 'CRD', version: Optional[str], 
                                max_depth: int, required_only: bool) -> str:
        """Format properties as a table."""
        schema, actual_version = self._get_schema_for_version(crd, version)
        if not schema:
            return f"CRD: {crd.name}\nVersion: {actual_version}\nNo schema information available."
        
        result = f"CRD: {crd.name}\n"
        result += f"Group: {crd.group}\n"
        result += f"Version: {actual_version}\n"
        result += f"Kind: {crd.kind}\n"
        result += f"Scope: {crd.scope}\n\n"
        
        if not schema.properties:
            return result + "No properties defined."
        
        headers = ["Property", "Type", "Required", "Description"]
        rows = []
        
        self._collect_properties_for_table(
            schema.properties, schema.required, rows, max_depth, required_only
        )
        
        if not rows:
            return result + "No properties found (after filtering)."
        
        result += tabulate(rows, headers=headers, tablefmt="grid")
        
        # Add summary
        total_props = len([r for r in rows if not r[0].startswith('  ')])
        required_props = len([r for r in rows if r[2] == "✓" and not r[0].startswith('  ')])
        result += f"\n\nSummary: {total_props} properties ({required_props} required)"
        
        return result

    def _format_properties_rich(self, crd: 'CRD', version: Optional[str], 
                               max_depth: int, required_only: bool) -> str:
        """Format properties using rich formatting."""
        from rich.table import Table
        from rich.panel import Panel
        from rich.tree import Tree
        from rich.text import Text
        
        schema, actual_version = self._get_schema_for_version(crd, version)
        
        # Build all content first
        parts = []
        
        # CRD header
        header_text = f"[bold cyan]{crd.name}[/bold cyan]\n"
        header_text += f"Group: [magenta]{crd.group}[/magenta]\n"
        header_text += f"Version: [yellow]{actual_version}[/yellow]\n"
        header_text += f"Kind: [green]{crd.kind}[/green]\n"
        header_text += f"Scope: [blue]{crd.scope}[/blue]"
        
        with self.console.capture() as capture:
            self.console.print(Panel(header_text, title="CRD Information", style="cyan"))
        parts.append(capture.get())
        
        if not schema:
            with self.console.capture() as capture:
                self.console.print("\n[red]No schema information available[/red]")
            parts.append(capture.get())
            return "".join(parts)
        
        if not schema.properties:
            with self.console.capture() as capture:
                self.console.print("\n[yellow]No properties defined[/yellow]")
            parts.append(capture.get())
            return "".join(parts)
        
        # Properties tree
        tree = Tree(f"[bold]Properties[/bold] ({len(schema.properties)} total)")
        
        self._build_properties_tree(
            tree, schema.properties, schema.required, max_depth, required_only
        )
        
        with self.console.capture() as capture:
            self.console.print("\n")
            self.console.print(tree)
        parts.append(capture.get())
        
        # Summary statistics
        total_props, required_props, nested_props = self._count_properties(
            schema.properties, schema.required, max_depth
        )
        
        summary = f"Total: [cyan]{total_props}[/cyan] | "
        summary += f"Required: [green]{required_props}[/green] | "
        summary += f"Nested: [yellow]{nested_props}[/yellow]"
        
        if required_only:
            summary += f" | [dim]Filtering: required only[/dim]"
        
        with self.console.capture() as capture:
            self.console.print(f"\n{summary}")
        parts.append(capture.get())
        
        return "".join(parts)

    def _extract_properties_data(self, properties: Dict[str, 'CRDProperty'], 
                               required_list: List[str], max_depth: int, 
                               required_only: bool, current_depth: int = 0):
        """Extract properties data for JSON/YAML output."""
        if current_depth >= max_depth:
            return {}
        
        result = {}
        for prop_name, prop in properties.items():
            is_required = prop_name in required_list
            
            if required_only and not is_required:
                continue
            
            prop_data = {
                "type": prop.type,
                "required": is_required,
                "description": prop.description or "No description"
            }
            
            if prop.format:
                prop_data["format"] = prop.format
            
            if prop.enum:
                prop_data["enum"] = prop.enum
            
            # Add nested properties
            if prop.type == "object" and prop.properties and current_depth < max_depth - 1:
                prop_data["properties"] = self._extract_properties_data(
                    prop.properties, [], max_depth, required_only, current_depth + 1
                )
            
            # Add array item information
            if prop.type == "array" and prop.items:
                prop_data["items"] = {
                    "type": prop.items.type,
                    "description": prop.items.description or "No description"
                }
                if prop.items.properties and current_depth < max_depth - 1:
                    prop_data["items"]["properties"] = self._extract_properties_data(
                        prop.items.properties, [], max_depth, required_only, current_depth + 1
                    )
            
            result[prop_name] = prop_data
        
        return result

    def _collect_properties_for_table(self, properties: Dict[str, 'CRDProperty'], 
                                    required_list: List[str], rows: List, 
                                    max_depth: int, required_only: bool, 
                                    current_depth: int = 0, prefix: str = ""):
        """Collect properties for table output."""
        if current_depth >= max_depth:
            return
        
        for prop_name, prop in sorted(properties.items()):
            is_required = prop_name in required_list
            
            if required_only and not is_required:
                continue
            
            full_name = f"{prefix}{prop_name}"
            type_display = self._format_property_type_display(prop)
            required_display = "✓" if is_required else ""
            description = (prop.description or "No description")[:80] + "..." if len(prop.description or "") > 80 else (prop.description or "No description")
            
            rows.append([full_name, type_display, required_display, description])
            
            # Add nested properties
            if prop.type == "object" and prop.properties and current_depth < max_depth - 1:
                self._collect_properties_for_table(
                    prop.properties, [], rows, max_depth, required_only, 
                    current_depth + 1, f"{prefix}  "
                )

    def _build_properties_tree(self, parent_tree, properties: Dict[str, 'CRDProperty'], 
                              required_list: List[str], max_depth: int, 
                              required_only: bool, current_depth: int = 0):
        """Build properties tree for rich output."""
        if current_depth >= max_depth:
            return
        
        for prop_name, prop in sorted(properties.items()):
            is_required = prop_name in required_list
            
            if required_only and not is_required:
                continue
            
            # Format property display
            prop_display = f"[bold]{prop_name}[/bold]"
            
            if is_required:
                prop_display += " [red]*[/red]"
            
            type_info = self._format_property_type_display(prop)
            prop_display += f" [dim]({type_info})[/dim]"
            
            if prop.description:
                desc = prop.description[:100] + "..." if len(prop.description) > 100 else prop.description
                prop_display += f"\n[italic]{desc}[/italic]"
            
            # Add the property to the tree
            prop_branch = parent_tree.add(prop_display)
            
            # Add nested properties
            if prop.type == "object" and prop.properties and current_depth < max_depth - 1:
                self._build_properties_tree(
                    prop_branch, prop.properties, [], max_depth, required_only, current_depth + 1
                )
            elif prop.type == "array" and prop.items and prop.items.properties and current_depth < max_depth - 1:
                items_branch = prop_branch.add(f"[dim]items ({prop.items.type})[/dim]")
                self._build_properties_tree(
                    items_branch, prop.items.properties, [], max_depth, required_only, current_depth + 1
                )

    def _format_property_type_display(self, prop: 'CRDProperty') -> str:
        """Format property type for display."""
        type_str = prop.type
        
        if prop.format:
            type_str += f"[{prop.format}]"
        
        if prop.enum:
            if len(prop.enum) <= 3:
                enum_str = "|".join(prop.enum)
                type_str += f" enum({enum_str})"
            else:
                type_str += f" enum({len(prop.enum)} values)"
        
        return type_str

    def _count_properties(self, properties: Dict[str, 'CRDProperty'], 
                         required_list: List[str], max_depth: int, 
                         current_depth: int = 0) -> tuple:
        """Count total, required, and nested properties."""
        if current_depth >= max_depth:
            return 0, 0, 0
        
        total = len(properties)
        required = len([p for p in properties.keys() if p in required_list])
        nested = 0
        
        for prop in properties.values():
            if prop.type == "object" and prop.properties:
                nested += 1
                if current_depth < max_depth - 1:
                    sub_total, sub_required, sub_nested = self._count_properties(
                        prop.properties, [], max_depth, current_depth + 1
                    )
                    total += sub_total
                    nested += sub_nested
        
        return total, required, nested

    def format_summary(self, crds: List[CRDInfo], operators: List[OperatorInfo],
                      csvs=None, output_format: str = "rich") -> str:
        """Format a summary of CRDs, operators, and optionally OLM CSVs.
        
        Args:
            crds: List of CRDs
            operators: List of operators
            csvs: Optional list of OLM ClusterServiceVersions
            output_format: Output format (rich, table, json, yaml)
        
        Returns:
            Formatted summary string
        """
        if output_format.lower() == "json":
            return self._format_summary_json(crds, operators, csvs)
        elif output_format.lower() == "yaml":
            return self._format_summary_yaml(crds, operators, csvs)
        elif output_format.lower() == "table":
            return self._format_summary_table(crds, operators, csvs)
        else:  # rich
            return self._format_summary_rich(crds, operators, csvs)

    def _format_summary_rich(self, crds: List[CRDInfo], operators: List[OperatorInfo], csvs=None) -> str:
        """Format summary using rich formatting."""
        # Statistics
        total_crds = len(crds)
        total_operators = len(operators)
        total_csvs = len(csvs) if csvs else 0
        
        # Group by framework
        crd_frameworks = {}
        operator_frameworks = {}
        
        for crd in crds:
            framework = self._detect_crd_framework(crd.labels, crd.annotations) or "Unknown"
            crd_frameworks[framework] = crd_frameworks.get(framework, 0) + 1
        
        for op in operators:
            framework = op.operator_framework or "Unknown"
            operator_frameworks[framework] = operator_frameworks.get(framework, 0) + 1

        # Create summary panels
        crd_stats = f"Total CRDs: {total_crds}\n"
        for framework, count in sorted(crd_frameworks.items()):
            crd_stats += f"  {framework}: {count}\n"

        operator_stats = f"Total Operators: {total_operators}\n"
        for framework, count in sorted(operator_frameworks.items()):
            operator_stats += f"  {framework}: {count}\n"

        with self.console.capture() as capture:
            self.console.print(Panel(crd_stats.strip(), title="CRDs", style="cyan"))
            self.console.print(Panel(operator_stats.strip(), title="Operators", style="magenta"))
            
            # Add OLM panel if we have CSV data
            if csvs:
                csv_phases = {}
                for csv in csvs:
                    phase = csv.phase or "Unknown"
                    csv_phases[phase] = csv_phases.get(phase, 0) + 1
                
                olm_stats = f"Total OLM CSVs: {total_csvs}\n"
                for phase, count in sorted(csv_phases.items()):
                    olm_stats += f"  {phase}: {count}\n"
                
                self.console.print(Panel(olm_stats.strip(), title="OLM Status", style="green"))
        
        return capture.get()

    def _format_summary_json(self, crds: List[CRDInfo], operators: List[OperatorInfo], csvs=None) -> str:
        """Format summary as JSON."""
        crd_frameworks = {}
        operator_frameworks = {}
        
        for crd in crds:
            framework = self._detect_crd_framework(crd.labels, crd.annotations) or "Unknown"
            crd_frameworks[framework] = crd_frameworks.get(framework, 0) + 1
        
        for op in operators:
            framework = op.operator_framework or "Unknown"
            operator_frameworks[framework] = operator_frameworks.get(framework, 0) + 1

        data = {
            "summary": {
                "crds": {
                    "total": len(crds),
                    "by_framework": crd_frameworks
                },
                "operators": {
                    "total": len(operators),
                    "by_framework": operator_frameworks
                }
            }
        }
        
        # Add OLM data if available
        if csvs:
            csv_phases = {}
            for csv in csvs:
                phase = csv.phase or "Unknown"
                csv_phases[phase] = csv_phases.get(phase, 0) + 1
            
            data["summary"]["olm"] = {
                "total_csvs": len(csvs),
                "by_phase": csv_phases
            }
        
        return json.dumps(data, indent=2)

    def _format_summary_yaml(self, crds: List[CRDInfo], operators: List[OperatorInfo], csvs=None) -> str:
        """Format summary as YAML."""
        data = json.loads(self._format_summary_json(crds, operators, csvs))
        return yaml.dump(data, default_flow_style=False)

    def _format_summary_table(self, crds: List[CRDInfo], operators: List[OperatorInfo], csvs=None) -> str:
        """Format summary as table."""
        result = f"Summary:\n"
        result += f"  Total CRDs: {len(crds)}\n"
        result += f"  Total Operators: {len(operators)}\n"
        if csvs:
            result += f"  Total OLM CSVs: {len(csvs)}\n"
        
        return result
