# Output Formats

Complete guide to output formats supported by K8s Inventory CLI for integration and automation.

## Overview

K8s Inventory CLI supports multiple output formats to accommodate different use cases, from human-readable terminal output to machine-readable formats for automation and integration.

## Available Formats

### Table Format (Default)

Human-readable grid format optimized for terminal viewing:

```bash
k8s-datamodel crd list --output table
k8s-datamodel operators list --output table
```

**Characteristics:**
- Clean, aligned columns
- Truncated data for readability
- Color coding for status indicators
- Sortable columns
- Perfect for interactive terminal use

**Example Output:**
```
NAME                               GROUP                      SCOPE         AGE    INSTANCES
certificates.cert-manager.io       cert-manager.io           Namespaced    30d    5
issuers.cert-manager.io           cert-manager.io           Namespaced    30d    3
clusterissuers.cert-manager.io    cert-manager.io           Cluster       30d    1
```

### Rich Format

Enhanced terminal output with styling, colors, and visual enhancements:

```bash
k8s-datamodel crd list --output rich
k8s-datamodel operators list --output rich
```

**Features:**
- Syntax highlighting
- Color-coded status indicators
- Box-drawing characters for structure
- Enhanced typography
- Progress indicators
- Rich panels and cards

**Best For:**
- Interactive terminal sessions
- Presentations and demos
- Status dashboards
- Visual debugging

### JSON Format

Machine-readable JSON format for automation and integration:

```bash
k8s-datamodel crd list --output json
k8s-datamodel operators list --output json
k8s-datamodel cluster export --output json
```

**Characteristics:**
- Complete data preservation
- Structured, nested objects
- Easy to parse programmatically
- Supports complex data types
- Perfect for APIs and scripting

**Example Structure:**
```json
{
  "name": "certificates.cert-manager.io",
  "group": "cert-manager.io",
  "kind": "Certificate",
  "scope": "Namespaced",
  "versions": ["v1", "v1beta1"],
  "categories": ["cert-manager"],
  "short_names": ["cert", "certs"],
  "age_days": 30,
  "instance_count": 5,
  "framework": "Helm",
  "creation_timestamp": "2024-01-15T10:30:00Z"
}
```

### YAML Format

Human and machine-readable YAML format:

```bash
k8s-datamodel crd list --output yaml
k8s-datamodel operators list --output yaml
k8s-datamodel cluster export --output yaml
```

**Features:**
- Human-readable structure
- Preserves complex data relationships
- Easy to edit and version control
- Compatible with GitOps workflows
- Supports comments and documentation

**Example Structure:**
```yaml
name: certificates.cert-manager.io
group: cert-manager.io
kind: Certificate
scope: Namespaced
versions:
  - v1
  - v1beta1
categories:
  - cert-manager
short_names:
  - cert
  - certs
age_days: 30
instance_count: 5
framework: Helm
creation_timestamp: "2024-01-15T10:30:00Z"
```

## Format Selection Guidelines

### Use Table Format When:
- Working interactively in terminal
- Need quick overview of data
- Presenting information to humans
- Terminal space is limited
- Quick status checks

### Use Rich Format When:
- Creating visual presentations
- Need enhanced readability
- Working with status dashboards
- Demonstrating functionality
- Color coding is important

### Use JSON Format When:
- Building automation scripts
- Integrating with APIs
- Processing with jq or similar tools
- Storing in databases
- Creating monitoring integrations

### Use YAML Format When:
- Creating configuration files
- Working with GitOps workflows
- Need human-editable output
- Integrating with Kubernetes manifests
- Documenting infrastructure

## Output Customization

### Filtering Combined with Formats

All formats support the same filtering options:

```bash
# JSON output with filtering
k8s-datamodel crd list --group cert-manager.io --output json

# YAML output with namespace filtering
k8s-datamodel operators list --namespace kube-system --output yaml

# Rich format with scope filtering
k8s-datamodel crd list --scope Cluster --output rich
```

### File Output

Save formatted output directly to files:

```bash
# Save JSON export
k8s-datamodel cluster export --output json --file cluster-inventory.json

# Save YAML export
k8s-datamodel cluster export --output yaml --file cluster-inventory.yaml

# Save filtered CRD list
k8s-datamodel crd list --group networking.k8s.io --output json > networking-crds.json
```

## Integration Examples

### JSON Processing with jq

```bash
# Extract specific fields
k8s-datamodel crd list --output json | jq '.[] | {name, group, instances: .instance_count}'

# Filter and transform
k8s-datamodel operators list --output json | \
  jq '.[] | select(.framework == "Helm") | .name'

# Generate summary statistics
k8s-datamodel cluster export --output json | \
  jq '{
    total_crds: (.crds | length),
    total_operators: (.operators | length),
    frameworks: [.operators[].framework] | group_by(.) | map({framework: .[0], count: length})
  }'
```

