# Quick Start Guide

Get up and running with K8s Inventory CLI in minutes.

## Installation

### Via pipx (Recommended)
```bash
pipx install k8s-datamodel
```

### Via pip
```bash
pip install k8s-datamodel
```

### Development Installation
```bash
git clone https://github.com/brun-s/k8s-datamodel.git
cd k8s-datamodel
uv sync
uv run k8s-datamodel --help
```

## Prerequisites

- Kubernetes cluster access
- Valid kubeconfig file
- Python 3.10 or higher

## First Steps

### 1. Test Cluster Connection
```bash
k8s-datamodel cluster test-connection
```

### 2. Get Cluster Information
```bash
k8s-datamodel cluster info
```

### 3. View Cluster Summary
```bash
k8s-datamodel cluster summary
```

## Common Commands

### List All CRDs
```bash
k8s-datamodel crd list
```

### Find Operators
```bash
k8s-datamodel operators list
```

### Export Complete Inventory
```bash
k8s-datamodel cluster export --file inventory.json --output json
```

## Output Formats

K8s Inventory CLI supports multiple output formats:

- **Table** (default): Human-readable grid format
- **Rich**: Enhanced terminal output with colors
- **JSON**: Machine-readable format
- **YAML**: Structured format for both humans and machines

Example with different formats:
```bash
k8s-datamodel crd list --output table
k8s-datamodel crd list --output json
k8s-datamodel crd list --output yaml
k8s-datamodel crd list --output rich
```

## Next Steps

- Explore [CRD Commands](crds.md) for detailed CRD analysis
- Learn about [Operator Detection](operators.md) capabilities  
- Check [Cluster Operations](cluster.md) for advanced features
- Review [Output Formats](output-formats.md) for integration options
