# CRD Schema Documentation - argoproj.io API Group

> **Generated:** 2025-09-07 17:05:14
> 
> **Total CRDs:** 3
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [argoproj.io](#argoprojio) (3 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **3 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 3 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 3 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 3/3 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **argoproj.io**: 3 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `AppProject` (argoproj.io): 14 properties
2. `ApplicationSet` (argoproj.io): 10 properties
3. `Application` (argoproj.io): 9 properties


## 📁 argoproj.io

### Overview

**API Group:** `argoproj.io`  
**CRDs in Group:** 3  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `AppProject` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Application` | Namespaced | v1alpha1 | 0 | *No description available* |
| `ApplicationSet` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: argoproj.io
    class argoproj_io_AppProject {
        +string kind: AppProject
        +string apiVersion: argoproj.io/v1alpha1
        +string scope: Namespaced
        +array<object> clusterResourceBlacklist
        +array<object> clusterResourceWhitelist
        +string description
        +array<object> destinationServiceAccounts
        +array<object> destinations
        +array<object> namespaceResourceBlacklist
        +array<object> namespaceResourceWhitelist
        +object orphanedResources
        +array<object> orphanedResources.ignore
        +boolean orphanedResources.warn
        +boolean permitOnlyProjectScopedClusters
        +array<object> roles
    }
    argoproj_io_AppProject : <<Namespaced>>
    class argoproj_io_Application {
        +string kind: Application
        +string apiVersion: argoproj.io/v1alpha1
        +string scope: Namespaced
        +object destination
        +string destination.name
        +string destination.namespace
        +string destination.server
        +array<object> ignoreDifferences
        +array<object> info
        +string project
        +integer(int64) revisionHistoryLimit
        +object source
        +string source.chart
        +object source.directory
        +object source.helm
        +object source.kustomize
        +string source.name
        +string source.path
        +object source.plugin
        +string source.ref
        +string source.repoURL
        +string source.targetRevision
        +object sourceHydrator
        +object sourceHydrator.drySource
        +object sourceHydrator.hydrateTo
        +object sourceHydrator.syncSource
        +array<object> sources
        +object syncPolicy
        +object syncPolicy.automated
        +object syncPolicy.managedNamespaceMetadata
        +object syncPolicy.retry
        +array<string> syncPolicy.syncOptions
    }
    argoproj_io_Application : <<Namespaced>>
    class argoproj_io_ApplicationSet {
        +string kind: ApplicationSet
        +string apiVersion: argoproj.io/v1alpha1
        +string scope: Namespaced
        +boolean applyNestedSelectors
        +array<object> generators
        +boolean goTemplate
        +array<string> goTemplateOptions
        +array<object> ignoreApplicationDifferences
        +object preservedFields
        +array<string> preservedFields.annotations
        +array<string> preservedFields.labels
        +object strategy
        +object strategy.rollingSync
        +string strategy.type
        +object syncPolicy
        +enum[4 values] syncPolicy.applicationsSync
        +boolean syncPolicy.preserveResourcesOnDeletion
        +object template
        +object template.metadata
        +object template.spec
        +string templatePatch
    }
    argoproj_io_ApplicationSet : <<Namespaced>>
    argoproj_io_Application --> argoproj_io_ApplicationSet : references
    argoproj_io_Application --> argoproj_io_ApplicationSet : uses
    argoproj_io_Application --> argoproj_io_ApplicationSet : federates
    argoproj_io_Application --> argoproj_io_AppProject : references
    argoproj_io_Application --> argoproj_io_AppProject : references
    argoproj_io_Application --> argoproj_io_AppProject : uses
    argoproj_io_Application --> argoproj_io_AppProject : routes to
    argoproj_io_Application --> argoproj_io_AppProject : flows to
    argoproj_io_ApplicationSet --> argoproj_io_AppProject : references
```
### Detailed CRD Documentation

#### AppProject

**Full Name:** `appprojects.argoproj.io`  
**API Version:** `argoproj.io/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** appproj, appprojs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clusterResourceBlacklist` | `array<object>` |  | ClusterResourceBlacklist contains list of blacklisted clu... |
| `clusterResourceWhitelist` | `array<object>` |  | ClusterResourceWhitelist contains list of whitelisted clu... |
| `description` | `string` |  | Description contains optional project description |
| `destinationServiceAccounts` | `array<object>` |  | DestinationServiceAccounts holds information about the se... |
| `destinations` | `array<object>` |  | Destinations contains list of destinations available for ... |
| `namespaceResourceBlacklist` | `array<object>` |  | NamespaceResourceBlacklist contains list of blacklisted n... |
| `namespaceResourceWhitelist` | `array<object>` |  | NamespaceResourceWhitelist contains list of whitelisted n... |
| `orphanedResources` | `object` |  | OrphanedResources specifies if controller should monitor ... |
| `permitOnlyProjectScopedClusters` | `boolean` |  | PermitOnlyProjectScopedClusters determines whether destin... |
| `roles` | `array<object>` |  | Roles are user defined RBAC roles associated with this pr... |
| `signatureKeys` | `array<object>` |  | SignatureKeys contains a list of PGP key IDs that commits... |
| `sourceNamespaces` | `array<string>` |  | SourceNamespaces defines the namespaces application resou... |
| `sourceRepos` | `array<string>` |  | SourceRepos contains list of repository URLs which can be... |
| `syncWindows` | `array<object>` |  | SyncWindows controls when syncs can be run for apps in th... |


#### Application

**Full Name:** `applications.argoproj.io`  
**API Version:** `argoproj.io/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** app, apps  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `destination` | `object` | ✓ | Destination is a reference to the target Kubernetes serve... |
| `project` | `string` | ✓ | Project is a reference to the project this application be... |
| `ignoreDifferences` | `array<object>` |  | IgnoreDifferences is a list of resources and their fields... |
| `info` | `array<object>` |  | Info contains a list of information (URLs, email addresse... |
| `revisionHistoryLimit` | `integer(int64)` |  | RevisionHistoryLimit limits the number of items kept in t... |
| `source` | `object` |  | Source is a reference to the location of the application'... |
| `sourceHydrator` | `object` |  | SourceHydrator provides a way to push hydrated manifests ... |
| `sources` | `array<object>` |  | Sources is a reference to the location of the application... |
| `syncPolicy` | `object` |  | SyncPolicy controls when and how a sync will be performed |


#### ApplicationSet

**Full Name:** `applicationsets.argoproj.io`  
**API Version:** `argoproj.io/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** appset, appsets  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `generators` | `array<object>` | ✓ | *No description* |
| `template` | `object` | ✓ | *No description* |
| `applyNestedSelectors` | `boolean` |  | *No description* |
| `goTemplate` | `boolean` |  | *No description* |
| `goTemplateOptions` | `array<string>` |  | *No description* |
| `ignoreApplicationDifferences` | `array<object>` |  | *No description* |
| `preservedFields` | `object` |  | *No description* |
| `strategy` | `object` |  | *No description* |
| `syncPolicy` | `object` |  | *No description* |
| `templatePatch` | `string` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `applications.argoproj.io` | `Application` | `argoproj.io` | Namespaced | 0 |
| `applicationsets.argoproj.io` | `ApplicationSet` | `argoproj.io` | Namespaced | 0 |
| `appprojects.argoproj.io` | `AppProject` | `argoproj.io` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `array` | 17 |
| `object` | 9 |
| `string` | 3 |
| `boolean` | 3 |
| `integer` | 1 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `Application` | `ApplicationSet` | `argoproj.io (intra-group)` | references |
| `Application` | `ApplicationSet` | `argoproj.io (intra-group)` | uses |
| `Application` | `ApplicationSet` | `argoproj.io (intra-group)` | federates |
| `Application` | `AppProject` | `argoproj.io (intra-group)` | references |
| `Application` | `AppProject` | `argoproj.io (intra-group)` | references |
| `Application` | `AppProject` | `argoproj.io (intra-group)` | uses |
| `Application` | `AppProject` | `argoproj.io (intra-group)` | routes_to |
| `Application` | `AppProject` | `argoproj.io (intra-group)` | flows_to |
| `ApplicationSet` | `AppProject` | `argoproj.io (intra-group)` | references |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:14*