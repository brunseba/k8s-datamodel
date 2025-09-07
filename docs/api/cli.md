# CLI Commands Reference

Complete API reference for all K8s Inventory CLI commands, options, and parameters.

## Global Options

These options are available for all commands:

```bash
k8s-inventory [GLOBAL_OPTIONS] COMMAND [COMMAND_OPTIONS]
```

### Global Parameters

| Option | Short | Description | Default |
|--------|--------|-------------|---------|
| `--kubeconfig` | `-k` | Path to kubeconfig file | `$HOME/.kube/config` |
| `--context` | `-c` | Kubernetes context to use | Current context |
| `--namespace` | `-n` | Default namespace for operations | `default` |
| `--verbose` | `-v` | Enable verbose output | `false` |
| `--quiet` | `-q` | Suppress non-essential output | `false` |
| `--help` | `-h` | Show help information | - |
| `--version` | | Show version information | - |

### Output Options

Available for most commands:

| Option | Values | Description | Default |
|--------|--------|-------------|---------|
| `--output` | `table`, `rich`, `json`, `yaml` | Output format | `table` |
| `--sort-by` | Column name | Sort output by column | - |
| `--no-headers` | | Suppress table headers | `false` |

## Cluster Commands

Commands for cluster-wide operations.

### `cluster test-connection`

Test connectivity to the Kubernetes cluster.

```bash
k8s-inventory cluster test-connection [OPTIONS]
```

**Options:**
- `--timeout DURATION`: Connection timeout (default: 30s)
- `--verbose`: Show detailed connection information

**Exit Codes:**
- `0`: Connection successful
- `1`: Connection failed
- `2`: Authentication failed
- `3`: Permission denied

**Examples:**
```bash
k8s-inventory cluster test-connection
k8s-inventory cluster test-connection --timeout 60s --verbose
```

### `cluster info`

Display detailed cluster information.

```bash
k8s-inventory cluster info [OPTIONS]
```

**Output includes:**
- Kubernetes version
- API server endpoint
- Node count and status
- Available API resources
- Authentication method

**Examples:**
```bash
k8s-inventory cluster info
k8s-inventory cluster info --output json
```

### `cluster summary`

Generate statistical summary of cluster resources.

```bash
k8s-inventory cluster summary [OPTIONS]
```

**Output includes:**
- CRD statistics (count, groups, scopes)
- Operator analysis (frameworks, health)
- Resource utilization metrics
- Deployment pattern analysis

**Examples:**
```bash
k8s-inventory cluster summary
k8s-inventory cluster summary --output yaml
```

### `cluster export`

Export complete cluster inventory.

```bash
k8s-inventory cluster export [OPTIONS]
```

**Options:**
- `--file PATH`: Output file path (default: stdout)
- `--include-instances`: Include custom resource instances
- `--compress`: Compress output file

**Examples:**
```bash
k8s-inventory cluster export --file inventory.json
k8s-inventory cluster export --output yaml --file inventory.yaml
k8s-inventory cluster export --compress --file inventory.json.gz
```

## CRD Commands

Commands for Custom Resource Definition management.

### `crd list`

List Custom Resource Definitions with filtering.

```bash
k8s-inventory crd list [OPTIONS]
```

**Filtering Options:**
- `--group GROUP`: Filter by API group
- `--kind KIND`: Filter by resource kind  
- `--scope SCOPE`: Filter by scope (`Namespaced` or `Cluster`)
- `--category CATEGORY`: Filter by category
- `--framework FRAMEWORK`: Filter by deployment framework

**Display Options:**
- `--show-instances`: Show instance counts
- `--show-versions`: Show all versions
- `--show-categories`: Show categories
- `--age-format FORMAT`: Age display format (`days`, `hours`, `duration`)

**Examples:**
```bash
k8s-inventory crd list
k8s-inventory crd list --group cert-manager.io
k8s-inventory crd list --scope Cluster --output json
k8s-inventory crd list --kind Certificate --show-instances
```

### `crd get`

Get detailed information about a specific CRD.

```bash
k8s-inventory crd get CRD_NAME [OPTIONS]
```

**Arguments:**
- `CRD_NAME`: Full CRD name (e.g., `certificates.cert-manager.io`)

