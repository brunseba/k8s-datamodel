"""CRD (Custom Resource Definition) inventory service."""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from kubernetes.client.rest import ApiException
from pathlib import Path
import logging

from .k8s_client import K8sClient
from .models import CRD, CRDSchema, CRDProperty

logger = logging.getLogger(__name__)


@dataclass
class CRDInfo:
    """Information about a Custom Resource Definition."""
    name: str
    group: str
    version: str
    kind: str
    plural: str
    singular: str
    scope: str  # Namespaced or Cluster
    creation_timestamp: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    served_versions: List[str]
    stored_version: str
    categories: List[str]
    short_names: List[str]
    description: Optional[str] = None
    instance_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


class CRDInventory:
    """Service for inventorying Custom Resource Definitions."""

    def __init__(self, k8s_client: K8sClient):
        """Initialize CRD inventory service.
        
        Args:
            k8s_client: Kubernetes client instance
        """
        self.k8s_client = k8s_client

    def list_crds(self) -> List[CRDInfo]:
        """List all Custom Resource Definitions in the cluster.
        
        Returns:
            List of CRDInfo objects
        """
        try:
            crds = self.k8s_client.extensions_v1_api.list_custom_resource_definition()
            crd_list = []
            
            for crd in crds.items:
                # Get basic info
                name = crd.metadata.name
                group = crd.spec.group
                kind = crd.spec.names.kind
                plural = crd.spec.names.plural
                singular = crd.spec.names.singular
                scope = crd.spec.scope
                creation_timestamp = crd.metadata.creation_timestamp.isoformat() if crd.metadata.creation_timestamp else ""
                labels = crd.metadata.labels or {}
                annotations = crd.metadata.annotations or {}
                categories = crd.spec.names.categories or []
                short_names = crd.spec.names.short_names or []
                
                # Get version information
                served_versions = []
                stored_version = ""
                
                for version in crd.spec.versions:
                    served_versions.append(version.name)
                    if version.storage:
                        stored_version = version.name
                
                # Try to get instance count
                instance_count = self._count_custom_resources(group, plural, crd.spec.scope)
                
                # Extract schemas for each version
                schemas = self._extract_schemas(crd)
                
                crd_info = CRD(
                    name=name,
                    group=group,
                    version=stored_version,
                    kind=kind,
                    plural=plural,
                    singular=singular,
                    scope=scope,
                    creation_timestamp=creation_timestamp,
                    labels=labels,
                    annotations=annotations,
                    served_versions=served_versions,
                    stored_version=stored_version,
                    categories=categories,
                    short_names=short_names,
                    instance_count=instance_count,
                    schemas=schemas
                )
                
                crd_list.append(crd_info)
            
            return sorted(crd_list, key=lambda x: x.name)
        
        except ApiException as e:
            logger.error(f"Failed to list CRDs: {e}")
            raise

    def get_crd_details(self, crd_name: str) -> Optional[CRDInfo]:
        """Get detailed information about a specific CRD.
        
        Args:
            crd_name: Name of the CRD
        
        Returns:
            CRDInfo object or None if not found
        """
        try:
            crd = self.k8s_client.extensions_v1_api.read_custom_resource_definition(crd_name)
            
            # Extract detailed information (similar to list_crds but for single CRD)
            name = crd.metadata.name
            group = crd.spec.group
            kind = crd.spec.names.kind
            plural = crd.spec.names.plural
            singular = crd.spec.names.singular
            scope = crd.spec.scope
            creation_timestamp = crd.metadata.creation_timestamp.isoformat() if crd.metadata.creation_timestamp else ""
            labels = crd.metadata.labels or {}
            annotations = crd.metadata.annotations or {}
            categories = crd.spec.names.categories or []
            short_names = crd.spec.names.short_names or []
            
            served_versions = []
            stored_version = ""
            
            for version in crd.spec.versions:
                served_versions.append(version.name)
                if version.storage:
                    stored_version = version.name
            
            instance_count = self._count_custom_resources(group, plural, crd.spec.scope)
            
            # Extract schemas for each version
            schemas = self._extract_schemas(crd)
            
            return CRD(
                name=name,
                group=group,
                version=stored_version,
                kind=kind,
                plural=plural,
                singular=singular,
                scope=scope,
                creation_timestamp=creation_timestamp,
                labels=labels,
                annotations=annotations,
                served_versions=served_versions,
                stored_version=stored_version,
                categories=categories,
                short_names=short_names,
                instance_count=instance_count,
                schemas=schemas
            )
        
        except ApiException as e:
            if e.status == 404:
                return None
            logger.error(f"Failed to get CRD details for {crd_name}: {e}")
            raise

    def _count_custom_resources(self, group: str, plural: str, scope: str) -> int:
        """Count instances of a custom resource.
        
        Args:
            group: API group of the custom resource
            plural: Plural name of the custom resource
            scope: Scope (Namespaced or Cluster)
        
        Returns:
            Number of instances
        """
        try:
            if scope.lower() == 'namespaced':
                # List across all namespaces
                response = self.k8s_client.custom_objects_api.list_cluster_custom_object(
                    group=group,
                    version='v1',  # Default to v1, might need adjustment
                    plural=plural
                )
            else:
                # Cluster-scoped resource
                response = self.k8s_client.custom_objects_api.list_cluster_custom_object(
                    group=group,
                    version='v1',
                    plural=plural
                )
            
            return len(response.get('items', []))
        
        except Exception as e:
            logger.debug(f"Could not count instances for {group}/{plural}: {e}")
            return 0
    
    def _extract_schemas(self, crd) -> Dict[str, CRDSchema]:
        """Extract schema information from CRD versions.
        
        Args:
            crd: The CRD object from Kubernetes API
        
        Returns:
            Dictionary of version -> CRDSchema
        """
        schemas = {}
        
        try:
            for version in crd.spec.versions:
                logger.debug(f"Processing version {version.name} for CRD {crd.metadata.name}")
                
                # Check if version has schema with OpenAPI v3 schema
                if hasattr(version, 'schema') and version.schema is not None:
                    # The correct attribute name is 'open_apiv3_schema' (with underscores)
                    if hasattr(version.schema, 'open_apiv3_schema') and version.schema.open_apiv3_schema is not None:
                        # Convert the schema to dictionary if it's a Kubernetes object
                        schema_dict = version.schema.open_apiv3_schema
                        
                        # Handle both dict and Kubernetes object types
                        if hasattr(schema_dict, 'to_dict'):
                            schema_dict = schema_dict.to_dict()
                        elif hasattr(schema_dict, '__dict__'):
                            # Convert object attributes to dict
                            schema_dict = self._k8s_obj_to_dict(schema_dict)
                        
                        if schema_dict and isinstance(schema_dict, dict):
                            logger.debug(f"Found schema for version {version.name}, keys: {list(schema_dict.keys())}")
                            
                            # Extract the main properties from the schema
                            # The schema contains properties like 'apiVersion', 'kind', 'metadata', 'spec', 'status'
                            root_props = schema_dict.get('properties', {})
                            if isinstance(root_props, dict):
                                # Focus on the 'spec' properties as they contain the CRD-specific schema
                                spec_schema = root_props.get('spec', {})
                                if isinstance(spec_schema, dict) and 'properties' in spec_schema:
                                    logger.debug(f"Found spec properties for {version.name}: {list(spec_schema['properties'].keys())}")
                                    properties = self._parse_schema_properties(spec_schema.get('properties', {}))
                                    required = spec_schema.get('required', [])
                                    
                                    schemas[version.name] = CRDSchema(
                                        version=version.name,
                                        properties=properties,
                                        required=required if isinstance(required, list) else []
                                    )
                                    logger.debug(f"Successfully extracted {len(properties)} properties for version {version.name}")
                                else:
                                    logger.debug(f"No spec properties found for version {version.name}")
                                    
                                    # Fallback: try to use root properties directly (for some CRDs)
                                    if root_props:
                                        logger.debug(f"Using root properties as fallback for {version.name}")
                                        properties = self._parse_schema_properties(root_props)
                                        required = schema_dict.get('required', [])
                                        
                                        schemas[version.name] = CRDSchema(
                                            version=version.name,
                                            properties=properties,
                                            required=required if isinstance(required, list) else []
                                        )
                            else:
                                logger.debug(f"Schema properties is not a dict for version {version.name}: {type(root_props)}")
                        else:
                            logger.debug(f"Schema dict is invalid for version {version.name}: {type(schema_dict)}")
                    else:
                        logger.debug(f"No open_apiv3_schema found for version {version.name}")
                else:
                    logger.debug(f"No schema found for version {version.name}")
                    
        except Exception as e:
            logger.error(f"Failed to extract schema from CRD {crd.metadata.name}: {e}")
            import traceback
            logger.debug(f"Full traceback: {traceback.format_exc()}")
        
        logger.debug(f"Extracted schemas for CRD {crd.metadata.name}: {list(schemas.keys())}")
        return schemas
    
    def _k8s_obj_to_dict(self, obj: Any) -> Dict[str, Any]:
        """Convert a Kubernetes client object to a dictionary.
        
        Args:
            obj: Kubernetes client object
            
        Returns:
            Dictionary representation of the object
        """
        try:
            # First, try the standard to_dict method
            if hasattr(obj, 'to_dict'):
                return obj.to_dict()
            
            # If that doesn't work, try to access attributes directly
            result = {}
            if hasattr(obj, '__dict__'):
                for key, value in obj.__dict__.items():
                    if key.startswith('_'):
                        continue
                    
                    # Handle nested objects recursively
                    if hasattr(value, '__dict__') and not isinstance(value, (str, int, float, bool, list, dict)):
                        result[key] = self._k8s_obj_to_dict(value)
                    elif isinstance(value, list):
                        result[key] = []
                        for item in value:
                            if hasattr(item, '__dict__') and not isinstance(item, (str, int, float, bool)):
                                result[key].append(self._k8s_obj_to_dict(item))
                            else:
                                result[key].append(item)
                    elif isinstance(value, dict):
                        result[key] = {}
                        for k, v in value.items():
                            if hasattr(v, '__dict__') and not isinstance(v, (str, int, float, bool)):
                                result[key][k] = self._k8s_obj_to_dict(v)
                            else:
                                result[key][k] = v
                    else:
                        result[key] = value
            
            return result
            
        except Exception as e:
            logger.warning(f"Failed to convert Kubernetes object to dict: {e}")
            return {}
    
    def _parse_schema_properties(self, properties_dict: Dict[str, Any]) -> Dict[str, CRDProperty]:
        """Parse OpenAPI schema properties into CRDProperty objects.
        
        Args:
            properties_dict: Properties dictionary from OpenAPI schema
        
        Returns:
            Dictionary of property name -> CRDProperty
        """
        properties = {}
        
        if not isinstance(properties_dict, dict):
            return properties
        
        for prop_name, prop_schema in properties_dict.items():
            if not isinstance(prop_schema, dict):
                continue
            prop_type = prop_schema.get('type', 'object')
            description = prop_schema.get('description', '')
            format_type = prop_schema.get('format')
            enum_values = prop_schema.get('enum', [])
            
            # Handle nested properties for object types
            nested_properties = None
            if prop_type == 'object' and 'properties' in prop_schema:
                nested_properties = self._parse_schema_properties(prop_schema['properties'])
            
            # Handle array items
            items_property = None
            if prop_type == 'array' and 'items' in prop_schema:
                items_schema = prop_schema['items']
                items_type = items_schema.get('type', 'object')
                items_nested_props = None
                if items_type == 'object' and 'properties' in items_schema:
                    items_nested_props = self._parse_schema_properties(items_schema['properties'])
                
                items_property = CRDProperty(
                    name='items',
                    type=items_type,
                    description=items_schema.get('description', ''),
                    properties=items_nested_props
                )
            
            properties[prop_name] = CRDProperty(
                name=prop_name,
                type=prop_type,
                description=description,
                format=format_type,
                enum=enum_values,
                properties=nested_properties,
                items=items_property
            )
        
        return properties

    def filter_crds(self, crds: List[CRD], 
                   group_filter: Optional[str] = None,
                   kind_filter: Optional[str] = None,
                   scope_filter: Optional[str] = None) -> List[CRD]:
        """Filter CRDs based on criteria.
        
        Args:
            crds: List of CRD objects to filter
            group_filter: Filter by group (partial match)
            kind_filter: Filter by kind (partial match)
            scope_filter: Filter by scope (exact match)
        
        Returns:
            Filtered list of CRD objects
        """
        filtered = crds
        
        if group_filter:
            filtered = [crd for crd in filtered if group_filter.lower() in crd.group.lower()]
        
        if kind_filter:
            filtered = [crd for crd in filtered if kind_filter.lower() in crd.kind.lower()]
        
        if scope_filter:
            filtered = [crd for crd in filtered if crd.scope.lower() == scope_filter.lower()]
        
        return filtered

    def get_group_synthesis(self, crds: List[CRD]) -> Dict[str, Any]:
        """Generate synthesis and statistics by API groups.
        
        Args:
            crds: List of CRD objects to analyze
        
        Returns:
            Dictionary containing group synthesis data
        """
        if not crds:
            return {
                'total_groups': 0,
                'total_crds': 0,
                'total_instances': 0,
                'groups': {},
                'summary': {
                    'by_scope': {'Namespaced': 0, 'Cluster': 0},
                    'by_category': {},
                    'by_version': {},
                    'most_active_groups': [],
                    'diversity': {
                        'single_crd_groups': 0,
                        'multi_crd_groups': 0,
                        'largest_group': None,
                        'average_crds_per_group': 0
                    }
                }
            }
        
        groups = {}
        total_instances = 0
        scope_counts = {'Namespaced': 0, 'Cluster': 0}
        category_counts = {}
        version_counts = {}
        
        # Analyze each CRD
        for crd in crds:
            group_name = crd.group or 'core'
            
            # Initialize group if not exists
            if group_name not in groups:
                groups[group_name] = {
                    'name': group_name,
                    'crd_count': 0,
                    'total_instances': 0,
                    'crds': [],
                    'scopes': {'Namespaced': 0, 'Cluster': 0},
                    'versions': set(),
                    'categories': set(),
                    'latest_creation': None,
                    'oldest_creation': None
                }
            
            group_data = groups[group_name]
            
            # Update group statistics
            group_data['crd_count'] += 1
            group_data['total_instances'] += crd.instance_count
            group_data['crds'].append({
                'name': crd.name,
                'kind': crd.kind,
                'version': crd.version,
                'scope': crd.scope,
                'instance_count': crd.instance_count,
                'creation_timestamp': crd.creation_timestamp
            })
            group_data['scopes'][crd.scope] += 1
            group_data['versions'].add(crd.version)
            
            # Track categories
            for category in crd.categories:
                group_data['categories'].add(category)
                category_counts[category] = category_counts.get(category, 0) + 1
            
            # Track creation timestamps
            if crd.creation_timestamp:
                if not group_data['latest_creation'] or crd.creation_timestamp > group_data['latest_creation']:
                    group_data['latest_creation'] = crd.creation_timestamp
                if not group_data['oldest_creation'] or crd.creation_timestamp < group_data['oldest_creation']:
                    group_data['oldest_creation'] = crd.creation_timestamp
            
            # Update overall statistics
            total_instances += crd.instance_count
            scope_counts[crd.scope] += 1
            version_counts[crd.version] = version_counts.get(crd.version, 0) + 1
        
        # Convert sets to lists for JSON serialization
        for group_data in groups.values():
            group_data['versions'] = sorted(list(group_data['versions']))
            group_data['categories'] = sorted(list(group_data['categories']))
        
        # Calculate most active groups by instance count
        most_active_groups = sorted(
            [(name, data['total_instances'], data['crd_count']) 
             for name, data in groups.items()],
            key=lambda x: (x[1], x[2]),  # Sort by instances, then CRD count
            reverse=True
        )[:10]  # Top 10
        
        # Calculate group diversity metrics
        group_diversity = {
            'single_crd_groups': len([g for g in groups.values() if g['crd_count'] == 1]),
            'multi_crd_groups': len([g for g in groups.values() if g['crd_count'] > 1]),
            'largest_group': max(groups.values(), key=lambda x: x['crd_count'])['name'] if groups else None,
            'average_crds_per_group': len(crds) / len(groups) if groups else 0
        }
        
        return {
            'total_groups': len(groups),
            'total_crds': len(crds),
            'total_instances': total_instances,
            'groups': groups,
            'summary': {
                'by_scope': scope_counts,
                'by_category': category_counts,
                'by_version': version_counts,
                'most_active_groups': most_active_groups,
                'diversity': group_diversity
            }
        }

    def generate_mermaid_diagram(self, crds: List[CRD], group_filter: Optional[str] = None) -> str:
        """Generate Mermaid class diagrams showing CRD schemas by API groups.
        
        Args:
            crds: List of CRD objects with schema information
            group_filter: Optional filter for specific group
        
        Returns:
            Mermaid diagrams as string (one per API group)
        """
        if not crds:
            return "```mermaid\nclassDiagram\n    note \"No CRDs found\"\n```"
        
        # Group CRDs by API group
        groups = {}
        for crd in crds:
            group_name = crd.group or 'core'
            if group_filter and group_filter.lower() not in group_name.lower():
                continue
            
            if group_name not in groups:
                groups[group_name] = []
            groups[group_name].append(crd)
        
        if not groups:
            return "```mermaid\nclassDiagram\n    note \"No CRDs found matching filter\"\n```"
        
        # Generate one diagram per API group
        diagrams = []
        
        for group_name in sorted(groups.keys()):
            group_crds = groups[group_name]
            diagram = self._generate_group_schema_diagram(group_name, group_crds)
            diagrams.append(diagram)
        
        return "\n\n---\n\n".join(diagrams)
    
    def generate_comprehensive_markdown(self, crds: List[CRD], group_filter: Optional[str] = None) -> str:
        """Generate comprehensive markdown documentation with CRD schema diagrams.
        
        Args:
            crds: List of CRD objects with schema information
            group_filter: Optional filter for specific group
        
        Returns:
            Complete markdown documentation with summary, TOC, and chapters
        """
        if not crds:
            return "# CRD Schema Documentation\n\nNo CRDs found."
        
        # Filter CRDs if requested
        if group_filter:
            crds = [crd for crd in crds if group_filter.lower() in crd.group.lower()]
        
        if not crds:
            return "# CRD Schema Documentation\n\nNo CRDs found matching the specified filter."
        
        # Group CRDs by API group
        groups = {}
        for crd in crds:
            group_name = crd.group or 'core'
            if group_name not in groups:
                groups[group_name] = []
            groups[group_name].append(crd)
        
        # Generate markdown sections
        doc_parts = []
        
        # Title and metadata
        doc_parts.append(self._generate_markdown_header(crds, groups, group_filter))
        
        # Table of Contents
        doc_parts.append(self._generate_markdown_toc(groups))
        
        # Executive Summary
        doc_parts.append(self._generate_markdown_summary(crds, groups))
        
        # API Group Chapters
        for group_name in sorted(groups.keys()):
            group_crds = groups[group_name]
            chapter = self._generate_group_markdown_chapter(group_name, group_crds)
            doc_parts.append(chapter)
        
        # Appendices
        doc_parts.append(self._generate_markdown_appendices(crds, groups))
        
        return "\n\n".join(doc_parts)
    
    def convert_markdown_to_pdf(self, markdown_content: str, output_file: str) -> str:
        """Convert markdown content to PDF using available converters.
        
        Args:
            markdown_content: Markdown content to convert
            output_file: Output PDF file path
        
        Returns:
            Status message about the conversion
        """
        import subprocess
        import tempfile
        import os
        from pathlib import Path
        
        # Create temporary markdown file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp_md:
            tmp_md.write(markdown_content)
            tmp_md_path = tmp_md.name
        
        try:
            output_path = Path(output_file).resolve()
            
            # Try different PDF conversion tools in order of preference
            converters = [
                # Python-based converters (preferred for ease of installation)
                (self._convert_via_reportlab, markdown_content, output_path),
                (self._convert_via_weasyprint, markdown_content, output_path),
                (self._convert_via_pdfkit, markdown_content, output_path),
                
                # pandoc (most comprehensive)
                ['pandoc', tmp_md_path, '-o', str(output_path), 
                 '--pdf-engine=xelatex', '--toc', '--toc-depth=3'],
                
                # pandoc with pdflatex fallback
                ['pandoc', tmp_md_path, '-o', str(output_path), 
                 '--pdf-engine=pdflatex', '--toc'],
                
                # pandoc minimal
                ['pandoc', tmp_md_path, '-o', str(output_path)],
                
                # md-to-pdf (if available)
                ['md-to-pdf', tmp_md_path, '--dest', str(output_path)],
                
                # wkhtmltopdf with markdown-to-html conversion
                self._convert_via_html(tmp_md_path, output_path)
            ]
            
            last_error = None
            
            for converter in converters:
                if converter is None:
                    continue
                    
                if isinstance(converter, tuple) and len(converter) == 3:
                    # Python-based converter
                    converter_func, content, path = converter
                    try:
                        converter_instance = converter_func(content, path)
                        if converter_instance:
                            result = converter_instance()
                            if result is True and output_path.exists():
                                return f"Successfully converted to PDF using Python converter"
                            elif isinstance(result, str):
                                last_error = result
                    except Exception as e:
                        last_error = f"Python converter: {str(e)}"
                        continue
                else:
                    # Subprocess-based converter
                    try:
                        result = subprocess.run(
                            converter, 
                            capture_output=True, 
                            text=True, 
                            timeout=60  # 1 minute timeout
                        )
                        
                        if result.returncode == 0 and output_path.exists():
                            return f"Successfully converted to PDF using {converter[0]}"
                        else:
                            last_error = f"{converter[0]}: {result.stderr}"
                            
                    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
                        last_error = f"{converter[0]}: {str(e)}"
                        continue
            
            # If all converters failed, provide helpful error message
            return self._generate_pdf_fallback_message(markdown_content, output_file, last_error)
            
        finally:
            # Clean up temporary file
            try:
                os.unlink(tmp_md_path)
            except OSError:
                pass
    
    def _convert_via_reportlab(self, markdown_content: str, output_path: Path) -> Optional[callable]:
        """Convert markdown to PDF using ReportLab (simple but reliable).
        
        Returns:
            Callable converter function or None if not available
        """
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.units import inch
            from reportlab.lib.colors import black, blue, grey, white
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
            import re
            
            def convert():
                try:
                    # Create the PDF document
                    doc = SimpleDocTemplate(str(output_path), pagesize=A4,
                                          rightMargin=72, leftMargin=72,
                                          topMargin=72, bottomMargin=18)
                    
                    # Define styles
                    styles = getSampleStyleSheet()
                    title_style = ParagraphStyle('CustomTitle', parent=styles['Title'],
                                               fontSize=18, textColor=blue)
                    heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading1'],
                                                 fontSize=14, textColor=black)
                    normal_style = styles['Normal']
                    
                    story = []
                    
                    # Parse markdown content into sections
                    lines = markdown_content.split('\n')
                    current_section = []
                    
                    for line in lines:
                        line = line.strip()
                        
                        # Skip empty lines in sections but add them as spacers
                        if not line:
                            if current_section:
                                current_section.append('')
                            continue
                        
                        # Handle headers
                        if line.startswith('# '):
                            # Add previous section
                            if current_section:
                                story.extend(self._process_section(current_section, styles))
                                current_section = []
                            
                            title_text = line[2:].strip()
                            story.append(Paragraph(title_text, title_style))
                            story.append(Spacer(1, 12))
                        
                        elif line.startswith('## '):
                            # Add previous section
                            if current_section:
                                story.extend(self._process_section(current_section, styles))
                                current_section = []
                            
                            heading_text = line[3:].strip()
                            story.append(Paragraph(heading_text, heading_style))
                            story.append(Spacer(1, 6))
                        
                        elif line.startswith('### '):
                            # Add previous section
                            if current_section:
                                story.extend(self._process_section(current_section, styles))
                                current_section = []
                            
                            subheading_text = line[4:].strip()
                            subheading_style = ParagraphStyle('Subheading', parent=styles['Heading2'],
                                                             fontSize=12, textColor=grey)
                            story.append(Paragraph(subheading_text, subheading_style))
                            story.append(Spacer(1, 4))
                        
                        else:
                            current_section.append(line)
                    
                    # Add final section
                    if current_section:
                        story.extend(self._process_section(current_section, styles))
                    
                    # Build the PDF
                    doc.build(story)
                    return True
                    
                except Exception as e:
                    return f"ReportLab error: {str(e)}"
            
            return convert
            
        except ImportError:
            return None
    
    def _process_section(self, section_lines, styles):
        """Process a section of markdown lines into ReportLab elements."""
        import re
        from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.colors import grey, white
        from reportlab.lib.styles import ParagraphStyle
        
        elements = []
        current_paragraph = []
        in_table = False
        table_rows = []
        
        for line in section_lines:
            line = line.strip()
            
            if not line:
                # Empty line - end current paragraph and add spacer
                if current_paragraph:
                    para_text = ' '.join(current_paragraph)
                    elements.append(Paragraph(para_text, styles['Normal']))
                    current_paragraph = []
                elements.append(Spacer(1, 6))
                continue
            
            # Handle tables
            if line.startswith('|') and '|' in line[1:]:
                if current_paragraph:
                    para_text = ' '.join(current_paragraph)
                    elements.append(Paragraph(para_text, styles['Normal']))
                    current_paragraph = []
                
                if not in_table:
                    in_table = True
                    table_rows = []
                
                # Parse table row
                row_data = [cell.strip() for cell in line.split('|')[1:-1]]
                if not all(cell.startswith('-') for cell in row_data):  # Skip separator rows
                    table_rows.append(row_data)
            else:
                # End table if we were in one
                if in_table:
                    if table_rows:
                        table = Table(table_rows)
                        table.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), white),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 10),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), white),
                            ('GRID', (0, 0), (-1, -1), 1, grey)
                        ]))
                        elements.append(table)
                        elements.append(Spacer(1, 12))
                    
                    in_table = False
                    table_rows = []
                
                # Handle code blocks
                if line.startswith('```'):
                    continue  # Skip code block markers for now
                
                # Handle lists
                if line.startswith('- ') or line.startswith('* '):
                    if current_paragraph:
                        para_text = ' '.join(current_paragraph)
                        elements.append(Paragraph(para_text, styles['Normal']))
                        current_paragraph = []
                    
                    list_text = line[2:].strip()
                    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
                                                 leftIndent=20, bulletIndent=10)
                    elements.append(Paragraph(f'• {list_text}', bullet_style))
                else:
                    # Regular text - add to current paragraph
                    # Clean up markdown formatting
                    clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)  # Bold
                    clean_line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', clean_line)  # Italic
                    clean_line = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', clean_line)  # Code
                    current_paragraph.append(clean_line)
        
        # Handle final table
        if in_table and table_rows:
            table = Table(table_rows)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), white),
                ('GRID', (0, 0), (-1, -1), 1, grey)
            ]))
            elements.append(table)
        
        # Handle final paragraph
        if current_paragraph:
            para_text = ' '.join(current_paragraph)
            elements.append(Paragraph(para_text, styles['Normal']))
        
        return elements
    
    def _convert_via_weasyprint(self, markdown_content: str, output_path: Path) -> Optional[callable]:
        """Convert markdown to PDF using WeasyPrint (Python-based).
        
        Returns:
            Callable converter function or None if not available
        """
        try:
            import weasyprint
            import markdown
            from pathlib import Path
            
            def convert():
                try:
                    # Convert markdown to HTML
                    html_content = markdown.markdown(
                        markdown_content,
                        extensions=['tables', 'toc', 'codehilite', 'fenced_code']
                    )
                    
                    # Add basic CSS for better formatting
                    styled_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <style>
                            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                            h1 {{ color: #333; border-bottom: 2px solid #333; }}
                            h2 {{ color: #666; border-bottom: 1px solid #ccc; }}
                            h3 {{ color: #999; }}
                            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                            th {{ background-color: #f2f2f2; }}
                            code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
                            pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
                            blockquote {{ border-left: 4px solid #ddd; margin: 0; padding-left: 20px; color: #666; }}
                        </style>
                    </head>
                    <body>
                    {html_content}
                    </body>
                    </html>
                    """
                    
                    # Convert HTML to PDF
                    weasyprint.HTML(string=styled_html).write_pdf(str(output_path))
                    return True
                except Exception as e:
                    return f"WeasyPrint error: {str(e)}"
            
            return convert
            
        except ImportError:
            return None
    
    def _convert_via_pdfkit(self, markdown_content: str, output_path: Path) -> Optional[callable]:
        """Convert markdown to PDF using pdfkit (requires wkhtmltopdf).
        
        Returns:
            Callable converter function or None if not available
        """
        try:
            import pdfkit
            import markdown
            import tempfile
            
            def convert():
                try:
                    # Convert markdown to HTML
                    html_content = markdown.markdown(
                        markdown_content,
                        extensions=['tables', 'toc', 'codehilite', 'fenced_code']
                    )
                    
                    # Add CSS for better formatting
                    styled_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <style>
                            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                            h1 {{ color: #333; border-bottom: 2px solid #333; }}
                            h2 {{ color: #666; border-bottom: 1px solid #ccc; }}
                            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                            th {{ background-color: #f2f2f2; }}
                            code {{ background-color: #f4f4f4; padding: 2px 4px; }}
                            pre {{ background-color: #f4f4f4; padding: 10px; }}
                        </style>
                    </head>
                    <body>
                    {html_content}
                    </body>
                    </html>
                    """
                    
                    # Convert HTML to PDF using pdfkit
                    options = {
                        'page-size': 'A4',
                        'margin-top': '0.75in',
                        'margin-right': '0.75in',
                        'margin-bottom': '0.75in',
                        'margin-left': '0.75in',
                        'encoding': "UTF-8",
                        'no-outline': None
                    }
                    
                    pdfkit.from_string(styled_html, str(output_path), options=options)
                    return True
                except Exception as e:
                    return f"pdfkit error: {str(e)}"
            
            return convert
            
        except ImportError:
            return None
    
    def _convert_via_html(self, md_path: str, output_path: Path) -> Optional[List[str]]:
        """Convert markdown to PDF via HTML using wkhtmltopdf.
        
        Returns:
            Command list or None if not feasible
        """
        try:
            import subprocess
            import tempfile
            
            # Check if we have markdown converter and wkhtmltopdf
            subprocess.run(['which', 'pandoc'], capture_output=True, check=True)
            subprocess.run(['which', 'wkhtmltopdf'], capture_output=True, check=True)
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp_html:
                # Convert markdown to HTML first
                html_result = subprocess.run(
                    ['pandoc', md_path, '-t', 'html', '--standalone'],
                    capture_output=True, text=True
                )
                
                if html_result.returncode == 0:
                    tmp_html.write(html_result.stdout)
                    tmp_html_path = tmp_html.name
                    
                    return ['wkhtmltopdf', '--enable-local-file-access', 
                           tmp_html_path, str(output_path)]
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
    
    def _generate_pdf_fallback_message(self, markdown_content: str, output_file: str, 
                                      last_error: Optional[str]) -> str:
        """Generate fallback message when PDF conversion fails.
        
        Args:
            markdown_content: Original markdown content
            output_file: Intended output file
            last_error: Last conversion error
        
        Returns:
            Helpful error message with suggestions
        """
        # Save markdown as fallback
        fallback_file = output_file.replace('.pdf', '.md') if output_file.endswith('.pdf') else f"{output_file}.md"
        
        try:
            with open(fallback_file, 'w') as f:
                f.write(markdown_content)
                
            return f"""❌ PDF conversion failed. Saved as Markdown instead: {fallback_file}

💡 To enable PDF export, install one of these options:

🐍 Python-based (Recommended - easiest to install):
   • WeasyPrint: pip install weasyprint markdown
   • pdfkit: pip install pdfkit markdown (requires wkhtmltopdf)

🔧 System tools:
   • pandoc + LaTeX: brew install pandoc mactex (macOS) or apt-get install pandoc texlive (Linux)
   • md-to-pdf: npm install -g md-to-pdf

Last error: {last_error or 'No PDF converter found'}

🔄 You can manually convert the markdown file to PDF using:
   • WeasyPrint: python -c "import weasyprint, markdown; weasyprint.HTML(string=markdown.markdown(open('{fallback_file}').read())).write_pdf('{output_file}')"
   • pandoc: pandoc {fallback_file} -o {output_file} --pdf-engine=xelatex --toc"""
            
        except Exception as e:
            return f"❌ PDF conversion failed and could not save markdown fallback: {e}"
    
    
    def _generate_markdown_header(self, crds: List[CRD], groups: Dict[str, List[CRD]], 
                                 group_filter: Optional[str] = None) -> str:
        """Generate markdown document header with metadata."""
        from datetime import datetime
        
        title = "CRD Schema Documentation"
        if group_filter:
            title += f" - {group_filter} API Group"
        
        header = f"""# {title}

> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> 
> **Total CRDs:** {len(crds)}
> 
> **API Groups:** {len(groups)}
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---"""
        
        return header
    
    def _generate_markdown_toc(self, groups: Dict[str, List[CRD]]) -> str:
        """Generate table of contents."""
        toc_lines = ["## 📋 Table of Contents", ""]
        
        # Main sections
        toc_lines.extend([
            "1. [Executive Summary](#-executive-summary)",
            "2. [API Group Documentation](#-api-group-documentation)"
        ])
        
        # Add each API group as a subsection
        for i, group_name in enumerate(sorted(groups.keys()), 3):
            group_crds = groups[group_name]
            safe_group = group_name.replace('.', '').replace('-', '').lower()
            toc_lines.append(f"   - [{group_name}](#{safe_group}) ({len(group_crds)} CRDs)")
        
        toc_lines.extend([
            f"{len(groups) + 2}. [Appendices](#-appendices)",
            f"   - [CRD Index](#crd-index)",
            f"   - [Property Types Summary](#property-types-summary)",
            f"   - [Relationship Matrix](#relationship-matrix)"
        ])
        
        return "\n".join(toc_lines)
    
    def _generate_markdown_summary(self, crds: List[CRD], groups: Dict[str, List[CRD]]) -> str:
        """Generate executive summary section."""
        # Calculate statistics
        total_crds = len(crds)
        total_groups = len(groups)
        namespaced_count = len([crd for crd in crds if crd.scope == "Namespaced"])
        cluster_count = len([crd for crd in crds if crd.scope == "Cluster"])
        total_instances = sum(crd.instance_count for crd in crds)
        
        # Find groups with most CRDs and most instances
        groups_by_size = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
        groups_by_instances = sorted(groups.items(), key=lambda x: sum(crd.instance_count for crd in x[1]), reverse=True)
        
        # Count CRDs with schemas
        crds_with_schemas = len([crd for crd in crds if crd.schemas])
        schema_coverage = (crds_with_schemas / total_crds * 100) if total_crds > 0 else 0
        
        summary = f"""## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **{total_crds} Custom Resource Definitions** distributed across **{total_groups} API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | {total_crds} |
| **API Groups** | {total_groups} |
| **Total Instances** | {total_instances:,} |
| **Namespaced CRDs** | {namespaced_count} ({namespaced_count/total_crds*100:.1f}%) |
| **Cluster-scoped CRDs** | {cluster_count} ({cluster_count/total_crds*100:.1f}%) |
| **Schema Coverage** | {crds_with_schemas}/{total_crds} ({schema_coverage:.1f}%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)
"""
        
        # Add top 5 groups by CRD count
        for i, (group_name, group_crds) in enumerate(groups_by_size[:5], 1):
            summary += f"\n{i}. **{group_name}**: {len(group_crds)} CRDs"
        
        if groups_by_instances[0][0] != groups_by_size[0][0]:  # Different top group by instances
            most_active_group, most_active_crds = groups_by_instances[0]
            most_active_instances = sum(crd.instance_count for crd in most_active_crds)
            summary += f"\n\n#### Most Active API Group (by instance count)\n\n**{most_active_group}**: {most_active_instances:,} instances across {len(most_active_crds)} CRDs"
        
        summary += "\n\n### Schema Analysis\n\n"
        
        if crds_with_schemas > 0:
            # Find most complex schemas (most properties)
            complex_crds = []
            for crd in crds:
                if crd.schemas:
                    for schema in crd.schemas.values():
                        prop_count = len(schema.properties)
                        if prop_count > 0:
                            complex_crds.append((crd, prop_count))
            
            if complex_crds:
                complex_crds.sort(key=lambda x: x[1], reverse=True)
                summary += "**Most Complex CRDs (by property count):**\n\n"
                for i, (crd, prop_count) in enumerate(complex_crds[:3], 1):
                    summary += f"{i}. `{crd.kind}` ({crd.group}): {prop_count} properties\n"
        else:
            summary += "⚠️ **Note**: No OpenAPI schemas found for the CRDs. Diagrams will show basic CRD metadata only."
        
        return summary
    
    def _generate_group_markdown_chapter(self, group_name: str, group_crds: List[CRD]) -> str:
        """Generate a complete chapter for an API group."""
        safe_group = group_name.replace('.', '').replace('-', '').lower()
        
        chapter = f"""## 📁 {group_name}

### Overview

**API Group:** `{group_name}`  
**CRDs in Group:** {len(group_crds)}  
**Total Instances:** {sum(crd.instance_count for crd in group_crds):,}

### CRDs in this Group
"""
        
        # Add table of CRDs in this group
        chapter += "\n| Kind | Scope | Version | Instances | Description |\n"
        chapter += "|------|-------|---------|-----------|-------------|\n"
        
        for crd in sorted(group_crds, key=lambda x: x.kind):
            description = crd.description or "*No description available*"
            if len(description) > 80:
                description = description[:77] + "..."
            
            chapter += f"| `{crd.kind}` | {crd.scope} | {crd.version} | {crd.instance_count:,} | {description} |\n"
        
        # Add schema diagram
        chapter += f"\n### Schema Diagram\n\n"
        diagram = self._generate_group_schema_diagram(group_name, group_crds)
        chapter += diagram
        
        # Add detailed CRD documentation
        chapter += f"\n### Detailed CRD Documentation\n\n"
        
        for crd in sorted(group_crds, key=lambda x: x.kind):
            chapter += self._generate_crd_detail_section(crd)
        
        return chapter
    
    def _generate_crd_detail_section(self, crd: CRD) -> str:
        """Generate detailed documentation section for a single CRD."""
        section = f"""#### {crd.kind}

**Full Name:** `{crd.name}`  
**API Version:** `{crd.group}/{crd.version}`  
**Scope:** {crd.scope}  
**Instances:** {crd.instance_count:,}  """
        
        if crd.categories:
            section += f"\n**Categories:** {', '.join(crd.categories[:5])}  "
        
        if crd.short_names:
            section += f"\n**Short Names:** {', '.join(crd.short_names)}  "
        
        if crd.description:
            section += f"\n\n**Description:** {crd.description}"
        
        # Add schema information if available
        if crd.schemas:
            section += "\n\n**Schema Properties:**\n\n"
            primary_schema = self._get_primary_schema(crd)
            if primary_schema and primary_schema.properties:
                section += self._format_properties_table(primary_schema.properties, primary_schema.required)
            else:
                section += "*No schema properties found*\n"
        else:
            section += "\n\n*No OpenAPI schema available*\n"
        
        return section + "\n"
    
    def _format_properties_table(self, properties: Dict[str, 'CRDProperty'], required: List[str], 
                                max_properties: int = 20) -> str:
        """Format properties as a markdown table."""
        if not properties:
            return "*No properties defined*\n\n"
        
        table = "| Property | Type | Required | Description |\n"
        table += "|----------|------|----------|-------------|\n"
        
        # Sort properties: required first, then alphabetical
        sorted_props = sorted(properties.items(), key=lambda x: (x[0] not in required, x[0]))
        
        for prop_name, prop in sorted_props[:max_properties]:
            is_required = "✓" if prop_name in required else ""
            prop_type = self._format_property_type(prop)
            description = prop.description or "*No description*"
            
            # Truncate long descriptions
            if len(description) > 60:
                description = description[:57] + "..."
            
            table += f"| `{prop_name}` | `{prop_type}` | {is_required} | {description} |\n"
        
        if len(properties) > max_properties:
            table += f"\n*... and {len(properties) - max_properties} more properties*\n"
        
        return table + "\n"
    
    def _generate_markdown_appendices(self, crds: List[CRD], groups: Dict[str, List[CRD]]) -> str:
        """Generate appendices section."""
        appendices = """## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|"""
        
        # Sort CRDs alphabetically by name
        sorted_crds = sorted(crds, key=lambda x: x.name.lower())
        
        for crd in sorted_crds:
            appendices += f"\n| `{crd.name}` | `{crd.kind}` | `{crd.group}` | {crd.scope} | {crd.instance_count:,} |"
        
        # Property types summary
        appendices += "\n\n### Property Types Summary\n\n"
        
        type_counts = {}
        for crd in crds:
            if crd.schemas:
                for schema in crd.schemas.values():
                    for prop in schema.properties.values():
                        prop_type = prop.type
                        type_counts[prop_type] = type_counts.get(prop_type, 0) + 1
        
        if type_counts:
            appendices += "Property type usage across all CRDs:\n\n"
            appendices += "| Type | Usage Count |\n|------|-------------|\n"
            
            for prop_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
                appendices += f"| `{prop_type}` | {count} |\n"
        else:
            appendices += "*No property type information available*\n"
        
        # Relationship matrix
        appendices += "\n### Relationship Matrix\n\n"
        appendices += "Schema-based relationships detected between CRDs:\n\n"
        
        # Find relationships within and across API groups
        relationships = []
        all_crds = []
        for group_crds in groups.values():
            all_crds.extend(group_crds)
        
        # Within-group relationships
        for group_name, group_crds in groups.items():
            if len(group_crds) < 2:
                continue
            
            for i, crd1 in enumerate(group_crds):
                for crd2 in group_crds[i+1:]:
                    detected_relationships = self._detect_schema_relationships(crd1, crd2)
                    for rel_type in detected_relationships:
                        relationships.append((crd1.kind, crd2.kind, f"{group_name} (intra-group)", rel_type))
        
        # Cross-group relationships for related ecosystems
        cross_group_relationships = self._detect_cross_group_relationships(groups)
        relationships.extend(cross_group_relationships)
        
        if relationships:
            appendices += "| Source CRD | Target CRD | API Group | Relationship Type |\n"
            appendices += "|------------|------------|-----------|-------------------|\n"
            
            for source, target, group, rel_type in relationships:
                appendices += f"| `{source}` | `{target}` | `{group}` | {rel_type} |\n"
        else:
            appendices += "*No schema-based relationships detected*\n"
        
        # Add generation footer
        from datetime import datetime
        appendices += f"\n\n---\n\n*Documentation generated by k8s-inventory-cli on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
        
        return appendices
    
    def _generate_group_schema_diagram(self, group_name: str, crds: List[CRD]) -> str:
        """Generate a Mermaid class diagram for a single API group showing CRD schemas.
        
        Args:
            group_name: Name of the API group
            crds: List of CRDs in this group
        
        Returns:
            Mermaid diagram as string for this group
        """
        safe_group = self._sanitize_mermaid_name(group_name)
        diagram_lines = [
            "```mermaid",
            "classDiagram",
            f"    %% API Group: {group_name}"
        ]
        
        # Generate classes for each CRD in the group
        for crd in sorted(crds, key=lambda x: x.kind):
            self._add_crd_schema_class(diagram_lines, crd, safe_group)
        
        # Add relationships based on schema analysis
        self._add_schema_relationships(diagram_lines, crds, safe_group)
        
        diagram_lines.append("```")
        return "\n".join(diagram_lines)
    
    def _add_crd_schema_class(self, diagram_lines: List[str], crd: CRD, group_prefix: str) -> None:
        """Add a class definition for a CRD showing its schema properties.
        
        Args:
            diagram_lines: Lines of the diagram being built
            crd: CRD object with schema information
            group_prefix: Sanitized group name prefix
        """
        class_name = self._sanitize_mermaid_name(f"{group_prefix}_{crd.kind}")
        
        diagram_lines.append(f"    class {class_name} {{")
        diagram_lines.append(f"        +string kind: {crd.kind}")
        diagram_lines.append(f"        +string apiVersion: {crd.group}/{crd.version}")
        diagram_lines.append(f"        +string scope: {crd.scope}")
        
        # Add schema properties from the stored version
        if crd.schemas and crd.stored_version in crd.schemas:
            schema = crd.schemas[crd.stored_version]
            self._add_schema_properties_to_class(diagram_lines, schema.properties, max_depth=2)
        elif crd.schemas:
            # Use the first available schema if stored version not found
            first_schema = next(iter(crd.schemas.values()))
            self._add_schema_properties_to_class(diagram_lines, first_schema.properties, max_depth=2)
        else:
            diagram_lines.append(f"        +object spec")
            diagram_lines.append(f"        +object status")
        
        diagram_lines.append(f"    }}")
        
        # Add styling based on scope
        if crd.scope == "Namespaced":
            diagram_lines.append(f"    {class_name} : <<Namespaced>>")
        else:
            diagram_lines.append(f"    {class_name} : <<Cluster>>")
        
        # Add instance count annotation if available
        if crd.instance_count > 0:
            diagram_lines.append(f"    note for {class_name} : {crd.instance_count} instances")
    
    def _add_schema_properties_to_class(self, diagram_lines: List[str], properties: Dict[str, CRDProperty], 
                                       max_depth: int = 2, current_depth: int = 0, prefix: str = "") -> None:
        """Add schema properties to a class definition.
        
        Args:
            diagram_lines: Lines of the diagram being built
            properties: Dictionary of properties to add
            max_depth: Maximum nesting depth to display
            current_depth: Current nesting depth
            prefix: Prefix for nested properties
        """
        if current_depth >= max_depth:
            return
        
        # Sort properties, putting required ones first
        sorted_props = sorted(properties.items(), key=lambda x: (not x[1].required, x[0]))
        
        for prop_name, prop in sorted_props[:10]:  # Limit to 10 properties per level
            prop_prefix = f"{prefix}." if prefix else ""
            full_name = f"{prop_prefix}{prop_name}"
            
            # Format type display
            type_display = self._format_property_type(prop)
            required_marker = "*" if prop.required else ""
            
            diagram_lines.append(f"        +{type_display} {full_name}{required_marker}")
            
            # Add nested properties for objects (limited depth)
            if prop.type == "object" and prop.properties and current_depth < max_depth - 1:
                self._add_schema_properties_to_class(
                    diagram_lines, prop.properties, max_depth, current_depth + 1, full_name
                )
    
    def _format_property_type(self, prop: CRDProperty) -> str:
        """Format a property type for display in Mermaid.
        
        Args:
            prop: CRDProperty object
        
        Returns:
            Formatted type string
        """
        base_type = prop.type
        
        if prop.format:
            return f"{base_type}({prop.format})"
        elif prop.enum:
            if len(prop.enum) <= 3:
                enum_str = "|".join(prop.enum)
                return f"enum[{enum_str}]"
            else:
                return f"enum[{len(prop.enum)} values]"
        elif base_type == "array" and prop.items:
            item_type = self._format_property_type(prop.items)
            return f"array<{item_type}>"
        
        return base_type
    
    def _add_schema_relationships(self, diagram_lines: List[str], crds: List[CRD], group_prefix: str) -> None:
        """Add relationships between CRDs based on schema analysis.
        
        Args:
            diagram_lines: Lines of the diagram being built
            crds: List of CRDs in the group
            group_prefix: Sanitized group name prefix
        """
        if len(crds) < 2:
            return
        
        # Analyze schema relationships
        for i, crd1 in enumerate(crds):
            for crd2 in crds[i+1:]:
                relationships = self._detect_schema_relationships(crd1, crd2)
                
                class1 = self._sanitize_mermaid_name(f"{group_prefix}_{crd1.kind}")
                class2 = self._sanitize_mermaid_name(f"{group_prefix}_{crd2.kind}")
                
                for relationship in relationships:
                    if relationship == "references":
                        diagram_lines.append(f"    {class1} --> {class2} : references")
                    elif relationship == "owns":
                        diagram_lines.append(f"    {class1} --> {class2} : owns")
                    elif relationship == "uses":
                        diagram_lines.append(f"    {class1} --> {class2} : uses")
                    elif relationship == "configures":
                        diagram_lines.append(f"    {class1} --> {class2} : configures")
                    elif relationship == "templates":
                        diagram_lines.append(f"    {class1} --> {class2} : templates")
                    elif relationship == "similar_schema":
                        diagram_lines.append(f"    {class1} --> {class2} : similar schema")
                    elif relationship == "federates":
                        diagram_lines.append(f"    {class1} --> {class2} : federates")
                    elif relationship == "routes_to":
                        diagram_lines.append(f"    {class1} --> {class2} : routes to")
                    elif relationship == "flows_to":
                        diagram_lines.append(f"    {class1} --> {class2} : flows to")
    
    def _detect_schema_relationships(self, crd1: CRD, crd2: CRD) -> List[str]:
        """Detect relationships between CRDs based on their schemas.
        
        Enhanced for complex ecosystems like Strimzi, Istio, Knative, etc.
        
        Args:
            crd1: First CRD
            crd2: Second CRD
        
        Returns:
            List of detected relationship types
        """
        relationships = []
        
        # Get schemas for both CRDs
        schema1 = self._get_primary_schema(crd1)
        schema2 = self._get_primary_schema(crd2)
        
        if not schema1 or not schema2:
            return relationships
        
        # Enhanced reference detection
        if self._schemas_have_references(schema1, schema2, crd2.kind):
            relationships.append("references")
        
        if self._schemas_have_references(schema2, schema1, crd1.kind):
            relationships.append("references")
        
        # Enhanced ownership patterns (parent-child)
        if self._detect_ownership_pattern(schema1, crd2.kind):
            relationships.append("owns")
        elif self._detect_ownership_pattern(schema2, crd1.kind):
            relationships.append("owns")
        
        # Composition pattern (uses/depends on)
        if self._detect_composition_pattern(schema1, crd2.kind):
            relationships.append("uses")
        elif self._detect_composition_pattern(schema2, crd1.kind):
            relationships.append("uses")
        
        # Configuration pattern (configures)
        if self._detect_configuration_pattern(schema1, crd2.kind):
            relationships.append("configures")
        elif self._detect_configuration_pattern(schema2, crd1.kind):
            relationships.append("configures")
        
        # Resource template pattern (templates)
        if self._detect_template_pattern(schema1, crd2.kind):
            relationships.append("templates")
        elif self._detect_template_pattern(schema2, crd1.kind):
            relationships.append("templates")
        
        # Extended similar schemas check with higher threshold for widget CRDs
        similarity_threshold = 0.3  # Default threshold
        
        # Use higher threshold for widget template CRDs to reduce noise
        if (crd1.group == "widgets.templates.krateo.io" and crd2.group == "widgets.templates.krateo.io") or \
           ("widget" in crd1.kind.lower() or "widget" in crd2.kind.lower()):
            similarity_threshold = 0.6  # Higher threshold for widgets
            
        if self._schemas_similar(schema1, schema2, similarity_threshold):
            relationships.append("similar_schema")
        
        # Cross-namespace/cross-cluster patterns
        if self._detect_federation_pattern(schema1, crd2.kind):
            relationships.append("federates")
        elif self._detect_federation_pattern(schema2, crd1.kind):
            relationships.append("federates")
        
        # Network/service mesh patterns
        if self._detect_network_dependency(schema1, crd2.kind):
            relationships.append("routes_to")
        elif self._detect_network_dependency(schema2, crd1.kind):
            relationships.append("routes_to")
        
        # Data flow patterns
        if self._detect_data_flow_pattern(schema1, crd2.kind):
            relationships.append("flows_to")
        elif self._detect_data_flow_pattern(schema2, crd1.kind):
            relationships.append("flows_to")
        
        return relationships
    
    def _get_primary_schema(self, crd: CRD) -> Optional[CRDSchema]:
        """Get the primary schema for a CRD (stored version or first available).
        
        Args:
            crd: CRD object
        
        Returns:
            Primary CRDSchema or None
        """
        if not crd.schemas:
            return None
        
        if crd.stored_version in crd.schemas:
            return crd.schemas[crd.stored_version]
        
        return next(iter(crd.schemas.values())) if crd.schemas else None
    
    def _schemas_have_references(self, schema1: CRDSchema, schema2: CRDSchema, target_kind: str) -> bool:
        """Check if schema1 has properties that reference target_kind.
        
        Enhanced for complex reference patterns in ecosystems like Strimzi.
        
        Args:
            schema1: Source schema
            schema2: Target schema
            target_kind: Target CRD kind to look for
        
        Returns:
            True if references found
        """
        target_kind_lower = target_kind.lower()
        
        # Enhanced reference patterns for different ecosystems
        reference_patterns = {
            # Strimzi/Kafka patterns
            'kafka': ['kafkaCluster', 'cluster', 'brokers', 'bootstrapServers', 'kafkaRef'],
            'kafkaconnect': ['connectCluster', 'connect', 'connectRef'],
            'kafkatopic': ['topics', 'topicName', 'topicRef'],
            'kafkauser': ['users', 'username', 'authentication', 'userRef'],
            'kafkamirrormaker': ['sourceCluster', 'targetCluster', 'mirrorMaker'],
            'kafkabridge': ['bridge', 'bridgeRef'],
            'kafkarebalance': ['rebalance', 'rebalanceRef'],
            'kafkanodepool': ['nodePool', 'nodePoolRef'],
            
            # Cert-manager patterns
            'certificate': ['certificateRef', 'certRef', 'tlsCert', 'serverCert', 'clientCert'],
            'issuer': ['issuerRef', 'clusterIssuer', 'caIssuer'],
            'certificaterequest': ['certificateRequestRef', 'certRequestRef'],
            'clusterissuer': ['clusterIssuerRef', 'issuer'],
            
            # Istio patterns
            'virtualservice': ['virtualServiceRef', 'vsRef', 'routing'],
            'destinationrule': ['destinationRuleRef', 'drRef', 'destination'],
            'gateway': ['gatewayRef', 'gw', 'ingress'],
            'serviceentry': ['serviceEntryRef', 'se'],
            'envoyfilter': ['envoyFilterRef', 'filter'],
            'peerauthentication': ['peerAuthRef', 'mtls'],
            'requestauthentication': ['requestAuthRef', 'jwt'],
            'authorizationpolicy': ['authzRef', 'policy'],
            
            # PostgreSQL/Database patterns
            'cluster': ['clusterRef', 'postgresCluster', 'databaseCluster'],
            'backup': ['backupRef', 'sourceCluster', 'targetCluster'],
            'database': ['databaseRef', 'dbRef', 'schema'],
            'pooler': ['poolerRef', 'connectionPool'],
            'subscription': ['subscriptionRef', 'publication'],
            'publication': ['publicationRef', 'replication'],
            
            # ArgoCD patterns
            'application': ['applicationRef', 'appRef', 'sourceApp'],
            'appproject': ['projectRef', 'project'],
            'applicationset': ['applicationSetRef', 'appSet'],
            
            # Kubernetes core resource patterns
            'service': ['serviceName', 'serviceRef', 'svc'],
            'secret': ['secretName', 'secretRef', 'secretKeyRef'],
            'configmap': ['configMapName', 'configMapRef', 'configMapKeyRef'],
            'persistentvolume': ['pvRef', 'volumeRef'],
            'persistentvolumeclaim': ['pvcRef', 'claimRef', 'volumeClaimRef'],
            'serviceaccount': ['serviceAccountRef', 'serviceAccount'],
            'role': ['roleRef', 'clusterRoleRef'],
            'rolebinding': ['roleBindingRef', 'subjectRef'],
            'networkpolicy': ['networkPolicyRef', 'policyRef'],
            'ingress': ['ingressRef', 'ingressClass'],
            'storageclass': ['storageClass', 'storageClassRef'],
            'pod': ['podRef', 'podSelector', 'podTemplate'],
            'deployment': ['deploymentRef', 'workloadRef'],
            'statefulset': ['statefulSetRef', 'stsRef'],
            'daemonset': ['daemonSetRef', 'dsRef'],
            'job': ['jobRef', 'jobTemplate'],
            'cronjob': ['cronJobRef', 'scheduledJob'],
            'namespace': ['namespaceRef', 'targetNamespace'],
            'node': ['nodeRef', 'nodeSelector', 'nodeName'],
            'endpoint': ['endpointRef', 'endpoints'],
            
            # Operator Framework patterns
            'subscription': ['subscriptionRef', 'packageRef', 'channel'],
            'installplan': ['installPlanRef', 'plan'],
            'clusterserviceversion': ['csvRef', 'operatorRef'],
            'catalogsource': ['catalogSourceRef', 'packageManifest'],
            'operatorgroup': ['operatorGroupRef', 'targetNamespaces'],
            
            # Networking patterns
            'httproute': ['httpRouteRef', 'routeRef'],
            'grpcroute': ['grpcRouteRef'],
            'tcproute': ['tcpRouteRef'],
            'udproute': ['udpRouteRef'],
            'referencegrant': ['referenceGrantRef', 'grantRef'],
            'backendtlspolicy': ['backendRef', 'tlsPolicyRef'],
            
            # Monitoring patterns
            'servicemonitor': ['serviceMonitorRef', 'monitorRef'],
            'podmonitor': ['podMonitorRef'],
            'prometheus': ['prometheusRef', 'prometheusInstance'],
            'alertmanager': ['alertManagerRef', 'amRef'],
            'prometheusrule': ['ruleRef', 'alertRule'],
            'grafana': ['grafanaRef', 'dashboard'],
            
            # Storage patterns
            'volume': ['volumeRef', 'pv', 'pvc'],
            'volumesnapshot': ['snapshotRef', 'sourceVolume'],
            'volumesnapshotclass': ['snapshotClass', 'driver'],
            'volumesnapshotcontent': ['contentRef', 'snapshotHandle'],
            
            # Security patterns
            'policy': ['policyRef', 'securityPolicy'],
            'networkpolicy': ['networkPolicyRef', 'isolation'],
            'podsecuritypolicy': ['pspRef', 'securityContext'],
            'securitycontextconstraints': ['sccRef', 'constraints'],
            
            # Krateo patterns
            'fireworksapp': ['compositionRef', 'applicationRef', 'appRef'],
            'compositiondefinition': ['compositionDefRef', 'definitionRef'],
            'compositionreference': ['compositionRef', 'refId'],
            'template': ['templateRef', 'compositionTemplateRef'],
            'restaction': ['actionRef', 'templateRef'],
            'restdefinition': ['definitionRef', 'swaggerRef'],
            'krateplatformops': ['platformRef', 'opsRef'],
            'deployment': ['deploymentRef', 'krateoDeploymentRef'],
            'registration': ['registrationRef', 'eventRouterRef'],
            'strategy': ['strategyRef', 'authStrategyRef'],
            'bearerauth': ['authRef', 'bearerRef'],
            'ldapconfig': ['ldapRef', 'authConfigRef'],
            'oauthconfig': ['oauthRef', 'authConfigRef'], 
            'oidcconfig': ['oidcRef', 'authConfigRef'],
            'user': ['userRef', 'authUserRef'],
            'repo': ['repoRef', 'gitRepoRef', 'repositoryRef'],
            'collaborator': ['collaboratorRef', 'repoCollaboratorRef'],
            'workflow': ['workflowRef', 'githubWorkflowRef'],
            'runnergroup': ['runnerGroupRef', 'githubRunnerRef'],
            'teamrepo': ['teamRepoRef', 'repositoryRef'],
            
            # Widget template patterns
            'page': ['pageRef', 'widgetPageRef'],
            'panel': ['panelRef', 'widgetPanelRef'],
            'button': ['buttonRef', 'widgetButtonRef'],
            'form': ['formRef', 'widgetFormRef'],
            'table': ['tableRef', 'widgetTableRef'],
            'datagrid': ['dataGridRef', 'gridRef'],
            'filters': ['filtersRef', 'filterRef'],
            'column': ['columnRef', 'layoutColumnRef'],
            'row': ['rowRef', 'layoutRowRef'],
            'route': ['routeRef', 'navigationRouteRef'],
            'routesloader': ['routesLoaderRef', 'routeLoaderRef'],
            'navmenu': ['navMenuRef', 'navigationMenuRef'],
            'navmenuitem': ['navMenuItemRef', 'menuItemRef'],
            'tablist': ['tabListRef', 'tabsRef'],
            'yamlviewer': ['yamlViewerRef', 'viewerRef'],
            'paragraph': ['paragraphRef', 'textRef'],
            'eventlist': ['eventListRef', 'eventsRef'],
            'barchart': ['barChartRef', 'chartRef'],
            'linechart': ['lineChartRef', 'chartRef'],
            'piechart': ['pieChartRef', 'chartRef'],
            'flowchart': ['flowChartRef', 'diagramRef'],
        }
        
        def check_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 4:  # Prevent infinite recursion
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Direct target kind references
                if target_kind_lower in prop_name_lower:
                    return True
                
                # Check enhanced reference patterns
                if target_kind_lower in reference_patterns:
                    for pattern in reference_patterns[target_kind_lower]:
                        if pattern in prop_name_lower:
                            return True
                
                # Check property descriptions for references
                if prop.description:
                    desc_lower = prop.description.lower()
                    if target_kind_lower in desc_lower:
                        return True
                    
                    # Check for reference words + target kind
                    reference_words = ['refers to', 'references', 'points to', 'uses', 'targets']
                    for ref_word in reference_words:
                        if ref_word in desc_lower and target_kind_lower in desc_lower:
                            return True
                
                # Check for selector patterns (common in Kubernetes)
                if 'selector' in prop_name_lower and prop.type == 'object':
                    if prop.properties and any(
                        target_kind_lower in nested_name.lower() 
                        for nested_name in prop.properties.keys()
                    ):
                        return True
                
                # Check for reference object patterns
                if prop_name_lower.endswith('ref') or prop_name_lower.endswith('reference'):
                    if prop.properties and any(
                        'name' in nested_name.lower() or 'kind' in nested_name.lower()
                        for nested_name in prop.properties.keys()
                    ):
                        return True
                
                # Recursively check nested properties
                if prop.properties and check_properties(prop.properties, depth + 1):
                    return True
                
                # Check array items
                if prop.items and prop.items.properties and check_properties(
                    prop.items.properties, depth + 1
                ):
                    return True
            
            return False
        
        return check_properties(schema1.properties)
    
    def _detect_ownership_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect if schema indicates ownership of target_kind resources.
        
        Enhanced with more sophisticated ownership patterns across different ecosystems.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if ownership pattern detected
        """
        target_lower = target_kind.lower()
        
        # Enhanced ownership keywords with context
        ownership_patterns = {
            # Direct ownership patterns
            'selector': ['podSelector', 'nodeSelector', 'labelSelector', 'matchLabels'],
            'template': ['podTemplate', 'containerTemplate', 'jobTemplate', 'volumeTemplate'],
            'spec': ['podSpec', 'containerSpec', 'jobSpec', 'serviceSpec'],
            'managed': ['managedResources', 'managedBy', 'ownedResources'],
            'children': ['childResources', 'dependentResources'],
            
            # Lifecycle management patterns
            'create': ['createPolicy', 'autoCreate', 'provision'],
            'delete': ['deletePolicy', 'autoDelete', 'cleanup'],
            'update': ['updateStrategy', 'rollout', 'upgrade'],
            
            # Controller patterns
            'controller': ['controllerRef', 'ownerRef', 'parentRef'],
            'owner': ['ownerReference', 'ownedBy', 'controlledBy'],
            'replica': ['replicas', 'replicaSet', 'instances'],
            
            # Resource management patterns
            'resource': ['resourceQuota', 'resourceLimits', 'allocatedResources'],
            'policy': ['creationPolicy', 'deletionPolicy', 'managementPolicy'],
            
            # Krateo-specific ownership patterns
            'composition': ['compositionTemplate', 'composedResources', 'managedComposition'],
            'widget': ['widgetItems', 'childWidgets', 'nestedWidgets', 'widgetChildren'],
            'layout': ['layoutItems', 'layoutChildren', 'containedItems'],
            'navigation': ['navItems', 'menuItems', 'routeItems'],
            'form': ['formFields', 'formItems', 'formComponents'],
            'page': ['pageItems', 'pageComponents', 'pageContent'],
            'panel': ['panelItems', 'panelContent', 'panelChildren'],
            'template': ['templateItems', 'templateResources', 'instantiatedResources'],
            'auth': ['authUsers', 'authStrategies', 'managedAuth'],
            'git': ['repositories', 'managedRepos', 'gitResources'],
        }
        
        def check_ownership_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 3:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Direct target kind ownership
                if target_lower in prop_name_lower:
                    # Check if it's in an ownership context
                    for pattern_key, patterns in ownership_patterns.items():
                        if any(pattern in prop_name_lower for pattern in patterns):
                            return True
                
                # Check for ownership indicators in descriptions
                if prop.description:
                    desc_lower = prop.description.lower()
                    ownership_indicators = [
                        f'manages {target_lower}', f'creates {target_lower}', f'owns {target_lower}',
                        f'controls {target_lower}', f'provisions {target_lower}', f'spawns {target_lower}',
                        f'{target_lower} template', f'{target_lower} specification', f'{target_lower} selector'
                    ]
                    if any(indicator in desc_lower for indicator in ownership_indicators):
                        return True
                
                # Check for Kubernetes-style owner references
                if 'ownerreference' in prop_name_lower or 'controllerref' in prop_name_lower:
                    if prop.properties and any(
                        'kind' in nested_prop.lower() for nested_prop in prop.properties.keys()
                    ):
                        return True
                
                # Check nested properties
                if prop.properties and check_ownership_properties(prop.properties, depth + 1):
                    return True
                    
                # Check array items for ownership patterns
                if prop.items and prop.items.properties and check_ownership_properties(
                    prop.items.properties, depth + 1
                ):
                    return True
            
            return False
        
        return check_ownership_properties(schema.properties)
    
    def _detect_composition_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect if schema uses/depends on target_kind resources.
        
        Enhanced for Strimzi patterns like Kafka using KafkaConnect, Topics using Kafka, etc.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if composition pattern detected
        """
        target_lower = target_kind.lower()
        
        # Strimzi-specific composition patterns
        strimzi_patterns = {
            'topic': ['kafka', 'cluster'],
            'user': ['kafka', 'cluster'],
            'connector': ['kafkaconnect', 'connect'],
            'mirror': ['kafka', 'cluster'],
            'bridge': ['kafka', 'cluster']
        }
        
        composition_keywords = [
            'cluster', 'clusterName', 'kafkaCluster', 'connectCluster',
            'bootstrapServers', 'brokers', 'endpoints',
            'source', 'target', 'destination', 'upstream', 'downstream'
        ]
        
        def check_composition_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 3:  # Limit recursion depth
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Direct target kind references
                if target_lower in prop_name_lower:
                    return True
                
                # Check for composition keywords combined with target
                for keyword in composition_keywords:
                    if keyword in prop_name_lower and (
                        target_lower in prop_name_lower or
                        (prop.description and target_lower in prop.description.lower())
                    ):
                        return True
                
                # Check Strimzi-specific patterns
                for source_pattern, targets in strimzi_patterns.items():
                    if source_pattern in schema.version.lower() or any(
                        source_pattern in prop_name_lower for prop_name_lower in props.keys()
                    ):
                        if target_lower in targets:
                            return True
                
                # Check nested properties
                if prop.properties and check_composition_properties(prop.properties, depth + 1):
                    return True
                
                # Check array items
                if prop.items and prop.items.properties and check_composition_properties(
                    prop.items.properties, depth + 1
                ):
                    return True
            
            return False
        
        return check_composition_properties(schema.properties)
    
    def _detect_configuration_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect if schema configures target_kind resources.
        
        Enhanced for configuration relationships like KafkaConnect configuring Connectors.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if configuration pattern detected
        """
        target_lower = target_kind.lower()
        
        config_keywords = [
            'config', 'configuration', 'settings', 'properties', 'params',
            'options', 'overrides', 'customization', 'tuning'
        ]
        
        def check_config_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 2:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Look for configuration keywords with target references
                for keyword in config_keywords:
                    if keyword in prop_name_lower and target_lower in prop_name_lower:
                        return True
                    
                    # Check if property is a config object that might configure target
                    if keyword in prop_name_lower and prop.type == "object":
                        if prop.description and target_lower in prop.description.lower():
                            return True
                
                # Check nested properties
                if prop.properties and check_config_properties(prop.properties, depth + 1):
                    return True
            
            return False
        
        return check_config_properties(schema.properties)
    
    def _detect_template_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect if schema templates target_kind resources.
        
        Enhanced for template relationships like StatefulSet templates for Kafka pods.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if template pattern detected
        """
        target_lower = target_kind.lower()
        
        template_keywords = [
            'template', 'podTemplate', 'containerTemplate', 'volumeTemplate',
            'spec', 'podSpec', 'containerSpec', 'serviceTemplate'
        ]
        
        def check_template_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 2:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Look for template keywords
                for keyword in template_keywords:
                    if keyword in prop_name_lower:
                        # If it's a template, check if it's for the target kind
                        if target_lower in prop_name_lower or (
                            prop.description and target_lower in prop.description.lower()
                        ):
                            return True
                        
                        # Template objects often contain the target spec
                        if prop.type == "object" and prop.properties:
                            # Look for target-specific properties in template
                            if any(target_lower in nested_name.lower() 
                                 for nested_name in prop.properties.keys()):
                                return True
                
                # Check nested properties
                if prop.properties and check_template_properties(prop.properties, depth + 1):
                    return True
            
            return False
        
        return check_template_properties(schema.properties)
    
    def _detect_federation_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect cross-namespace or cross-cluster federation patterns.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if federation pattern detected
        """
        target_lower = target_kind.lower()
        
        federation_keywords = [
            'crossCluster', 'multiCluster', 'federation', 'remote', 'external',
            'crossNamespace', 'targetNamespace', 'sourceNamespace',
            'peer', 'mirror', 'replica', 'sync', 'replication'
        ]
        
        def check_federation_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 2:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Check for federation keywords combined with target
                for keyword in federation_keywords:
                    if keyword in prop_name_lower and (
                        target_lower in prop_name_lower or
                        (prop.description and target_lower in prop.description.lower())
                    ):
                        return True
                
                # Check nested properties
                if prop.properties and check_federation_properties(prop.properties, depth + 1):
                    return True
            
            return False
        
        return check_federation_properties(schema.properties)
    
    def _detect_network_dependency(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect network routing or service mesh dependencies.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if network dependency detected
        """
        target_lower = target_kind.lower()
        
        network_keywords = [
            'route', 'routing', 'destination', 'target', 'upstream', 'downstream',
            'backend', 'frontend', 'proxy', 'loadBalance', 'traffic',
            'ingress', 'egress', 'gateway', 'mesh', 'sidecar',
            'endpoint', 'host', 'port', 'protocol', 'tls'
        ]
        
        def check_network_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 2:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Check for network keywords combined with target
                for keyword in network_keywords:
                    if keyword in prop_name_lower and (
                        target_lower in prop_name_lower or
                        (prop.description and target_lower in prop.description.lower())
                    ):
                        return True
                
                # Check for service references in network context
                if 'service' in prop_name_lower and target_lower in prop_name_lower:
                    return True
                
                # Check nested properties
                if prop.properties and check_network_properties(prop.properties, depth + 1):
                    return True
            
            return False
        
        return check_network_properties(schema.properties)
    
    def _detect_data_flow_pattern(self, schema: CRDSchema, target_kind: str) -> bool:
        """Detect data flow or pipeline dependencies.
        
        Args:
            schema: Source schema
            target_kind: Target CRD kind
        
        Returns:
            True if data flow pattern detected
        """
        target_lower = target_kind.lower()
        
        data_flow_keywords = [
            'source', 'sink', 'input', 'output', 'pipeline', 'stream',
            'producer', 'consumer', 'publisher', 'subscriber',
            'queue', 'topic', 'channel', 'buffer', 'flow',
            'transform', 'filter', 'aggregate', 'process'
        ]
        
        def check_data_flow_properties(props: Dict[str, CRDProperty], depth: int = 0) -> bool:
            if depth > 2:
                return False
                
            for prop_name, prop in props.items():
                prop_name_lower = prop_name.lower()
                
                # Check for data flow keywords combined with target
                for keyword in data_flow_keywords:
                    if keyword in prop_name_lower and (
                        target_lower in prop_name_lower or
                        (prop.description and target_lower in prop.description.lower())
                    ):
                        return True
                
                # Check nested properties
                if prop.properties and check_data_flow_properties(prop.properties, depth + 1):
                    return True
            
            return False
        
        return check_data_flow_properties(schema.properties)
    
    def _detect_cross_group_relationships(self, groups: Dict[str, List[CRD]]) -> List[Tuple[str, str, str, str]]:
        """Detect relationships between CRDs across different API groups.
        
        Args:
            groups: Dictionary mapping API group names to CRD lists
        
        Returns:
            List of (source_kind, target_kind, group_info, relationship_type) tuples
        """
        cross_relationships = []
        
        # Define related ecosystems that should be checked for cross-group relationships
        related_ecosystems = {
            'krateo': [
                'composition.krateo.io', 'widgets.templates.krateo.io', 'templates.krateo.io',
                'core.krateo.io', 'resourcetrees.krateo.io', 'deployment.krateo.io',
                'eventrouter.krateo.io', 'authn.krateo.io', 'basic.authn.krateo.io',
                'ldap.authn.krateo.io', 'oauth.authn.krateo.io', 'oidc.authn.krateo.io',
                'git.krateo.io', 'github.kog.krateo.io', 'swaggergen.krateo.io',
                'krateo.io'
            ],
            'cert-manager': ['cert-manager.io', 'acme.cert-manager.io'],
            'strimzi': ['kafka.strimzi.io'],
            'istio': [
                'networking.istio.io', 'security.istio.io', 'telemetry.istio.io',
                'extensions.istio.io', 'install.istio.io'
            ],
            'postgresql': ['postgresql.cnpg.io', 'backup.postgresql.cnpg.io']
        }
        
        # Check relationships within each ecosystem
        for ecosystem_name, ecosystem_groups in related_ecosystems.items():
            ecosystem_crds = []
            for group_name in ecosystem_groups:
                if group_name in groups:
                    ecosystem_crds.extend(groups[group_name])
            
            if len(ecosystem_crds) < 2:
                continue
            
            # Find cross-group relationships within the ecosystem
            for i, crd1 in enumerate(ecosystem_crds):
                for crd2 in ecosystem_crds[i+1:]:
                    if crd1.group != crd2.group:  # Only cross-group relationships
                        detected_relationships = self._detect_schema_relationships(crd1, crd2)
                        for rel_type in detected_relationships:
                            cross_relationships.append((
                                crd1.kind, 
                                crd2.kind, 
                                f"{crd1.group} → {crd2.group} ({ecosystem_name})", 
                                rel_type
                            ))
        
        return cross_relationships
    
    def _schemas_similar(self, schema1: CRDSchema, schema2: CRDSchema, similarity_threshold: float = 0.3) -> bool:
        """Check if two schemas are similar based on common properties.
        
        Args:
            schema1: First schema
            schema2: Second schema
            similarity_threshold: Minimum similarity ratio
        
        Returns:
            True if schemas are similar
        """
        props1 = set(schema1.properties.keys())
        props2 = set(schema2.properties.keys())
        
        if not props1 or not props2:
            return False
        
        common_props = props1.intersection(props2)
        total_props = props1.union(props2)
        
        similarity = len(common_props) / len(total_props) if total_props else 0
        return similarity >= similarity_threshold
    
    def _sanitize_mermaid_name(self, name: str) -> str:
        """Sanitize name for Mermaid diagram compatibility.
        
        Args:
            name: Original name
        
        Returns:
            Sanitized name safe for Mermaid
        """
        import re
        # Replace dots, dashes, and other special chars with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        # Ensure it starts with a letter
        if sanitized and sanitized[0].isdigit():
            sanitized = f"CRD_{sanitized}"
        # Remove consecutive underscores
        sanitized = re.sub(r'_+', '_', sanitized)
        # Remove trailing underscores
        sanitized = sanitized.strip('_')
        return sanitized or 'Unknown'
