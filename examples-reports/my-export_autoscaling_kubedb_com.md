# CRD Schema Documentation - autoscaling.kubedb.com API Group

> **Generated:** 2025-09-07 17:05:14
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
   - [autoscaling.kubedb.com](#autoscalingkubedbcom) (9 CRDs)
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

1. **autoscaling.kubedb.com**: 9 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `ElasticsearchAutoscaler` (autoscaling.kubedb.com): 4 properties
2. `KafkaAutoscaler` (autoscaling.kubedb.com): 4 properties
3. `MariaDBAutoscaler` (autoscaling.kubedb.com): 4 properties


## 📁 autoscaling.kubedb.com

### Overview

**API Group:** `autoscaling.kubedb.com`  
**CRDs in Group:** 9  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `ElasticsearchAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `KafkaAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MSSQLServerAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MariaDBAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MongoDBAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MySQLAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `PostgresAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `RedisAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |
| `RedisSentinelAutoscaler` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: autoscaling.kubedb.com
    class autoscaling_kubedb_com_ElasticsearchAutoscaler {
        +string kind: ElasticsearchAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.coordinating
        +object compute.data
        +object compute.dataCold
        +object compute.dataContent
        +object compute.dataFrozen
        +object compute.dataHot
        +object compute.dataWarm
        +object compute.ingest
        +object compute.master
        +object compute.ml
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +object opsRequestOptions.readinessCriteria
        +string opsRequestOptions.timeout
        +object storage
        +object storage.coordinating
        +object storage.data
        +object storage.dataCold
        +object storage.dataContent
        +object storage.dataFrozen
        +object storage.dataHot
        +object storage.dataWarm
        +object storage.ingest
        +object storage.master
        +object storage.ml
    }
    autoscaling_kubedb_com_ElasticsearchAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_KafkaAutoscaler {
        +string kind: KafkaAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.broker
        +object compute.controller
        +object compute.node
        +object compute.nodeTopology
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +string opsRequestOptions.timeout
        +object storage
        +object storage.broker
        +object storage.controller
        +object storage.node
    }
    autoscaling_kubedb_com_KafkaAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_MSSQLServerAutoscaler {
        +string kind: MSSQLServerAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.mssqlserver
        +object compute.nodeTopology
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +string opsRequestOptions.timeout
        +object storage
        +object storage.mssqlserver
    }
    autoscaling_kubedb_com_MSSQLServerAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_MariaDBAutoscaler {
        +string kind: MariaDBAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.mariadb
        +object compute.nodeTopology
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +object opsRequestOptions.readinessCriteria
        +string opsRequestOptions.timeout
        +object storage
        +object storage.mariadb
    }
    autoscaling_kubedb_com_MariaDBAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_MongoDBAutoscaler {
        +string kind: MongoDBAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.arbiter
        +object compute.configServer
        +object compute.hidden
        +object compute.mongos
        +object compute.nodeTopology
        +object compute.replicaSet
        +object compute.shard
        +object compute.standalone
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +object opsRequestOptions.readinessCriteria
        +string opsRequestOptions.timeout
        +object storage
        +object storage.configServer
        +object storage.hidden
        +object storage.replicaSet
        +object storage.shard
        +object storage.standalone
    }
    autoscaling_kubedb_com_MongoDBAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_MySQLAutoscaler {
        +string kind: MySQLAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.mysql
        +object compute.nodeTopology
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +object opsRequestOptions.readinessCriteria
        +string opsRequestOptions.timeout
        +object storage
        +object storage.mysql
    }
    autoscaling_kubedb_com_MySQLAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_PostgresAutoscaler {
        +string kind: PostgresAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.nodeTopology
        +object compute.postgres
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +string opsRequestOptions.timeout
        +object storage
        +object storage.postgres
    }
    autoscaling_kubedb_com_PostgresAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_RedisAutoscaler {
        +string kind: RedisAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.cluster
        +object compute.nodeTopology
        +object compute.sentinel
        +object compute.standalone
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +string opsRequestOptions.timeout
        +object storage
        +object storage.cluster
        +object storage.sentinel
        +object storage.standalone
    }
    autoscaling_kubedb_com_RedisAutoscaler : <<Namespaced>>
    class autoscaling_kubedb_com_RedisSentinelAutoscaler {
        +string kind: RedisSentinelAutoscaler
        +string apiVersion: autoscaling.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object compute
        +object compute.nodeTopology
        +object compute.sentinel
        +object databaseRef
        +string databaseRef.name
        +object opsRequestOptions
        +enum[IfReady|Always] opsRequestOptions.apply
        +string opsRequestOptions.timeout
    }
    autoscaling_kubedb_com_RedisSentinelAutoscaler : <<Namespaced>>
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_KafkaAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_KafkaAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_KafkaAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_ElasticsearchAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MariaDBAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_KafkaAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MongoDBAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MariaDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MSSQLServerAutoscaler : similar schema
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : similar schema
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MongoDBAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_MySQLAutoscaler : similar schema
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MSSQLServerAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_PostgresAutoscaler : similar schema
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_MySQLAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : references
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisAutoscaler : similar schema
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_PostgresAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
    autoscaling_kubedb_com_RedisAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_RedisAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : references
    autoscaling_kubedb_com_RedisAutoscaler --> autoscaling_kubedb_com_RedisSentinelAutoscaler : similar schema
```
### Detailed CRD Documentation

#### ElasticsearchAutoscaler

**Full Name:** `elasticsearchautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** esscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### KafkaAutoscaler

**Full Name:** `kafkaautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** kfscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### MSSQLServerAutoscaler

**Full Name:** `mssqlserverautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** msscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### MariaDBAutoscaler

**Full Name:** `mariadbautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** mdscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### MongoDBAutoscaler

**Full Name:** `mongodbautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** mgscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### MySQLAutoscaler

**Full Name:** `mysqlautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** myscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### PostgresAutoscaler

**Full Name:** `postgresautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** pgscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### RedisAutoscaler

**Full Name:** `redisautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** rdscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |
| `storage` | `object` |  | *No description* |


#### RedisSentinelAutoscaler

**Full Name:** `redissentinelautoscalers.autoscaling.kubedb.com`  
**API Version:** `autoscaling.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** autoscaler, kubedb, appscode  
**Short Names:** rdsscaler  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `compute` | `object` |  | *No description* |
| `opsRequestOptions` | `object` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `elasticsearchautoscalers.autoscaling.kubedb.com` | `ElasticsearchAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `kafkaautoscalers.autoscaling.kubedb.com` | `KafkaAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `mariadbautoscalers.autoscaling.kubedb.com` | `MariaDBAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `mongodbautoscalers.autoscaling.kubedb.com` | `MongoDBAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `mssqlserverautoscalers.autoscaling.kubedb.com` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `mysqlautoscalers.autoscaling.kubedb.com` | `MySQLAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `postgresautoscalers.autoscaling.kubedb.com` | `PostgresAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `redisautoscalers.autoscaling.kubedb.com` | `RedisAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |
| `redissentinelautoscalers.autoscaling.kubedb.com` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 35 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `ElasticsearchAutoscaler` | `KafkaAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `KafkaAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `KafkaAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `ElasticsearchAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MariaDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `KafkaAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `KafkaAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MongoDBAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MariaDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MariaDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MongoDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `MSSQLServerAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MongoDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MongoDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MongoDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MongoDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MongoDBAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `MySQLAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MSSQLServerAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MySQLAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `PostgresAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MySQLAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `MySQLAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `MySQLAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `PostgresAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `PostgresAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `PostgresAutoscaler` | `RedisAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `PostgresAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `PostgresAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `PostgresAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |
| `RedisAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `RedisAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | references |
| `RedisAutoscaler` | `RedisSentinelAutoscaler` | `autoscaling.kubedb.com (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:14*