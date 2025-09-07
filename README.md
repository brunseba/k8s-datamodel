# K8s Inventory CLI

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)](tests/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive CLI tool to inventory Custom Resource Definitions (CRDs) and operators in Kubernetes clusters.

## Features

- 🔍 **CRD Discovery**: List and analyze all Custom Resource Definitions with complete specs
- 🗂️ **CRD Group Synthesis**: Aggregate and analyze CRDs by API groups with detailed statistics
- 🤖 **Operator Detection**: Automatically identify and inventory operators with full specifications
- 🏷️ **Framework Detection**: Detect operator frameworks (OLM, Helm, Manual)
- 📂 **OLM Integration**: Complete ClusterServiceVersion management and analysis
- 💾 **Database Storage**: SQLite database with complete resource specification storage
- 📸 **Snapshot Management**: Historical cluster inventory with datetime serialization
- 🔄 **Configuration Drift**: Compare cluster specifications across snapshots
- 📊 **Multiple Output Formats**: Table, JSON, YAML, and rich terminal output
- 🔎 **Advanced Filtering**: Filter by namespace, group, framework, and more
- 📤 **Export Capabilities**: Export complete inventories with full specs for analysis
- 📈 **Cluster Analytics**: Comprehensive cluster summaries and statistics
- 🔒 **Security Analysis**: Deep inspection of RBAC, security contexts, and permissions
- 🕐 **Historical Tracking**: Track cluster evolution over time with persistent storage

## Installation

### Using pipx (Recommended)

```bash
pipx install k8s-inventory-cli
```

### Using pip

```bash
pip install k8s-inventory-cli
```

### From Source

```bash
git clone https://github.com/brun-s/k8s-inventory-cli.git
cd k8s-inventory-cli
uv sync
uv run k8s-inventory --help
```

## Quick Start

### Prerequisites

- Python 3.10 or later
- Access to a Kubernetes cluster
- Valid kubeconfig file

### Basic Commands

```bash
# Test cluster connection
k8s-inventory cluster test-connection

# List all CRDs
k8s-inventory crd list

# List all operators
k8s-inventory operators list

# List OLM ClusterServiceVersions
k8s-inventory olm list

# Store complete cluster inventory
k8s-inventory database store --notes "My first snapshot"

# List stored snapshots
k8s-inventory database list

# Get cluster summary
k8s-inventory cluster summary

# Export complete inventory
k8s-inventory cluster export --file inventory.json
```

## Usage Examples

### CRD Operations

```bash
# List CRDs with rich output
k8s-inventory crd list --output rich

# Filter CRDs by group
k8s-inventory crd list --group "cert-manager"

# Get details of specific CRD
k8s-inventory crd get certificates.cert-manager.io

# Count CRDs by scope
k8s-inventory crd count --scope Namespaced

# Analyze CRDs by API groups (NEW!)
k8s-inventory crd groups --output rich
k8s-inventory crd groups --sort-by instances
k8s-inventory crd groups --group "cert-manager" --output json
```

### Operator Operations

```bash
# List operators with table output
k8s-inventory operators list --output table

# Filter operators by framework
k8s-inventory operators list --framework OLM

# List operators in specific namespace
k8s-inventory operators list --namespace kube-system

# Get operator details
k8s-inventory operators get cert-manager --namespace cert-manager

# List CRDs managed by an operator
k8s-inventory operators managed-crds cert-manager --namespace cert-manager
```

### OLM Operations

```bash
# List all OLM ClusterServiceVersions
k8s-inventory olm list --output rich

# Show OLM status and statistics
k8s-inventory olm status

# Filter OLM operators by phase
k8s-inventory olm list --phase Succeeded

# Get specific ClusterServiceVersion details
k8s-inventory olm get my-operator.v1.0.0 --namespace operators

# Count OLM operators with breakdown
k8s-inventory olm count --verbose
```

### Cluster Operations

```bash
# Get cluster information
k8s-inventory cluster info

# Generate comprehensive summary
k8s-inventory cluster summary --output rich

# Export inventory to different formats
k8s-inventory cluster export --output yaml --file cluster-inventory.yaml
k8s-inventory cluster export --output json --file cluster-inventory.json

# Export only CRDs or operators
k8s-inventory cluster export --no-operators --file crds-only.json
k8s-inventory cluster export --no-crds --file operators-only.json
```

### Database Operations

```bash
# Store current cluster inventory in database
k8s-inventory database store --notes "Production cluster snapshot"

# List stored snapshots
k8s-inventory database list --output rich

# Show specific snapshot details
k8s-inventory database show 1

# Export snapshot to file
k8s-inventory database export 1 --file snapshot-1.json

# Store inventory with specific components
k8s-inventory crd list --store-db --notes "CRD inventory only"
k8s-inventory operators list --store-db --db-path /path/to/db.sqlite

# Database maintenance
k8s-inventory database stats
k8s-inventory database cleanup --keep 10
k8s-inventory database delete 1 --yes
```

### Global Options

```bash
# Use specific kubeconfig
k8s-inventory --kubeconfig /path/to/config crd list

# Use specific context
k8s-inventory --context prod-cluster crd list

# Focus on specific namespace
k8s-inventory --namespace kube-system operators list

# Enable verbose output
k8s-inventory --verbose cluster summary

# Disable colored output
k8s-inventory crd list --no-color
```

## Output Formats

### Table Format (Default)

Human-readable table format perfect for terminal viewing.

### Rich Format

Enhanced terminal output with colors, styling, and better formatting.

### JSON Format

Machine-readable format ideal for scripting and integration.

### YAML Format

Human and machine-readable format, great for configuration management.

## Architecture

```
├── src/k8s_inventory_cli/
│   ├── __init__.py
│   ├── main.py                 # CLI entry point
│   ├── commands/               # Command implementations
│   │   ├── crd.py             # CRD commands
│   │   ├── operators.py       # Operator commands
│   │   ├── olm.py             # OLM commands
│   │   ├── cluster.py         # Cluster commands
│   │   └── database.py        # Database commands
│   ├── core/                   # Core functionality
│   │   ├── k8s_client.py      # Kubernetes client wrapper
│   │   ├── crd_inventory.py   # CRD inventory logic
│   │   ├── operator_inventory.py # Operator inventory logic
│   │   ├── olm_inventory.py   # OLM inventory logic
│   │   ├── database.py        # Database management
│   │   └── models.py          # Data models
│   └── utils/                  # Utilities
│       └── formatters.py      # Output formatting
├── tests/                      # Unit tests
├── docs/                       # Documentation
└── README.md
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/brun-s/k8s-inventory-cli.git
cd k8s-inventory-cli

# Install dependencies with uv
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/k8s_inventory_cli --cov-report=html

# Run specific test file
uv run pytest tests/test_crd_inventory.py
```

### Code Quality

```bash
# Format code
uv run black src/ tests/

# Sort imports
uv run isort src/ tests/

# Lint code
uv run flake8 src/ tests/

# Type checking
uv run mypy src/

# Run all checks
uv run pre-commit run --all-files
```

### Building Documentation

```bash
# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Run code quality checks
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📚 [Documentation](https://brun-s.github.io/k8s-inventory-cli/)
- 🐛 [Issues](https://github.com/brun-s/k8s-inventory-cli/issues)
- 💬 [Discussions](https://github.com/brun-s/k8s-inventory-cli/discussions)

## Roadmap

- [x] **Database Storage**: Persistent SQLite storage for historical tracking
- [x] **Snapshot Management**: Store and manage cluster inventory snapshots
- [x] **CRD Group Analysis**: Advanced grouping and synthesis of CRDs by API groups
- [ ] Support for more operator frameworks (Kustomize, etc.)
- [ ] Historical diff and comparison capabilities
- [ ] Integration with monitoring systems
- [ ] Web UI for visualization
- [ ] Automated reporting and alerts
- [ ] Plugin system for custom extensions

---

**Built with ❤️ by [brun_s](https://github.com/brun-s)**
