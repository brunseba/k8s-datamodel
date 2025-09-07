# CRD Schema Documentation - postgres.kubedb.com API Group

> **Generated:** 2025-09-07 17:05:16
> 
> **Total CRDs:** 2
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [postgres.kubedb.com](#postgreskubedbcom) (2 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **2 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 2 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 2 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 2/2 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **postgres.kubedb.com**: 2 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `Publisher` (postgres.kubedb.com): 9 properties
2. `Subscriber` (postgres.kubedb.com): 7 properties


## 📁 postgres.kubedb.com

### Overview

**API Group:** `postgres.kubedb.com`  
**CRDs in Group:** 2  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `Publisher` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Subscriber` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: postgres.kubedb.com
    class postgres_kubedb_com_Publisher {
        +string kind: Publisher
        +string apiVersion: postgres.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object allowedSubscribers
        +object allowedSubscribers.namespaces
        +object allowedSubscribers.selector
        +string databaseName
        +object databaseRef
        +string databaseRef.name
        +enum[Delete|Retain] deletionPolicy
        +boolean disable
        +string name
        +object parameters
        +array<string> parameters.operations
        +boolean parameters.publishViaPartitionRoot
        +boolean publishAllTables
        +array<string> tables
    }
    postgres_kubedb_com_Publisher : <<Namespaced>>
    class postgres_kubedb_com_Subscriber {
        +string kind: Subscriber
        +string apiVersion: postgres.kubedb.com/v1alpha1
        +string scope: Namespaced
        +string databaseName
        +object databaseRef
        +string databaseRef.name
        +enum[Delete|Retain] deletionPolicy
        +boolean disable
        +string name
        +object parameters
        +boolean parameters.binary
        +boolean parameters.connect
        +boolean parameters.copyData
        +boolean parameters.createSlot
        +boolean parameters.enabled
        +string parameters.slotName
        +boolean parameters.streaming
        +string parameters.synchronousCommit
        +string parameters.tableCreationPolicy
        +object publisher
        +object publisher.external
        +object publisher.managed
    }
    postgres_kubedb_com_Subscriber : <<Namespaced>>
    postgres_kubedb_com_Publisher --> postgres_kubedb_com_Subscriber : references
    postgres_kubedb_com_Publisher --> postgres_kubedb_com_Subscriber : references
    postgres_kubedb_com_Publisher --> postgres_kubedb_com_Subscriber : uses
    postgres_kubedb_com_Publisher --> postgres_kubedb_com_Subscriber : similar schema
    postgres_kubedb_com_Publisher --> postgres_kubedb_com_Subscriber : flows to
```
### Detailed CRD Documentation

#### Publisher

**Full Name:** `publishers.postgres.kubedb.com`  
**API Version:** `postgres.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** pgstore, kubedb, appscode  
**Short Names:** pub  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseName` | `string` | ✓ | *No description* |
| `databaseRef` | `object` | ✓ | *No description* |
| `name` | `string` | ✓ | *No description* |
| `allowedSubscribers` | `object` |  | *No description* |
| `deletionPolicy` | `enum[Delete|Retain]` |  | *No description* |
| `disable` | `boolean` |  | *No description* |
| `parameters` | `object` |  | *No description* |
| `publishAllTables` | `boolean` |  | *No description* |
| `tables` | `array<string>` |  | *No description* |


#### Subscriber

**Full Name:** `subscribers.postgres.kubedb.com`  
**API Version:** `postgres.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** pgstore, kubedb, appscode  
**Short Names:** sub  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseName` | `string` | ✓ | *No description* |
| `databaseRef` | `object` | ✓ | *No description* |
| `name` | `string` | ✓ | *No description* |
| `publisher` | `object` | ✓ | *No description* |
| `deletionPolicy` | `enum[Delete|Retain]` |  | *No description* |
| `disable` | `boolean` |  | *No description* |
| `parameters` | `object` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `publishers.postgres.kubedb.com` | `Publisher` | `postgres.kubedb.com` | Namespaced | 0 |
| `subscribers.postgres.kubedb.com` | `Subscriber` | `postgres.kubedb.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 6 |
| `string` | 6 |
| `boolean` | 3 |
| `array` | 1 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `Publisher` | `Subscriber` | `postgres.kubedb.com (intra-group)` | references |
| `Publisher` | `Subscriber` | `postgres.kubedb.com (intra-group)` | references |
| `Publisher` | `Subscriber` | `postgres.kubedb.com (intra-group)` | uses |
| `Publisher` | `Subscriber` | `postgres.kubedb.com (intra-group)` | similar_schema |
| `Publisher` | `Subscriber` | `postgres.kubedb.com (intra-group)` | flows_to |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*