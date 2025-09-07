#!/usr/bin/env python3
"""
Debug script to investigate CRD schema structure
"""

import json
from kubernetes import client, config
from pprint import pprint

def main():
    # Load Kubernetes config
    config.load_kube_config()
    extensions_v1_api = client.ApiextensionsV1Api()
    
    # Get the Kafka CRD
    crd_name = 'kafkas.kafka.strimzi.io'
    crd = extensions_v1_api.read_custom_resource_definition(crd_name)
    
    print(f"=== CRD: {crd_name} ===")
    print(f"Metadata name: {crd.metadata.name}")
    print(f"Group: {crd.spec.group}")
    print(f"Versions: {[v.name for v in crd.spec.versions]}")
    
    # Inspect the first version
    version = crd.spec.versions[0]
    print(f"\n=== Version: {version.name} ===")
    print(f"Has schema attribute: {hasattr(version, 'schema')}")
    if hasattr(version, 'schema'):
        print(f"Schema is not None: {version.schema is not None}")
        if version.schema is not None:
            print(f"Schema type: {type(version.schema)}")
            print(f"Schema attributes: {dir(version.schema)}")
            
            # Check for openAPIV3Schema (note the correct attribute)
            if hasattr(version.schema, 'open_apiv3_schema'):
                print(f"Has open_apiv3_schema: True")
                schema_obj = version.schema.open_apiv3_schema
                print(f"open_apiv3_schema type: {type(schema_obj)}")
                print(f"open_apiv3_schema is not None: {schema_obj is not None}")
                
                if schema_obj is not None:
                    print(f"Schema object attributes: {dir(schema_obj)[:10]}...")  # First 10 attributes
                    
                    # Try to convert to dict
                    if hasattr(schema_obj, 'to_dict'):
                        print("Has to_dict method")
                        try:
                            schema_dict = schema_obj.to_dict()
                            print(f"Converted to dict successfully, type: {type(schema_dict)}")
                            if isinstance(schema_dict, dict):
                                print(f"Dict keys: {list(schema_dict.keys())}")
                                if 'properties' in schema_dict:
                                    props = schema_dict['properties']
                                    print(f"Properties keys: {list(props.keys())}")
                                    if 'spec' in props:
                                        spec = props['spec']
                                        print(f"Spec type: {type(spec)}")
                                        if isinstance(spec, dict) and 'properties' in spec:
                                            spec_props = spec['properties']
                                            print(f"Spec properties (first 10): {list(spec_props.keys())[:10]}")
                        except Exception as e:
                            print(f"Error converting to dict: {e}")
                            import traceback
                            traceback.print_exc()
                    else:
                        print("No to_dict method")
                        print(f"Direct access test - checking __dict__: {hasattr(schema_obj, '__dict__')}")
                        if hasattr(schema_obj, '__dict__'):
                            print(f"__dict__ keys: {list(schema_obj.__dict__.keys())[:5]}...")
            else:
                print(f"No open_apiv3_schema attribute found")
                return

if __name__ == "__main__":
    main()
