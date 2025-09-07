# CRD Schema Documentation - helm.cattle.io API Group

> **Generated:** 2025-09-07 17:05:15
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
   - [helm.cattle.io](#helmcattleio) (2 CRDs)
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

1. **helm.cattle.io**: 2 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `HelmChart` (helm.cattle.io): 24 properties
2. `HelmChartConfig` (helm.cattle.io): 3 properties


## 📁 helm.cattle.io

### Overview

**API Group:** `helm.cattle.io`  
**CRDs in Group:** 2  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `HelmChart` | Namespaced | v1 | 0 | *No description available* |
| `HelmChartConfig` | Namespaced | v1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: helm.cattle.io
    class helm_cattle_io_HelmChart {
        +string kind: HelmChart
        +string apiVersion: helm.cattle.io/v1
        +string scope: Namespaced
        +boolean authPassCredentials
        +object authSecret
        +string authSecret.name
        +integer backOffLimit
        +boolean bootstrap
        +string chart
        +string chartContent
        +boolean createNamespace
        +object dockerRegistrySecret
        +string dockerRegistrySecret.name
        +string failurePolicy
        +string helmVersion
    }
    helm_cattle_io_HelmChart : <<Namespaced>>
    class helm_cattle_io_HelmChartConfig {
        +string kind: HelmChartConfig
        +string apiVersion: helm.cattle.io/v1
        +string scope: Namespaced
        +string failurePolicy
        +string valuesContent
        +array<object> valuesSecrets
    }
    helm_cattle_io_HelmChartConfig : <<Namespaced>>
```
### Detailed CRD Documentation

#### HelmChart

**Full Name:** `helmcharts.helm.cattle.io`  
**API Version:** `helm.cattle.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authPassCredentials` | `boolean` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `backOffLimit` | `integer` |  | *No description* |
| `bootstrap` | `boolean` |  | *No description* |
| `chart` | `string` |  | *No description* |
| `chartContent` | `string` |  | *No description* |
| `createNamespace` | `boolean` |  | *No description* |
| `dockerRegistrySecret` | `object` |  | *No description* |
| `failurePolicy` | `string` |  | *No description* |
| `helmVersion` | `string` |  | *No description* |
| `insecureSkipTLSVerify` | `boolean` |  | *No description* |
| `jobImage` | `string` |  | *No description* |
| `plainHTTP` | `boolean` |  | *No description* |
| `podSecurityContext` | `object` |  | *No description* |
| `repo` | `string` |  | *No description* |
| `repoCA` | `string` |  | *No description* |
| `repoCAConfigMap` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `set` | `object` |  | *No description* |
| `targetNamespace` | `string` |  | *No description* |

*... and 4 more properties*


#### HelmChartConfig

**Full Name:** `helmchartconfigs.helm.cattle.io`  
**API Version:** `helm.cattle.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `failurePolicy` | `string` |  | *No description* |
| `valuesContent` | `string` |  | *No description* |
| `valuesSecrets` | `array<object>` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `helmchartconfigs.helm.cattle.io` | `HelmChartConfig` | `helm.cattle.io` | Namespaced | 0 |
| `helmcharts.helm.cattle.io` | `HelmChart` | `helm.cattle.io` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `string` | 13 |
| `object` | 6 |
| `boolean` | 5 |
| `array` | 2 |
| `integer` | 1 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

*No schema-based relationships detected*


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:15*