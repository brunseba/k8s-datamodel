# CRD Schema Documentation - kafka.strimzi.io API Group

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
   - [kafka.strimzi.io](#kafkastrimziio) (9 CRDs)
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

1. **kafka.strimzi.io**: 9 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `KafkaConnect` (kafka.strimzi.io): 21 properties
2. `KafkaBridge` (kafka.strimzi.io): 19 properties
3. `KafkaMirrorMaker2` (kafka.strimzi.io): 18 properties


## 📁 kafka.strimzi.io

### Overview

**API Group:** `kafka.strimzi.io`  
**CRDs in Group:** 9  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `Kafka` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaBridge` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaConnect` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaConnector` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaMirrorMaker2` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaNodePool` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaRebalance` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaTopic` | Namespaced | v1beta2 | 0 | *No description available* |
| `KafkaUser` | Namespaced | v1beta2 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: kafka.strimzi.io
    class kafka_strimzi_io_Kafka {
        +string kind: Kafka
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object clientsCa
        +enum[renew-certificate|replace-key] clientsCa.certificateExpirationPolicy
        +boolean clientsCa.generateCertificateAuthority
        +boolean clientsCa.generateSecretOwnerReference
        +integer clientsCa.renewalDays
        +integer clientsCa.validityDays
        +object clusterCa
        +enum[renew-certificate|replace-key] clusterCa.certificateExpirationPolicy
        +boolean clusterCa.generateCertificateAuthority
        +boolean clusterCa.generateSecretOwnerReference
        +integer clusterCa.renewalDays
        +integer clusterCa.validityDays
        +object cruiseControl
        +object cruiseControl.apiUsers
        +array<object> cruiseControl.autoRebalance
        +object cruiseControl.brokerCapacity
        +object cruiseControl.config
        +string cruiseControl.image
        +object cruiseControl.jvmOptions
        +object cruiseControl.livenessProbe
        +object cruiseControl.logging
        +object cruiseControl.metricsConfig
        +object cruiseControl.readinessProbe
        +object entityOperator
        +object entityOperator.template
        +object entityOperator.tlsSidecar
        +object entityOperator.topicOperator
        +object entityOperator.userOperator
        +object jmxTrans
        +string jmxTrans.image
        +array<object> jmxTrans.kafkaQueries
        +string jmxTrans.logLevel
        +array<object> jmxTrans.outputDefinitions
        +object jmxTrans.resources
        +object jmxTrans.template
        +object kafka
        +object kafka.authorization
        +string kafka.brokerRackInitImage
        +object kafka.config
        +string kafka.image
        +object kafka.jmxOptions
        +object kafka.jvmOptions
        +array<object> kafka.listeners
        +object kafka.livenessProbe
        +object kafka.logging
        +string kafka.metadataVersion
        +object kafkaExporter
        +boolean kafkaExporter.enableSaramaLogging
        +string kafkaExporter.groupExcludeRegex
        +string kafkaExporter.groupRegex
        +string kafkaExporter.image
        +object kafkaExporter.livenessProbe
        +string kafkaExporter.logging
        +object kafkaExporter.readinessProbe
        +object kafkaExporter.resources
        +boolean kafkaExporter.showAllOffsets
        +object kafkaExporter.template
        +array<string> maintenanceTimeWindows
        +object zookeeper
        +object zookeeper.config
        +string zookeeper.image
        +object zookeeper.jmxOptions
        +object zookeeper.jvmOptions
        +object zookeeper.livenessProbe
        +object zookeeper.logging
        +object zookeeper.metricsConfig
        +object zookeeper.readinessProbe
        +integer zookeeper.replicas
        +object zookeeper.resources
    }
    kafka_strimzi_io_Kafka : <<Namespaced>>
    class kafka_strimzi_io_KafkaBridge {
        +string kind: KafkaBridge
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object adminClient
        +object adminClient.config
        +object authentication
        +object authentication.accessToken
        +boolean authentication.accessTokenIsJwt
        +string authentication.accessTokenLocation
        +string authentication.audience
        +object authentication.certificateAndKey
        +object authentication.clientAssertion
        +string authentication.clientAssertionLocation
        +string authentication.clientAssertionType
        +string authentication.clientId
        +object authentication.clientSecret
        +string bootstrapServers
        +string clientRackInitImage
        +object consumer
        +object consumer.config
        +boolean consumer.enabled
        +integer consumer.timeoutSeconds
        +boolean enableMetrics
        +object http
        +object http.cors
        +integer http.port
        +string image
        +object jvmOptions
        +object jvmOptions.-XX
        +string jvmOptions.-Xms
        +string jvmOptions.-Xmx
        +boolean jvmOptions.gcLoggingEnabled
        +array<object> jvmOptions.javaSystemProperties
        +object livenessProbe
        +integer livenessProbe.failureThreshold
        +integer livenessProbe.initialDelaySeconds
        +integer livenessProbe.periodSeconds
        +integer livenessProbe.successThreshold
        +integer livenessProbe.timeoutSeconds
    }
    kafka_strimzi_io_KafkaBridge : <<Namespaced>>
    class kafka_strimzi_io_KafkaConnect {
        +string kind: KafkaConnect
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object authentication
        +object authentication.accessToken
        +boolean authentication.accessTokenIsJwt
        +string authentication.accessTokenLocation
        +string authentication.audience
        +object authentication.certificateAndKey
        +object authentication.clientAssertion
        +string authentication.clientAssertionLocation
        +string authentication.clientAssertionType
        +string authentication.clientId
        +object authentication.clientSecret
        +string bootstrapServers
        +object build
        +object build.output
        +array<object> build.plugins
        +object build.resources
        +string clientRackInitImage
        +object config
        +object externalConfiguration
        +array<object> externalConfiguration.env
        +array<object> externalConfiguration.volumes
        +string image
        +object jmxOptions
        +object jmxOptions.authentication
        +object jvmOptions
        +object jvmOptions.-XX
        +string jvmOptions.-Xms
        +string jvmOptions.-Xmx
        +boolean jvmOptions.gcLoggingEnabled
        +array<object> jvmOptions.javaSystemProperties
        +object livenessProbe
        +integer livenessProbe.failureThreshold
        +integer livenessProbe.initialDelaySeconds
        +integer livenessProbe.periodSeconds
        +integer livenessProbe.successThreshold
        +integer livenessProbe.timeoutSeconds
    }
    kafka_strimzi_io_KafkaConnect : <<Namespaced>>
    class kafka_strimzi_io_KafkaConnector {
        +string kind: KafkaConnector
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object alterOffsets
        +object alterOffsets.fromConfigMap
        +object autoRestart
        +boolean autoRestart.enabled
        +integer autoRestart.maxRestarts
        +string class
        +object config
        +object listOffsets
        +object listOffsets.toConfigMap
        +boolean pause
        +enum[paused|stopped|running] state
        +integer tasksMax
    }
    kafka_strimzi_io_KafkaConnector : <<Namespaced>>
    class kafka_strimzi_io_KafkaMirrorMaker2 {
        +string kind: KafkaMirrorMaker2
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +string clientRackInitImage
        +array<object> clusters
        +string connectCluster
        +object externalConfiguration
        +array<object> externalConfiguration.env
        +array<object> externalConfiguration.volumes
        +string image
        +object jmxOptions
        +object jmxOptions.authentication
        +object jvmOptions
        +object jvmOptions.-XX
        +string jvmOptions.-Xms
        +string jvmOptions.-Xmx
        +boolean jvmOptions.gcLoggingEnabled
        +array<object> jvmOptions.javaSystemProperties
        +object livenessProbe
        +integer livenessProbe.failureThreshold
        +integer livenessProbe.initialDelaySeconds
        +integer livenessProbe.periodSeconds
        +integer livenessProbe.successThreshold
        +integer livenessProbe.timeoutSeconds
        +object logging
        +object logging.loggers
        +enum[inline|external] logging.type
        +object logging.valueFrom
        +object metricsConfig
        +enum[jmxPrometheusExporter|strimziMetricsReporter] metricsConfig.type
        +object metricsConfig.valueFrom
        +object metricsConfig.values
    }
    kafka_strimzi_io_KafkaMirrorMaker2 : <<Namespaced>>
    class kafka_strimzi_io_KafkaNodePool {
        +string kind: KafkaNodePool
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object jvmOptions
        +object jvmOptions.-XX
        +string jvmOptions.-Xms
        +string jvmOptions.-Xmx
        +boolean jvmOptions.gcLoggingEnabled
        +array<object> jvmOptions.javaSystemProperties
        +integer replicas
        +object resources
        +array<object> resources.claims
        +object resources.limits
        +object resources.requests
        +array<string> roles
        +object storage
        +string storage.class
        +boolean storage.deleteClaim
        +integer storage.id
        +enum[shared] storage.kraftMetadata
        +array<object> storage.overrides
        +object storage.selector
        +string storage.size
        +string storage.sizeLimit
        +enum[ephemeral|persistent-claim|jbod] storage.type
        +array<object> storage.volumes
        +object template
        +object template.initContainer
        +object template.kafkaContainer
        +object template.perPodIngress
        +object template.perPodRoute
        +object template.perPodService
        +object template.persistentVolumeClaim
        +object template.pod
        +object template.podSet
    }
    kafka_strimzi_io_KafkaNodePool : <<Namespaced>>
    class kafka_strimzi_io_KafkaRebalance {
        +string kind: KafkaRebalance
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +array<integer> brokers
        +integer concurrentIntraBrokerPartitionMovements
        +integer concurrentLeaderMovements
        +integer concurrentPartitionMovementsPerBroker
        +string excludedTopics
        +array<string> goals
        +enum[4 values] mode
        +array<object> moveReplicasOffVolumes
        +boolean rebalanceDisk
        +array<string> replicaMovementStrategies
    }
    kafka_strimzi_io_KafkaRebalance : <<Namespaced>>
    class kafka_strimzi_io_KafkaTopic {
        +string kind: KafkaTopic
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object config
        +integer partitions
        +integer replicas
        +string topicName
    }
    kafka_strimzi_io_KafkaTopic : <<Namespaced>>
    class kafka_strimzi_io_KafkaUser {
        +string kind: KafkaUser
        +string apiVersion: kafka.strimzi.io/v1beta2
        +string scope: Namespaced
        +object authentication
        +object authentication.password
        +enum[tls|tls-external|scram-sha-512] authentication.type
        +object authorization
        +array<object> authorization.acls
        +enum[simple] authorization.type
        +object quotas
        +integer quotas.consumerByteRate
        +number quotas.controllerMutationRate
        +integer quotas.producerByteRate
        +integer quotas.requestPercentage
        +object template
        +object template.secret
    }
    kafka_strimzi_io_KafkaUser : <<Namespaced>>
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaConnector : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaConnect : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaConnect : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaConnect : similar schema
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaMirrorMaker2 : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaMirrorMaker2 : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaMirrorMaker2 : similar schema
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaRebalance : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : uses
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : configures
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : templates
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : routes to
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_Kafka : flows to
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaBridge --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_KafkaConnect : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_KafkaMirrorMaker2 : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_Kafka : configures
    kafka_strimzi_io_KafkaConnector --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaMirrorMaker2 : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaMirrorMaker2 : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaMirrorMaker2 : similar schema
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaRebalance : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : uses
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : configures
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : templates
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_Kafka : federates
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaConnect --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaNodePool : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaRebalance : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : uses
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : configures
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : templates
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_Kafka : federates
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaMirrorMaker2 --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_KafkaRebalance : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : uses
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : templates
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : federates
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_Kafka : routes to
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaNodePool --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_KafkaRebalance --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaRebalance --> kafka_strimzi_io_Kafka : references
    kafka_strimzi_io_KafkaRebalance --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_KafkaRebalance --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_Kafka --> kafka_strimzi_io_KafkaTopic : references
    kafka_strimzi_io_Kafka --> kafka_strimzi_io_KafkaTopic : uses
    kafka_strimzi_io_Kafka --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_Kafka --> kafka_strimzi_io_KafkaUser : references
    kafka_strimzi_io_Kafka --> kafka_strimzi_io_KafkaUser : templates
    kafka_strimzi_io_KafkaTopic --> kafka_strimzi_io_KafkaUser : references
```
### Detailed CRD Documentation

#### Kafka

**Full Name:** `kafkas.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** k  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kafka` | `object` | ✓ | Configuration of the Kafka cluster. |
| `clientsCa` | `object` |  | Configuration of the clients certificate authority. |
| `clusterCa` | `object` |  | Configuration of the cluster certificate authority. |
| `cruiseControl` | `object` |  | Configuration for Cruise Control deployment. Deploys a Cr... |
| `entityOperator` | `object` |  | Configuration of the Entity Operator. |
| `jmxTrans` | `object` |  | As of Strimzi 0.35.0, JMXTrans is not supported anymore a... |
| `kafkaExporter` | `object` |  | Configuration of the Kafka Exporter. Kafka Exporter can p... |
| `maintenanceTimeWindows` | `array<string>` |  | A list of time windows for maintenance tasks (that is, ce... |
| `zookeeper` | `object` |  | As of Strimzi 0.46.0, ZooKeeper-based Apache Kafka cluste... |


#### KafkaBridge

**Full Name:** `kafkabridges.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kb  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bootstrapServers` | `string` | ✓ | A list of host:port pairs for establishing the initial co... |
| `adminClient` | `object` |  | Kafka AdminClient related configuration. |
| `authentication` | `object` |  | Authentication configuration for connecting to the cluster. |
| `clientRackInitImage` | `string` |  | The image of the init container used for initializing the... |
| `consumer` | `object` |  | Kafka consumer related configuration. |
| `enableMetrics` | `boolean` |  | Enable the metrics for the Kafka Bridge. Default is false. |
| `http` | `object` |  | The HTTP related configuration. |
| `image` | `string` |  | The container image used for Kafka Bridge pods. If no ima... |
| `jvmOptions` | `object` |  | **Currently not supported** JVM Options for pods. |
| `livenessProbe` | `object` |  | Pod liveness checking. |
| `logging` | `object` |  | Logging configuration for Kafka Bridge. |
| `producer` | `object` |  | Kafka producer related configuration. |
| `rack` | `object` |  | Configuration of the node label which will be used as the... |
| `readinessProbe` | `object` |  | Pod readiness checking. |
| `replicas` | `integer` |  | The number of pods in the `Deployment`.  Defaults to `1`. |
| `resources` | `object` |  | CPU and memory resources to reserve. |
| `template` | `object` |  | Template for Kafka Bridge resources. The template allows ... |
| `tls` | `object` |  | TLS configuration for connecting Kafka Bridge to the clus... |
| `tracing` | `object` |  | The configuration of tracing in Kafka Bridge. |


#### KafkaConnect

**Full Name:** `kafkaconnects.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kc  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bootstrapServers` | `string` | ✓ | Bootstrap servers to connect to. This should be given as ... |
| `authentication` | `object` |  | Authentication configuration for Kafka Connect. |
| `build` | `object` |  | Configures how the Connect container image should be buil... |
| `clientRackInitImage` | `string` |  | The image of the init container used for initializing the... |
| `config` | `object` |  | The Kafka Connect configuration. Properties with the foll... |
| `externalConfiguration` | `object` |  | Pass data from Secrets or ConfigMaps to the Kafka Connect... |
| `image` | `string` |  | The container image used for Kafka Connect pods. If no im... |
| `jmxOptions` | `object` |  | JMX Options. |
| `jvmOptions` | `object` |  | JVM Options for pods. |
| `livenessProbe` | `object` |  | Pod liveness checking. |
| `logging` | `object` |  | Logging configuration for Kafka Connect. |
| `metricsConfig` | `object` |  | Metrics configuration. Only `jmxPrometheusExporter` can b... |
| `plugins` | `array<object>` |  | List of connector plugins to mount into the `KafkaConnect... |
| `rack` | `object` |  | Configuration of the node label which will be used as the... |
| `readinessProbe` | `object` |  | Pod readiness checking. |
| `replicas` | `integer` |  | The number of pods in the Kafka Connect group. Defaults t... |
| `resources` | `object` |  | The maximum limits for CPU and memory resources and the r... |
| `template` | `object` |  | Template for Kafka Connect and Kafka MirrorMaker 2 resour... |
| `tls` | `object` |  | TLS configuration. |
| `tracing` | `object` |  | The configuration of tracing in Kafka Connect. |

*... and 1 more properties*


#### KafkaConnector

**Full Name:** `kafkaconnectors.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kctr  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `alterOffsets` | `object` |  | Configuration for altering offsets. |
| `autoRestart` | `object` |  | Automatic restart of connector and tasks configuration. |
| `class` | `string` |  | The Class for the Kafka Connector. |
| `config` | `object` |  | The Kafka Connector configuration. The following properti... |
| `listOffsets` | `object` |  | Configuration for listing offsets. |
| `pause` | `boolean` |  | Whether the connector should be paused. Defaults to false. |
| `state` | `enum[paused|stopped|running]` |  | The state the connector should be in. Defaults to running. |
| `tasksMax` | `integer` |  | The maximum number of tasks for the Kafka Connector. |


#### KafkaMirrorMaker2

**Full Name:** `kafkamirrormaker2s.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kmm2  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `connectCluster` | `string` | ✓ | The cluster alias used for Kafka Connect. The value must ... |
| `clientRackInitImage` | `string` |  | The image of the init container used for initializing the... |
| `clusters` | `array<object>` |  | Kafka clusters for mirroring. |
| `externalConfiguration` | `object` |  | Pass data from Secrets or ConfigMaps to the Kafka Connect... |
| `image` | `string` |  | The container image used for Kafka Connect pods. If no im... |
| `jmxOptions` | `object` |  | JMX Options. |
| `jvmOptions` | `object` |  | JVM Options for pods. |
| `livenessProbe` | `object` |  | Pod liveness checking. |
| `logging` | `object` |  | Logging configuration for Kafka Connect. |
| `metricsConfig` | `object` |  | Metrics configuration. Only `jmxPrometheusExporter` can b... |
| `mirrors` | `array<object>` |  | Configuration of the MirrorMaker 2 connectors. |
| `rack` | `object` |  | Configuration of the node label which will be used as the... |
| `readinessProbe` | `object` |  | Pod readiness checking. |
| `replicas` | `integer` |  | The number of pods in the Kafka Connect group. Defaults t... |
| `resources` | `object` |  | The maximum limits for CPU and memory resources and the r... |
| `template` | `object` |  | Template for Kafka Connect and Kafka MirrorMaker 2 resour... |
| `tracing` | `object` |  | The configuration of tracing in Kafka Connect. |
| `version` | `string` |  | The Kafka Connect version. Defaults to the latest version... |


#### KafkaNodePool

**Full Name:** `kafkanodepools.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** knp  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `replicas` | `integer` | ✓ | The number of pods in the pool. |
| `roles` | `array<string>` | ✓ | The roles assigned to the node pool. Supported values are... |
| `storage` | `object` | ✓ | Storage configuration (disk). Cannot be updated. |
| `jvmOptions` | `object` |  | JVM Options for pods. |
| `resources` | `object` |  | CPU and memory resources to reserve. |
| `template` | `object` |  | Template for pool resources. The template allows users to... |


#### KafkaRebalance

**Full Name:** `kafkarebalances.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kr  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brokers` | `array<integer>` |  | The list of newly added brokers in case of scaling up or ... |
| `concurrentIntraBrokerPartitionMovements` | `integer` |  | The upper bound of ongoing partition replica movements be... |
| `concurrentLeaderMovements` | `integer` |  | The upper bound of ongoing partition leadership movements... |
| `concurrentPartitionMovementsPerBroker` | `integer` |  | The upper bound of ongoing partition replica movements go... |
| `excludedTopics` | `string` |  | A regular expression where any matching topics will be ex... |
| `goals` | `array<string>` |  | A list of goals, ordered by decreasing priority, to use f... |
| `mode` | `enum[4 values]` |  | Mode to run the rebalancing. The supported modes are `ful... |
| `moveReplicasOffVolumes` | `array<object>` |  | List of brokers and their corresponding volumes from whic... |
| `rebalanceDisk` | `boolean` |  | Enables intra-broker disk balancing, which balances disk ... |
| `replicaMovementStrategies` | `array<string>` |  | A list of strategy class names used to determine the exec... |
| `replicationThrottle` | `integer` |  | The upper bound, in bytes per second, on the bandwidth us... |
| `skipHardGoalCheck` | `boolean` |  | Whether to allow the hard goals specified in the Kafka CR... |


#### KafkaTopic

**Full Name:** `kafkatopics.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** kt  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `config` | `object` |  | The topic configuration. |
| `partitions` | `integer` |  | The number of partitions the topic should have. This cann... |
| `replicas` | `integer` |  | The number of replicas the topic should have. When absent... |
| `topicName` | `string` |  | The name of the topic. When absent this will default to t... |


#### KafkaUser

**Full Name:** `kafkausers.kafka.strimzi.io`  
**API Version:** `kafka.strimzi.io/v1beta2`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** strimzi  
**Short Names:** ku  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authentication` | `object` |  | Authentication mechanism enabled for this Kafka user. The... |
| `authorization` | `object` |  | Authorization rules for this Kafka user. |
| `quotas` | `object` |  | Quotas on requests to control the broker resources used b... |
| `template` | `object` |  | Template to specify how Kafka User `Secrets` are generated. |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `kafkabridges.kafka.strimzi.io` | `KafkaBridge` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkaconnectors.kafka.strimzi.io` | `KafkaConnector` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkaconnects.kafka.strimzi.io` | `KafkaConnect` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkamirrormaker2s.kafka.strimzi.io` | `KafkaMirrorMaker2` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkanodepools.kafka.strimzi.io` | `KafkaNodePool` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkarebalances.kafka.strimzi.io` | `KafkaRebalance` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkas.kafka.strimzi.io` | `Kafka` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkatopics.kafka.strimzi.io` | `KafkaTopic` | `kafka.strimzi.io` | Namespaced | 0 |
| `kafkausers.kafka.strimzi.io` | `KafkaUser` | `kafka.strimzi.io` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 71 |
| `string` | 18 |
| `integer` | 15 |
| `array` | 9 |
| `boolean` | 4 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `KafkaBridge` | `KafkaConnector` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaConnect` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaConnect` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaConnect` | `kafka.strimzi.io (intra-group)` | similar_schema |
| `KafkaBridge` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | similar_schema |
| `KafkaBridge` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaRebalance` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | uses |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | configures |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | templates |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | routes_to |
| `KafkaBridge` | `Kafka` | `kafka.strimzi.io (intra-group)` | flows_to |
| `KafkaBridge` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaBridge` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `KafkaConnect` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnector` | `Kafka` | `kafka.strimzi.io (intra-group)` | configures |
| `KafkaConnector` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaMirrorMaker2` | `kafka.strimzi.io (intra-group)` | similar_schema |
| `KafkaConnect` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaRebalance` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | uses |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | configures |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | templates |
| `KafkaConnect` | `Kafka` | `kafka.strimzi.io (intra-group)` | federates |
| `KafkaConnect` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaConnect` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `KafkaNodePool` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `KafkaRebalance` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | uses |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | configures |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | templates |
| `KafkaMirrorMaker2` | `Kafka` | `kafka.strimzi.io (intra-group)` | federates |
| `KafkaMirrorMaker2` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaMirrorMaker2` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `KafkaRebalance` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | uses |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | templates |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | federates |
| `KafkaNodePool` | `Kafka` | `kafka.strimzi.io (intra-group)` | routes_to |
| `KafkaNodePool` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaNodePool` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaRebalance` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaRebalance` | `Kafka` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaRebalance` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `KafkaRebalance` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `Kafka` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | references |
| `Kafka` | `KafkaTopic` | `kafka.strimzi.io (intra-group)` | uses |
| `Kafka` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `Kafka` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |
| `Kafka` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | templates |
| `KafkaTopic` | `KafkaUser` | `kafka.strimzi.io (intra-group)` | references |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:15*