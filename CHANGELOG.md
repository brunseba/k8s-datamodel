# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Complete Database Functionality**: Full SQLite database support for persistent cluster inventory storage
  - Store complete CRD, Operator, and CSV specifications in database
  - Comprehensive snapshot management (create, list, view, export, delete)
  - Multi-cluster support with cluster context tracking
  - Database statistics and storage analytics
  - Historical tracking and comparison capabilities
  
- **Enhanced OLM Support**: Complete Operator Lifecycle Manager integration
  - ClusterServiceVersion (CSV) discovery and analysis
  - OLM operator relationship mapping to deployments
  - Installation strategy and permission analysis
  - Version management tracking (replaces, skips, upgrade paths)
  
- **Full Spec Storage**: Complete Kubernetes resource specification persistence
  - CRD specifications with metadata, spec, status, and schema details
  - Operator specifications from deployments and statefulsets
  - CSV specifications with complete OLM metadata
  - Deep analysis capabilities for stored specifications

### Fixed
- **Datetime Serialization**: Resolved "Object of type datetime is not JSON serializable" errors
  - Added recursive datetime conversion utility for nested data structures
  - Enhanced JSON serialization with custom DateTimeEncoder
  - Proper handling of Kubernetes timestamp fields in all resource specs
  - Robust datetime processing for conditions, managed fields, and metadata timestamps

### Enhanced
- **Database Operations**: Complete set of database management commands
  - `database store`: Store complete cluster inventory snapshots
  - `database list`: List all stored snapshots with filtering
  - `database show`: View detailed snapshot information
  - `database export`: Export snapshots to JSON/YAML files
  - `database stats`: Database statistics and storage analytics
  - `database cleanup`: Manage database size and old snapshots
  - `database delete`: Remove specific snapshots

- **Spec Analysis**: Deep analysis capabilities for stored specifications
  - Security context analysis from operator specs
  - RBAC permission extraction from CSV specs
  - Resource requirements analysis from container specs
  - Configuration drift detection between snapshots
  - Custom analysis script support

### Performance
- **Optimized Storage**: Efficient storage of large resource specifications
  - SQLite database with proper indexing for query performance
  - Recursive datetime conversion with depth limiting
  - Compressed JSON storage for specifications
  - Efficient multi-resource batch operations

### Testing
- **Enhanced Test Coverage**: Comprehensive testing of new functionality
  - Database schema migration testing
  - Datetime serialization validation
  - Spec storage and retrieval testing
  - Multi-cluster scenario testing

## [Previous] - Initial Release

### Added
- **CRD Inventory**: Complete Custom Resource Definition discovery and analysis
- **Operator Detection**: Smart identification of operators from deployments/statefulsets
- **Framework Classification**: Detection of Helm, OLM, and Manual deployments
- **Multi-format Output**: Table, Rich, JSON, and YAML output formats
- **Cluster Operations**: Connection testing, info, and summary commands
- **Export Functionality**: Complete cluster inventory export capabilities
- **CLI Framework**: Comprehensive Click-based command line interface

### Features
- Python 3.10+ support with UV package management
- Rich terminal output with colors and styling
- Kubeconfig and context flexibility
- Error handling and verbose modes
- Real-time cluster analysis
- Framework detection and classification
- Resource counting and statistics

## Technical Details

### Database Schema Version: 2
- Added `spec` columns to `crds`, `operators`, and `csvs` tables
- Automatic schema migration from version 1 to version 2
- Proper datetime handling throughout the schema

### Supported Kubernetes Resources
- **CRDs**: Complete CustomResourceDefinition specs with OpenAPI schemas
- **Operators**: Deployment and StatefulSet specs with container configurations
- **CSVs**: ClusterServiceVersion specs with installation and permission details

### Storage Capabilities
- **Full Specifications**: Complete Kubernetes resource manifests
- **Metadata Preservation**: All labels, annotations, and timestamps
- **Relationship Mapping**: Links between operators, CRDs, and CSVs
- **Historical Snapshots**: Point-in-time cluster state preservation

### Analysis Features
- **Configuration Analysis**: Deep inspection of resource configurations
- **Security Assessment**: Security context and RBAC permission analysis
- **Drift Detection**: Compare configurations between snapshots
- **Compliance Reporting**: Generate compliance reports from stored data

---

For migration guides, usage examples, and detailed documentation, see the [docs/](docs/) directory.
