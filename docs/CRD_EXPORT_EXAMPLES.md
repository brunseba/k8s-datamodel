# CRD Export-All Command Examples

The `k8s-datamodel crd export-all` command allows you to export all CRDs in your cluster with their complete property schemas to a well-formatted Markdown document with a table of contents.

## Command Syntax

```bash
k8s-datamodel crd export-all [OPTIONS]
```

## Available Options

- `-f, --output-file TEXT`: Output markdown file name (default: `crd-export.md`)
- `--max-depth INTEGER`: Maximum depth for nested properties (default: 3)
- `--required-only`: Show only required properties
- `-g, --group TEXT`: Filter by API group (partial match)
- `-s, --scope [Namespaced|Cluster]`: Filter by scope
- `--include-toc`: Include table of contents (default: true)

## Usage Examples

### 1. Export All CRDs (Full Inventory)

```bash
k8s-datamodel crd export-all --output-file cluster-inventory.md
```

This exports all CRDs in your cluster to `cluster-inventory.md` with complete property documentation.

### 2. Export Specific API Group (e.g., cert-manager)

```bash
k8s-datamodel crd export-all --group cert-manager.io --output-file cert-manager-crds.md --max-depth 2
```

Exports only cert-manager CRDs with properties nested to depth 2.

### 3. Export Only Namespaced CRDs

```bash
k8s-datamodel crd export-all --scope Namespaced --output-file namespaced-crds.md
```

Focuses on CRDs that create namespaced resources only.

### 4. Export Required Properties Only

```bash
k8s-datamodel crd export-all --group kafka.strimzi.io --required-only --output-file kafka-required.md
```

Shows only the mandatory fields for Kafka CRDs.

### 5. Database-Related CRDs

```bash
k8s-datamodel crd export-all --group postgresql.cnpg.io --output-file postgresql-inventory.md --max-depth 3
```

Exports PostgreSQL operator CRDs with detailed property nesting.

## Generated Markdown Structure

The exported markdown file contains:

1. **Header with Summary Statistics**
   - Total CRDs count
   - Total properties documented
   - Generation timestamp

2. **Table of Contents (if enabled)**
   - Organized by API group
   - Clickable links to each CRD section
   - Easy navigation for large exports

3. **CRD Details by API Group**
   - Each CRD includes:
     - Basic information table (API Group, Version, Kind, Scope, Instance Count)
     - Complete property schema with types and descriptions
     - Nested property structure (respects max-depth setting)
     - Required property indicators
     - Enum value displays
     - Array item specifications

## Example Output Features

### Property Documentation Format

```markdown
- **propertyName** (`type`) ***(required)***
  • Description of the property and its usage
  - **nestedProperty** (`string` (enum: value1|value2|value3))
    • Description of nested property
```

### Basic Information Table

| Property | Value |
|----------|-------|
| **API Group** | `cert-manager.io` |
| **Version** | `v1` |
| **Kind** | `Certificate` |
| **Scope** | Namespaced |
| **Instances** | 6 |

### Summary Statistics

- **Total properties**: 21 | **Required**: 2

## Use Cases

1. **Cluster Documentation**: Generate comprehensive documentation of your Kubernetes cluster's custom resources
2. **Operator Analysis**: Understand the capabilities and configuration options of installed operators
3. **Migration Planning**: Document current CRD schemas before cluster migrations
4. **Developer Onboarding**: Provide detailed references for team members working with custom resources
5. **Compliance Auditing**: Document all custom resources for security and compliance reviews
6. **Schema Evolution Tracking**: Create snapshots of CRD schemas to track changes over time

## Performance Notes

- Large clusters may take several minutes to process all CRDs
- Use filters (`--group`, `--scope`) to reduce processing time for focused exports
- Generated files can be quite large (hundreds of KB to several MB for comprehensive exports)
- The tool processes only CRDs with valid OpenAPI v3 schemas

## Integration with Other Tools

The generated Markdown files can be:
- Viewed in any Markdown viewer or editor
- Converted to PDF, HTML, or other formats using pandoc
- Integrated into documentation systems like GitBook, MkDocs, or Gitiles
- Stored in version control for schema change tracking
- Used as input for automated documentation pipelines

## Example Command for Different Scenarios

### Production Cluster Audit
```bash
k8s-datamodel crd export-all --output-file prod-cluster-audit.md --max-depth 2
```

### Specific Operator Documentation
```bash
k8s-datamodel crd export-all --group strimzi.io --output-file kafka-operator-docs.md
```

### Quick Reference (Required Fields Only)
```bash
k8s-datamodel crd export-all --required-only --output-file crd-quick-reference.md --max-depth 1
```
