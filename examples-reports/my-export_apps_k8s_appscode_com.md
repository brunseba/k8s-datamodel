# CRD Schema Documentation - apps.k8s.appscode.com API Group

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
   - [apps.k8s.appscode.com](#appsk8sappscodecom) (3 CRDs)
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
| **Total Instances** | 1 |
| **Namespaced CRDs** | 2 (66.7%) |
| **Cluster-scoped CRDs** | 1 (33.3%) |
| **Schema Coverage** | 3/3 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **apps.k8s.appscode.com**: 3 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `Sidekick` (apps.k8s.appscode.com): 39 properties
2. `PetSet` (apps.k8s.appscode.com): 13 properties
3. `PlacementPolicy` (apps.k8s.appscode.com): 4 properties


## 📁 apps.k8s.appscode.com

### Overview

**API Group:** `apps.k8s.appscode.com`  
**CRDs in Group:** 3  
**Total Instances:** 1

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `PetSet` | Namespaced | v1 | 0 | *No description available* |
| `PlacementPolicy` | Cluster | v1 | 1 | *No description available* |
| `Sidekick` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: apps.k8s.appscode.com
    class apps_k8s_appscode_com_PetSet {
        +string kind: PetSet
        +string apiVersion: apps.k8s.appscode.com/v1
        +string scope: Namespaced
        +boolean distributed
        +integer(int32) minReadySeconds
        +object ordinals
        +integer(int32) ordinals.start
        +object persistentVolumeClaimRetentionPolicy
        +string persistentVolumeClaimRetentionPolicy.whenDeleted
        +string persistentVolumeClaimRetentionPolicy.whenScaled
        +string podManagementPolicy
        +object podPlacementPolicy
        +string podPlacementPolicy.name
        +integer(int32) replicas
        +integer(int32) revisionHistoryLimit
        +object selector
        +array<object> selector.matchExpressions
        +object selector.matchLabels
        +string serviceName
    }
    apps_k8s_appscode_com_PetSet : <<Namespaced>>
    class apps_k8s_appscode_com_PlacementPolicy {
        +string kind: PlacementPolicy
        +string apiVersion: apps.k8s.appscode.com/v1
        +string scope: Cluster
        +object affinity
        +array<object> affinity.nodeAffinity
        +object nodeSpreadConstraint
        +integer(int32) nodeSpreadConstraint.maxSkew
        +string nodeSpreadConstraint.whenUnsatisfiable
        +object ocm
        +array<object> ocm.distributionRules
        +string ocm.sliceName
        +object zoneSpreadConstraint
        +integer(int32) zoneSpreadConstraint.maxSkew
        +string zoneSpreadConstraint.whenUnsatisfiable
    }
    apps_k8s_appscode_com_PlacementPolicy : <<Cluster>>
    note for apps_k8s_appscode_com_PlacementPolicy : 1 instances
    class apps_k8s_appscode_com_Sidekick {
        +string kind: Sidekick
        +string apiVersion: apps.k8s.appscode.com/v1alpha1
        +string scope: Namespaced
        +integer(int64) activeDeadlineSeconds
        +object affinity
        +object affinity.nodeAffinity
        +object affinity.podAffinity
        +object affinity.podAntiAffinity
        +boolean automountServiceAccountToken
        +integer(int32) backoffLimit
        +array<object> containers
        +object dnsConfig
        +array<string> dnsConfig.nameservers
        +array<object> dnsConfig.options
        +array<string> dnsConfig.searches
        +string dnsPolicy
        +boolean enableServiceLinks
        +array<object> ephemeralContainers
        +array<object> hostAliases
    }
    apps_k8s_appscode_com_Sidekick : <<Namespaced>>
    apps_k8s_appscode_com_PetSet --> apps_k8s_appscode_com_PlacementPolicy : references
    apps_k8s_appscode_com_PetSet --> apps_k8s_appscode_com_PlacementPolicy : uses
    apps_k8s_appscode_com_PetSet --> apps_k8s_appscode_com_Sidekick : references
    apps_k8s_appscode_com_PetSet --> apps_k8s_appscode_com_Sidekick : references
    apps_k8s_appscode_com_PlacementPolicy --> apps_k8s_appscode_com_Sidekick : references
```
### Detailed CRD Documentation

#### PetSet

**Full Name:** `petsets.apps.k8s.appscode.com`  
**API Version:** `apps.k8s.appscode.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `selector` | `object` | ✓ | selector is a label query over pods that should match the... |
| `serviceName` | `string` | ✓ | serviceName is the name of the service that governs this ... |
| `template` | `object` | ✓ | template is the object that describes the pod that will b... |
| `distributed` | `boolean` |  | Distributed means manifestworks will be used to manage pods |
| `minReadySeconds` | `integer(int32)` |  | Minimum number of seconds for which a newly created pod s... |
| `ordinals` | `object` |  | ordinals controls the numbering of replica indices in a P... |
| `persistentVolumeClaimRetentionPolicy` | `object` |  | persistentVolumeClaimRetentionPolicy describes the lifecy... |
| `podManagementPolicy` | `string` |  | podManagementPolicy controls how pods are created during ... |
| `podPlacementPolicy` | `object` |  | LocalObjectReference contains enough information to let y... |
| `replicas` | `integer(int32)` |  | replicas is the desired number of replicas of the given T... |
| `revisionHistoryLimit` | `integer(int32)` |  | revisionHistoryLimit is the maximum number of revisions t... |
| `updateStrategy` | `object` |  | updateStrategy indicates the PetSetUpdateStrategy that wi... |
| `volumeClaimTemplates` | `array<object>` |  | volumeClaimTemplates is a list of claims that pods are al... |


#### PlacementPolicy

**Full Name:** `placementpolicies.apps.k8s.appscode.com`  
**API Version:** `apps.k8s.appscode.com/v1`  
**Scope:** Cluster  
**Instances:** 1  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affinity` | `object` |  | If specified, the pod's scheduling constraints |
| `nodeSpreadConstraint` | `object` |  | *No description* |
| `ocm` | `object` |  | OCM provides spec for distributed pod placements using op... |
| `zoneSpreadConstraint` | `object` |  | *No description* |


#### Sidekick

**Full Name:** `sidekicks.apps.k8s.appscode.com`  
**API Version:** `apps.k8s.appscode.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `containers` | `array<object>` | ✓ | List of containers belonging to the pod.
Containers canno... |
| `leader` | `object` | ✓ | *No description* |
| `activeDeadlineSeconds` | `integer(int64)` |  | Optional duration in seconds the pod may be active on the... |
| `affinity` | `object` |  | If specified, the pod's scheduling constraints |
| `automountServiceAccountToken` | `boolean` |  | AutomountServiceAccountToken indicates whether a service ... |
| `backoffLimit` | `integer(int32)` |  | Specifies the number of retries before marking this job f... |
| `dnsConfig` | `object` |  | Specifies the DNS parameters of a pod.
Parameters specifi... |
| `dnsPolicy` | `string` |  | Set DNS policy for the pod.
Defaults to "ClusterFirst".
V... |
| `enableServiceLinks` | `boolean` |  | EnableServiceLinks indicates whether information about se... |
| `ephemeralContainers` | `array<object>` |  | List of ephemeral containers run in this pod. Ephemeral c... |
| `hostAliases` | `array<object>` |  | HostAliases is an optional list of hosts and IPs that wil... |
| `hostIPC` | `boolean` |  | Use the host's ipc namespace.
Optional: Default to false. |
| `hostNetwork` | `boolean` |  | Host networking requested for this pod. Use the host's ne... |
| `hostPID` | `boolean` |  | Use the host's pid namespace.
Optional: Default to false. |
| `hostUsers` | `boolean` |  | Use the host's user namespace.
Optional: Default to true.... |
| `hostname` | `string` |  | Specifies the hostname of the Pod
If not specified, the p... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is an optional list of references to sec... |
| `initContainers` | `array<object>` |  | List of initialization containers belonging to the pod.
I... |
| `nodeName` | `string` |  | NodeName is a request to schedule this pod onto a specifi... |
| `nodeSelector` | `object` |  | NodeSelector is a selector which must be true for the pod... |

*... and 19 more properties*




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `petsets.apps.k8s.appscode.com` | `PetSet` | `apps.k8s.appscode.com` | Namespaced | 0 |
| `placementpolicies.apps.k8s.appscode.com` | `PlacementPolicy` | `apps.k8s.appscode.com` | Cluster | 1 |
| `sidekicks.apps.k8s.appscode.com` | `Sidekick` | `apps.k8s.appscode.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 17 |
| `string` | 13 |
| `array` | 10 |
| `boolean` | 9 |
| `integer` | 7 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `PetSet` | `PlacementPolicy` | `apps.k8s.appscode.com (intra-group)` | references |
| `PetSet` | `PlacementPolicy` | `apps.k8s.appscode.com (intra-group)` | uses |
| `PetSet` | `Sidekick` | `apps.k8s.appscode.com (intra-group)` | references |
| `PetSet` | `Sidekick` | `apps.k8s.appscode.com (intra-group)` | references |
| `PlacementPolicy` | `Sidekick` | `apps.k8s.appscode.com (intra-group)` | references |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:14*