# CRD Schema Documentation - catalog.kubedb.com API Group

> **Generated:** 2025-09-07 17:05:14
> 
> **Total CRDs:** 27
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [catalog.kubedb.com](#catalogkubedbcom) (27 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **27 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 27 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 0 (0.0%) |
| **Cluster-scoped CRDs** | 27 (100.0%) |
| **Schema Coverage** | 27/27 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **catalog.kubedb.com**: 27 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `MySQLVersion` (catalog.kubedb.com): 17 properties
2. `ElasticsearchVersion` (catalog.kubedb.com): 15 properties
3. `PostgresVersion` (catalog.kubedb.com): 15 properties


## 📁 catalog.kubedb.com

### Overview

**API Group:** `catalog.kubedb.com`  
**CRDs in Group:** 27  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `CassandraVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `ClickHouseVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `DruidVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `ElasticsearchVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `EtcdVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `FerretDBVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `HazelcastVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `IgniteVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `KafkaConnectorVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `KafkaVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `MSSQLServerVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `MariaDBVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `MemcachedVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `MongoDBVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `MySQLVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `OracleVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `PerconaXtraDBVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `PgBouncerVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `PgpoolVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `PostgresVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `ProxySQLVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `RabbitMQVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `RedisVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `SchemaRegistryVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `SinglestoreVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `SolrVersion` | Cluster | v1alpha1 | 0 | *No description available* |
| `ZooKeeperVersion` | Cluster | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: catalog.kubedb.com
    class catalog_kubedb_com_CassandraVersion {
        +string kind: CassandraVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +object exporter
        +string exporter.image
        +object initContainer
        +string initContainer.image
        +object medusa
        +string medusa.image
        +object medusa.init
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_CassandraVersion : <<Cluster>>
    class catalog_kubedb_com_ClickHouseVersion {
        +string kind: ClickHouseVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object clickHouseKeeper
        +string clickHouseKeeper.image
        +object db
        +string db.image
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_ClickHouseVersion : <<Cluster>>
    class catalog_kubedb_com_DruidVersion {
        +string kind: DruidVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_DruidVersion : <<Cluster>>
    class catalog_kubedb_com_ElasticsearchVersion {
        +string kind: ElasticsearchVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +enum[4 values] authPlugin
        +object dashboard
        +string dashboard.image
        +object dashboardInitContainer
        +string dashboardInitContainer.yqImage
        +object db
        +string db.image
        +boolean deprecated
        +enum[5 values] distribution
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +string initContainer.yqImage
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
    }
    catalog_kubedb_com_ElasticsearchVersion : <<Cluster>>
    class catalog_kubedb_com_EtcdVersion {
        +string kind: EtcdVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
        +string version
    }
    catalog_kubedb_com_EtcdVersion : <<Cluster>>
    class catalog_kubedb_com_FerretDBVersion {
        +string kind: FerretDBVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object postgres
        +string postgres.version
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_FerretDBVersion : <<Cluster>>
    class catalog_kubedb_com_HazelcastVersion {
        +string kind: HazelcastVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_HazelcastVersion : <<Cluster>>
    class catalog_kubedb_com_IgniteVersion {
        +string kind: IgniteVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsGroup
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_IgniteVersion : <<Cluster>>
    class catalog_kubedb_com_KafkaConnectorVersion {
        +string kind: KafkaConnectorVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object connectorPlugin
        +string connectorPlugin.image
        +boolean deprecated
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +string type
        +string version
    }
    catalog_kubedb_com_KafkaConnectorVersion : <<Cluster>>
    class catalog_kubedb_com_KafkaVersion {
        +string kind: KafkaVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object connectCluster
        +string connectCluster.image
        +object cruiseControl
        +string cruiseControl.image
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
    }
    catalog_kubedb_com_KafkaVersion : <<Cluster>>
    class catalog_kubedb_com_MSSQLServerVersion {
        +string kind: MSSQLServerVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object archiver
        +object archiver.addon
        +object archiver.walg
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
    }
    catalog_kubedb_com_MSSQLServerVersion : <<Cluster>>
    class catalog_kubedb_com_MariaDBVersion {
        +string kind: MariaDBVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object archiver
        +object archiver.addon
        +object archiver.walg
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object maxscale
        +string maxscale.image
        +object maxscale.securityContext
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
    }
    catalog_kubedb_com_MariaDBVersion : <<Cluster>>
    class catalog_kubedb_com_MemcachedVersion {
        +string kind: MemcachedVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_MemcachedVersion : <<Cluster>>
    class catalog_kubedb_com_MongoDBVersion {
        +string kind: MongoDBVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object archiver
        +object archiver.addon
        +object archiver.walg
        +object db
        +string db.image
        +boolean deprecated
        +enum[4 values] distribution
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object replicationModeDetector
        +string replicationModeDetector.image
        +object securityContext
        +integer(int64) securityContext.runAsGroup
        +integer(int64) securityContext.runAsUser
    }
    catalog_kubedb_com_MongoDBVersion : <<Cluster>>
    class catalog_kubedb_com_MySQLVersion {
        +string kind: MySQLVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object archiver
        +object archiver.addon
        +object archiver.walg
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +enum[5 values] distribution
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object replicationModeDetector
        +string replicationModeDetector.image
    }
    catalog_kubedb_com_MySQLVersion : <<Cluster>>
    class catalog_kubedb_com_OracleVersion {
        +string kind: OracleVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object coordinator
        +string coordinator.image
        +object dataGuard
        +object dataGuard.initContainer
        +object dataGuard.observer
        +object db
        +string db.baseOS
        +string db.image
        +boolean deprecated
        +enum[Official] distribution
        +object exporter
        +string exporter.image
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
    }
    catalog_kubedb_com_OracleVersion : <<Cluster>>
    class catalog_kubedb_com_PerconaXtraDBVersion {
        +string kind: PerconaXtraDBVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
        +array<object> ui
    }
    catalog_kubedb_com_PerconaXtraDBVersion : <<Cluster>>
    class catalog_kubedb_com_PgBouncerVersion {
        +string kind: PgBouncerVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object pgBouncer
        +string pgBouncer.image
        +object securityContext
        +boolean securityContext.runAsAnyNonRoot
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_PgBouncerVersion : <<Cluster>>
    class catalog_kubedb_com_PgpoolVersion {
        +string kind: PgpoolVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object pgpool
        +string pgpool.image
        +object securityContext
        +boolean securityContext.runAsAnyNonRoot
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_PgpoolVersion : <<Cluster>>
    class catalog_kubedb_com_PostgresVersion {
        +string kind: PostgresVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object archiver
        +object archiver.addon
        +object archiver.walg
        +object coordinator
        +string coordinator.image
        +object db
        +string db.baseOS
        +string db.image
        +boolean deprecated
        +enum[6 values] distribution
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +boolean securityContext.runAsAnyNonRoot
        +integer(int64) securityContext.runAsUser
    }
    catalog_kubedb_com_PostgresVersion : <<Cluster>>
    class catalog_kubedb_com_ProxySQLVersion {
        +string kind: ProxySQLVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object proxysql
        +string proxysql.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_ProxySQLVersion : <<Cluster>>
    class catalog_kubedb_com_RabbitMQVersion {
        +string kind: RabbitMQVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +array<object> ui
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_RabbitMQVersion : <<Cluster>>
    class catalog_kubedb_com_RedisVersion {
        +string kind: RedisVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +enum[Official|Valkey] distribution
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
    }
    catalog_kubedb_com_RedisVersion : <<Cluster>>
    class catalog_kubedb_com_SchemaRegistryVersion {
        +string kind: SchemaRegistryVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +boolean deprecated
        +enum[Apicurio|Aiven] distribution
        +object inMemory
        +string inMemory.image
        +object registry
        +string registry.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_SchemaRegistryVersion : <<Cluster>>
    class catalog_kubedb_com_SinglestoreVersion {
        +string kind: SinglestoreVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsGroup
        +integer(int64) securityContext.runAsUser
        +object standalone
        +string standalone.image
        +object stash
        +object stash.addon
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_SinglestoreVersion : <<Cluster>>
    class catalog_kubedb_com_SolrVersion {
        +string kind: SolrVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object db
        +string db.image
        +boolean deprecated
        +object initContainer
        +string initContainer.image
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
        +string version
    }
    catalog_kubedb_com_SolrVersion : <<Cluster>>
    class catalog_kubedb_com_ZooKeeperVersion {
        +string kind: ZooKeeperVersion
        +string apiVersion: catalog.kubedb.com/v1alpha1
        +string scope: Cluster
        +object coordinator
        +string coordinator.image
        +object db
        +string db.image
        +boolean deprecated
        +object exporter
        +string exporter.image
        +object gitSyncer
        +string gitSyncer.image
        +object initContainer
        +string initContainer.image
        +object podSecurityPolicies
        +string podSecurityPolicies.databasePolicyName
        +object securityContext
        +integer(int64) securityContext.runAsUser
        +object stash
        +object stash.addon
        +object updateConstraints
        +array<string> updateConstraints.allowlist
        +array<string> updateConstraints.denylist
    }
    catalog_kubedb_com_ZooKeeperVersion : <<Cluster>>
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_ClickHouseVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_DruidVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_ElasticsearchVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_EtcdVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_FerretDBVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_CassandraVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_DruidVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_ElasticsearchVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_FerretDBVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_ClickHouseVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_ElasticsearchVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_EtcdVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_FerretDBVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_KafkaConnectorVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_DruidVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_EtcdVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_FerretDBVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_ElasticsearchVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_FerretDBVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_KafkaConnectorVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_EtcdVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_HazelcastVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_KafkaConnectorVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_FerretDBVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_IgniteVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_KafkaConnectorVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_HazelcastVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_KafkaConnectorVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_KafkaVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_IgniteVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_KafkaConnectorVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_MariaDBVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_KafkaVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_MemcachedVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_MariaDBVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_MongoDBVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_MemcachedVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_MSSQLServerVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_MongoDBVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_MySQLVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_MSSQLServerVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_OracleVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_MySQLVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_PerconaXtraDBVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_OracleVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_PgBouncerVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_PerconaXtraDBVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_PgpoolVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_PgBouncerVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_PostgresVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_PgpoolVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_ProxySQLVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_PostgresVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_RabbitMQVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_ProxySQLVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_RabbitMQVersion --> catalog_kubedb_com_RedisVersion : similar schema
    catalog_kubedb_com_RabbitMQVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_RabbitMQVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_RabbitMQVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_RabbitMQVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_RedisVersion --> catalog_kubedb_com_SchemaRegistryVersion : similar schema
    catalog_kubedb_com_RedisVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_RedisVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_RedisVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_SchemaRegistryVersion --> catalog_kubedb_com_SinglestoreVersion : similar schema
    catalog_kubedb_com_SchemaRegistryVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_SinglestoreVersion --> catalog_kubedb_com_SolrVersion : similar schema
    catalog_kubedb_com_SinglestoreVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
    catalog_kubedb_com_SolrVersion --> catalog_kubedb_com_ZooKeeperVersion : similar schema
```
### Detailed CRD Documentation

#### CassandraVersion

**Full Name:** `cassandraversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** casversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `medusa` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### ClickHouseVersion

**Full Name:** `clickhouseversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** chversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clickHouseKeeper` | `object` | ✓ | *No description* |
| `db` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### DruidVersion

**Full Name:** `druidversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** drversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### ElasticsearchVersion

**Full Name:** `elasticsearchversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** esversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authPlugin` | `enum[4 values]` | ✓ | *No description* |
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `dashboard` | `object` |  | *No description* |
| `dashboardInitContainer` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[5 values]` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### EtcdVersion

**Full Name:** `etcdversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** etcversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |


#### FerretDBVersion

**Full Name:** `ferretdbversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** frversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `postgres` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### HazelcastVersion

**Full Name:** `hazelcastversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** hzversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### IgniteVersion

**Full Name:** `igniteversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** igversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### KafkaConnectorVersion

**Full Name:** `kafkaconnectorversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** kcversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `connectorPlugin` | `object` | ✓ | *No description* |
| `type` | `string` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |


#### KafkaVersion

**Full Name:** `kafkaversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** kfversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `connectCluster` | `object` | ✓ | *No description* |
| `cruiseControl` | `object` | ✓ | *No description* |
| `db` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `podSecurityPolicies` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### MSSQLServerVersion

**Full Name:** `mssqlserverversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** msversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `archiver` | `object` |  | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### MariaDBVersion

**Full Name:** `mariadbversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** mdversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `archiver` | `object` |  | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `maxscale` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### MemcachedVersion

**Full Name:** `memcachedversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** mcversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### MongoDBVersion

**Full Name:** `mongodbversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** mgversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `replicationModeDetector` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `archiver` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[4 values]` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### MySQLVersion

**Full Name:** `mysqlversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** myversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `archiver` | `object` |  | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[5 values]` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `replicationModeDetector` | `object` |  | *No description* |
| `router` | `object` |  | *No description* |
| `routerInitContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### OracleVersion

**Full Name:** `oracleversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** oraversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `coordinator` | `object` |  | *No description* |
| `dataGuard` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[Official]` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### PerconaXtraDBVersion

**Full Name:** `perconaxtradbversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** pxversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### PgBouncerVersion

**Full Name:** `pgbouncerversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** pbversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `exporter` | `object` | ✓ | *No description* |
| `pgBouncer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### PgpoolVersion

**Full Name:** `pgpoolversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** ppversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pgpool` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `exporter` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### PostgresVersion

**Full Name:** `postgresversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** pgversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `archiver` | `object` |  | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[6 values]` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `tls` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### ProxySQLVersion

**Full Name:** `proxysqlversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** prxversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `proxysql` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `exporter` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### RabbitMQVersion

**Full Name:** `rabbitmqversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** rmversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### RedisVersion

**Full Name:** `redisversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** rdversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `exporter` | `object` | ✓ | *No description* |
| `podSecurityPolicies` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `distribution` | `enum[Official|Valkey]` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `ui` | `array<object>` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### SchemaRegistryVersion

**Full Name:** `schemaregistryversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** ksrversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `distribution` | `enum[Apicurio|Aiven]` | ✓ | *No description* |
| `registry` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `inMemory` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### SinglestoreVersion

**Full Name:** `singlestoreversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** sdbv  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `standalone` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### SolrVersion

**Full Name:** `solrversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** slversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `initContainer` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |


#### ZooKeeperVersion

**Full Name:** `zookeeperversions.catalog.kubedb.com`  
**API Version:** `catalog.kubedb.com/v1alpha1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** catalog, kubedb, appscode  
**Short Names:** zkversion  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `db` | `object` | ✓ | *No description* |
| `version` | `string` | ✓ | *No description* |
| `coordinator` | `object` |  | *No description* |
| `deprecated` | `boolean` |  | *No description* |
| `exporter` | `object` |  | *No description* |
| `gitSyncer` | `object` |  | *No description* |
| `initContainer` | `object` |  | *No description* |
| `podSecurityPolicies` | `object` |  | *No description* |
| `securityContext` | `object` |  | *No description* |
| `stash` | `object` |  | *No description* |
| `updateConstraints` | `object` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `cassandraversions.catalog.kubedb.com` | `CassandraVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `clickhouseversions.catalog.kubedb.com` | `ClickHouseVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `druidversions.catalog.kubedb.com` | `DruidVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `elasticsearchversions.catalog.kubedb.com` | `ElasticsearchVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `etcdversions.catalog.kubedb.com` | `EtcdVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `ferretdbversions.catalog.kubedb.com` | `FerretDBVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `hazelcastversions.catalog.kubedb.com` | `HazelcastVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `igniteversions.catalog.kubedb.com` | `IgniteVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `kafkaconnectorversions.catalog.kubedb.com` | `KafkaConnectorVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `kafkaversions.catalog.kubedb.com` | `KafkaVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `mariadbversions.catalog.kubedb.com` | `MariaDBVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `memcachedversions.catalog.kubedb.com` | `MemcachedVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `mongodbversions.catalog.kubedb.com` | `MongoDBVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `mssqlserverversions.catalog.kubedb.com` | `MSSQLServerVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `mysqlversions.catalog.kubedb.com` | `MySQLVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `oracleversions.catalog.kubedb.com` | `OracleVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `perconaxtradbversions.catalog.kubedb.com` | `PerconaXtraDBVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `pgbouncerversions.catalog.kubedb.com` | `PgBouncerVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `pgpoolversions.catalog.kubedb.com` | `PgpoolVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `postgresversions.catalog.kubedb.com` | `PostgresVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `proxysqlversions.catalog.kubedb.com` | `ProxySQLVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `rabbitmqversions.catalog.kubedb.com` | `RabbitMQVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `redisversions.catalog.kubedb.com` | `RedisVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `schemaregistryversions.catalog.kubedb.com` | `SchemaRegistryVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `singlestoreversions.catalog.kubedb.com` | `SinglestoreVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `solrversions.catalog.kubedb.com` | `SolrVersion` | `catalog.kubedb.com` | Cluster | 0 |
| `zookeeperversions.catalog.kubedb.com` | `ZooKeeperVersion` | `catalog.kubedb.com` | Cluster | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 176 |
| `string` | 36 |
| `boolean` | 25 |
| `array` | 20 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `CassandraVersion` | `ClickHouseVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `DruidVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `ElasticsearchVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `EtcdVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `FerretDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `CassandraVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `DruidVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `ElasticsearchVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `FerretDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ClickHouseVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `ElasticsearchVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `EtcdVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `FerretDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `KafkaConnectorVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `DruidVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `EtcdVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `FerretDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ElasticsearchVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `FerretDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `KafkaConnectorVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `EtcdVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `HazelcastVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `KafkaConnectorVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `FerretDBVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `IgniteVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `KafkaConnectorVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `HazelcastVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `KafkaConnectorVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `KafkaVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `IgniteVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaConnectorVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `MariaDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `KafkaVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `MemcachedVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MariaDBVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `MongoDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MemcachedVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `MSSQLServerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MongoDBVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `MySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MSSQLServerVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `OracleVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `MySQLVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `PerconaXtraDBVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `OracleVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `PgBouncerVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PerconaXtraDBVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `PgpoolVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgBouncerVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `PostgresVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PgpoolVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `ProxySQLVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `PostgresVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `RabbitMQVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `ProxySQLVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RabbitMQVersion` | `RedisVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RabbitMQVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RabbitMQVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RabbitMQVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RabbitMQVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RedisVersion` | `SchemaRegistryVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RedisVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RedisVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `RedisVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `SchemaRegistryVersion` | `SinglestoreVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `SchemaRegistryVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `SinglestoreVersion` | `SolrVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `SinglestoreVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |
| `SolrVersion` | `ZooKeeperVersion` | `catalog.kubedb.com (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:14*