### YAML Processing with yq

```bash
# Extract operator information
k8s-datamodel operators list --output yaml | \
  yq eval '.[] | select(.namespace == "kube-system")'

# Transform structure
k8s-datamodel crd list --output yaml | \
  yq eval 'map({(.name): {group: .group, scope: .scope}}) | add'

# Merge with existing YAML
k8s-datamodel cluster export --output yaml | \
  yq eval-all '. as $item ireduce ({}; . * $item)' - existing-config.yaml
```

### Shell Processing

```bash
# Table format with shell tools
k8s-datamodel crd list --output table | grep "cert-manager"
k8s-datamodel operators list --output table | awk '{print $1, $3}' | sort

# Count operations
CRD_COUNT=$(k8s-datamodel crd list --output json | jq '. | length')
echo "Total CRDs: $CRD_COUNT"
```

## Automation Patterns

### CI/CD Integration

```bash
#!/bin/bash
# Export and validate cluster state

# Export current state
k8s-datamodel cluster export --output json --file current-state.json

# Validate against expected state
if ! jq -e '.crds | length >= 50' current-state.json; then
  echo "ERROR: Expected minimum 50 CRDs"
  exit 1
fi

# Check operator health
UNHEALTHY=$(k8s-datamodel operators list --output json | \
  jq '.[] | select(.replicas.ready != .replicas.desired) | .name' | wc -l)

if [[ $UNHEALTHY -gt 0 ]]; then
  echo "ERROR: $UNHEALTHY unhealthy operators detected"
  exit 1
fi
```

### Monitoring Integration

```bash
# Generate Prometheus metrics
k8s-datamodel cluster summary --output json | \
  jq -r '
    "k8s_inventory_crds_total " + (.crds.total | tostring),
    "k8s_inventory_operators_total " + (.operators.total | tostring),
    "k8s_inventory_operators_healthy " + (.operators.healthy | tostring)
  ' > /tmp/metrics.prom
```

### Configuration Management

```bash
# Generate Ansible inventory
k8s-datamodel operators list --output json | \
  jq -r '.[] | "\(.name) ansible_host=\(.namespace) operator_framework=\(.framework)"'

# Generate Terraform variables
k8s-datamodel crd list --output json | \
  jq '{crds: [.[] | {name: .name, group: .group, scope: .scope}]}' > terraform-vars.json
```

## Performance Considerations

### Large Datasets

For clusters with many resources, consider:

```bash
# Use pagination for large results (if supported)
k8s-datamodel crd list --output json | jq '. | to_entries | .[0:50] | from_entries'

# Filter early to reduce data transfer
k8s-datamodel crd list --group specific.domain.com --output json

# Use streaming processing for large exports
k8s-datamodel cluster export --output json | jq -c '.crds[]' | while read crd; do
  # Process each CRD individually
  echo "$crd" | jq '.name'
done
```

### Memory Management

```bash
# For very large exports, consider split processing
k8s-datamodel cluster export --output json | \
  jq -c '{crds: .crds}' > crds-only.json

k8s-datamodel cluster export --output json | \
  jq -c '{operators: .operators}' > operators-only.json
```

## Format-Specific Best Practices

### JSON Best Practices
- Use `jq -c` for compact output in pipelines
- Always validate JSON integrity with `jq empty`
- Use meaningful field names when transforming
- Consider schema validation for critical integrations

### YAML Best Practices  
- Use consistent indentation (2 spaces recommended)
- Add comments for documentation
- Validate YAML syntax before committing
- Use anchors and aliases for repeated data

### Table Best Practices
- Adjust terminal width for optimal display
- Use filtering to limit column count
- Consider pagination for large datasets
- Combine with tools like `less -S` for horizontal scrolling

### Rich Best Practices
- Ensure terminal supports color output
- Use in interactive sessions, not automation
- Consider accessibility for color-blind users
- Test with different terminal themes

## Troubleshooting Output Issues

### Encoding Problems
```bash
# Force UTF-8 encoding
export LC_ALL=C.UTF-8
k8s-datamodel crd list --output rich
```

### Terminal Compatibility
```bash
# Fallback to table format if rich fails
k8s-datamodel crd list --output table
```

### Large Output Handling
```bash
# Use pagination
k8s-datamodel crd list --output table | less

# Filter to reduce output size
k8s-datamodel crd list --group cert-manager.io --output table
```

### JSON Parsing Issues
```bash
# Validate JSON output
k8s-datamodel crd list --output json | jq empty && echo "Valid JSON" || echo "Invalid JSON"

# Pretty print for debugging
k8s-datamodel crd list --output json | jq .
```

## Related Documentation

- [CRDs](crds.md): CRD-specific command examples
- [Operators](operators.md): Operator command examples  
- [Cluster Operations](cluster.md): Cluster-wide export examples