**Options:**
- `--show-spec`: Include full CRD specification
- `--show-status`: Include status information
- `--version VERSION`: Show specific version details

**Examples:**
```bash
k8s-inventory crd get certificates.cert-manager.io
k8s-inventory crd get certificates.cert-manager.io --show-spec --output yaml
```

### `crd count`

Count custom resource instances for each CRD.

```bash
k8s-inventory crd count [OPTIONS]
```

**Filtering Options:**
- `--group GROUP`: Filter by API group
- `--scope SCOPE`: Filter by scope
- `--namespace NAMESPACE`: Count instances in specific namespace

**Display Options:**
- `--zero-instances`: Include CRDs with zero instances
- `--sort-by-count`: Sort by instance count

**Examples:**
```bash
k8s-inventory crd count
k8s-inventory crd count --group networking.k8s.io
k8s-inventory crd count --zero-instances --output json
```

## Operator Commands

Commands for Kubernetes operator management.

### `operators list`

List detected operators with classification.

```bash
k8s-inventory operators list [OPTIONS]
```

**Filtering Options:**
- `--namespace NAMESPACE`: Filter by namespace
- `--framework FRAMEWORK`: Filter by framework (`OLM`, `Helm`, `Manual`)
- `--status STATUS`: Filter by health status (`Healthy`, `Degraded`, `Failed`)
- `--all-namespaces`: Search across all namespaces

**Display Options:**
- `--show-images`: Show container images
- `--show-resources`: Show resource requirements
- `--show-conditions`: Show pod conditions
- `--group-by-namespace`: Group output by namespace

**Examples:**
```bash
k8s-inventory operators list
k8s-inventory operators list --namespace kube-system
k8s-inventory operators list --framework OLM --output json
k8s-inventory operators list --all-namespaces --show-images
```

### `operators get`

Get detailed information about a specific operator.

```bash
k8s-inventory operators get OPERATOR_NAME [OPTIONS]
```

**Arguments:**
- `OPERATOR_NAME`: Name of the operator

**Options:**
- `--namespace NAMESPACE`: Operator namespace
- `--show-pods`: Include pod details
- `--show-logs`: Include recent log entries
- `--show-events`: Include related events

**Examples:**
```bash
k8s-inventory operators get cert-manager --namespace cert-manager
k8s-inventory operators get prometheus-operator --show-pods --output yaml
```

### `operators managed-crds`

Show CRDs managed by a specific operator.

```bash
k8s-inventory operators managed-crds OPERATOR_NAME [OPTIONS]
```

**Arguments:**
- `OPERATOR_NAME`: Name of the operator

**Options:**
- `--namespace NAMESPACE`: Operator namespace
- `--show-instances`: Show instance counts for each CRD
- `--include-versions`: Show all CRD versions

**Examples:**
```bash
k8s-inventory operators managed-crds cert-manager
k8s-inventory operators managed-crds istio-pilot --show-instances --output json
```

## Common Parameters

### Filtering Expressions

Many commands support advanced filtering:

```bash
# Multiple values (OR logic)
--group "cert-manager.io,networking.k8s.io"

# Wildcard patterns  
--group "*.coreos.com"

# Negation
--group "!kustomize.config.k8s.io"

# Combined filters (AND logic)
--group cert-manager.io --scope Namespaced
```

### Output Formatting

#### Table Format Options
- `--no-headers`: Suppress column headers
- `--sort-by COLUMN`: Sort by specific column
- `--max-width WIDTH`: Maximum column width

#### JSON Format Options
- `--pretty`: Pretty-print JSON output
- `--compact`: Compact JSON output

#### YAML Format Options
- `--flow-style`: Use flow style for sequences

### Time Formats

Age and timestamp formatting options:

```bash
# Age display formats
--age-format days     # "30d"
--age-format hours    # "720h"  
--age-format duration # "30d12h45m"

# Timestamp formats
--timestamp-format rfc3339 # "2024-01-15T10:30:00Z"
--timestamp-format unix    # "1705312200"
--timestamp-format local   # "2024-01-15 10:30:00"
```

## Environment Variables

