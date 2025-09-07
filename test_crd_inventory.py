#!/usr/bin/env python3
"""
Test script to debug CRDInventory class
"""

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')

import sys
sys.path.insert(0, 'src')

from k8s_inventory_cli.core.k8s_client import K8sClient
from k8s_inventory_cli.core.crd_inventory import CRDInventory

def main():
    k8s_client = K8sClient()
    inventory = CRDInventory(k8s_client)
    
    # Test the exact method that should extract schemas
    crd_raw = k8s_client.extensions_v1_api.read_custom_resource_definition('kafkas.kafka.strimzi.io')
    
    print("=== Testing _extract_schemas method ===")
    schemas = inventory._extract_schemas(crd_raw)
    print(f"Extracted schemas: {list(schemas.keys())}")
    
    if schemas:
        for version, schema in schemas.items():
            print(f"Version {version}:")
            print(f"  Properties: {len(schema.properties)}")
            print(f"  Required: {schema.required}")
            print(f"  First 5 properties: {list(schema.properties.keys())[:5]}")
    
    print("\n=== Testing get_crd_details method ===")
    crd = inventory.get_crd_details('kafkas.kafka.strimzi.io')
    if crd:
        print(f"CRD found: {crd.name}")
        print(f"Schemas: {list(crd.schemas.keys())}")
        if crd.schemas:
            for version, schema in crd.schemas.items():
                print(f"  {version}: {len(schema.properties)} properties")
    else:
        print("CRD not found")

if __name__ == "__main__":
    main()
