# CRD Schema Documentation - kubevirt.io API Group

> **Generated:** 2025-09-07 17:05:16
> 
> **Total CRDs:** 6
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [kubevirt.io](#kubevirtio) (6 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **6 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 6 |
| **API Groups** | 1 |
| **Total Instances** | 1 |
| **Namespaced CRDs** | 6 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 6/6 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **kubevirt.io**: 6 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `VirtualMachineInstance` (kubevirt.io): 21 properties
2. `VirtualMachineInstance` (kubevirt.io): 21 properties
3. `KubeVirt` (kubevirt.io): 18 properties


## 📁 kubevirt.io

### Overview

**API Group:** `kubevirt.io`  
**CRDs in Group:** 6  
**Total Instances:** 1

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `KubeVirt` | Namespaced | v1 | 1 | *No description available* |
| `VirtualMachine` | Namespaced | v1 | 0 | *No description available* |
| `VirtualMachineInstance` | Namespaced | v1 | 0 | *No description available* |
| `VirtualMachineInstanceMigration` | Namespaced | v1 | 0 | *No description available* |
| `VirtualMachineInstancePreset` | Namespaced | v1alpha3 | 0 | *No description available* |
| `VirtualMachineInstanceReplicaSet` | Namespaced | v1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: kubevirt.io
    class kubevirt_io_KubeVirt {
        +string kind: KubeVirt
        +string apiVersion: kubevirt.io/v1
        +string scope: Namespaced
        +object certificateRotateStrategy
        +object certificateRotateStrategy.selfSigned
        +object configuration
        +string configuration.additionalGuestMemoryOverheadRatio
        +object configuration.apiConfiguration
        +object configuration.architectureConfiguration
        +object configuration.autoCPULimitNamespaceLabelSelector
        +object configuration.commonInstancetypesDeployment
        +object configuration.controllerConfiguration
        +string configuration.cpuModel
        +None configuration.cpuRequest
        +string configuration.defaultRuntimeClass
        +object configuration.developerConfiguration
        +object customizeComponents
        +object customizeComponents.flags
        +array<object> customizeComponents.patches
        +string imagePullPolicy
        +array<object> imagePullSecrets
        +string imageRegistry
        +string imageTag
        +object infra
        +object infra.nodePlacement
        +integer infra.replicas
        +string monitorAccount
        +string monitorNamespace
    }
    kubevirt_io_KubeVirt : <<Namespaced>>
    note for kubevirt_io_KubeVirt : 1 instances
    class kubevirt_io_VirtualMachine {
        +string kind: VirtualMachine
        +string apiVersion: kubevirt.io/v1
        +string scope: Namespaced
        +array<object> dataVolumeTemplates
        +object instancetype
        +string instancetype.inferFromVolume
        +string instancetype.inferFromVolumeFailurePolicy
        +string instancetype.kind
        +string instancetype.name
        +string instancetype.revisionName
        +object preference
        +string preference.inferFromVolume
        +string preference.inferFromVolumeFailurePolicy
        +string preference.kind
        +string preference.name
        +string preference.revisionName
        +string runStrategy
        +boolean running
        +object template
        +object template.metadata
        +object template.spec
        +string updateVolumesStrategy
    }
    kubevirt_io_VirtualMachine : <<Namespaced>>
    class kubevirt_io_VirtualMachineInstance {
        +string kind: VirtualMachineInstance
        +string apiVersion: kubevirt.io/v1
        +string scope: Namespaced
        +array<object> accessCredentials
        +object affinity
        +object affinity.nodeAffinity
        +object affinity.podAffinity
        +object affinity.podAntiAffinity
        +string architecture
        +object dnsConfig
        +array<string> dnsConfig.nameservers
        +array<object> dnsConfig.options
        +array<string> dnsConfig.searches
        +string dnsPolicy
        +object domain
        +object domain.chassis
        +object domain.clock
        +object domain.cpu
        +object domain.devices
        +object domain.features
        +object domain.firmware
        +object domain.ioThreads
        +string domain.ioThreadsPolicy
        +object domain.launchSecurity
        +object domain.machine
        +string evictionStrategy
        +string hostname
        +object livenessProbe
        +object livenessProbe.exec
        +integer(int32) livenessProbe.failureThreshold
        +object livenessProbe.guestAgentPing
        +object livenessProbe.httpGet
        +integer(int32) livenessProbe.initialDelaySeconds
        +integer(int32) livenessProbe.periodSeconds
        +integer(int32) livenessProbe.successThreshold
        +object livenessProbe.tcpSocket
        +integer(int32) livenessProbe.timeoutSeconds
        +array<object> networks
    }
    kubevirt_io_VirtualMachineInstance : <<Namespaced>>
    class kubevirt_io_VirtualMachineInstanceMigration {
        +string kind: VirtualMachineInstanceMigration
        +string apiVersion: kubevirt.io/v1
        +string scope: Namespaced
        +object addedNodeSelector
        +object receive
        +string receive.migrationID
        +object sendTo
        +string sendTo.connectURL
        +string sendTo.migrationID
        +string vmiName
    }
    kubevirt_io_VirtualMachineInstanceMigration : <<Namespaced>>
    class kubevirt_io_VirtualMachineInstancePreset {
        +string kind: VirtualMachineInstancePreset
        +string apiVersion: kubevirt.io/v1alpha3
        +string scope: Namespaced
        +object domain
        +object domain.chassis
        +object domain.clock
        +object domain.cpu
        +object domain.devices
        +object domain.features
        +object domain.firmware
        +object domain.ioThreads
        +string domain.ioThreadsPolicy
        +object domain.launchSecurity
        +object domain.machine
        +object selector
        +array<object> selector.matchExpressions
        +object selector.matchLabels
    }
    kubevirt_io_VirtualMachineInstancePreset : <<Namespaced>>
    class kubevirt_io_VirtualMachineInstanceReplicaSet {
        +string kind: VirtualMachineInstanceReplicaSet
        +string apiVersion: kubevirt.io/v1
        +string scope: Namespaced
        +boolean paused
        +integer(int32) replicas
        +object selector
        +array<object> selector.matchExpressions
        +object selector.matchLabels
        +object template
        +object template.metadata
        +object template.spec
    }
    kubevirt_io_VirtualMachineInstanceReplicaSet : <<Namespaced>>
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstancePreset : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstanceReplicaSet : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstance : owns
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachineInstance : uses
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachine : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachine : references
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachine : owns
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachine : uses
    kubevirt_io_KubeVirt --> kubevirt_io_VirtualMachine : configures
    kubevirt_io_VirtualMachineInstanceMigration --> kubevirt_io_VirtualMachineInstanceReplicaSet : references
    kubevirt_io_VirtualMachineInstanceMigration --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstanceMigration --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstanceMigration --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstanceMigration --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachineInstanceReplicaSet : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachineInstance : flows to
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstancePreset --> kubevirt_io_VirtualMachine : flows to
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachineInstance : references
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachineInstance : owns
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachineInstance : templates
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstanceReplicaSet --> kubevirt_io_VirtualMachine : templates
    kubevirt_io_VirtualMachineInstance --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstance --> kubevirt_io_VirtualMachine : references
    kubevirt_io_VirtualMachineInstance --> kubevirt_io_VirtualMachine : owns
    kubevirt_io_VirtualMachineInstance --> kubevirt_io_VirtualMachine : templates
    kubevirt_io_VirtualMachineInstance --> kubevirt_io_VirtualMachine : flows to
```
### Detailed CRD Documentation

#### KubeVirt

**Full Name:** `kubevirts.kubevirt.io`  
**API Version:** `kubevirt.io/v1`  
**Scope:** Namespaced  
**Instances:** 1  
**Categories:** all  
**Short Names:** kv, kvs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `certificateRotateStrategy` | `object` |  | *No description* |
| `configuration` | `object` |  | holds kubevirt configurations.
same as the virt-configMap |
| `customizeComponents` | `object` |  | *No description* |
| `imagePullPolicy` | `string` |  | The ImagePullPolicy to use. |
| `imagePullSecrets` | `array<object>` |  | The imagePullSecrets to pull the container images from
De... |
| `imageRegistry` | `string` |  | The image registry to pull the container images from
Defa... |
| `imageTag` | `string` |  | The image tag to use for the continer images installed.
D... |
| `infra` | `object` |  | selectors and tolerations that should apply to KubeVirt i... |
| `monitorAccount` | `string` |  | The name of the Prometheus service account that needs rea... |
| `monitorNamespace` | `string` |  | The namespace Prometheus is deployed in
Defaults to opens... |
| `productComponent` | `string` |  | Designate the apps.kubevirt.io/component label for KubeVi... |
| `productName` | `string` |  | Designate the apps.kubevirt.io/part-of label for KubeVirt... |
| `productVersion` | `string` |  | Designate the apps.kubevirt.io/version label for KubeVirt... |
| `serviceMonitorNamespace` | `string` |  | The namespace the service monitor will be deployed
 When ... |
| `synchronizationPort` | `string` |  | Specify the port to listen on for VMI status synchronizat... |
| `uninstallStrategy` | `string` |  | Specifies if kubevirt can be deleted if workloads are sti... |
| `workloadUpdateStrategy` | `object` |  | WorkloadUpdateStrategy defines at the cluster level how t... |
| `workloads` | `object` |  | selectors and tolerations that should apply to KubeVirt w... |


#### VirtualMachine

**Full Name:** `virtualmachines.kubevirt.io`  
**API Version:** `kubevirt.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** all  
**Short Names:** vm, vms  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `template` | `object` | ✓ | Template is the direct specification of VirtualMachineIns... |
| `dataVolumeTemplates` | `array<object>` |  | dataVolumeTemplates is a list of dataVolumes that the Vir... |
| `instancetype` | `object` |  | InstancetypeMatcher references a instancetype that is use... |
| `preference` | `object` |  | PreferenceMatcher references a set of preference that is ... |
| `runStrategy` | `string` |  | Running state indicates the requested running state of th... |
| `running` | `boolean` |  | Running controls whether the associatied VirtualMachineIn... |
| `updateVolumesStrategy` | `string` |  | UpdateVolumesStrategy is the strategy to apply on volumes... |


#### VirtualMachineInstance

**Full Name:** `virtualmachineinstances.kubevirt.io`  
**API Version:** `kubevirt.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** all  
**Short Names:** vmi, vmis  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `domain` | `object` | ✓ | Specification of the desired behavior of the VirtualMachi... |
| `accessCredentials` | `array<object>` |  | Specifies a set of public keys to inject into the vm guest |
| `affinity` | `object` |  | If affinity is specifies, obey all the affinity rules |
| `architecture` | `string` |  | Specifies the architecture of the vm guest you are attemp... |
| `dnsConfig` | `object` |  | Specifies the DNS parameters of a pod.
Parameters specifi... |
| `dnsPolicy` | `string` |  | Set DNS policy for the pod.
Defaults to "ClusterFirst".
V... |
| `evictionStrategy` | `string` |  | EvictionStrategy describes the strategy to follow when a ... |
| `hostname` | `string` |  | Specifies the hostname of the vmi
If not specified, the h... |
| `livenessProbe` | `object` |  | Periodic probe of VirtualMachineInstance liveness.
Virtua... |
| `networks` | `array<object>` |  | List of networks that can be attached to a vm's virtual i... |
| `nodeSelector` | `object` |  | NodeSelector is a selector which must be true for the vmi... |
| `priorityClassName` | `string` |  | If specified, indicates the pod's priority.
If not specif... |
| `readinessProbe` | `object` |  | Periodic probe of VirtualMachineInstance service readines... |
| `resourceClaims` | `array<object>` |  | ResourceClaims define which ResourceClaims must be alloca... |
| `schedulerName` | `string` |  | If specified, the VMI will be dispatched by specified sch... |
| `startStrategy` | `string` |  | StartStrategy can be set to "Paused" if Virtual Machine s... |
| `subdomain` | `string` |  | If specified, the fully qualified vmi hostname will be "<... |
| `terminationGracePeriodSeconds` | `integer(int64)` |  | Grace period observed after signalling a VirtualMachineIn... |
| `tolerations` | `array<object>` |  | If toleration is specified, obey all the toleration rules. |
| `topologySpreadConstraints` | `array<object>` |  | TopologySpreadConstraints describes how a group of VMIs w... |

*... and 1 more properties*


#### VirtualMachineInstanceMigration

**Full Name:** `virtualmachineinstancemigrations.kubevirt.io`  
**API Version:** `kubevirt.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** all  
**Short Names:** vmim, vmims  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `addedNodeSelector` | `object` |  | AddedNodeSelector is an additional selector that can be u... |
| `receive` | `object` |  | If receieve is specified, this VirtualMachineInstanceMigr... |
| `sendTo` | `object` |  | If sendTo is specified, this VirtualMachineInstanceMigrat... |
| `vmiName` | `string` |  | The name of the VMI to perform the migration on. VMI must... |


#### VirtualMachineInstancePreset

**Full Name:** `virtualmachineinstancepresets.kubevirt.io`  
**API Version:** `kubevirt.io/v1alpha3`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** all  
**Short Names:** vmipreset, vmipresets  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `selector` | `object` | ✓ | Selector is a label query over a set of VMIs.
Required. |
| `domain` | `object` |  | Domain is the same object type as contained in VirtualMac... |


#### VirtualMachineInstanceReplicaSet

**Full Name:** `virtualmachineinstancereplicasets.kubevirt.io`  
**API Version:** `kubevirt.io/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** all  
**Short Names:** vmirs, vmirss  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `selector` | `object` | ✓ | Label selector for pods. Existing ReplicaSets whose pods ... |
| `template` | `object` | ✓ | Template describes the pods that will be created. |
| `paused` | `boolean` |  | Indicates that the replica set is paused. |
| `replicas` | `integer(int32)` |  | Number of desired pods. This is a pointer to distinguish ... |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `kubevirts.kubevirt.io` | `KubeVirt` | `kubevirt.io` | Namespaced | 1 |
| `virtualmachineinstancemigrations.kubevirt.io` | `VirtualMachineInstanceMigration` | `kubevirt.io` | Namespaced | 0 |
| `virtualmachineinstancepresets.kubevirt.io` | `VirtualMachineInstancePreset` | `kubevirt.io` | Namespaced | 0 |
| `virtualmachineinstancereplicasets.kubevirt.io` | `VirtualMachineInstanceReplicaSet` | `kubevirt.io` | Namespaced | 0 |
| `virtualmachineinstances.kubevirt.io` | `VirtualMachineInstance` | `kubevirt.io` | Namespaced | 0 |
| `virtualmachines.kubevirt.io` | `VirtualMachine` | `kubevirt.io` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 44 |
| `string` | 44 |
| `array` | 16 |
| `boolean` | 4 |
| `integer` | 4 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `KubeVirt` | `VirtualMachineInstancePreset` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachineInstanceReplicaSet` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | owns |
| `KubeVirt` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | uses |
| `KubeVirt` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `KubeVirt` | `VirtualMachine` | `kubevirt.io (intra-group)` | owns |
| `KubeVirt` | `VirtualMachine` | `kubevirt.io (intra-group)` | uses |
| `KubeVirt` | `VirtualMachine` | `kubevirt.io (intra-group)` | configures |
| `VirtualMachineInstanceMigration` | `VirtualMachineInstanceReplicaSet` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceMigration` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceMigration` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceMigration` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceMigration` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachineInstanceReplicaSet` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | flows_to |
| `VirtualMachineInstancePreset` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstancePreset` | `VirtualMachine` | `kubevirt.io (intra-group)` | flows_to |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | owns |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachineInstance` | `kubevirt.io (intra-group)` | templates |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstanceReplicaSet` | `VirtualMachine` | `kubevirt.io (intra-group)` | templates |
| `VirtualMachineInstance` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstance` | `VirtualMachine` | `kubevirt.io (intra-group)` | references |
| `VirtualMachineInstance` | `VirtualMachine` | `kubevirt.io (intra-group)` | owns |
| `VirtualMachineInstance` | `VirtualMachine` | `kubevirt.io (intra-group)` | templates |
| `VirtualMachineInstance` | `VirtualMachine` | `kubevirt.io (intra-group)` | flows_to |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*