Configuration via environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `KUBECONFIG` | Path to kubeconfig file | `$HOME/.kube/config` |
| `K8S_INVENTORY_CONTEXT` | Default Kubernetes context | Current context |
| `K8S_INVENTORY_OUTPUT` | Default output format | `table` |
| `K8S_INVENTORY_NAMESPACE` | Default namespace | `default` |
| `K8S_INVENTORY_TIMEOUT` | Default timeout duration | `30s` |
| `NO_COLOR` | Disable colored output | `false` |
| `COLUMNS` | Terminal width override | Auto-detected |

## Configuration Files

### Config File Locations

K8s Inventory CLI looks for configuration files in:

1. `$HOME/.k8s-inventory/config.yaml`
2. `$XDG_CONFIG_HOME/k8s-inventory/config.yaml`
3. `/etc/k8s-inventory/config.yaml`

### Config File Format

```yaml
# ~/.k8s-inventory/config.yaml
defaults:
  output: table
  kubeconfig: ~/.kube/config
  timeout: 30s
  
filters:
  exclude_groups:
    - "kustomize.config.k8s.io"
    - "internal.example.com"
    
display:
  max_width: 120
  show_age: true
  timestamp_format: rfc3339

aliases:
  crds: crd list
  ops: operators list
  summary: cluster summary
```

## Exit Codes

Standard exit codes used by all commands:

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | General error |
| `2` | Authentication error |
| `3` | Permission denied |
| `4` | Resource not found |
| `5` | Connection timeout |
| `6` | Invalid configuration |
| `7` | Invalid arguments |
| `8` | Resource conflict |

## Error Handling

### Common Error Messages

**Connection Errors:**
```
Error: Failed to connect to cluster
Cause: Unable to reach API server at https://k8s.example.com
Solution: Check network connectivity and cluster status
```

**Authentication Errors:**
```
Error: Authentication failed
Cause: Invalid or expired credentials
Solution: Update kubeconfig or refresh authentication tokens
```

**Permission Errors:**
```
Error: Insufficient permissions
Cause: Missing RBAC permissions for CustomResourceDefinitions
Solution: Grant required permissions or use different credentials
```

### Troubleshooting Commands

```bash
# Test basic connectivity
k8s-inventory cluster test-connection --verbose

# Check authentication
kubectl auth whoami

# Verify permissions
kubectl auth can-i get customresourcedefinitions
kubectl auth can-i list deployments --all-namespaces
```

## Shell Completion

Enable shell completion for enhanced CLI experience:

### Bash
```bash
# Install completion
k8s-inventory completion bash > /etc/bash_completion.d/k8s-inventory

# Or for user only
k8s-inventory completion bash > ~/.local/share/bash-completion/completions/k8s-inventory
```

### Zsh
```bash
# Install completion
k8s-inventory completion zsh > "${fpath[1]}/_k8s-inventory"
```

### Fish
```bash
k8s-inventory completion fish > ~/.config/fish/completions/k8s-inventory.fish
```

## Advanced Usage

### Scripting Integration

```bash
#!/bin/bash
# Example automation script

# Set error handling
set -euo pipefail

# Export inventory with error handling
if ! k8s-inventory cluster export --file inventory.json; then
  echo "Failed to export cluster inventory" >&2
  exit 1
fi

# Process with jq
CRITICAL_OPERATORS=$(k8s-inventory operators list --output json | \
  jq -r '.[] | select(.framework == "OLM" and .replicas.ready != .replicas.desired) | .name')

if [[ -n "$CRITICAL_OPERATORS" ]]; then
  echo "Critical operators unhealthy: $CRITICAL_OPERATORS" >&2
  exit 1
fi
```

### Monitoring Integration

```bash
# Prometheus metrics export
k8s-inventory cluster summary --output json | \
  jq -r '
    "k8s_inventory_crds_total " + (.crds.total | tostring),
    "k8s_inventory_operators_total " + (.operators.total | tostring),
    "k8s_inventory_operators_healthy " + (.operators.healthy | tostring),
    "k8s_inventory_last_scan " + (now | tostring)
  '
```

## Related Documentation

- [Quick Start Guide](../usage/quick-start.md): Getting started with the CLI
- [Output Formats](../usage/output-formats.md): Detailed format specifications
- [Core Modules](core.md): API reference for core functionality
