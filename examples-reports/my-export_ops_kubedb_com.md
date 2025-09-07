# CRD Schema Documentation - ops.kubedb.com API Group

> **Generated:** 2025-09-07 17:05:16
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
   - [ops.kubedb.com](#opskubedbcom) (9 CRDs)
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

1. **ops.kubedb.com**: 9 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `MongoDBOpsRequest` (ops.kubedb.com): 16 properties
2. `PostgresOpsRequest` (ops.kubedb.com): 15 properties
3. `RedisOpsRequest` (ops.kubedb.com): 14 properties


## 📁 ops.kubedb.com

### Overview

**API Group:** `ops.kubedb.com`  
**CRDs in Group:** 9  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `ElasticsearchOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `KafkaOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MSSQLServerOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MariaDBOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MongoDBOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MySQLOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `PostgresOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `RedisOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |
| `RedisSentinelOpsRequest` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: ops.kubedb.com
    class ops_kubedb_com_ElasticsearchOpsRequest {
        +string kind: ElasticsearchOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +boolean configuration.removeSecureCustomConfig
        +object configuration.secureConfigSecret
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +integer(int32) horizontalScaling.node
        +object horizontalScaling.topology
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.rotateCertificates
        +enum[9 values] type
        +object updateVersion
        +string updateVersion.targetVersion
    }
    ops_kubedb_com_ElasticsearchOpsRequest : <<Namespaced>>
    class ops_kubedb_com_KafkaOpsRequest {
        +string kind: KafkaOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +integer(int32) horizontalScaling.node
        +object horizontalScaling.topology
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.rotateCertificates
        +enum[8 values] type
        +object updateVersion
        +string updateVersion.targetVersion
    }
    ops_kubedb_com_KafkaOpsRequest : <<Namespaced>>
    class ops_kubedb_com_MSSQLServerOpsRequest {
        +string kind: MSSQLServerOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +integer(int32) horizontalScaling.replicas
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +boolean tls.clientTLS
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.rotateCertificates
        +enum[8 values] type
        +object updateVersion
        +string updateVersion.targetVersion
    }
    ops_kubedb_com_MSSQLServerOpsRequest : <<Namespaced>>
    class ops_kubedb_com_MariaDBOpsRequest {
        +string kind: MariaDBOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +boolean horizontalScaling.maxscale
        +integer(int32) horizontalScaling.member
        +integer(int32) horizontalScaling.memberWeight
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.requireSSL
        +boolean tls.rotateCertificates
        +enum[9 values] type
        +object updateVersion
        +string updateVersion.targetVersion
    }
    ops_kubedb_com_MariaDBOpsRequest : <<Namespaced>>
    class ops_kubedb_com_MongoDBOpsRequest {
        +string kind: MongoDBOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object archiver
        +enum[ConfigureArchiver|DisableArchiver] archiver.operation
        +object archiver.ref
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.arbiter
        +object configuration.configServer
        +object configuration.hidden
        +object configuration.mongos
        +object configuration.replicaSet
        +object configuration.shard
        +object configuration.standalone
        +object databaseRef
        +string databaseRef.name
        +object horizons
        +string horizons.dns
        +array<string> horizons.pods
        +object horizontalScaling
        +object horizontalScaling.configServer
        +object horizontalScaling.hidden
        +object horizontalScaling.mongos
        +integer(int32) horizontalScaling.replicas
        +object horizontalScaling.shard
        +object readinessCriteria
        +integer(int32) readinessCriteria.objectsCountDiffPercentage
        +integer(int32) readinessCriteria.oplogMaxLagSeconds
        +object reprovision
        +object restart
    }
    ops_kubedb_com_MongoDBOpsRequest : <<Namespaced>>
    class ops_kubedb_com_MySQLOpsRequest {
        +string kind: MySQLOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +integer(int32) horizontalScaling.member
        +object replicationModeTransformation
        +array<object> replicationModeTransformation.certificates
        +object replicationModeTransformation.issuerRef
        +enum[Single-Primary|Multi-Primary] replicationModeTransformation.mode
        +boolean replicationModeTransformation.requireSSL
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.requireSSL
        +boolean tls.rotateCertificates
        +enum[10 values] type
    }
    ops_kubedb_com_MySQLOpsRequest : <<Namespaced>>
    class ops_kubedb_com_PostgresOpsRequest {
        +string kind: PostgresOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object forceFailOver
        +array<string> forceFailOver.candidates
        +object horizontalScaling
        +integer(int32) horizontalScaling.replicas
        +enum[Hot|Warm] horizontalScaling.standbyMode
        +enum[Synchronous|Asynchronous] horizontalScaling.streamingMode
        +object reconnectStandby
        +string reconnectStandby.readyTimeOut
        +object restart
        +object setRaftKeyPair
        +object setRaftKeyPair.keyPair
        +string timeout
    }
    ops_kubedb_com_PostgresOpsRequest : <<Namespaced>>
    class ops_kubedb_com_RedisOpsRequest {
        +string kind: RedisOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +object announce
        +array<object> announce.shards
        +enum[ip|hostname] announce.type
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +object horizontalScaling.announce
        +integer(int32) horizontalScaling.replicas
        +integer(int32) horizontalScaling.shards
        +object restart
        +object sentinel
        +object sentinel.ref
        +boolean sentinel.removeUnusedSentinel
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.rotateCertificates
        +object tls.sentinel
    }
    ops_kubedb_com_RedisOpsRequest : <<Namespaced>>
    class ops_kubedb_com_RedisSentinelOpsRequest {
        +string kind: RedisSentinelOpsRequest
        +string apiVersion: ops.kubedb.com/v1alpha1
        +string scope: Namespaced
        +enum[IfReady|Always] apply
        +object authentication
        +object authentication.secretRef
        +object configuration
        +object configuration.applyConfig
        +object configuration.configSecret
        +boolean configuration.removeCustomConfig
        +object databaseRef
        +string databaseRef.name
        +object horizontalScaling
        +integer(int32) horizontalScaling.replicas
        +object restart
        +string timeout
        +object tls
        +array<object> tls.certificates
        +object tls.issuerRef
        +boolean tls.remove
        +boolean tls.rotateCertificates
        +enum[7 values] type
        +object updateVersion
        +object updateVersion.readinessCriteria
        +string updateVersion.targetVersion
    }
    ops_kubedb_com_RedisSentinelOpsRequest : <<Namespaced>>
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_KafkaOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_KafkaOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_KafkaOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_MySQLOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_ElasticsearchOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MariaDBOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_MySQLOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_KafkaOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MongoDBOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MariaDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MSSQLServerOpsRequest : similar schema
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_MySQLOpsRequest : similar schema
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MongoDBOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_MySQLOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_MySQLOpsRequest : similar schema
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MSSQLServerOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_PostgresOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_PostgresOpsRequest : similar schema
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_MySQLOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisOpsRequest : references
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisOpsRequest : similar schema
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_PostgresOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
    ops_kubedb_com_RedisOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_RedisOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : references
    ops_kubedb_com_RedisOpsRequest --> ops_kubedb_com_RedisSentinelOpsRequest : similar schema
```
### Detailed CRD Documentation

#### ElasticsearchOpsRequest

**Full Name:** `elasticsearchopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** esops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[9 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### KafkaOpsRequest

**Full Name:** `kafkaopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** kfops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[8 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### MSSQLServerOpsRequest

**Full Name:** `mssqlserveropsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** msops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[8 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### MariaDBOpsRequest

**Full Name:** `mariadbopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** mariaops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[9 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### MongoDBOpsRequest

**Full Name:** `mongodbopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** mgops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[11 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `archiver` | `object` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizons` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `readinessCriteria` | `object` |  | *No description* |
| `reprovision` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### MySQLOpsRequest

**Full Name:** `mysqlopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** myops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[10 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `replicationModeTransformation` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### PostgresOpsRequest

**Full Name:** `postgresopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** pgops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[12 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `forceFailOver` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `reconnectStandby` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `setRaftKeyPair` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### RedisOpsRequest

**Full Name:** `redisopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** rdops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[10 values]` | ✓ | *No description* |
| `announce` | `object` |  | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `sentinel` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |
| `volumeExpansion` | `object` |  | *No description* |


#### RedisSentinelOpsRequest

**Full Name:** `redissentinelopsrequests.ops.kubedb.com`  
**API Version:** `ops.kubedb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** ops, kubedb, appscode  
**Short Names:** rdsops  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `databaseRef` | `object` | ✓ | *No description* |
| `type` | `enum[7 values]` | ✓ | *No description* |
| `apply` | `enum[IfReady|Always]` |  | *No description* |
| `authentication` | `object` |  | *No description* |
| `configuration` | `object` |  | *No description* |
| `horizontalScaling` | `object` |  | *No description* |
| `restart` | `object` |  | *No description* |
| `timeout` | `string` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `updateVersion` | `object` |  | *No description* |
| `verticalScaling` | `object` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `elasticsearchopsrequests.ops.kubedb.com` | `ElasticsearchOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `kafkaopsrequests.ops.kubedb.com` | `KafkaOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `mariadbopsrequests.ops.kubedb.com` | `MariaDBOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `mongodbopsrequests.ops.kubedb.com` | `MongoDBOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `mssqlserveropsrequests.ops.kubedb.com` | `MSSQLServerOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `mysqlopsrequests.ops.kubedb.com` | `MySQLOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `postgresopsrequests.ops.kubedb.com` | `PostgresOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `redisopsrequests.ops.kubedb.com` | `RedisOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |
| `redissentinelopsrequests.ops.kubedb.com` | `RedisSentinelOpsRequest` | `ops.kubedb.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 90 |
| `string` | 27 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `ElasticsearchOpsRequest` | `KafkaOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `KafkaOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `KafkaOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `ElasticsearchOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MariaDBOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `KafkaOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `KafkaOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MongoDBOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MariaDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MariaDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MongoDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `MSSQLServerOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MongoDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MongoDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MongoDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MongoDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MongoDBOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `MySQLOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MSSQLServerOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MySQLOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `PostgresOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MySQLOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `MySQLOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `MySQLOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `PostgresOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `PostgresOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `PostgresOpsRequest` | `RedisOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `PostgresOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `PostgresOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `PostgresOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |
| `RedisOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `RedisOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | references |
| `RedisOpsRequest` | `RedisSentinelOpsRequest` | `ops.kubedb.com (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:16*