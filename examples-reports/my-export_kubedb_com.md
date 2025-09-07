# CRD Schema Documentation - kubedb.com API Group

> **Generated:** 2025-09-07 17:05:15
> 
> **Total CRDs:** 9
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [kubedb.com](#kubedbcom) (9 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **9 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 9 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 9 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 9/9 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **kubedb.com**: 9 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `Postgres` (kubedb.com): 28 properties
2. `Postgres` (kubedb.com): 28 properties
3. `MongoDB` (kubedb.com): 27 properties


## 📁 kubedb.com

### Overview

**API Group:** `kubedb.com`  
**CRDs in Group:** 9  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `Elasticsearch` | Namespaced | v1 | 0 | *No description available* |
| `Kafka` | Namespaced | v1 | 0 | *No description available* |
| `MSSQLServer` | Namespaced | v1alpha2 | 0 | *No description available* |
| `MariaDB` | Namespaced | v1 | 0 | *No description available* |
| `MongoDB` | Namespaced | v1 | 0 | *No description available* |
| `MySQL` | Namespaced | v1 | 0 | *No description available* |
| `Postgres` | Namespaced | v1 | 0 | *No description available* |
| `Redis` | Namespaced | v1 | 0 | *No description available* |
| `RedisSentinel` | Namespaced | v1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: kubedb.com
    class kubedb_com_Elasticsearch {
        +string kind: Elasticsearch
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean disableSecurity
        +boolean enableSSL
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +integer(int32) heapSizePercentage
        +object init
        +object init.archiver
        +boolean init.initialized
        +object init.script
        +boolean init.waitForInitialRestore
    }
    kubedb_com_Elasticsearch : <<Namespaced>>
    class kubedb_com_Kafka {
        +string kind: Kafka
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object configSecret
        +string configSecret.name
        +object cruiseControl
        +object cruiseControl.brokerCapacity
        +object cruiseControl.configSecret
        +object cruiseControl.podTemplate
        +integer(int32) cruiseControl.replicas
        +object cruiseControl.resources
        +string cruiseControl.suffix
        +enum[4 values] deletionPolicy
        +boolean disableSecurity
        +boolean enableSSL
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object keystoreCredSecret
        +string(date-time) keystoreCredSecret.activeFrom
        +string keystoreCredSecret.apiGroup
        +boolean keystoreCredSecret.externallyManaged
        +string keystoreCredSecret.name
        +string keystoreCredSecret.rotateAfter
        +string keystoreCredSecret.secretStoreName
    }
    kubedb_com_Kafka : <<Namespaced>>
    class kubedb_com_MSSQLServer {
        +string kind: MSSQLServer
        +string apiVersion: kubedb.com/v1alpha2
        +string scope: Namespaced
        +object arbiter
        +object arbiter.nodeSelector
        +object arbiter.resources
        +array<object> arbiter.tolerations
        +object archiver
        +boolean archiver.pause
        +object archiver.ref
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object init
        +object init.archiver
        +boolean init.initialized
        +object init.script
        +boolean init.waitForInitialRestore
        +object monitor
        +enum[prometheus.io/operator|prometheus.io|prometheus.io/builtin] monitor.agent
        +object monitor.prometheus
    }
    kubedb_com_MSSQLServer : <<Namespaced>>
    class kubedb_com_MariaDB {
        +string kind: MariaDB
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object allowedSchemas
        +object allowedSchemas.namespaces
        +object allowedSchemas.selector
        +object archiver
        +boolean archiver.pause
        +object archiver.ref
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean distributed
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object init
        +object init.archiver
        +boolean init.initialized
        +object init.script
        +boolean init.waitForInitialRestore
    }
    kubedb_com_MariaDB : <<Namespaced>>
    class kubedb_com_MongoDB {
        +string kind: MongoDB
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object allowedSchemas
        +object allowedSchemas.namespaces
        +object allowedSchemas.selector
        +object arbiter
        +object arbiter.configSecret
        +object arbiter.podTemplate
        +object archiver
        +boolean archiver.pause
        +object archiver.ref
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +enum[4 values] clusterAuthMode
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +object ephemeralStorage
        +string ephemeralStorage.medium
        +None ephemeralStorage.sizeLimit
        +boolean halted
    }
    kubedb_com_MongoDB : <<Namespaced>>
    class kubedb_com_MySQL {
        +string kind: MySQL
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object allowedReadReplicas
        +object allowedReadReplicas.namespaces
        +object allowedReadReplicas.selector
        +object allowedSchemas
        +object allowedSchemas.namespaces
        +object allowedSchemas.selector
        +object archiver
        +boolean archiver.pause
        +object archiver.ref
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object init
        +object init.archiver
        +boolean init.initialized
        +object init.script
        +boolean init.waitForInitialRestore
    }
    kubedb_com_MySQL : <<Namespaced>>
    class kubedb_com_Postgres {
        +string kind: Postgres
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object allowedSchemas
        +object allowedSchemas.namespaces
        +object allowedSchemas.selector
        +object arbiter
        +object arbiter.nodeSelector
        +object arbiter.resources
        +array<object> arbiter.tolerations
        +object archiver
        +boolean archiver.pause
        +object archiver.ref
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +enum[md5|scram|cert] clientAuthMode
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean distributed
        +boolean enforceFsGroup
    }
    kubedb_com_Postgres : <<Namespaced>>
    class kubedb_com_Redis {
        +string kind: Redis
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object allowedSchemas
        +object allowedSchemas.namespaces
        +object allowedSchemas.selector
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +object cluster
        +object cluster.announce
        +integer(int32) cluster.replicas
        +integer(int32) cluster.shards
        +object configSecret
        +string configSecret.name
        +enum[4 values] deletionPolicy
        +boolean disableAuth
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object init
        +object init.archiver
        +boolean init.initialized
        +object init.script
        +boolean init.waitForInitialRestore
    }
    kubedb_com_Redis : <<Namespaced>>
    class kubedb_com_RedisSentinel {
        +string kind: RedisSentinel
        +string apiVersion: kubedb.com/v1
        +string scope: Namespaced
        +object authSecret
        +string(date-time) authSecret.activeFrom
        +string authSecret.apiGroup
        +boolean authSecret.externallyManaged
        +string authSecret.name
        +string authSecret.rotateAfter
        +string authSecret.secretStoreName
        +object autoOps
        +boolean autoOps.disabled
        +enum[4 values] deletionPolicy
        +boolean disableAuth
        +boolean halted
        +object healthChecker
        +boolean healthChecker.disableWriteCheck
        +integer(int32) healthChecker.failureThreshold
        +integer(int32) healthChecker.periodSeconds
        +integer(int32) healthChecker.timeoutSeconds
        +object monitor
        +enum[prometheus.io/operator|prometheus.io|prometheus.io/builtin] monitor.agent
        +object monitor.prometheus
        +object podTemplate
        +object podTemplate.controller
        +object podTemplate.metadata
        +object podTemplate.spec
        +integer(int32) replicas
        +array<object> serviceTemplates
    }
    kubedb_com_RedisSentinel : <<Namespaced>>
    kubedb_com_Elasticsearch --> kubedb_com_Kafka : references
    kubedb_com_Elasticsearch --> kubedb_com_Kafka : references
    kubedb_com_Elasticsearch --> kubedb_com_Kafka : uses
    kubedb_com_Elasticsearch --> kubedb_com_Kafka : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_MariaDB : references
    kubedb_com_Elasticsearch --> kubedb_com_MariaDB : references
    kubedb_com_Elasticsearch --> kubedb_com_MariaDB : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_MongoDB : references
    kubedb_com_Elasticsearch --> kubedb_com_MongoDB : references
    kubedb_com_Elasticsearch --> kubedb_com_MongoDB : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_MSSQLServer : references
    kubedb_com_Elasticsearch --> kubedb_com_MSSQLServer : references
    kubedb_com_Elasticsearch --> kubedb_com_MSSQLServer : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_MySQL : references
    kubedb_com_Elasticsearch --> kubedb_com_MySQL : references
    kubedb_com_Elasticsearch --> kubedb_com_MySQL : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_Postgres : references
    kubedb_com_Elasticsearch --> kubedb_com_Postgres : references
    kubedb_com_Elasticsearch --> kubedb_com_Postgres : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_Redis : references
    kubedb_com_Elasticsearch --> kubedb_com_Redis : references
    kubedb_com_Elasticsearch --> kubedb_com_Redis : uses
    kubedb_com_Elasticsearch --> kubedb_com_Redis : similar schema
    kubedb_com_Elasticsearch --> kubedb_com_RedisSentinel : references
    kubedb_com_Elasticsearch --> kubedb_com_RedisSentinel : references
    kubedb_com_Elasticsearch --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_Kafka --> kubedb_com_MariaDB : references
    kubedb_com_Kafka --> kubedb_com_MariaDB : references
    kubedb_com_Kafka --> kubedb_com_MariaDB : uses
    kubedb_com_Kafka --> kubedb_com_MariaDB : similar schema
    kubedb_com_Kafka --> kubedb_com_MongoDB : references
    kubedb_com_Kafka --> kubedb_com_MongoDB : references
    kubedb_com_Kafka --> kubedb_com_MongoDB : uses
    kubedb_com_Kafka --> kubedb_com_MongoDB : similar schema
    kubedb_com_Kafka --> kubedb_com_MSSQLServer : references
    kubedb_com_Kafka --> kubedb_com_MSSQLServer : references
    kubedb_com_Kafka --> kubedb_com_MSSQLServer : uses
    kubedb_com_Kafka --> kubedb_com_MSSQLServer : similar schema
    kubedb_com_Kafka --> kubedb_com_MySQL : references
    kubedb_com_Kafka --> kubedb_com_MySQL : references
    kubedb_com_Kafka --> kubedb_com_MySQL : uses
    kubedb_com_Kafka --> kubedb_com_MySQL : similar schema
    kubedb_com_Kafka --> kubedb_com_Postgres : references
    kubedb_com_Kafka --> kubedb_com_Postgres : references
    kubedb_com_Kafka --> kubedb_com_Postgres : uses
    kubedb_com_Kafka --> kubedb_com_Postgres : similar schema
    kubedb_com_Kafka --> kubedb_com_Redis : references
    kubedb_com_Kafka --> kubedb_com_Redis : references
    kubedb_com_Kafka --> kubedb_com_Redis : uses
    kubedb_com_Kafka --> kubedb_com_Redis : similar schema
    kubedb_com_Kafka --> kubedb_com_RedisSentinel : references
    kubedb_com_Kafka --> kubedb_com_RedisSentinel : references
    kubedb_com_Kafka --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_MariaDB --> kubedb_com_MongoDB : references
    kubedb_com_MariaDB --> kubedb_com_MongoDB : references
    kubedb_com_MariaDB --> kubedb_com_MongoDB : similar schema
    kubedb_com_MariaDB --> kubedb_com_MSSQLServer : references
    kubedb_com_MariaDB --> kubedb_com_MSSQLServer : references
    kubedb_com_MariaDB --> kubedb_com_MSSQLServer : similar schema
    kubedb_com_MariaDB --> kubedb_com_MySQL : references
    kubedb_com_MariaDB --> kubedb_com_MySQL : references
    kubedb_com_MariaDB --> kubedb_com_MySQL : similar schema
    kubedb_com_MariaDB --> kubedb_com_Postgres : references
    kubedb_com_MariaDB --> kubedb_com_Postgres : references
    kubedb_com_MariaDB --> kubedb_com_Postgres : similar schema
    kubedb_com_MariaDB --> kubedb_com_Redis : references
    kubedb_com_MariaDB --> kubedb_com_Redis : references
    kubedb_com_MariaDB --> kubedb_com_Redis : uses
    kubedb_com_MariaDB --> kubedb_com_Redis : similar schema
    kubedb_com_MariaDB --> kubedb_com_RedisSentinel : references
    kubedb_com_MariaDB --> kubedb_com_RedisSentinel : references
    kubedb_com_MariaDB --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_MongoDB --> kubedb_com_MSSQLServer : references
    kubedb_com_MongoDB --> kubedb_com_MSSQLServer : references
    kubedb_com_MongoDB --> kubedb_com_MSSQLServer : similar schema
    kubedb_com_MongoDB --> kubedb_com_MySQL : references
    kubedb_com_MongoDB --> kubedb_com_MySQL : references
    kubedb_com_MongoDB --> kubedb_com_MySQL : similar schema
    kubedb_com_MongoDB --> kubedb_com_Postgres : references
    kubedb_com_MongoDB --> kubedb_com_Postgres : references
    kubedb_com_MongoDB --> kubedb_com_Postgres : similar schema
    kubedb_com_MongoDB --> kubedb_com_Redis : references
    kubedb_com_MongoDB --> kubedb_com_Redis : references
    kubedb_com_MongoDB --> kubedb_com_Redis : uses
    kubedb_com_MongoDB --> kubedb_com_Redis : similar schema
    kubedb_com_MongoDB --> kubedb_com_RedisSentinel : references
    kubedb_com_MongoDB --> kubedb_com_RedisSentinel : references
    kubedb_com_MongoDB --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_MSSQLServer --> kubedb_com_MySQL : references
    kubedb_com_MSSQLServer --> kubedb_com_MySQL : references
    kubedb_com_MSSQLServer --> kubedb_com_MySQL : similar schema
    kubedb_com_MSSQLServer --> kubedb_com_Postgres : references
    kubedb_com_MSSQLServer --> kubedb_com_Postgres : references
    kubedb_com_MSSQLServer --> kubedb_com_Postgres : similar schema
    kubedb_com_MSSQLServer --> kubedb_com_Redis : references
    kubedb_com_MSSQLServer --> kubedb_com_Redis : references
    kubedb_com_MSSQLServer --> kubedb_com_Redis : uses
    kubedb_com_MSSQLServer --> kubedb_com_Redis : similar schema
    kubedb_com_MSSQLServer --> kubedb_com_RedisSentinel : references
    kubedb_com_MSSQLServer --> kubedb_com_RedisSentinel : references
    kubedb_com_MSSQLServer --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_MySQL --> kubedb_com_Postgres : references
    kubedb_com_MySQL --> kubedb_com_Postgres : references
    kubedb_com_MySQL --> kubedb_com_Postgres : similar schema
    kubedb_com_MySQL --> kubedb_com_Redis : references
    kubedb_com_MySQL --> kubedb_com_Redis : references
    kubedb_com_MySQL --> kubedb_com_Redis : uses
    kubedb_com_MySQL --> kubedb_com_Redis : similar schema
    kubedb_com_MySQL --> kubedb_com_RedisSentinel : references
    kubedb_com_MySQL --> kubedb_com_RedisSentinel : references
    kubedb_com_MySQL --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_Postgres --> kubedb_com_Redis : references
    kubedb_com_Postgres --> kubedb_com_Redis : references
    kubedb_com_Postgres --> kubedb_com_Redis : uses
    kubedb_com_Postgres --> kubedb_com_Redis : similar schema
    kubedb_com_Postgres --> kubedb_com_RedisSentinel : references
    kubedb_com_Postgres --> kubedb_com_RedisSentinel : references
    kubedb_com_Postgres --> kubedb_com_RedisSentinel : similar schema
    kubedb_com_Redis --> kubedb_com_RedisSentinel : references
    kubedb_com_Redis --> kubedb_com_RedisSentinel : references
    kubedb_com_Redis --> kubedb_com_RedisSentinel : uses
    kubedb_com_Redis --> kubedb_com_RedisSentinel : similar schema
```
### Detailed CRD Documentation

#### Elasticsearch

**Full Name:** `elasticsearches.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** es  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `disableSecurity` | `boolean` |  | *No description* |
| `enableSSL` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `heapSizePercentage` | `integer(int32)` |  | *No description* |
| `init` | `object` |  | *No description* |
| `internalUsers` | `object` |  | *No description* |
| `kernelSettings` | `object` |  | *No description* |
| `maxUnavailable` | `None` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `rolesMapping` | `object` |  | *No description* |
| `secureConfigSecret` | `object` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |

*... and 4 more properties*


#### Kafka

**Full Name:** `kafkas.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** kf  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `cruiseControl` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `disableSecurity` | `boolean` |  | *No description* |
| `enableSSL` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `keystoreCredSecret` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `topology` | `object` |  | *No description* |


#### MSSQLServer

**Full Name:** `mssqlservers.kubedb.com`  
**API Version:** `kubedb.com/v1alpha2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** ms  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `arbiter` | `object` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `topology` | `object` |  | *No description* |


#### MariaDB

**Full Name:** `mariadbs.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** md  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `allowedSchemas` | `object` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `distributed` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `requireSSL` | `boolean` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `topology` | `object` |  | *No description* |

*... and 1 more properties*


#### MongoDB

**Full Name:** `mongodbs.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** mg  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `allowedSchemas` | `object` |  | *No description* |
| `arbiter` | `object` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `clusterAuthMode` | `enum[4 values]` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `ephemeralStorage` | `object` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `hidden` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `keyFileSecret` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicaSet` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |

*... and 6 more properties*


#### MySQL

**Full Name:** `mysqls.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** my  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `allowedReadReplicas` | `object` |  | *No description* |
| `allowedSchemas` | `object` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `requireSSL` | `boolean` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `topology` | `object` |  | *No description* |

*... and 1 more properties*


#### Postgres

**Full Name:** `postgreses.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** pg  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `allowedSchemas` | `object` |  | *No description* |
| `arbiter` | `object` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `clientAuthMode` | `enum[md5|scram|cert]` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `distributed` | `boolean` |  | *No description* |
| `enforceFsGroup` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `leaderElection` | `object` |  | *No description* |
| `mode` | `string` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `remoteReplica` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |

*... and 8 more properties*


#### Redis

**Full Name:** `redises.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** rd  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `allowedSchemas` | `object` |  | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `cluster` | `object` |  | *No description* |
| `configSecret` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `disableAuth` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `init` | `object` |  | *No description* |
| `mode` | `enum[Standalone|Cluster|Sentinel]` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `sentinelRef` | `object` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |


#### RedisSentinel

**Full Name:** `redissentinels.kubedb.com`  
**API Version:** `kubedb.com/v1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** datastore, kubedb, appscode, all  
**Short Names:** rds  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | ✓ | *No description* |
| `authSecret` | `object` |  | *No description* |
| `autoOps` | `object` |  | *No description* |
| `deletionPolicy` | `enum[4 values]` |  | *No description* |
| `disableAuth` | `boolean` |  | *No description* |
| `halted` | `boolean` |  | *No description* |
| `healthChecker` | `object` |  | *No description* |
| `monitor` | `object` |  | *No description* |
| `podTemplate` | `object` |  | *No description* |
| `replicas` | `integer(int32)` |  | *No description* |
| `serviceTemplates` | `array<object>` |  | *No description* |
| `storage` | `object` |  | *No description* |
| `storageType` | `enum[Durable|Ephemeral]` |  | *No description* |
| `tls` | `object` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `elasticsearches.kubedb.com` | `Elasticsearch` | `kubedb.com` | Namespaced | 0 |
| `kafkas.kubedb.com` | `Kafka` | `kubedb.com` | Namespaced | 0 |
| `mariadbs.kubedb.com` | `MariaDB` | `kubedb.com` | Namespaced | 0 |
| `mongodbs.kubedb.com` | `MongoDB` | `kubedb.com` | Namespaced | 0 |
| `mssqlservers.kubedb.com` | `MSSQLServer` | `kubedb.com` | Namespaced | 0 |
| `mysqls.kubedb.com` | `MySQL` | `kubedb.com` | Namespaced | 0 |
| `postgreses.kubedb.com` | `Postgres` | `kubedb.com` | Namespaced | 0 |
| `redises.kubedb.com` | `Redis` | `kubedb.com` | Namespaced | 0 |
| `redissentinels.kubedb.com` | `RedisSentinel` | `kubedb.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 218 |
| `string` | 73 |
| `boolean` | 37 |
| `integer` | 19 |
| `array` | 17 |
| `None` | 2 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `Elasticsearch` | `Kafka` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Kafka` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Kafka` | `kubedb.com (intra-group)` | uses |
| `Elasticsearch` | `Kafka` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `MariaDB` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MariaDB` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MariaDB` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MongoDB` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MSSQLServer` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `MySQL` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MySQL` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `MySQL` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `Postgres` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Postgres` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `Redis` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Redis` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `Redis` | `kubedb.com (intra-group)` | uses |
| `Elasticsearch` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `Elasticsearch` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Elasticsearch` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `MariaDB` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MariaDB` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MariaDB` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `MariaDB` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MongoDB` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `MongoDB` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MSSQLServer` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `MSSQLServer` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `MySQL` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MySQL` | `kubedb.com (intra-group)` | references |
| `Kafka` | `MySQL` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `MySQL` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `Postgres` | `kubedb.com (intra-group)` | references |
| `Kafka` | `Postgres` | `kubedb.com (intra-group)` | references |
| `Kafka` | `Postgres` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `Redis` | `kubedb.com (intra-group)` | references |
| `Kafka` | `Redis` | `kubedb.com (intra-group)` | references |
| `Kafka` | `Redis` | `kubedb.com (intra-group)` | uses |
| `Kafka` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `Kafka` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Kafka` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Kafka` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MongoDB` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MongoDB` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MSSQLServer` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `MySQL` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `Redis` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `Redis` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `Redis` | `kubedb.com (intra-group)` | uses |
| `MariaDB` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `MariaDB` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MariaDB` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `MongoDB` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `MSSQLServer` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `MSSQLServer` | `kubedb.com (intra-group)` | similar_schema |
| `MongoDB` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `MySQL` | `kubedb.com (intra-group)` | similar_schema |
| `MongoDB` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `MongoDB` | `Redis` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `Redis` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `Redis` | `kubedb.com (intra-group)` | uses |
| `MongoDB` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `MongoDB` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MongoDB` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `MSSQLServer` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `MySQL` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `MySQL` | `kubedb.com (intra-group)` | similar_schema |
| `MSSQLServer` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `MSSQLServer` | `Redis` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `Redis` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `Redis` | `kubedb.com (intra-group)` | uses |
| `MSSQLServer` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `MSSQLServer` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MSSQLServer` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `MySQL` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MySQL` | `Postgres` | `kubedb.com (intra-group)` | references |
| `MySQL` | `Postgres` | `kubedb.com (intra-group)` | similar_schema |
| `MySQL` | `Redis` | `kubedb.com (intra-group)` | references |
| `MySQL` | `Redis` | `kubedb.com (intra-group)` | references |
| `MySQL` | `Redis` | `kubedb.com (intra-group)` | uses |
| `MySQL` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `MySQL` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MySQL` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `MySQL` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `Postgres` | `Redis` | `kubedb.com (intra-group)` | references |
| `Postgres` | `Redis` | `kubedb.com (intra-group)` | references |
| `Postgres` | `Redis` | `kubedb.com (intra-group)` | uses |
| `Postgres` | `Redis` | `kubedb.com (intra-group)` | similar_schema |
| `Postgres` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Postgres` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Postgres` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |
| `Redis` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Redis` | `RedisSentinel` | `kubedb.com (intra-group)` | references |
| `Redis` | `RedisSentinel` | `kubedb.com (intra-group)` | uses |
| `Redis` | `RedisSentinel` | `kubedb.com (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*