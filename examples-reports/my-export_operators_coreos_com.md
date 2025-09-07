# CRD Schema Documentation - operators.coreos.com API Group

> **Generated:** 2025-09-07 17:05:16
> 
> **Total CRDs:** 8
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [operators.coreos.com](#operatorscoreoscom) (8 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **8 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 8 |
| **API Groups** | 1 |
| **Total Instances** | 12 |
| **Namespaced CRDs** | 6 (75.0%) |
| **Cluster-scoped CRDs** | 2 (25.0%) |
| **Schema Coverage** | 7/8 (87.5%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **operators.coreos.com**: 8 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `ClusterServiceVersion` (operators.coreos.com): 23 properties
2. `CatalogSource` (operators.coreos.com): 12 properties
3. `Subscription` (operators.coreos.com): 7 properties


## 📁 operators.coreos.com

### Overview

**API Group:** `operators.coreos.com`  
**CRDs in Group:** 8  
**Total Instances:** 12

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `CatalogSource` | Namespaced | v1alpha1 | 0 | *No description available* |
| `ClusterServiceVersion` | Namespaced | v1alpha1 | 0 | *No description available* |
| `InstallPlan` | Namespaced | v1alpha1 | 0 | *No description available* |
| `OLMConfig` | Cluster | v1 | 1 | *No description available* |
| `Operator` | Cluster | v1 | 4 | *No description available* |
| `OperatorCondition` | Namespaced | v2 | 5 | *No description available* |
| `OperatorGroup` | Namespaced | v1 | 2 | *No description available* |
| `Subscription` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: operators.coreos.com
    class operators_coreos_com_CatalogSource {
        +string kind: CatalogSource
        +string apiVersion: operators.coreos.com/v1alpha1
        +string scope: Namespaced
        +string address
        +string configMap
        +string description
        +string displayName
        +object grpcPodConfig
        +object grpcPodConfig.affinity
        +object grpcPodConfig.extractContent
        +None grpcPodConfig.memoryTarget
        +object grpcPodConfig.nodeSelector
        +string grpcPodConfig.priorityClassName
        +enum[legacy|restricted] grpcPodConfig.securityContextConfig
        +array<object> grpcPodConfig.tolerations
        +object icon
        +string icon.base64data
        +string icon.mediatype
        +string image
        +integer priority
        +string publisher
        +array<string> secrets
    }
    operators_coreos_com_CatalogSource : <<Namespaced>>
    class operators_coreos_com_ClusterServiceVersion {
        +string kind: ClusterServiceVersion
        +string apiVersion: operators.coreos.com/v1alpha1
        +string scope: Namespaced
        +object annotations
        +object apiservicedefinitions
        +array<object> apiservicedefinitions.owned
        +array<object> apiservicedefinitions.required
        +object cleanup
        +boolean cleanup.enabled
        +object customresourcedefinitions
        +array<object> customresourcedefinitions.owned
        +array<object> customresourcedefinitions.required
        +string description
        +string displayName
        +array<object> icon
        +object install
        +object install.spec
        +string install.strategy
        +array<object> installModes
        +array<string> keywords
    }
    operators_coreos_com_ClusterServiceVersion : <<Namespaced>>
    class operators_coreos_com_InstallPlan {
        +string kind: InstallPlan
        +string apiVersion: operators.coreos.com/v1alpha1
        +string scope: Namespaced
        +string approval
        +boolean approved
        +array<string> clusterServiceVersionNames
        +integer generation
        +string source
        +string sourceNamespace
    }
    operators_coreos_com_InstallPlan : <<Namespaced>>
    class operators_coreos_com_OLMConfig {
        +string kind: OLMConfig
        +string apiVersion: operators.coreos.com/v1
        +string scope: Cluster
        +object features
        +boolean features.disableCopiedCSVs
        +string features.packageServerSyncInterval
    }
    operators_coreos_com_OLMConfig : <<Cluster>>
    note for operators_coreos_com_OLMConfig : 1 instances
    class operators_coreos_com_Operator {
        +string kind: Operator
        +string apiVersion: operators.coreos.com/v1
        +string scope: Cluster
        +object spec
        +object status
    }
    operators_coreos_com_Operator : <<Cluster>>
    note for operators_coreos_com_Operator : 4 instances
    class operators_coreos_com_OperatorCondition {
        +string kind: OperatorCondition
        +string apiVersion: operators.coreos.com/v2
        +string scope: Namespaced
        +array<object> conditions
        +array<string> deployments
        +array<object> overrides
        +array<string> serviceAccounts
    }
    operators_coreos_com_OperatorCondition : <<Namespaced>>
    note for operators_coreos_com_OperatorCondition : 5 instances
    class operators_coreos_com_OperatorGroup {
        +string kind: OperatorGroup
        +string apiVersion: operators.coreos.com/v1
        +string scope: Namespaced
        +object selector
        +array<object> selector.matchExpressions
        +object selector.matchLabels
        +string serviceAccountName
        +boolean staticProvidedAPIs
        +array<string> targetNamespaces
        +enum[Default|TechPreviewUnsafeFailForward] upgradeStrategy
    }
    operators_coreos_com_OperatorGroup : <<Namespaced>>
    note for operators_coreos_com_OperatorGroup : 2 instances
    class operators_coreos_com_Subscription {
        +string kind: Subscription
        +string apiVersion: operators.coreos.com/v1alpha1
        +string scope: Namespaced
        +string channel
        +object config
        +object config.affinity
        +object config.annotations
        +array<object> config.env
        +array<object> config.envFrom
        +object config.nodeSelector
        +object config.resources
        +object config.selector
        +array<object> config.tolerations
        +array<object> config.volumeMounts
        +array<object> config.volumes
        +string installPlanApproval
        +string name
        +string source
        +string sourceNamespace
        +string startingCSV
    }
    operators_coreos_com_Subscription : <<Namespaced>>
    operators_coreos_com_CatalogSource --> operators_coreos_com_OLMConfig : references
    operators_coreos_com_CatalogSource --> operators_coreos_com_OLMConfig : federates
    operators_coreos_com_CatalogSource --> operators_coreos_com_Subscription : references
    operators_coreos_com_ClusterServiceVersion --> operators_coreos_com_InstallPlan : references
    operators_coreos_com_ClusterServiceVersion --> operators_coreos_com_InstallPlan : uses
    operators_coreos_com_ClusterServiceVersion --> operators_coreos_com_InstallPlan : routes to
    operators_coreos_com_ClusterServiceVersion --> operators_coreos_com_OperatorGroup : references
    operators_coreos_com_ClusterServiceVersion --> operators_coreos_com_Subscription : references
    operators_coreos_com_InstallPlan --> operators_coreos_com_OperatorGroup : references
    operators_coreos_com_InstallPlan --> operators_coreos_com_Subscription : references
    operators_coreos_com_InstallPlan --> operators_coreos_com_Subscription : uses
    operators_coreos_com_OLMConfig --> operators_coreos_com_OperatorGroup : references
    operators_coreos_com_OLMConfig --> operators_coreos_com_Subscription : references
    operators_coreos_com_OperatorCondition --> operators_coreos_com_Subscription : references
    operators_coreos_com_OperatorGroup --> operators_coreos_com_Subscription : references
    operators_coreos_com_OperatorGroup --> operators_coreos_com_Subscription : references
```
### Detailed CRD Documentation

#### CatalogSource

**Full Name:** `catalogsources.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** olm  
**Short Names:** catsrc  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceType` | `string` | ✓ | SourceType is the type of source |
| `address` | `string` |  | Address is a host that OLM can use to connect to a pre-ex... |
| `configMap` | `string` |  | ConfigMap is the name of the ConfigMap to be used to back... |
| `description` | `string` |  | *No description* |
| `displayName` | `string` |  | Metadata |
| `grpcPodConfig` | `object` |  | GrpcPodConfig exposes different overrides for the pod spe... |
| `icon` | `object` |  | *No description* |
| `image` | `string` |  | Image is an operator-registry container image to instanti... |
| `priority` | `integer` |  | Priority field assigns a weight to the catalog source to ... |
| `publisher` | `string` |  | *No description* |
| `secrets` | `array<string>` |  | Secrets represent set of secrets that can be used to acce... |
| `updateStrategy` | `object` |  | UpdateStrategy defines how updated catalog source images ... |


#### ClusterServiceVersion

**Full Name:** `clusterserviceversions.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** olm  
**Short Names:** csv, csvs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `displayName` | `string` | ✓ | The name of the operator in display format. |
| `install` | `object` | ✓ | NamedInstallStrategy represents the block of an ClusterSe... |
| `annotations` | `object` |  | Annotations is an unstructured key value map stored with ... |
| `apiservicedefinitions` | `object` |  | APIServiceDefinitions declares all of the extension apis ... |
| `cleanup` | `object` |  | Cleanup specifies the cleanup behaviour when the CSV gets... |
| `customresourcedefinitions` | `object` |  | CustomResourceDefinitions declares all of the CRDs manage... |
| `description` | `string` |  | Description of the operator. Can include the features, li... |
| `icon` | `array<object>` |  | The icon for this operator. |
| `installModes` | `array<object>` |  | InstallModes specify supported installation types |
| `keywords` | `array<string>` |  | A list of keywords describing the operator. |
| `labels` | `object` |  | Map of string keys and values that can be used to organiz... |
| `links` | `array<object>` |  | A list of links related to the operator. |
| `maintainers` | `array<object>` |  | A list of organizational entities maintaining the operator. |
| `maturity` | `string` |  | *No description* |
| `minKubeVersion` | `string` |  | *No description* |
| `nativeAPIs` | `array<object>` |  | *No description* |
| `provider` | `object` |  | The publishing entity behind the operator. |
| `relatedImages` | `array<object>` |  | List any related images, or other container images that y... |
| `replaces` | `string` |  | The name of a CSV this one replaces. Should match the `me... |
| `selector` | `object` |  | Label selector for related resources. |

*... and 3 more properties*


#### InstallPlan

**Full Name:** `installplans.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** olm  
**Short Names:** ip  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `approval` | `string` | ✓ | Approval is the user approval policy for an InstallPlan.
... |
| `approved` | `boolean` | ✓ | *No description* |
| `clusterServiceVersionNames` | `array<string>` | ✓ | *No description* |
| `generation` | `integer` |  | *No description* |
| `source` | `string` |  | *No description* |
| `sourceNamespace` | `string` |  | *No description* |


#### OLMConfig

**Full Name:** `olmconfigs.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1`  
**Scope:** Cluster  
**Instances:** 1  
**Categories:** olm  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `features` | `object` |  | Features contains the list of configurable OLM features. |


#### Operator

**Full Name:** `operators.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1`  
**Scope:** Cluster  
**Instances:** 4  
**Categories:** olm  

*No OpenAPI schema available*

#### OperatorCondition

**Full Name:** `operatorconditions.operators.coreos.com`  
**API Version:** `operators.coreos.com/v2`  
**Scope:** Namespaced  
**Instances:** 5  
**Categories:** olm  
**Short Names:** condition  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `conditions` | `array<object>` |  | *No description* |
| `deployments` | `array<string>` |  | *No description* |
| `overrides` | `array<object>` |  | *No description* |
| `serviceAccounts` | `array<string>` |  | *No description* |


#### OperatorGroup

**Full Name:** `operatorgroups.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1`  
**Scope:** Namespaced  
**Instances:** 2  
**Categories:** olm  
**Short Names:** og  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `selector` | `object` |  | Selector selects the OperatorGroup's target namespaces. |
| `serviceAccountName` | `string` |  | ServiceAccountName is the admin specified service account... |
| `staticProvidedAPIs` | `boolean` |  | Static tells OLM not to update the OperatorGroup's provid... |
| `targetNamespaces` | `array<string>` |  | TargetNamespaces is an explicit set of namespaces to targ... |
| `upgradeStrategy` | `enum[Default|TechPreviewUnsafeFailForward]` |  | UpgradeStrategy defines the upgrade strategy for operator... |


#### Subscription

**Full Name:** `subscriptions.operators.coreos.com`  
**API Version:** `operators.coreos.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** olm  
**Short Names:** sub, subs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | ✓ | *No description* |
| `source` | `string` | ✓ | *No description* |
| `sourceNamespace` | `string` | ✓ | *No description* |
| `channel` | `string` |  | *No description* |
| `config` | `object` |  | SubscriptionConfig contains configuration specified for a... |
| `installPlanApproval` | `string` |  | Approval is the user approval policy for an InstallPlan.
... |
| `startingCSV` | `string` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `catalogsources.operators.coreos.com` | `CatalogSource` | `operators.coreos.com` | Namespaced | 0 |
| `clusterserviceversions.operators.coreos.com` | `ClusterServiceVersion` | `operators.coreos.com` | Namespaced | 0 |
| `installplans.operators.coreos.com` | `InstallPlan` | `operators.coreos.com` | Namespaced | 0 |
| `olmconfigs.operators.coreos.com` | `OLMConfig` | `operators.coreos.com` | Cluster | 1 |
| `operatorconditions.operators.coreos.com` | `OperatorCondition` | `operators.coreos.com` | Namespaced | 5 |
| `operatorgroups.operators.coreos.com` | `OperatorGroup` | `operators.coreos.com` | Namespaced | 2 |
| `operators.operators.coreos.com` | `Operator` | `operators.coreos.com` | Cluster | 4 |
| `subscriptions.operators.coreos.com` | `Subscription` | `operators.coreos.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `string` | 25 |
| `array` | 20 |
| `object` | 15 |
| `boolean` | 3 |
| `integer` | 2 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `CatalogSource` | `OLMConfig` | `operators.coreos.com (intra-group)` | references |
| `CatalogSource` | `OLMConfig` | `operators.coreos.com (intra-group)` | federates |
| `CatalogSource` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `ClusterServiceVersion` | `InstallPlan` | `operators.coreos.com (intra-group)` | references |
| `ClusterServiceVersion` | `InstallPlan` | `operators.coreos.com (intra-group)` | uses |
| `ClusterServiceVersion` | `InstallPlan` | `operators.coreos.com (intra-group)` | routes_to |
| `ClusterServiceVersion` | `OperatorGroup` | `operators.coreos.com (intra-group)` | references |
| `ClusterServiceVersion` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `InstallPlan` | `OperatorGroup` | `operators.coreos.com (intra-group)` | references |
| `InstallPlan` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `InstallPlan` | `Subscription` | `operators.coreos.com (intra-group)` | uses |
| `OLMConfig` | `OperatorGroup` | `operators.coreos.com (intra-group)` | references |
| `OLMConfig` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `OperatorCondition` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `OperatorGroup` | `Subscription` | `operators.coreos.com (intra-group)` | references |
| `OperatorGroup` | `Subscription` | `operators.coreos.com (intra-group)` | references |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*