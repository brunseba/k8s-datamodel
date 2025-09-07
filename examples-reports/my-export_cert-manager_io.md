# CRD Schema Documentation - cert-manager.io API Group

> **Generated:** 2025-09-07 17:05:14
> 
> **Total CRDs:** 4
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [cert-manager.io](#certmanagerio) (4 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **4 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 4 |
| **API Groups** | 1 |
| **Total Instances** | 16 |
| **Namespaced CRDs** | 3 (75.0%) |
| **Cluster-scoped CRDs** | 1 (25.0%) |
| **Schema Coverage** | 4/4 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **cert-manager.io**: 4 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `Certificate` (cert-manager.io): 21 properties
2. `CertificateRequest` (cert-manager.io): 9 properties
3. `ClusterIssuer` (cert-manager.io): 5 properties


## 📁 cert-manager.io

### Overview

**API Group:** `cert-manager.io`  
**CRDs in Group:** 4  
**Total Instances:** 16

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `Certificate` | Namespaced | v1 | 6 | *No description available* |
| `CertificateRequest` | Namespaced | v1 | 6 | *No description available* |
| `ClusterIssuer` | Cluster | v1 | 0 | *No description available* |
| `Issuer` | Namespaced | v1 | 4 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: cert-manager.io
    class cert_manager_io_Certificate {
        +string kind: Certificate
        +string apiVersion: cert-manager.io/v1
        +string scope: Namespaced
        +array<object> additionalOutputFormats
        +string commonName
        +array<string> dnsNames
        +string duration
        +array<string> emailAddresses
        +boolean encodeUsagesInRequest
        +array<string> ipAddresses
        +boolean isCA
        +object issuerRef
        +string issuerRef.group
        +string issuerRef.kind
        +string issuerRef.name
        +object keystores
        +object keystores.jks
        +object keystores.pkcs12
    }
    cert_manager_io_Certificate : <<Namespaced>>
    note for cert_manager_io_Certificate : 6 instances
    class cert_manager_io_CertificateRequest {
        +string kind: CertificateRequest
        +string apiVersion: cert-manager.io/v1
        +string scope: Namespaced
        +string duration
        +object extra
        +array<string> groups
        +boolean isCA
        +object issuerRef
        +string issuerRef.group
        +string issuerRef.kind
        +string issuerRef.name
        +string(byte) request
        +string uid
        +array<string> usages
        +string username
    }
    cert_manager_io_CertificateRequest : <<Namespaced>>
    note for cert_manager_io_CertificateRequest : 6 instances
    class cert_manager_io_ClusterIssuer {
        +string kind: ClusterIssuer
        +string apiVersion: cert-manager.io/v1
        +string scope: Cluster
        +object acme
        +string(byte) acme.caBundle
        +boolean acme.disableAccountKeyGeneration
        +string acme.email
        +boolean acme.enableDurationFeature
        +object acme.externalAccountBinding
        +string acme.preferredChain
        +object acme.privateKeySecretRef
        +string acme.server
        +boolean acme.skipTLSVerify
        +array<object> acme.solvers
        +object ca
        +array<string> ca.crlDistributionPoints
        +array<string> ca.issuingCertificateURLs
        +array<string> ca.ocspServers
        +string ca.secretName
        +object selfSigned
        +array<string> selfSigned.crlDistributionPoints
        +object vault
        +object vault.auth
        +string(byte) vault.caBundle
        +object vault.caBundleSecretRef
        +object vault.clientCertSecretRef
        +object vault.clientKeySecretRef
        +string vault.namespace
        +string vault.path
        +string vault.server
        +object venafi
        +object venafi.cloud
        +object venafi.tpp
        +string venafi.zone
    }
    cert_manager_io_ClusterIssuer : <<Cluster>>
    class cert_manager_io_Issuer {
        +string kind: Issuer
        +string apiVersion: cert-manager.io/v1
        +string scope: Namespaced
        +object acme
        +string(byte) acme.caBundle
        +boolean acme.disableAccountKeyGeneration
        +string acme.email
        +boolean acme.enableDurationFeature
        +object acme.externalAccountBinding
        +string acme.preferredChain
        +object acme.privateKeySecretRef
        +string acme.server
        +boolean acme.skipTLSVerify
        +array<object> acme.solvers
        +object ca
        +array<string> ca.crlDistributionPoints
        +array<string> ca.issuingCertificateURLs
        +array<string> ca.ocspServers
        +string ca.secretName
        +object selfSigned
        +array<string> selfSigned.crlDistributionPoints
        +object vault
        +object vault.auth
        +string(byte) vault.caBundle
        +object vault.caBundleSecretRef
        +object vault.clientCertSecretRef
        +object vault.clientKeySecretRef
        +string vault.namespace
        +string vault.path
        +string vault.server
        +object venafi
        +object venafi.cloud
        +object venafi.tpp
        +string venafi.zone
    }
    cert_manager_io_Issuer : <<Namespaced>>
    note for cert_manager_io_Issuer : 4 instances
    cert_manager_io_CertificateRequest --> cert_manager_io_Certificate : references
    cert_manager_io_CertificateRequest --> cert_manager_io_Certificate : references
    cert_manager_io_CertificateRequest --> cert_manager_io_ClusterIssuer : references
    cert_manager_io_CertificateRequest --> cert_manager_io_ClusterIssuer : references
    cert_manager_io_CertificateRequest --> cert_manager_io_Issuer : references
    cert_manager_io_CertificateRequest --> cert_manager_io_Issuer : references
    cert_manager_io_CertificateRequest --> cert_manager_io_Issuer : uses
    cert_manager_io_Certificate --> cert_manager_io_ClusterIssuer : references
    cert_manager_io_Certificate --> cert_manager_io_ClusterIssuer : references
    cert_manager_io_Certificate --> cert_manager_io_ClusterIssuer : uses
    cert_manager_io_Certificate --> cert_manager_io_ClusterIssuer : routes to
    cert_manager_io_Certificate --> cert_manager_io_Issuer : references
    cert_manager_io_Certificate --> cert_manager_io_Issuer : references
    cert_manager_io_Certificate --> cert_manager_io_Issuer : uses
    cert_manager_io_Certificate --> cert_manager_io_Issuer : routes to
    cert_manager_io_ClusterIssuer --> cert_manager_io_Issuer : references
    cert_manager_io_ClusterIssuer --> cert_manager_io_Issuer : references
    cert_manager_io_ClusterIssuer --> cert_manager_io_Issuer : similar schema
```
### Detailed CRD Documentation

#### Certificate

**Full Name:** `certificates.cert-manager.io`  
**API Version:** `cert-manager.io/v1`  
**Scope:** Namespaced  
**Instances:** 6  
**Categories:** cert-manager  
**Short Names:** cert, certs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `issuerRef` | `object` | ✓ | Reference to the issuer responsible for issuing the certi... |
| `secretName` | `string` | ✓ | Name of the Secret resource that will be automatically cr... |
| `additionalOutputFormats` | `array<object>` |  | Defines extra output formats of the private key and signe... |
| `commonName` | `string` |  | Requested common name X509 certificate subject attribute.... |
| `dnsNames` | `array<string>` |  | Requested DNS subject alternative names. |
| `duration` | `string` |  | Requested 'duration' (i.e. lifetime) of the Certificate. ... |
| `emailAddresses` | `array<string>` |  | Requested email subject alternative names. |
| `encodeUsagesInRequest` | `boolean` |  | Whether the KeyUsage and ExtKeyUsage extensions should be... |
| `ipAddresses` | `array<string>` |  | Requested IP address subject alternative names. |
| `isCA` | `boolean` |  | Requested basic constraints isCA value.
The isCA value is... |
| `keystores` | `object` |  | Additional keystore output formats to be stored in the Ce... |
| `literalSubject` | `string` |  | Requested X.509 certificate subject, represented using th... |
| `nameConstraints` | `object` |  | x.509 certificate NameConstraint extension which MUST NOT... |
| `otherNames` | `array<object>` |  | `otherNames` is an escape hatch for SAN that allows any t... |
| `privateKey` | `object` |  | Private key options. These include the key algorithm and ... |
| `renewBefore` | `string` |  | How long before the currently issued certificate's expiry... |
| `revisionHistoryLimit` | `integer(int32)` |  | The maximum number of CertificateRequest revisions that a... |
| `secretTemplate` | `object` |  | Defines annotations and labels to be copied to the Certif... |
| `subject` | `object` |  | Requested set of X509 certificate subject attributes.
Mor... |
| `uris` | `array<string>` |  | Requested URI subject alternative names. |

*... and 1 more properties*


#### CertificateRequest

**Full Name:** `certificaterequests.cert-manager.io`  
**API Version:** `cert-manager.io/v1`  
**Scope:** Namespaced  
**Instances:** 6  
**Categories:** cert-manager  
**Short Names:** cr, crs  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `issuerRef` | `object` | ✓ | Reference to the issuer responsible for issuing the certi... |
| `request` | `string(byte)` | ✓ | The PEM-encoded X.509 certificate signing request to be s... |
| `duration` | `string` |  | Requested 'duration' (i.e. lifetime) of the Certificate. ... |
| `extra` | `object` |  | Extra contains extra attributes of the user that created ... |
| `groups` | `array<string>` |  | Groups contains group membership of the user that created... |
| `isCA` | `boolean` |  | Requested basic constraints isCA value. Note that the iss... |
| `uid` | `string` |  | UID contains the uid of the user that created the Certifi... |
| `usages` | `array<string>` |  | Requested key usages and extended key usages.


NOTE: If ... |
| `username` | `string` |  | Username contains the name of the user that created the C... |


#### ClusterIssuer

**Full Name:** `clusterissuers.cert-manager.io`  
**API Version:** `cert-manager.io/v1`  
**Scope:** Cluster  
**Instances:** 0  
**Categories:** cert-manager  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `acme` | `object` |  | ACME configures this issuer to communicate with a RFC8555... |
| `ca` | `object` |  | CA configures this issuer to sign certificates using a si... |
| `selfSigned` | `object` |  | SelfSigned configures this issuer to 'self sign' certific... |
| `vault` | `object` |  | Vault configures this issuer to sign certificates using a... |
| `venafi` | `object` |  | Venafi configures this issuer to sign certificates using ... |


#### Issuer

**Full Name:** `issuers.cert-manager.io`  
**API Version:** `cert-manager.io/v1`  
**Scope:** Namespaced  
**Instances:** 4  
**Categories:** cert-manager  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `acme` | `object` |  | ACME configures this issuer to communicate with a RFC8555... |
| `ca` | `object` |  | CA configures this issuer to sign certificates using a si... |
| `selfSigned` | `object` |  | SelfSigned configures this issuer to 'self sign' certific... |
| `vault` | `object` |  | Vault configures this issuer to sign certificates using a... |
| `venafi` | `object` |  | Venafi configures this issuer to sign certificates using ... |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `certificaterequests.cert-manager.io` | `CertificateRequest` | `cert-manager.io` | Namespaced | 6 |
| `certificates.cert-manager.io` | `Certificate` | `cert-manager.io` | Namespaced | 6 |
| `clusterissuers.cert-manager.io` | `ClusterIssuer` | `cert-manager.io` | Cluster | 0 |
| `issuers.cert-manager.io` | `Issuer` | `cert-manager.io` | Namespaced | 4 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `object` | 18 |
| `string` | 9 |
| `array` | 9 |
| `boolean` | 3 |
| `integer` | 1 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `CertificateRequest` | `Certificate` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `Certificate` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `ClusterIssuer` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `ClusterIssuer` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `CertificateRequest` | `Issuer` | `cert-manager.io (intra-group)` | uses |
| `Certificate` | `ClusterIssuer` | `cert-manager.io (intra-group)` | references |
| `Certificate` | `ClusterIssuer` | `cert-manager.io (intra-group)` | references |
| `Certificate` | `ClusterIssuer` | `cert-manager.io (intra-group)` | uses |
| `Certificate` | `ClusterIssuer` | `cert-manager.io (intra-group)` | routes_to |
| `Certificate` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `Certificate` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `Certificate` | `Issuer` | `cert-manager.io (intra-group)` | uses |
| `Certificate` | `Issuer` | `cert-manager.io (intra-group)` | routes_to |
| `ClusterIssuer` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `ClusterIssuer` | `Issuer` | `cert-manager.io (intra-group)` | references |
| `ClusterIssuer` | `Issuer` | `cert-manager.io (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:14*