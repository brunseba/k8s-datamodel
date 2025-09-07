#!/bin/bash

# K8s Inventory CLI Demo Script
# This script demonstrates the key features of k8s-inventory-cli

echo "🚀 K8s Inventory CLI Demo"
echo "=========================="
echo

# Test connection
echo "1. Testing connection to Kubernetes cluster..."
uv run k8s-inventory cluster test-connection
echo

# Get cluster summary
echo "2. Getting cluster summary..."
uv run k8s-inventory cluster summary
echo

# List CRDs with filtering
echo "3. Listing CRDs from cert-manager group..."
uv run k8s-inventory crd list --group cert-manager --output rich | head -15
echo

# Count CRDs by scope
echo "4. Counting CRDs..."
uv run k8s-inventory crd count --verbose
echo

# List operators
echo "5. Listing operators (first 10)..."
uv run k8s-inventory operators list --output table | head -12
echo

# Show OLM status
echo "6. Showing OLM (Operator Lifecycle Manager) status..."
uv run k8s-inventory olm status
echo

# List OLM operators
echo "7. Listing OLM ClusterServiceVersions (first 5)..."
uv run k8s-inventory olm list --output rich | head -10
echo

# Export inventory to file
echo "8. Exporting complete inventory to file..."
uv run k8s-inventory cluster export --file demo-export.json --include-crds --include-operators --include-olm
if [ -f demo-export.json ]; then
    echo "   ✓ Export successful! File size: $(du -h demo-export.json | cut -f1)"
    rm demo-export.json  # Cleanup
fi
echo

echo "✨ Demo complete! The CLI successfully inventoried your cluster."
echo
echo "📚 Try more commands:"
echo "   k8s-inventory crd get <crd-name>          # Get specific CRD details"
echo "   k8s-inventory operators get <op-name>     # Get specific operator details"
echo "   k8s-inventory olm list --phase Succeeded  # List successful OLM operators"
echo "   k8s-inventory olm get <csv-name> -n <ns> # Get specific CSV details"
echo "   k8s-inventory cluster export              # Export full inventory"
echo "   k8s-inventory --help                      # Show all available commands"
