#!/usr/bin/env python3
"""
Debug script to test the exact same flow as the CLI command.
This should help identify why the CLI shows "No schema information available" 
when the direct extraction works fine.
"""

from src.k8s_inventory_cli.core.k8s_client import K8sClient
from src.k8s_inventory_cli.core.crd_inventory import CRDInventory
from src.k8s_inventory_cli.utils.formatters import OutputFormatter

def main():
    print("=== Debug CLI Flow ===")
    
    # Initialize exactly like the CLI does
    k8s_client = K8sClient(
        kubeconfig_path=None,  # Use default
        context=None  # Use default
    )
    
    # Test connection
    if not k8s_client.test_connection():
        print("Failed to connect to Kubernetes cluster")
        return
    
    print("✓ Connected to Kubernetes")
    
    # Create inventory exactly like CLI
    inventory = CRDInventory(k8s_client)
    
    # Get CRD details exactly like CLI
    crd_name = "kafkas.kafka.strimzi.io"
    print(f"\nGetting CRD details for: {crd_name}")
    
    crd = inventory.get_crd_details(crd_name)
    
    if not crd:
        print(f"CRD '{crd_name}' not found")
        return
    
    print(f"✓ Found CRD: {crd.name}")
    print(f"  - Group: {crd.group}")
    print(f"  - Version: {crd.version}")
    print(f"  - Kind: {crd.kind}")
    print(f"  - Stored Version: {crd.stored_version}")
    
    # Check schemas attribute
    print(f"\n=== Schema Debug ===")
    print(f"CRD.schemas type: {type(crd.schemas)}")
    print(f"CRD.schemas value: {crd.schemas}")
    if hasattr(crd, 'schemas') and crd.schemas:
        print(f"Schema versions available: {list(crd.schemas.keys())}")
        for version, schema in crd.schemas.items():
            print(f"  - Version {version}: {type(schema)}")
            if hasattr(schema, 'properties'):
                print(f"    Properties count: {len(schema.properties) if schema.properties else 0}")
    else:
        print("❌ No schemas found in CRD object!")
    
    # Test formatter exactly like CLI
    print(f"\n=== Formatter Test ===")
    formatter = OutputFormatter(use_color=False)
    
    # Test the same formatter call as CLI
    try:
        output_text = formatter.format_crd_properties(
            crd, 
            output_format="rich",
            version=None,  # Let it use default (stored version)
            max_depth=3,
            required_only=False
        )
        print("Formatter output:")
        print(output_text)
    except Exception as e:
        print(f"Formatter error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
