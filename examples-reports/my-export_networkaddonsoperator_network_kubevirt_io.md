# CRD Schema Documentation - networkaddonsoperator.network.kubevirt.io API Group

> **Generated:** 2025-09-07 17:05:16
> 
> **Total CRDs:** 1
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [networkaddonsoperator.network.kubevirt.io](#networkaddonsoperatornetworkkubevirtio) (1 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **1 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 1 |
| **API Groups** | 1 |
| **Total Instances** | 1 |
| **Namespaced CRDs** | 0 (0.0%) |
| **Cluster-scoped CRDs** | 1 (100.0%) |
| **Schema Coverage** | 1/1 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **networkaddonsoperator.network.kubevirt.io**: 1 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `NetworkAddonsConfig` (networkaddonsoperator.network.kubevirt.io): 12 properties
2. `NetworkAddonsConfig` (networkaddonsoperator.network.kubevirt.io): 12 properties


## 📁 networkaddonsoperator.network.kubevirt.io

### Overview

**API Group:** `networkaddonsoperator.network.kubevirt.io`  
**CRDs in Group:** 1  
**Total Instances:** 1

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `NetworkAddonsConfig` | Cluster | v1 | 1 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: networkaddonsoperator.network.kubevirt.io
    class networkaddonsoperator_network_kubevirt_io_NetworkAddonsConfig {
        +string kind: NetworkAddonsConfig
        +string apiVersion: networkaddonsoperator.network.kubevirt.io/v1
        +string scope: Cluster
        +string imagePullPolicy
        +object kubeMacPool
        +string kubeMacPool.rangeEnd
        +string kubeMacPool.rangeStart
        +object kubeSecondaryDNS
        +string kubeSecondaryDNS.domain
        +string kubeSecondaryDNS.nameServerIP
        +object kubevirtIpamController
        +string kubevirtIpamController.defaultNetworkNADNamespace
        +object linuxBridge
        +object macvtap
        +string macvtap.devicePluginConfig
        +object multus
        +object multusDynamicNetworks
        +object ovs
        +object placementConfiguration
        +object placementConfiguration.infra
        +object placementConfiguration.workloads
    }
    networkaddonsoperator_network_kubevirt_io_NetworkAddonsConfig : <<Cluster>>
    note for networkaddonsoperator_network_kubevirt_io_NetworkAddonsConfig : 1 instances
```
### Detailed CRD Documentation

#### NetworkAddonsConfig

**Full Name:** `networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io`  
**API Version:** `networkaddonsoperator.network.kubevirt.io/v1`  
**Scope:** Cluster  
**Instances:** 1  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `imagePullPolicy` | `string` |  | PullPolicy describes a policy for if/when to pull a conta... |
| `kubeMacPool` | `object` |  | KubeMacPool plugin manages MAC allocation to Pods and VMs... |
| `kubeSecondaryDNS` | `object` |  | KubeSecondaryDNS plugin allows to support FQDN for VMI's ... |
| `kubevirtIpamController` | `object` |  | KubevirtIpamController plugin allows to support IPAM for ... |
| `linuxBridge` | `object` |  | LinuxBridge plugin allows users to create a bridge and ad... |
| `macvtap` | `object` |  | MacvtapCni plugin allows users to define Kubernetes netwo... |
| `multus` | `object` |  | Multus plugin enables attaching multiple network interfac... |
| `multusDynamicNetworks` | `object` |  | A multus extension enabling hot-plug and hot-unplug of Po... |
| `ovs` | `object` |  | Ovs plugin allows users to define Kubernetes networks on ... |
| `placementConfiguration` | `object` |  | PlacementConfiguration defines node placement configuration |
| `selfSignConfiguration` | `object` |  | SelfSignConfiguration defines self sign configuration |
| `tlsSecurityProfile` | `object` |  | TLSSecurityProfile defines the schema for a TLS security ... |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io` | `NetworkAddonsConfig` | `networkaddonsoperator.network.kubevirt.io` | Cluster | 1 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 22 |
| `string` | 2 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

*No schema-based relationships detected*


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*