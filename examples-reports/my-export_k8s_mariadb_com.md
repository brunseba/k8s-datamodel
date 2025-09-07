# CRD Schema Documentation - k8s.mariadb.com API Group

> **Generated:** 2025-09-07 17:05:15
> 
> **Total CRDs:** 10
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [k8s.mariadb.com](#k8smariadbcom) (10 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **10 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 10 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 10 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 10/10 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **k8s.mariadb.com**: 10 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `MariaDB` (k8s.mariadb.com): 56 properties
2. `MaxScale` (k8s.mariadb.com): 39 properties
3. `SqlJob` (k8s.mariadb.com): 27 properties


## 📁 k8s.mariadb.com

### Overview

**API Group:** `k8s.mariadb.com`  
**CRDs in Group:** 10  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `Backup` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Connection` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Database` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Grant` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MariaDB` | Namespaced | v1alpha1 | 0 | *No description available* |
| `MaxScale` | Namespaced | v1alpha1 | 0 | *No description available* |
| `PhysicalBackup` | Namespaced | v1alpha1 | 0 | *No description available* |
| `Restore` | Namespaced | v1alpha1 | 0 | *No description available* |
| `SqlJob` | Namespaced | v1alpha1 | 0 | *No description available* |
| `User` | Namespaced | v1alpha1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: k8s.mariadb.com
    class k8s_mariadb_com_Backup {
        +string kind: Backup
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +object affinity
        +boolean affinity.antiAffinityEnabled
        +object affinity.nodeAffinity
        +object affinity.podAntiAffinity
        +array<string> args
        +integer(int32) backoffLimit
        +enum[none|bzip2|gzip] compression
        +array<string> databases
        +integer(int32) failedJobsHistoryLimit
        +boolean ignoreGlobalPriv
        +array<object> imagePullSecrets
        +object inheritMetadata
        +object inheritMetadata.annotations
        +object inheritMetadata.labels
        +string logLevel
    }
    k8s_mariadb_com_Backup : <<Namespaced>>
    class k8s_mariadb_com_Connection {
        +string kind: Connection
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +string database
        +object healthCheck
        +string healthCheck.interval
        +string healthCheck.retryInterval
        +string host
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +object maxScaleRef
        +string maxScaleRef.name
        +string maxScaleRef.namespace
        +object params
        +object passwordSecretKeyRef
        +string passwordSecretKeyRef.key
        +string passwordSecretKeyRef.name
        +integer(int32) port
        +string secretName
        +object secretTemplate
        +string secretTemplate.databaseKey
        +string secretTemplate.format
        +string secretTemplate.hostKey
        +string secretTemplate.key
        +object secretTemplate.metadata
        +string secretTemplate.passwordKey
        +string secretTemplate.portKey
        +string secretTemplate.usernameKey
    }
    k8s_mariadb_com_Connection : <<Namespaced>>
    class k8s_mariadb_com_Database {
        +string kind: Database
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +string characterSet
        +enum[Skip|Delete] cleanupPolicy
        +string collate
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +string name
        +string requeueInterval
        +string retryInterval
    }
    k8s_mariadb_com_Database : <<Namespaced>>
    class k8s_mariadb_com_Grant {
        +string kind: Grant
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +enum[Skip|Delete] cleanupPolicy
        +string database
        +boolean grantOption
        +string host
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +array<string> privileges
        +string requeueInterval
        +string retryInterval
        +string table
        +string username
    }
    k8s_mariadb_com_Grant : <<Namespaced>>
    class k8s_mariadb_com_MariaDB {
        +string kind: MariaDB
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +object affinity
        +boolean affinity.antiAffinityEnabled
        +object affinity.nodeAffinity
        +object affinity.podAntiAffinity
        +array<string> args
        +object bootstrapFrom
        +enum[Logical|Physical] bootstrapFrom.backupContentType
        +object bootstrapFrom.backupRef
        +object bootstrapFrom.restoreJob
        +object bootstrapFrom.s3
        +object bootstrapFrom.stagingStorage
        +string(date-time) bootstrapFrom.targetRecoveryTime
        +object bootstrapFrom.volume
        +object bootstrapFrom.volumeSnapshotRef
        +array<string> command
        +object connection
        +object connection.healthCheck
        +object connection.params
        +integer(int32) connection.port
        +string connection.secretName
        +object connection.secretTemplate
        +string connection.serviceName
        +string database
        +array<object> env
        +array<object> envFrom
        +object galera
        +object galera.agent
        +boolean galera.availableWhenDonor
        +object galera.config
        +boolean galera.enabled
        +string galera.galeraLibPath
        +object galera.initContainer
        +object galera.initJob
        +object galera.primary
        +object galera.providerOptions
        +object galera.recovery
        +string image
    }
    k8s_mariadb_com_MariaDB : <<Namespaced>>
    class k8s_mariadb_com_MaxScale {
        +string kind: MaxScale
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +object admin
        +boolean admin.guiEnabled
        +integer(int32) admin.port
        +object affinity
        +boolean affinity.antiAffinityEnabled
        +object affinity.nodeAffinity
        +object affinity.podAntiAffinity
        +array<string> args
        +object auth
        +object auth.adminPasswordSecretKeyRef
        +string auth.adminUsername
        +integer(int32) auth.clientMaxConnections
        +object auth.clientPasswordSecretKeyRef
        +string auth.clientUsername
        +boolean auth.deleteDefaultAdmin
        +boolean auth.generate
        +object auth.metricsPasswordSecretKeyRef
        +string auth.metricsUsername
        +integer(int32) auth.monitorMaxConnections
        +array<string> command
        +object config
        +object config.params
        +object config.sync
        +object config.volumeClaimTemplate
        +object connection
        +object connection.healthCheck
        +object connection.params
        +integer(int32) connection.port
        +string connection.secretName
        +object connection.secretTemplate
        +string connection.serviceName
        +array<object> env
        +array<object> envFrom
        +object guiKubernetesService
        +boolean guiKubernetesService.allocateLoadBalancerNodePorts
        +string guiKubernetesService.externalTrafficPolicy
        +string guiKubernetesService.loadBalancerIP
        +array<string> guiKubernetesService.loadBalancerSourceRanges
        +object guiKubernetesService.metadata
        +string guiKubernetesService.sessionAffinity
        +enum[ClusterIP|NodePort|LoadBalancer] guiKubernetesService.type
    }
    k8s_mariadb_com_MaxScale : <<Namespaced>>
    class k8s_mariadb_com_PhysicalBackup {
        +string kind: PhysicalBackup
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +array<string> args
        +integer(int32) backoffLimit
        +enum[none|bzip2|gzip] compression
        +array<object> imagePullSecrets
        +object inheritMetadata
        +object inheritMetadata.annotations
        +object inheritMetadata.labels
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +string maxRetention
        +boolean podAffinity
        +object podMetadata
        +object podMetadata.annotations
        +object podMetadata.labels
        +object podSecurityContext
        +object podSecurityContext.appArmorProfile
        +integer(int64) podSecurityContext.fsGroup
        +string podSecurityContext.fsGroupChangePolicy
        +integer(int64) podSecurityContext.runAsGroup
        +boolean podSecurityContext.runAsNonRoot
        +integer(int64) podSecurityContext.runAsUser
        +object podSecurityContext.seLinuxOptions
        +object podSecurityContext.seccompProfile
        +array<integer> podSecurityContext.supplementalGroups
    }
    k8s_mariadb_com_PhysicalBackup : <<Namespaced>>
    class k8s_mariadb_com_Restore {
        +string kind: Restore
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +object affinity
        +boolean affinity.antiAffinityEnabled
        +object affinity.nodeAffinity
        +object affinity.podAntiAffinity
        +array<string> args
        +integer(int32) backoffLimit
        +object backupRef
        +string backupRef.name
        +string database
        +array<object> imagePullSecrets
        +object inheritMetadata
        +object inheritMetadata.annotations
        +object inheritMetadata.labels
        +string logLevel
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +object nodeSelector
    }
    k8s_mariadb_com_Restore : <<Namespaced>>
    class k8s_mariadb_com_SqlJob {
        +string kind: SqlJob
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +object affinity
        +boolean affinity.antiAffinityEnabled
        +object affinity.nodeAffinity
        +object affinity.podAntiAffinity
        +array<string> args
        +integer(int32) backoffLimit
        +string database
        +array<object> dependsOn
        +integer(int32) failedJobsHistoryLimit
        +array<object> imagePullSecrets
        +object inheritMetadata
        +object inheritMetadata.annotations
        +object inheritMetadata.labels
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +object nodeSelector
    }
    k8s_mariadb_com_SqlJob : <<Namespaced>>
    class k8s_mariadb_com_User {
        +string kind: User
        +string apiVersion: k8s.mariadb.com/v1alpha1
        +string scope: Namespaced
        +enum[Skip|Delete] cleanupPolicy
        +string host
        +object mariaDbRef
        +string mariaDbRef.name
        +string mariaDbRef.namespace
        +boolean mariaDbRef.waitForIt
        +integer(int32) maxUserConnections
        +string name
        +object passwordHashSecretKeyRef
        +string passwordHashSecretKeyRef.key
        +string passwordHashSecretKeyRef.name
        +object passwordPlugin
        +object passwordPlugin.pluginArgSecretKeyRef
        +object passwordPlugin.pluginNameSecretKeyRef
        +object passwordSecretKeyRef
        +string passwordSecretKeyRef.key
        +string passwordSecretKeyRef.name
        +string requeueInterval
        +object require
        +string require.issuer
        +boolean require.ssl
        +string require.subject
        +boolean require.x509
    }
    k8s_mariadb_com_User : <<Namespaced>>
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Connection : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Connection : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Connection : routes to
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Database : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Database : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Database : uses
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_MariaDB : uses
    k8s_mariadb_com_Backup --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_PhysicalBackup : similar schema
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Restore : uses
    k8s_mariadb_com_Backup --> k8s_mariadb_com_Restore : similar schema
    k8s_mariadb_com_Backup --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_SqlJob : similar schema
    k8s_mariadb_com_Backup --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Backup --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Database : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Database : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Database : uses
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Database : templates
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : uses
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : configures
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : templates
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : federates
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MariaDB : routes to
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : uses
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : configures
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : templates
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : federates
    k8s_mariadb_com_Connection --> k8s_mariadb_com_MaxScale : routes to
    k8s_mariadb_com_Connection --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_PhysicalBackup : routes to
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_Restore : routes to
    k8s_mariadb_com_Connection --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Connection --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_Connection --> k8s_mariadb_com_User : templates
    k8s_mariadb_com_Database --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_Grant : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_Grant : uses
    k8s_mariadb_com_Database --> k8s_mariadb_com_Grant : similar schema
    k8s_mariadb_com_Database --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_MariaDB : uses
    k8s_mariadb_com_Database --> k8s_mariadb_com_MariaDB : templates
    k8s_mariadb_com_Database --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_MaxScale : uses
    k8s_mariadb_com_Database --> k8s_mariadb_com_MaxScale : templates
    k8s_mariadb_com_Database --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_Restore : uses
    k8s_mariadb_com_Database --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_SqlJob : uses
    k8s_mariadb_com_Database --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Database --> k8s_mariadb_com_User : similar schema
    k8s_mariadb_com_Grant --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_MariaDB : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_MariaDB : uses
    k8s_mariadb_com_Grant --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Grant --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_Grant --> k8s_mariadb_com_User : similar schema
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : owns
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : uses
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : configures
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : templates
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : similar schema
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : federates
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_MaxScale : routes to
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_PhysicalBackup : uses
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_Restore : uses
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_SqlJob : uses
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_SqlJob : routes to
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_User : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_User : references
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_User : templates
    k8s_mariadb_com_MariaDB --> k8s_mariadb_com_User : federates
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_PhysicalBackup : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_User : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_User : references
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_User : templates
    k8s_mariadb_com_MaxScale --> k8s_mariadb_com_User : federates
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_Restore : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_Restore : similar schema
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_SqlJob : similar schema
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_User : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_User : references
    k8s_mariadb_com_PhysicalBackup --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_Restore --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Restore --> k8s_mariadb_com_SqlJob : references
    k8s_mariadb_com_Restore --> k8s_mariadb_com_SqlJob : similar schema
    k8s_mariadb_com_Restore --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Restore --> k8s_mariadb_com_User : references
    k8s_mariadb_com_Restore --> k8s_mariadb_com_User : uses
    k8s_mariadb_com_SqlJob --> k8s_mariadb_com_User : references
    k8s_mariadb_com_SqlJob --> k8s_mariadb_com_User : references
    k8s_mariadb_com_SqlJob --> k8s_mariadb_com_User : uses
```
### Detailed CRD Documentation

#### Backup

**Full Name:** `backups.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** bmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `storage` | `object` | ✓ | Storage defines the final storage for backups. |
| `affinity` | `object` |  | Affinity to be used in the Pod. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `backoffLimit` | `integer(int32)` |  | BackoffLimit defines the maximum number of attempts to su... |
| `compression` | `enum[none|bzip2|gzip]` |  | Compression algorithm to be used in the Backup. |
| `databases` | `array<string>` |  | Databases defines the logical databases to be backed up. ... |
| `failedJobsHistoryLimit` | `integer(int32)` |  | FailedJobsHistoryLimit defines the maximum number of fail... |
| `ignoreGlobalPriv` | `boolean` |  | IgnoreGlobalPriv indicates to ignore the mysql.global_pri... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `logLevel` | `string` |  | LogLevel to be used n the Backup Job. It defaults to 'info'. |
| `maxRetention` | `string` |  | MaxRetention defines the retention policy for backups. Ol... |
| `nodeSelector` | `object` |  | NodeSelector to be used in the Pod. |
| `podMetadata` | `object` |  | PodMetadata defines extra metadata for the Pod. |
| `podSecurityContext` | `object` |  | SecurityContext holds pod-level security attributes and c... |
| `priorityClassName` | `string` |  | PriorityClassName to be used in the Pod. |
| `resources` | `object` |  | Resources describes the compute resource requirements. |
| `restartPolicy` | `enum[Always|OnFailure|Never]` |  | RestartPolicy to be added to the Backup Pod. |
| `schedule` | `object` |  | Schedule defines when the Backup will be taken. |

*... and 6 more properties*


#### Connection

**Full Name:** `connections.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** cmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | ✓ | Username to use for configuring the Connection. |
| `database` | `string` |  | Database to use when configuring the Connection. |
| `healthCheck` | `object` |  | HealthCheck to be used in the Connection. |
| `host` | `string` |  | Host to connect to. If not provided, it defaults to the M... |
| `mariaDbRef` | `object` |  | MariaDBRef is a reference to the MariaDB to connect to. E... |
| `maxScaleRef` | `object` |  | MaxScaleRef is a reference to the MaxScale to connect to.... |
| `params` | `object` |  | Params to be used in the Connection. |
| `passwordSecretKeyRef` | `object` |  | PasswordSecretKeyRef is a reference to the password to us... |
| `port` | `integer(int32)` |  | Port to connect to. If not provided, it defaults to the M... |
| `secretName` | `string` |  | SecretName to be used in the Connection. |
| `secretTemplate` | `object` |  | SecretTemplate to be used in the Connection. |
| `serviceName` | `string` |  | ServiceName to be used in the Connection. |
| `tlsClientCertSecretRef` | `object` |  | TLSClientCertSecretRef is a reference to a Kubernetes TLS... |


#### Database

**Full Name:** `databases.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** dmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `characterSet` | `string` |  | CharacterSet to use in the Database. |
| `cleanupPolicy` | `enum[Skip|Delete]` |  | CleanupPolicy defines the behavior for cleaning up a SQL ... |
| `collate` | `string` |  | Collate to use in the Database. |
| `name` | `string` |  | Name overrides the default Database name provided by meta... |
| `requeueInterval` | `string` |  | RequeueInterval is used to perform requeue reconciliations. |
| `retryInterval` | `string` |  | RetryInterval is the interval used to perform retries. |


#### Grant

**Full Name:** `grants.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** gmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `privileges` | `array<string>` | ✓ | Privileges to use in the Grant. |
| `username` | `string` | ✓ | Username to use in the Grant. |
| `cleanupPolicy` | `enum[Skip|Delete]` |  | CleanupPolicy defines the behavior for cleaning up a SQL ... |
| `database` | `string` |  | Database to use in the Grant. |
| `grantOption` | `boolean` |  | GrantOption to use in the Grant. |
| `host` | `string` |  | Host to use in the Grant. It can be localhost, an IP or '%'. |
| `requeueInterval` | `string` |  | RequeueInterval is used to perform requeue reconciliations. |
| `retryInterval` | `string` |  | RetryInterval is the interval used to perform retries. |
| `table` | `string` |  | Table to use in the Grant. |


#### MariaDB

**Full Name:** `mariadbs.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** mdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `affinity` | `object` |  | Affinity to be used in the Pod. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `bootstrapFrom` | `object` |  | BootstrapFrom defines a source to bootstrap from. |
| `command` | `array<string>` |  | Command to be used in the Container. |
| `connection` | `object` |  | Connection defines a template to configure the general Co... |
| `database` | `string` |  | Database is the name of the initial Database. |
| `env` | `array<object>` |  | Env represents the environment variables to be injected i... |
| `envFrom` | `array<object>` |  | EnvFrom represents the references (via ConfigMap and Secr... |
| `galera` | `object` |  | Replication configures high availability via Galera. |
| `image` | `string` |  | Image name to be used by the MariaDB instances. The suppo... |
| `imagePullPolicy` | `enum[Always|Never|IfNotPresent]` |  | ImagePullPolicy is the image pull policy. One of `Always`... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `initContainers` | `array<object>` |  | InitContainers to be used in the Pod. |
| `livenessProbe` | `object` |  | LivenessProbe to be used in the Container. |
| `maxScale` | `object` |  | MaxScale is the MaxScale specification that defines the M... |
| `maxScaleRef` | `object` |  | MaxScaleRef is a reference to a MaxScale resource to be u... |
| `metrics` | `object` |  | Metrics configures metrics and how to scrape them. |
| `myCnf` | `string` |  | MyCnf allows to specify the my.cnf file mounted by Mariad... |
| `myCnfConfigMapKeyRef` | `object` |  | MyCnfConfigMapKeyRef is a reference to the my.cnf config ... |

*... and 36 more properties*


#### MaxScale

**Full Name:** `maxscales.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** mxs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `admin` | `object` |  | Admin configures the admin REST API and GUI. |
| `affinity` | `object` |  | Affinity to be used in the Pod. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `auth` | `object` |  | Auth defines the credentials required for MaxScale to con... |
| `command` | `array<string>` |  | Command to be used in the Container. |
| `config` | `object` |  | Config defines the MaxScale configuration. |
| `connection` | `object` |  | Connection provides a template to define the Connection f... |
| `env` | `array<object>` |  | Env represents the environment variables to be injected i... |
| `envFrom` | `array<object>` |  | EnvFrom represents the references (via ConfigMap and Secr... |
| `guiKubernetesService` | `object` |  | GuiKubernetesService defines a template for a Kubernetes ... |
| `image` | `string` |  | Image name to be used by the MaxScale instances. The supp... |
| `imagePullPolicy` | `enum[Always|Never|IfNotPresent]` |  | ImagePullPolicy is the image pull policy. One of `Always`... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `kubernetesService` | `object` |  | KubernetesService defines a template for a Kubernetes Ser... |
| `livenessProbe` | `object` |  | LivenessProbe to be used in the Container. |
| `mariaDbRef` | `object` |  | MariaDBRef is a reference to the MariaDB that MaxScale po... |
| `metrics` | `object` |  | Metrics configures metrics and how to scrape them. |
| `monitor` | `object` |  | Monitor monitors MariaDB server instances. It is required... |
| `nodeSelector` | `object` |  | NodeSelector to be used in the Pod. |

*... and 19 more properties*


#### PhysicalBackup

**Full Name:** `physicalbackups.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** pbmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `storage` | `object` | ✓ | Storage defines the final storage for backups. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `backoffLimit` | `integer(int32)` |  | BackoffLimit defines the maximum number of attempts to su... |
| `compression` | `enum[none|bzip2|gzip]` |  | Compression algorithm to be used in the Backup. |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `maxRetention` | `string` |  | MaxRetention defines the retention policy for backups. Ol... |
| `podAffinity` | `boolean` |  | PodAffinity indicates whether the Jobs should run in the ... |
| `podMetadata` | `object` |  | PodMetadata defines extra metadata for the Pod. |
| `podSecurityContext` | `object` |  | SecurityContext holds pod-level security attributes and c... |
| `priorityClassName` | `string` |  | PriorityClassName to be used in the Pod. |
| `resources` | `object` |  | Resources describes the compute resource requirements. |
| `restartPolicy` | `enum[Always|OnFailure|Never]` |  | RestartPolicy to be added to the PhysicalBackup Pod. |
| `schedule` | `object` |  | Schedule defines when the PhysicalBackup will be taken. |
| `securityContext` | `object` |  | SecurityContext holds security configuration that will be... |
| `serviceAccountName` | `string` |  | ServiceAccountName is the name of the ServiceAccount to b... |
| `stagingStorage` | `object` |  | StagingStorage defines the temporary storage used to keep... |
| `successfulJobsHistoryLimit` | `integer(int32)` |  | SuccessfulJobsHistoryLimit defines the maximum number of ... |
| `timeout` | `string` |  | Timeout defines the maximum duration of a PhysicalBackup ... |

*... and 1 more properties*


#### Restore

**Full Name:** `restores.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** rmdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `affinity` | `object` |  | Affinity to be used in the Pod. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `backoffLimit` | `integer(int32)` |  | BackoffLimit defines the maximum number of attempts to su... |
| `backupRef` | `object` |  | BackupRef is a reference to a Backup object. It has prior... |
| `database` | `string` |  | Database defines the logical database to be restored. If ... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `logLevel` | `string` |  | LogLevel to be used n the Backup Job. It defaults to 'info'. |
| `nodeSelector` | `object` |  | NodeSelector to be used in the Pod. |
| `podMetadata` | `object` |  | PodMetadata defines extra metadata for the Pod. |
| `podSecurityContext` | `object` |  | SecurityContext holds pod-level security attributes and c... |
| `priorityClassName` | `string` |  | PriorityClassName to be used in the Pod. |
| `resources` | `object` |  | Resources describes the compute resource requirements. |
| `restartPolicy` | `enum[Always|OnFailure|Never]` |  | RestartPolicy to be added to the Backup Job. |
| `s3` | `object` |  | S3 defines the configuration to restore backups from a S3... |
| `securityContext` | `object` |  | SecurityContext holds security configuration that will be... |
| `serviceAccountName` | `string` |  | ServiceAccountName is the name of the ServiceAccount to b... |
| `stagingStorage` | `object` |  | StagingStorage defines the temporary storage used to keep... |
| `targetRecoveryTime` | `string(date-time)` |  | TargetRecoveryTime is a RFC3339 (1970-01-01T00:00:00Z) da... |

*... and 2 more properties*


#### SqlJob

**Full Name:** `sqljobs.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** smdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `passwordSecretKeyRef` | `object` | ✓ | UserPasswordSecretKeyRef is a reference to the impersonat... |
| `username` | `string` | ✓ | Username to be impersonated when executing the SqlJob. |
| `affinity` | `object` |  | Affinity to be used in the Pod. |
| `args` | `array<string>` |  | Args to be used in the Container. |
| `backoffLimit` | `integer(int32)` |  | BackoffLimit defines the maximum number of attempts to su... |
| `database` | `string` |  | Username to be used when executing the SqlJob. |
| `dependsOn` | `array<object>` |  | DependsOn defines dependencies with other SqlJob objectecs. |
| `failedJobsHistoryLimit` | `integer(int32)` |  | FailedJobsHistoryLimit defines the maximum number of fail... |
| `imagePullSecrets` | `array<object>` |  | ImagePullSecrets is the list of pull Secrets to be used t... |
| `inheritMetadata` | `object` |  | InheritMetadata defines the metadata to be inherited by c... |
| `nodeSelector` | `object` |  | NodeSelector to be used in the Pod. |
| `podMetadata` | `object` |  | PodMetadata defines extra metadata for the Pod. |
| `podSecurityContext` | `object` |  | SecurityContext holds pod-level security attributes and c... |
| `priorityClassName` | `string` |  | PriorityClassName to be used in the Pod. |
| `resources` | `object` |  | Resources describes the compute resource requirements. |
| `restartPolicy` | `enum[Always|OnFailure|Never]` |  | RestartPolicy to be added to the SqlJob Pod. |
| `schedule` | `object` |  | Schedule defines when the SqlJob will be executed. |
| `securityContext` | `object` |  | SecurityContext holds security configuration that will be... |
| `serviceAccountName` | `string` |  | ServiceAccountName is the name of the ServiceAccount to b... |

*... and 7 more properties*


#### User

**Full Name:** `users.k8s.mariadb.com`  
**API Version:** `k8s.mariadb.com/v1alpha1`  
**Scope:** Namespaced  
**Instances:** 0  
**Short Names:** umdb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mariaDbRef` | `object` | ✓ | MariaDBRef is a reference to a MariaDB object. |
| `cleanupPolicy` | `enum[Skip|Delete]` |  | CleanupPolicy defines the behavior for cleaning up a SQL ... |
| `host` | `string` |  | Host related to the User. |
| `maxUserConnections` | `integer(int32)` |  | MaxUserConnections defines the maximum number of simultan... |
| `name` | `string` |  | Name overrides the default name provided by metadata.name. |
| `passwordHashSecretKeyRef` | `object` |  | PasswordHashSecretKeyRef is a reference to the password h... |
| `passwordPlugin` | `object` |  | PasswordPlugin is a reference to the password plugin and ... |
| `passwordSecretKeyRef` | `object` |  | PasswordSecretKeyRef is a reference to the password to be... |
| `requeueInterval` | `string` |  | RequeueInterval is used to perform requeue reconciliations. |
| `require` | `object` |  | Require specifies TLS requirements for the user to connec... |
| `retryInterval` | `string` |  | RetryInterval is the interval used to perform retries. |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `backups.k8s.mariadb.com` | `Backup` | `k8s.mariadb.com` | Namespaced | 0 |
| `connections.k8s.mariadb.com` | `Connection` | `k8s.mariadb.com` | Namespaced | 0 |
| `databases.k8s.mariadb.com` | `Database` | `k8s.mariadb.com` | Namespaced | 0 |
| `grants.k8s.mariadb.com` | `Grant` | `k8s.mariadb.com` | Namespaced | 0 |
| `mariadbs.k8s.mariadb.com` | `MariaDB` | `k8s.mariadb.com` | Namespaced | 0 |
| `maxscales.k8s.mariadb.com` | `MaxScale` | `k8s.mariadb.com` | Namespaced | 0 |
| `physicalbackups.k8s.mariadb.com` | `PhysicalBackup` | `k8s.mariadb.com` | Namespaced | 0 |
| `restores.k8s.mariadb.com` | `Restore` | `k8s.mariadb.com` | Namespaced | 0 |
| `sqljobs.k8s.mariadb.com` | `SqlJob` | `k8s.mariadb.com` | Namespaced | 0 |
| `users.k8s.mariadb.com` | `User` | `k8s.mariadb.com` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 112 |
| `string` | 62 |
| `array` | 37 |
| `integer` | 14 |
| `boolean` | 7 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `Backup` | `Connection` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Connection` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Connection` | `k8s.mariadb.com (intra-group)` | routes_to |
| `Backup` | `Database` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Database` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Database` | `k8s.mariadb.com (intra-group)` | uses |
| `Backup` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `MariaDB` | `k8s.mariadb.com (intra-group)` | uses |
| `Backup` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Backup` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `Restore` | `k8s.mariadb.com (intra-group)` | uses |
| `Backup` | `Restore` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Backup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Backup` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Backup` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `Connection` | `Database` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `Database` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `Database` | `k8s.mariadb.com (intra-group)` | uses |
| `Connection` | `Database` | `k8s.mariadb.com (intra-group)` | templates |
| `Connection` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | uses |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | configures |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | templates |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | federates |
| `Connection` | `MariaDB` | `k8s.mariadb.com (intra-group)` | routes_to |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | uses |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | configures |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | templates |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | federates |
| `Connection` | `MaxScale` | `k8s.mariadb.com (intra-group)` | routes_to |
| `Connection` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | routes_to |
| `Connection` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `Restore` | `k8s.mariadb.com (intra-group)` | routes_to |
| `Connection` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Connection` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `Connection` | `User` | `k8s.mariadb.com (intra-group)` | templates |
| `Database` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `Grant` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `Grant` | `k8s.mariadb.com (intra-group)` | uses |
| `Database` | `Grant` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Database` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `MariaDB` | `k8s.mariadb.com (intra-group)` | uses |
| `Database` | `MariaDB` | `k8s.mariadb.com (intra-group)` | templates |
| `Database` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `MaxScale` | `k8s.mariadb.com (intra-group)` | uses |
| `Database` | `MaxScale` | `k8s.mariadb.com (intra-group)` | templates |
| `Database` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `Restore` | `k8s.mariadb.com (intra-group)` | uses |
| `Database` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `SqlJob` | `k8s.mariadb.com (intra-group)` | uses |
| `Database` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Database` | `User` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Grant` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `MariaDB` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `MariaDB` | `k8s.mariadb.com (intra-group)` | uses |
| `Grant` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Grant` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `Grant` | `User` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | owns |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | uses |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | configures |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | templates |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | federates |
| `MariaDB` | `MaxScale` | `k8s.mariadb.com (intra-group)` | routes_to |
| `MariaDB` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | uses |
| `MariaDB` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `Restore` | `k8s.mariadb.com (intra-group)` | uses |
| `MariaDB` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `SqlJob` | `k8s.mariadb.com (intra-group)` | uses |
| `MariaDB` | `SqlJob` | `k8s.mariadb.com (intra-group)` | routes_to |
| `MariaDB` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `MariaDB` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `MariaDB` | `User` | `k8s.mariadb.com (intra-group)` | templates |
| `MariaDB` | `User` | `k8s.mariadb.com (intra-group)` | federates |
| `MaxScale` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `PhysicalBackup` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `MaxScale` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `MaxScale` | `User` | `k8s.mariadb.com (intra-group)` | templates |
| `MaxScale` | `User` | `k8s.mariadb.com (intra-group)` | federates |
| `PhysicalBackup` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `Restore` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `Restore` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `PhysicalBackup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `SqlJob` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `PhysicalBackup` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `PhysicalBackup` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `Restore` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Restore` | `SqlJob` | `k8s.mariadb.com (intra-group)` | references |
| `Restore` | `SqlJob` | `k8s.mariadb.com (intra-group)` | similar_schema |
| `Restore` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Restore` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `Restore` | `User` | `k8s.mariadb.com (intra-group)` | uses |
| `SqlJob` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `SqlJob` | `User` | `k8s.mariadb.com (intra-group)` | references |
| `SqlJob` | `User` | `k8s.mariadb.com (intra-group)` | uses |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:15*