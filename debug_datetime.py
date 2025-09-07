#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import logging
import json
from datetime import datetime
from k8s_inventory_cli.core.database import DatabaseManager
from k8s_inventory_cli.core.k8s_client import K8sClient
from k8s_inventory_cli.core.crd_inventory import CRDInventory
from k8s_inventory_cli.core.operator_inventory import OperatorInventory
from k8s_inventory_cli.core.olm_inventory import OLMInventory

logging.basicConfig(level=logging.DEBUG)

def find_datetime_in_object(obj, path="root", max_depth=10):
    """Recursively find datetime objects in nested structures."""
    if max_depth <= 0:
        return []
    
    results = []
    
    if isinstance(obj, datetime):
        results.append(f"FOUND datetime at {path}: {obj}")
    elif hasattr(obj, '__dict__'):
        for attr_name in dir(obj):
            if attr_name.startswith('_'):
                continue
            try:
                attr_value = getattr(obj, attr_name)
                if callable(attr_value):
                    continue
                results.extend(find_datetime_in_object(attr_value, f"{path}.{attr_name}", max_depth-1))
            except Exception as e:
                continue
    elif isinstance(obj, dict):
        for key, value in obj.items():
            results.extend(find_datetime_in_object(value, f"{path}[{key}]", max_depth-1))
    elif isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            results.extend(find_datetime_in_object(item, f"{path}[{i}]", max_depth-1))
    
    return results

def main():
    print("Starting debug...")
    
    # Initialize
    k8s_client = K8sClient()
    if not k8s_client.test_connection():
        print("Failed to connect")
        return
    
    # Get cluster info
    cluster_context = 'default'
    cluster_info = k8s_client.get_cluster_info()
    namespace_filter = None
    
    # Get CRDs
    print("Getting CRDs...")
    crd_inventory = CRDInventory(k8s_client)
    crds = crd_inventory.list_crds()
    
    print(f"Found {len(crds)} CRDs")
    
    # Look for datetime objects in CRDs
    for i, crd in enumerate(crds[:3]):  # Check first 3
        print(f"Checking CRD {i}: {crd.name}")
        datetime_found = find_datetime_in_object(crd, f"crd[{i}]")
        if datetime_found:
            print(f"  Datetime objects found in CRD {crd.name}:")
            for dt in datetime_found:
                print(f"    {dt}")
    
    # Get operators  
    print("Getting operators...")
    operator_inventory = OperatorInventory(k8s_client)
    operators = operator_inventory.list_operators()
    
    print(f"Found {len(operators)} operators")
    
    # Look for datetime objects in operators
    for i, operator in enumerate(operators[:3]):  # Check first 3
        print(f"Checking operator {i}: {operator.name}")
        datetime_found = find_datetime_in_object(operator, f"operator[{i}]")
        if datetime_found:
            print(f"  Datetime objects found in operator {operator.name}:")
            for dt in datetime_found:
                print(f"    {dt}")
    
    # Get CSVs
    print("Getting CSVs...")
    olm_inventory = OLMInventory(k8s_client)
    csvs = olm_inventory.list_csvs()
    
    print(f"Found {len(csvs)} CSVs")
    
    # Look for datetime objects in CSVs
    for i, csv in enumerate(csvs[:3]):  # Check first 3
        print(f"Checking CSV {i}: {csv.name}")
        datetime_found = find_datetime_in_object(csv, f"csv[{i}]")
        if datetime_found:
            print(f"  Datetime objects found in CSV {csv.name}:")
            for dt in datetime_found:
                print(f"    {dt}")
    
    print("Debug complete")

if __name__ == "__main__":
    main()
