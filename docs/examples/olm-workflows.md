# OLM (Operator Lifecycle Manager) Workflow Examples

This document provides comprehensive examples for managing and analyzing OLM-deployed operators using k8s-inventory-cli.

## Table of Contents

1. [Basic OLM Operations](#basic-olm-operations)
2. [ClusterServiceVersion Analysis](#clusterserviceversion-analysis)
3. [Operator Lifecycle Management](#operator-lifecycle-management)
4. [RBAC and Security Analysis](#rbac-and-security-analysis)
5. [Upgrade and Version Management](#upgrade-and-version-management)
6. [Multi-Environment OLM Management](#multi-environment-olm-management)
7. [Troubleshooting and Diagnostics](#troubleshooting-and-diagnostics)
8. [Integration with Monitoring](#integration-with-monitoring)

## Basic OLM Operations

### Discovering OLM-Managed Operators

```bash
# List all ClusterServiceVersions
k8s-inventory olm list

# List with rich formatting for better readability
k8s-inventory olm list --output rich

# Filter by installation status
k8s-inventory olm list --phase Succeeded
k8s-inventory olm list --phase Failed
k8s-inventory olm list --phase Installing

# List OLM operators in specific namespace
k8s-inventory olm list --namespace operators
```

**Expected Output:**
```
┌─────────────────────────────────────┬────────────────┬─────────────────────┬───────────┬────────────────────────────────────────┐
│ Name                                │ Namespace      │ Display Name        │ Version   │ Phase                                  │
├─────────────────────────────────────┼────────────────┼─────────────────────┼───────────┼────────────────────────────────────────┤
│ azure-service-operator.v1.0.28631   │ operators      │ Azure Service Operator │ 1.0.28631 │ Succeeded                              │
│ cloudnative-pg.v1.27.0              │ operators      │ CloudNativePG        │ 1.27.0    │ Succeeded                              │
│ mariadb-operator.v25.8.3            │ operators      │ MariaDB Operator     │ 25.8.3    │ Succeeded                              │
│ oracle-database-operator.v1.2.0     │ operators      │ Oracle DB Operator   │ 1.2.0     │ Succeeded                              │
└─────────────────────────────────────┴────────────────┴─────────────────────┴───────────┴────────────────────────────────────────┘
```

### Getting Detailed CSV Information

```bash
# Get detailed information about a specific CSV
k8s-inventory olm get azure-service-operator.v1.0.28631 --namespace operators

# Get CSV details in JSON format for processing
k8s-inventory olm get cloudnative-pg.v1.27.0 --namespace operators --output json

# Get CSV details in YAML format for human readability
k8s-inventory olm get mariadb-operator.v25.8.3 --namespace operators --output yaml
```

### OLM Statistics and Health

```bash
# Get comprehensive OLM statistics
k8s-inventory olm stats

# Get statistics with rich formatting
k8s-inventory olm stats --output rich

# Get statistics in JSON format for monitoring
k8s-inventory olm stats --output json
```

**Expected Output:**
```
╭─────────────────────────────────────────────────────── OLM Statistics ────────────────────────────────────────────────────────╮
│ Total ClusterServiceVersions: 33                                                                                               │
│ Succeeded: 29                                                                                                                  │
│ Failed: 2                                                                                                                      │
│ Installing: 2                                                                                                                  │
│                                                                                                                                │
│ Total Owned CRDs: 156                                                                                                         │
│ Total Required CRDs: 23                                                                                                       │
│                                                                                                                                │
│ Unique Providers: 12                                                                                                          │
│ Namespaces with OLM: 4                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## ClusterServiceVersion Analysis

### Analyzing CSV Metadata and Configuration

```bash
# Store current OLM state for analysis
k8s-inventory database store --notes "OLM Analysis - $(date +%Y-%m-%d)"

# Export OLM data for detailed analysis
k8s-inventory database export 1 --file olm-analysis.json

# Analyze CSV providers
echo "=== OLM Provider Analysis ==="
jq -r '.csvs[] | "\(.provider): \(.display_name) (\(.version))"' olm-analysis.json | sort | uniq -c | sort -nr

# Analyze installation strategies
echo "=== Installation Strategy Breakdown ==="
jq -r '.csvs[] | .install_strategy' olm-analysis.json | sort | uniq -c

# Find CSVs with specific capabilities
echo "=== CSVs with Full Lifecycle Management ==="
jq -r '.csvs[] | select(.spec.spec.installModes[]?.type == "AllNamespaces") | 
       "\(.name): \(.display_name) - Supports AllNamespaces"' olm-analysis.json
```

### CRD Ownership Analysis

```bash
# Analyze CRD ownership patterns
echo "=== CRD Ownership Analysis ==="

# Find CSVs with the most owned CRDs
echo "## Top CRD Owners:"
jq -r '.csvs[] | "\(.owned_crds | length) \(.name) \(.display_name)"' olm-analysis.json | 
    sort -nr | head -10

# Find CRDs managed by multiple operators
echo "## CRDs with Multiple Owners:"
jq -r '.csvs[] | .owned_crds[] as $crd | "\($crd) \(.name)"' olm-analysis.json | 
    sort | uniq | cut -d' ' -f1 | sort | uniq -d | 
    while read crd; do
        echo "CRD: $crd"
        grep "^$crd " <(jq -r '.csvs[] | .owned_crds[] as $crd | "\($crd) \(.name)"' olm-analysis.json) | 
            sed 's/^[^ ]* /  Owned by: /'
        echo
    done

# Analyze CRD dependencies  
echo "## CRD Dependencies:"
jq -r '.csvs[] | select(.required_crds | length > 0) | 
       "\(.name) requires: \(.required_crds | join(\", \"))"' olm-analysis.json
```

### CSV Resource Requirements Analysis

```bash
# Analyze resource requirements from CSV specs
echo "=== CSV Resource Requirements Analysis ==="

# Extract deployment specifications from CSVs
jq -r '.csvs[] | select(.spec.spec.install.strategy == "deployment") | 
       {name: .name, deployments: .spec.spec.install.spec.deployments[].spec.template.spec.containers[0].resources}' \
       olm-analysis.json > csv-resources.json

# Find CSVs without resource limits
echo "## CSVs without Resource Limits:"
jq -r 'select(.deployments.limits == null) | .name' csv-resources.json

# Calculate total resource requests
echo "## Total Resource Requests:"
jq -r 'select(.deployments.requests != null) | 
       "\(.name): CPU=\(.deployments.requests.cpu // "none"), Memory=\(.deployments.requests.memory // "none")"' \
       csv-resources.json

# Find high-resource CSVs
echo "## High Resource CSVs:"
jq -r 'select(.deployments.requests.memory != null) | 
       select(.deployments.requests.memory | test("Gi")) | 
       "\(.name): \(.deployments.requests.memory)"' csv-resources.json
```

## Operator Lifecycle Management

### Monitoring Operator Health

```bash
# Create OLM health monitoring script
cat > olm-health-monitor.sh << 'EOF'
#!/bin/bash
# OLM Health Monitoring Script

DATE=$(date +%Y-%m-%d-%H-%M)
LOG_FILE="olm-health-$DATE.log"

echo "=== OLM Health Check - $(date) ===" | tee $LOG_FILE

# Check overall OLM status
echo "## Overall OLM Status" | tee -a $LOG_FILE
k8s-inventory olm stats --output table | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

# Check failed CSVs
echo "## Failed ClusterServiceVersions" | tee -a $LOG_FILE
FAILED_CSVS=$(k8s-inventory olm list --phase Failed --output json)
if [ "$(echo "$FAILED_CSVS" | jq '. | length')" -gt 0 ]; then
    echo "$FAILED_CSVS" | jq -r '.[] | "❌ \(.name) in \(.namespace) - \(.phase)"' | tee -a $LOG_FILE
else
    echo "✅ No failed CSVs detected" | tee -a $LOG_FILE
fi
echo "" | tee -a $LOG_FILE

# Check installing CSVs (potential stuck installations)
echo "## Installing ClusterServiceVersions" | tee -a $LOG_FILE  
INSTALLING_CSVS=$(k8s-inventory olm list --phase Installing --output json)
if [ "$(echo "$INSTALLING_CSVS" | jq '. | length')" -gt 0 ]; then
    echo "⚠️ CSVs currently installing:" | tee -a $LOG_FILE
    echo "$INSTALLING_CSVS" | jq -r '.[] | "   \(.name) in \(.namespace)"' | tee -a $LOG_FILE
else
    echo "✅ No CSVs currently installing" | tee -a $LOG_FILE
fi
echo "" | tee -a $LOG_FILE

# Check for version mismatches
echo "## Version Consistency Check" | tee -a $LOG_FILE
k8s-inventory database export $(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id') --file current-olm.json
jq -r '.csvs[] | select(.replaces != null and .replaces != "") | 
       "Upgrade detected: \(.name) replaces \(.replaces)"' current-olm.json | tee -a $LOG_FILE

echo "Health check complete. Results saved to $LOG_FILE"
EOF

chmod +x olm-health-monitor.sh
```

### Upgrade Planning and Tracking

```bash
# Create upgrade planning workflow
cat > olm-upgrade-planner.sh << 'EOF'
#!/bin/bash
# OLM Upgrade Planning Script

UPGRADE_PLAN_FILE="olm-upgrade-plan-$(date +%Y-%m-%d).md"

echo "# OLM Upgrade Plan - $(date)" > $UPGRADE_PLAN_FILE
echo "" >> $UPGRADE_PLAN_FILE

# Store pre-upgrade snapshot
k8s-inventory database store --notes "Pre-upgrade baseline - $(date +%Y-%m-%d)"
BASELINE_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')

# Export current state
k8s-inventory database export $BASELINE_ID --file pre-upgrade-olm.json

echo "## Current OLM State" >> $UPGRADE_PLAN_FILE
echo "- Total CSVs: $(jq '.csvs | length' pre-upgrade-olm.json)" >> $UPGRADE_PLAN_FILE
echo "- Succeeded: $(jq '[.csvs[] | select(.phase == "Succeeded")] | length' pre-upgrade-olm.json)" >> $UPGRADE_PLAN_FILE
echo "- Failed: $(jq '[.csvs[] | select(.phase == "Failed")] | length' pre-upgrade-olm.json)" >> $UPGRADE_PLAN_FILE
echo "" >> $UPGRADE_PLAN_FILE

echo "## Operators Ready for Upgrade" >> $UPGRADE_PLAN_FILE
# Find CSVs that have newer versions available (based on replaces field analysis)
jq -r '.csvs[] | select(.replaces != null and .replaces != "") | 
       "- **\(.display_name)**: \(.version) (replaces: \(.replaces))"' pre-upgrade-olm.json >> $UPGRADE_PLAN_FILE
echo "" >> $UPGRADE_PLAN_FILE

echo "## Upgrade Dependencies" >> $UPGRADE_PLAN_FILE
# Analyze required CRDs for upgrade compatibility
jq -r '.csvs[] | select(.required_crds | length > 0) | 
       "- **\(.display_name)**: requires \(.required_crds | join(", "))"' pre-upgrade-olm.json >> $UPGRADE_PLAN_FILE
echo "" >> $UPGRADE_PLAN_FILE

echo "## Pre-Upgrade Checklist" >> $UPGRADE_PLAN_FILE
echo "- [ ] Backup cluster state" >> $UPGRADE_PLAN_FILE
echo "- [ ] Verify all CSVs are in Succeeded state" >> $UPGRADE_PLAN_FILE  
echo "- [ ] Check for stuck installations" >> $UPGRADE_PLAN_FILE
echo "- [ ] Review upgrade dependencies" >> $UPGRADE_PLAN_FILE
echo "- [ ] Schedule maintenance window" >> $UPGRADE_PLAN_FILE
echo "" >> $UPGRADE_PLAN_FILE

echo "Upgrade plan generated: $UPGRADE_PLAN_FILE"
echo "Baseline snapshot ID: $BASELINE_ID"
EOF

chmod +x olm-upgrade-planner.sh
```

### Post-Upgrade Verification

```bash
# Create post-upgrade verification script
cat > olm-upgrade-verify.sh << 'EOF'
#!/bin/bash
# OLM Post-Upgrade Verification Script

BASELINE_ID=${1:-$(cat .pre-upgrade-snapshot-id 2>/dev/null)}
if [ -z "$BASELINE_ID" ]; then
    echo "Error: Please provide baseline snapshot ID"
    echo "Usage: $0 <baseline_snapshot_id>"
    exit 1
fi

VERIFICATION_REPORT="olm-upgrade-verification-$(date +%Y-%m-%d).md"

echo "# OLM Upgrade Verification Report - $(date)" > $VERIFICATION_REPORT
echo "" >> $VERIFICATION_REPORT

# Store post-upgrade snapshot
k8s-inventory database store --notes "Post-upgrade verification - $(date +%Y-%m-%d)"
POST_UPGRADE_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')

# Export both snapshots
k8s-inventory database export $BASELINE_ID --file pre-upgrade.json
k8s-inventory database export $POST_UPGRADE_ID --file post-upgrade.json

echo "## Upgrade Summary" >> $VERIFICATION_REPORT
echo "- Baseline Snapshot: $BASELINE_ID" >> $VERIFICATION_REPORT
echo "- Post-Upgrade Snapshot: $POST_UPGRADE_ID" >> $VERIFICATION_REPORT
echo "" >> $VERIFICATION_REPORT

# Compare CSV counts
PRE_COUNT=$(jq '.csvs | length' pre-upgrade.json)
POST_COUNT=$(jq '.csvs | length' post-upgrade.json)
echo "## CSV Count Comparison" >> $VERIFICATION_REPORT
echo "- Pre-upgrade: $PRE_COUNT CSVs" >> $VERIFICATION_REPORT
echo "- Post-upgrade: $POST_COUNT CSVs" >> $VERIFICATION_REPORT
echo "- Change: $(($POST_COUNT - $PRE_COUNT))" >> $VERIFICATION_REPORT
echo "" >> $VERIFICATION_REPORT

# Check for failed CSVs
echo "## Failed CSVs After Upgrade" >> $VERIFICATION_REPORT
FAILED_CSVS=$(jq -r '.csvs[] | select(.phase == "Failed") | .name' post-upgrade.json)
if [ -n "$FAILED_CSVS" ]; then
    echo "⚠️ Failed CSVs detected:" >> $VERIFICATION_REPORT
    echo "$FAILED_CSVS" | while read csv; do echo "- ❌ $csv"; done >> $VERIFICATION_REPORT
else
    echo "✅ No failed CSVs detected" >> $VERIFICATION_REPORT
fi
echo "" >> $VERIFICATION_REPORT

# Check version changes
echo "## Version Changes" >> $VERIFICATION_REPORT
echo "### Upgraded CSVs" >> $VERIFICATION_REPORT
comm -13 <(jq -r '.csvs[] | "\(.name) \(.version)"' pre-upgrade.json | sort) \
         <(jq -r '.csvs[] | "\(.name) \(.version)"' post-upgrade.json | sort) | \
while read csv_version; do echo "- ✅ $csv_version"; done >> $VERIFICATION_REPORT

echo "" >> $VERIFICATION_REPORT
echo "### New CSVs Added" >> $VERIFICATION_REPORT
comm -13 <(jq -r '.csvs[].name' pre-upgrade.json | sort) \
         <(jq -r '.csvs[].name' post-upgrade.json | sort) | \
while read csv; do echo "- ➕ $csv"; done >> $VERIFICATION_REPORT

echo "" >> $VERIFICATION_REPORT
echo "### CSVs Removed" >> $VERIFICATION_REPORT
comm -23 <(jq -r '.csvs[].name' pre-upgrade.json | sort) \
         <(jq -r '.csvs[].name' post-upgrade.json | sort) | \
while read csv; do echo "- ➖ $csv"; done >> $VERIFICATION_REPORT

echo "" >> $VERIFICATION_REPORT
echo "## Verification Status" >> $VERIFICATION_REPORT
if [ -z "$FAILED_CSVS" ]; then
    echo "✅ Upgrade verification PASSED" >> $VERIFICATION_REPORT
else
    echo "⚠️ Upgrade verification REQUIRES ATTENTION" >> $VERIFICATION_REPORT
fi

echo "Verification report generated: $VERIFICATION_REPORT"
EOF

chmod +x olm-upgrade-verify.sh
```

## RBAC and Security Analysis

### Comprehensive RBAC Analysis

```bash
# Create comprehensive RBAC analysis script  
cat > olm-rbac-analyzer.sh << 'EOF'
#!/bin/bash
# OLM RBAC Analysis Script

REPORT_FILE="olm-rbac-analysis-$(date +%Y-%m-%d).md"

echo "# OLM RBAC Security Analysis - $(date)" > $REPORT_FILE
echo "" >> $REPORT_FILE

# Store current state for analysis
k8s-inventory database store --notes "RBAC Security Analysis - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $SNAPSHOT_ID --file rbac-analysis.json

echo "## Executive Summary" >> $REPORT_FILE
TOTAL_CSVS=$(jq '.csvs | length' rbac-analysis.json)
CSVS_WITH_CLUSTER_PERMS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions | length > 0)] | length' rbac-analysis.json)
echo "- Total CSVs analyzed: $TOTAL_CSVS" >> $REPORT_FILE
echo "- CSVs with cluster permissions: $CSVS_WITH_CLUSTER_PERMS" >> $REPORT_FILE
echo "- Security risk level: $([ $CSVS_WITH_CLUSTER_PERMS -gt $(($TOTAL_CSVS / 2)) ] && echo "HIGH" || echo "MODERATE")" >> $REPORT_FILE
echo "" >> $REPORT_FILE

echo "## Cluster-Level Permissions Analysis" >> $REPORT_FILE
echo "### CSVs with Cluster Permissions" >> $REPORT_FILE
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions | length > 0) | 
       "- **\(.display_name)** (\(.name)): \(.spec.spec.install.spec.clusterPermissions | length) cluster permissions"' \
       rbac-analysis.json >> $REPORT_FILE
echo "" >> $REPORT_FILE

echo "### High-Risk Permissions" >> $REPORT_FILE
echo "#### Wildcard Resource Access (*)" >> $REPORT_FILE
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | 
       "- 🚨 **\(.display_name)**: Has wildcard (*) resource access"' rbac-analysis.json >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "#### Wildcard Verb Access (*)" >> $REPORT_FILE
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*") | 
       "- 🚨 **\(.display_name)**: Has wildcard (*) verb access"' rbac-analysis.json >> $REPORT_FILE

echo "" >> $REPORT_FILE  
echo "#### Dangerous Resource Access" >> $REPORT_FILE
DANGEROUS_RESOURCES=("nodes" "persistentvolumes" "clusterroles" "clusterrolebindings" "secrets")
for resource in "${DANGEROUS_RESOURCES[@]}"; do
    echo "##### Access to $resource" >> $REPORT_FILE
    jq -r --arg res "$resource" '.csvs[] | 
           select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == $res) | 
           "- ⚠️ **\(.display_name)**: Can access \($res)"' rbac-analysis.json >> $REPORT_FILE
done

echo "" >> $REPORT_FILE
echo "## Namespace-Level Permissions Analysis" >> $REPORT_FILE
jq -r '.csvs[] | select(.spec.spec.install.spec.permissions | length > 0) | 
       "- **\(.display_name)**: \(.spec.spec.install.spec.permissions | length) namespace permissions"' \
       rbac-analysis.json >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "## Security Recommendations" >> $REPORT_FILE
echo "1. **Review Wildcard Permissions**: CSVs with wildcard access should be carefully reviewed" >> $REPORT_FILE
echo "2. **Implement Least Privilege**: Ensure operators only have necessary permissions" >> $REPORT_FILE  
echo "3. **Monitor Privilege Escalation**: Track changes in operator permissions over time" >> $REPORT_FILE
echo "4. **Audit Dangerous Resources**: Special attention to operators accessing sensitive resources" >> $REPORT_FILE
echo "5. **Regular Security Reviews**: Schedule periodic RBAC permission audits" >> $REPORT_FILE

echo "RBAC analysis complete: $REPORT_FILE"
EOF

chmod +x olm-rbac-analyzer.sh
```

### Security Context Analysis

```bash
# Analyze security contexts of OLM-managed operators
cat > olm-security-context-analyzer.sh << 'EOF'
#!/bin/bash
# OLM Security Context Analysis Script

REPORT_FILE="olm-security-contexts-$(date +%Y-%m-%d).md"

echo "# OLM Security Context Analysis - $(date)" > $REPORT_FILE
echo "" >> $REPORT_FILE

# Get current cluster state
k8s-inventory database store --notes "Security Context Analysis - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $SNAPSHOT_ID --file security-context-analysis.json

echo "## Security Context Summary" >> $REPORT_FILE

# Find operators managed by OLM (deployed via CSVs)
OLM_OPERATORS=$(jq -r '.csvs[] | .spec.spec.install.spec.deployments[]?.name' security-context-analysis.json | sort | uniq)

echo "### OLM-Managed Operators Security Analysis" >> $REPORT_FILE
while read operator; do
    if [ -n "$operator" ]; then
        echo "#### $operator" >> $REPORT_FILE
        
        # Find corresponding operator in operators list
        OPERATOR_INFO=$(jq --arg op "$operator" '.operators[] | select(.name == $op)' security-context-analysis.json)
        
        if [ "$OPERATOR_INFO" != "null" ] && [ -n "$OPERATOR_INFO" ]; then
            # Check security context
            PRIVILEGED=$(echo "$OPERATOR_INFO" | jq -r '.spec.spec.template.spec.containers[0].securityContext.privileged // false')
            RUN_AS_ROOT=$(echo "$OPERATOR_INFO" | jq -r '.spec.spec.template.spec.containers[0].securityContext.runAsUser // "not_set"')
            HOST_NETWORK=$(echo "$OPERATOR_INFO" | jq -r '.spec.spec.template.spec.hostNetwork // false')
            
            echo "- Privileged: $PRIVILEGED" >> $REPORT_FILE
            echo "- Run as root: $([ "$RUN_AS_ROOT" = "0" ] && echo "true" || echo "false ($RUN_AS_ROOT)")" >> $REPORT_FILE
            echo "- Host network: $HOST_NETWORK" >> $REPORT_FILE
            
            # Security score
            SECURITY_ISSUES=0
            [ "$PRIVILEGED" = "true" ] && ((SECURITY_ISSUES++))
            [ "$RUN_AS_ROOT" = "0" ] && ((SECURITY_ISSUES++))  
            [ "$HOST_NETWORK" = "true" ] && ((SECURITY_ISSUES++))
            
            if [ $SECURITY_ISSUES -eq 0 ]; then
                echo "- **Security Level: ✅ GOOD**" >> $REPORT_FILE
            elif [ $SECURITY_ISSUES -eq 1 ]; then
                echo "- **Security Level: ⚠️ MODERATE RISK**" >> $REPORT_FILE
            else
                echo "- **Security Level: 🚨 HIGH RISK**" >> $REPORT_FILE
            fi
        else
            echo "- **Status: Not found in operator inventory**" >> $REPORT_FILE
        fi
        echo "" >> $REPORT_FILE
    fi
done <<< "$OLM_OPERATORS"

echo "## High-Risk Security Configurations" >> $REPORT_FILE
echo "### Privileged Containers" >> $REPORT_FILE
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | 
       "- 🚨 **\(.name)** (namespace: \(.namespace)): Running privileged"' security-context-analysis.json >> $REPORT_FILE

echo "" >> $REPORT_FILE  
echo "### Host Network Access" >> $REPORT_FILE
jq -r '.operators[] | select(.spec.spec.template.spec.hostNetwork == true) | 
       "- ⚠️ **\(.name)** (namespace: \(.namespace)): Has host network access"' security-context-analysis.json >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "### Root User Execution" >> $REPORT_FILE
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.runAsUser == 0) | 
       "- ⚠️ **\(.name)** (namespace: \(.namespace)): Running as root user"' security-context-analysis.json >> $REPORT_FILE

echo "Security context analysis complete: $REPORT_FILE"
EOF

chmod +x olm-security-context-analyzer.sh
```

## Upgrade and Version Management

### Version Tracking and Analysis

```bash
# Create version tracking script
cat > olm-version-tracker.sh << 'EOF'
#!/bin/bash
# OLM Version Tracking Script

REPORT_FILE="olm-version-report-$(date +%Y-%m-%d).md"

echo "# OLM Version Tracking Report - $(date)" > $REPORT_FILE
echo "" >> $REPORT_FILE

# Store current state
k8s-inventory database store --notes "Version tracking - $(date +%Y-%m-%d)"
CURRENT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $CURRENT_ID --file current-versions.json

echo "## Current Version Inventory" >> $REPORT_FILE
echo "| Operator | Current Version | Replaces | Min Kube Version |" >> $REPORT_FILE
echo "|----------|----------------|----------|------------------|" >> $REPORT_FILE

jq -r '.csvs[] | "| \(.display_name) | \(.version) | \(.replaces // "None") | \(.min_kube_version // "Not specified") |"' \
   current-versions.json >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "## Version Management Analysis" >> $REPORT_FILE

# Check for upgrade chains
echo "### Active Upgrade Chains" >> $REPORT_FILE
jq -r '.csvs[] | select(.replaces != null and .replaces != "") | 
       "- **\(.display_name)**: \(.replaces) → \(.version)"' current-versions.json >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "### Skipped Versions" >> $REPORT_FILE
jq -r '.csvs[] | select(.skips | length > 0) | 
       "- **\(.display_name)**: skips versions \(.skips | join(\", \"))"' current-versions.json >> $REPORT_FILE

# Compare with previous snapshot if available
PREVIOUS_ID=$(k8s-inventory database list --offset 1 --limit 1 --output json | jq -r '.[0].id // empty')
if [ -n "$PREVIOUS_ID" ]; then
    echo "" >> $REPORT_FILE
    echo "## Changes Since Last Snapshot (ID: $PREVIOUS_ID)" >> $REPORT_FILE
    
    k8s-inventory database export $PREVIOUS_ID --file previous-versions.json
    
    echo "### Version Updates" >> $REPORT_FILE
    comm -13 <(jq -r '.csvs[] | "\(.name) \(.version)"' previous-versions.json | sort) \
             <(jq -r '.csvs[] | "\(.name) \(.version)"' current-versions.json | sort) | \
    while read update; do echo "- ✅ $update"; done >> $REPORT_FILE
    
    echo "" >> $REPORT_FILE
    echo "### New Operators" >> $REPORT_FILE  
    comm -13 <(jq -r '.csvs[].name' previous-versions.json | sort) \
             <(jq -r '.csvs[].name' current-versions.json | sort) | \
    while read new_op; do echo "- ➕ $new_op"; done >> $REPORT_FILE
    
    echo "" >> $REPORT_FILE
    echo "### Removed Operators" >> $REPORT_FILE
    comm -23 <(jq -r '.csvs[].name' previous-versions.json | sort) \
             <(jq -r '.csvs[].name' current-versions.json | sort) | \
    while read removed_op; do echo "- ➖ $removed_op"; done >> $REPORT_FILE
fi

echo "Version tracking report generated: $REPORT_FILE"
EOF

chmod +x olm-version-tracker.sh
```

## Multi-Environment OLM Management

### Cross-Environment OLM Comparison

```bash
# Create multi-environment OLM comparison script
cat > olm-multi-env-compare.sh << 'EOF'
#!/bin/bash
# Multi-Environment OLM Comparison Script

ENVIRONMENTS=("prod-cluster" "staging-cluster" "dev-cluster")
REPORT_FILE="olm-multi-env-comparison-$(date +%Y-%m-%d).md"

echo "# Multi-Environment OLM Comparison - $(date)" > $REPORT_FILE
echo "" >> $REPORT_FILE

# Store snapshots for each environment
declare -A ENV_SNAPSHOTS
for env in "${ENVIRONMENTS[@]}"; do
    echo "Collecting OLM data for $env..."
    k8s-inventory --context $env database store --notes "Multi-env comparison - $env - $(date +%Y-%m-%d)"
    ENV_SNAPSHOTS[$env]=$(k8s-inventory database list --cluster-context $env --limit 1 --output json | jq -r '.[0].id')
    k8s-inventory database export ${ENV_SNAPSHOTS[$env]} --file "olm-$env.json"
done

echo "## Environment Summary" >> $REPORT_FILE
echo "| Environment | Total CSVs | Succeeded | Failed | Installing |" >> $REPORT_FILE
echo "|-------------|------------|-----------|---------|------------|" >> $REPORT_FILE

for env in "${ENVIRONMENTS[@]}"; do
    TOTAL=$(jq '.csvs | length' "olm-$env.json")
    SUCCEEDED=$(jq '[.csvs[] | select(.phase == "Succeeded")] | length' "olm-$env.json")
    FAILED=$(jq '[.csvs[] | select(.phase == "Failed")] | length' "olm-$env.json")  
    INSTALLING=$(jq '[.csvs[] | select(.phase == "Installing")] | length' "olm-$env.json")
    
    echo "| $env | $TOTAL | $SUCCEEDED | $FAILED | $INSTALLING |" >> $REPORT_FILE
done

echo "" >> $REPORT_FILE
echo "## Operator Consistency Analysis" >> $REPORT_FILE

# Find operators present in all environments
echo "### Operators in All Environments" >> $REPORT_FILE
ALL_OPERATORS=""
for env in "${ENVIRONMENTS[@]}"; do
    if [ -z "$ALL_OPERATORS" ]; then
        ALL_OPERATORS=$(jq -r '.csvs[].name' "olm-$env.json" | sort)
    else
        ALL_OPERATORS=$(comm -12 <(echo "$ALL_OPERATORS") <(jq -r '.csvs[].name' "olm-$env.json" | sort))
    fi
done

while read operator; do
    if [ -n "$operator" ]; then
        echo "#### $operator" >> $REPORT_FILE
        for env in "${ENVIRONMENTS[@]}"; do
            VERSION=$(jq -r --arg op "$operator" '.csvs[] | select(.name == $op) | .version' "olm-$env.json")
            PHASE=$(jq -r --arg op "$operator" '.csvs[] | select(.name == $op) | .phase' "olm-$env.json")
            echo "- $env: $VERSION ($PHASE)" >> $REPORT_FILE
        done
        echo "" >> $REPORT_FILE
    fi
done <<< "$ALL_OPERATORS"

# Find environment-specific operators
echo "### Environment-Specific Operators" >> $REPORT_FILE
for env in "${ENVIRONMENTS[@]}"; do
    echo "#### Unique to $env" >> $REPORT_FILE
    UNIQUE_OPS=""
    OTHER_OPS=""
    
    for other_env in "${ENVIRONMENTS[@]}"; do
        if [ "$other_env" != "$env" ]; then
            OTHER_OPS="$OTHER_OPS $(jq -r '.csvs[].name' "olm-$other_env.json")"
        fi
    done
    
    jq -r '.csvs[].name' "olm-$env.json" | while read op; do
        if ! echo "$OTHER_OPS" | grep -q "$op"; then
            echo "- $op" >> $REPORT_FILE
        fi
    done
    echo "" >> $REPORT_FILE
done

echo "## Version Drift Analysis" >> $REPORT_FILE
echo "### Operators with Version Differences" >> $REPORT_FILE
while read operator; do
    if [ -n "$operator" ]; then
        VERSIONS=""
        for env in "${ENVIRONMENTS[@]}"; do
            VERSION=$(jq -r --arg op "$operator" '.csvs[] | select(.name == $op) | .version' "olm-$env.json")
            VERSIONS="$VERSIONS $VERSION"
        done
        
        # Check if all versions are the same
        UNIQUE_VERSIONS=$(echo "$VERSIONS" | tr ' ' '\n' | sort -u | wc -l)
        if [ $UNIQUE_VERSIONS -gt 1 ]; then
            echo "#### $operator" >> $REPORT_FILE
            for env in "${ENVIRONMENTS[@]}"; do
                VERSION=$(jq -r --arg op "$operator" '.csvs[] | select(.name == $op) | .version' "olm-$env.json")
                echo "- $env: $VERSION" >> $REPORT_FILE
            done
            echo "" >> $REPORT_FILE
        fi
    fi
done <<< "$ALL_OPERATORS"

# Cleanup temp files
for env in "${ENVIRONMENTS[@]}"; do
    rm "olm-$env.json"
done

echo "Multi-environment comparison complete: $REPORT_FILE"
EOF

chmod +x olm-multi-env-compare.sh
```

## Troubleshooting and Diagnostics

### OLM Troubleshooting Toolkit

```bash
# Create comprehensive OLM troubleshooting script
cat > olm-troubleshoot.sh << 'EOF'
#!/bin/bash
# OLM Troubleshooting Toolkit

ISSUE_TYPE=${1:-"general"}
OPERATOR_NAME=${2:-""}
NAMESPACE=${3:-"operators"}

REPORT_FILE="olm-troubleshoot-$(date +%Y-%m-%d-%H-%M).log"

echo "=== OLM Troubleshooting Report - $(date) ===" | tee $REPORT_FILE
echo "Issue Type: $ISSUE_TYPE" | tee -a $REPORT_FILE
echo "Operator: ${OPERATOR_NAME:-"All"}" | tee -a $REPORT_FILE
echo "Namespace: $NAMESPACE" | tee -a $REPORT_FILE
echo "" | tee -a $REPORT_FILE

case $ISSUE_TYPE in
    "stuck-install")
        echo "## Diagnosing Stuck Installation" | tee -a $REPORT_FILE
        
        # Check installing CSVs
        echo "### CSVs in Installing State" | tee -a $REPORT_FILE
        k8s-inventory olm list --phase Installing | tee -a $REPORT_FILE
        
        # Check for resource conflicts
        echo "### Checking for Resource Conflicts" | tee -a $REPORT_FILE
        if [ -n "$OPERATOR_NAME" ]; then
            CSV_INFO=$(k8s-inventory olm get "$OPERATOR_NAME" --namespace "$NAMESPACE" --output json 2>/dev/null)
            if [ $? -eq 0 ]; then
                echo "Owned CRDs:" | tee -a $REPORT_FILE
                echo "$CSV_INFO" | jq -r '.owned_crds[]? // "None"' | sed 's/^/  /' | tee -a $REPORT_FILE
                
                echo "Required CRDs:" | tee -a $REPORT_FILE  
                echo "$CSV_INFO" | jq -r '.required_crds[]? // "None"' | sed 's/^/  /' | tee -a $REPORT_FILE
            fi
        fi
        ;;
        
    "failed-csv")
        echo "## Diagnosing Failed CSV" | tee -a $REPORT_FILE
        
        # List all failed CSVs
        echo "### Failed CSVs" | tee -a $REPORT_FILE
        k8s-inventory olm list --phase Failed | tee -a $REPORT_FILE
        
        if [ -n "$OPERATOR_NAME" ]; then
            echo "### Specific CSV Analysis: $OPERATOR_NAME" | tee -a $REPORT_FILE
            CSV_DETAILS=$(k8s-inventory olm get "$OPERATOR_NAME" --namespace "$NAMESPACE" --output json 2>/dev/null)
            if [ $? -eq 0 ]; then
                echo "Display Name: $(echo "$CSV_DETAILS" | jq -r '.display_name')" | tee -a $REPORT_FILE
                echo "Version: $(echo "$CSV_DETAILS" | jq -r '.version')" | tee -a $REPORT_FILE
                echo "Provider: $(echo "$CSV_DETAILS" | jq -r '.provider')" | tee -a $REPORT_FILE
                echo "Install Strategy: $(echo "$CSV_DETAILS" | jq -r '.install_strategy')" | tee -a $REPORT_FILE
            fi
        fi
        ;;
        
    "permission-issues")
        echo "## Diagnosing Permission Issues" | tee -a $REPORT_FILE
        
        # Store current state for RBAC analysis
        k8s-inventory database store --notes "Permission troubleshooting - $(date)"
        SNAPSHOT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
        k8s-inventory database export $SNAPSHOT_ID --file troubleshoot-rbac.json
        
        if [ -n "$OPERATOR_NAME" ]; then
            echo "### RBAC Analysis for $OPERATOR_NAME" | tee -a $REPORT_FILE
            
            # Find CSV for the operator
            CSV_RBAC=$(jq --arg name "$OPERATOR_NAME" '.csvs[] | select(.name == $name or .display_name == $name)' troubleshoot-rbac.json)
            
            if [ "$CSV_RBAC" != "null" ] && [ -n "$CSV_RBAC" ]; then
                echo "Cluster Permissions:" | tee -a $REPORT_FILE
                echo "$CSV_RBAC" | jq -r '.spec.spec.install.spec.clusterPermissions[]?.rules[]? | 
                    "  - Resources: \(.resources | join(", ")) | Verbs: \(.verbs | join(", "))"' | tee -a $REPORT_FILE
                
                echo "Namespace Permissions:" | tee -a $REPORT_FILE  
                echo "$CSV_RBAC" | jq -r '.spec.spec.install.spec.permissions[]?.rules[]? | 
                    "  - Resources: \(.resources | join(", ")) | Verbs: \(.verbs | join(", "))"' | tee -a $REPORT_FILE
            else
                echo "CSV not found for operator: $OPERATOR_NAME" | tee -a $REPORT_FILE
            fi
        fi
        
        rm troubleshoot-rbac.json
        ;;
        
    "general"|*)
        echo "## General OLM Health Check" | tee -a $REPORT_FILE
        
        # Overall OLM statistics
        echo "### OLM Statistics" | tee -a $REPORT_FILE
        k8s-inventory olm stats | tee -a $REPORT_FILE
        
        # Check for problematic CSVs
        echo "### Problematic CSVs" | tee -a $REPORT_FILE
        echo "Failed CSVs:" | tee -a $REPORT_FILE
        k8s-inventory olm list --phase Failed --output table | tee -a $REPORT_FILE
        
        echo "Installing CSVs (potential stuck installations):" | tee -a $REPORT_FILE
        k8s-inventory olm list --phase Installing --output table | tee -a $REPORT_FILE
        ;;
esac

echo "" | tee -a $REPORT_FILE
echo "## Recommendations" | tee -a $REPORT_FILE

case $ISSUE_TYPE in
    "stuck-install")
        echo "1. Check if required CRDs are available in the cluster" | tee -a $REPORT_FILE
        echo "2. Verify sufficient RBAC permissions" | tee -a $REPORT_FILE
        echo "3. Check for resource conflicts with existing operators" | tee -a $REPORT_FILE
        echo "4. Review OLM operator logs for detailed error messages" | tee -a $REPORT_FILE
        ;;
    "failed-csv") 
        echo "1. Review CSV conditions for specific error messages" | tee -a $REPORT_FILE
        echo "2. Check if all required CRDs are satisfied" | tee -a $REPORT_FILE
        echo "3. Verify CSV syntax and format" | tee -a $REPORT_FILE
        echo "4. Check for conflicting CSV versions" | tee -a $REPORT_FILE
        ;;
    "permission-issues")
        echo "1. Verify ServiceAccount has necessary ClusterRole bindings" | tee -a $REPORT_FILE
        echo "2. Check for missing permissions in CSV RBAC definition" | tee -a $REPORT_FILE  
        echo "3. Review namespace-level permissions" | tee -a $REPORT_FILE
        echo "4. Consider if operator requires cluster-admin privileges" | tee -a $REPORT_FILE
        ;;
    *)
        echo "1. Monitor CSV phases for state changes" | tee -a $REPORT_FILE
        echo "2. Regular health checks with 'k8s-inventory olm stats'" | tee -a $REPORT_FILE
        echo "3. Keep snapshots for historical analysis" | tee -a $REPORT_FILE
        echo "4. Implement automated monitoring for failed CSVs" | tee -a $REPORT_FILE
        ;;
esac

echo "Troubleshooting report saved to: $REPORT_FILE"
EOF

chmod +x olm-troubleshoot.sh

# Usage examples:
# ./olm-troubleshoot.sh general
# ./olm-troubleshoot.sh stuck-install cert-manager.v1.12.0 cert-manager  
# ./olm-troubleshoot.sh failed-csv my-operator.v1.0.0 operators
# ./olm-troubleshoot.sh permission-issues cloudnative-pg.v1.27.0 operators
```

## Integration with Monitoring

### Prometheus Metrics for OLM

```bash
# Create OLM metrics exporter for Prometheus
cat > olm-metrics-exporter.sh << 'EOF'
#!/bin/bash
# OLM Metrics Exporter for Prometheus

METRICS_FILE="/var/lib/node_exporter/olm_metrics.prom"

# Store current OLM state
k8s-inventory database store --notes "Metrics collection - $(date)"
SNAPSHOT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $SNAPSHOT_ID --file metrics-olm.json

# Generate Prometheus metrics
cat > $METRICS_FILE << METRICS
# HELP olm_csvs_total Total number of ClusterServiceVersions
# TYPE olm_csvs_total gauge
olm_csvs_total $(jq '.csvs | length' metrics-olm.json)

# HELP olm_csvs_succeeded Number of succeeded CSVs
# TYPE olm_csvs_succeeded gauge  
olm_csvs_succeeded $(jq '[.csvs[] | select(.phase == "Succeeded")] | length' metrics-olm.json)

# HELP olm_csvs_failed Number of failed CSVs
# TYPE olm_csvs_failed gauge
olm_csvs_failed $(jq '[.csvs[] | select(.phase == "Failed")] | length' metrics-olm.json)

# HELP olm_csvs_installing Number of installing CSVs
# TYPE olm_csvs_installing gauge
olm_csvs_installing $(jq '[.csvs[] | select(.phase == "Installing")] | length' metrics-olm.json)

# HELP olm_owned_crds_total Total number of CRDs owned by OLM operators
# TYPE olm_owned_crds_total gauge
olm_owned_crds_total $(jq '[.csvs[].owned_crds | length] | add' metrics-olm.json)

# HELP olm_required_crds_total Total number of CRDs required by OLM operators  
# TYPE olm_required_crds_total gauge
olm_required_crds_total $(jq '[.csvs[].required_crds | length] | add' metrics-olm.json)

# HELP olm_cluster_permissions_total Total cluster permissions across all CSVs
# TYPE olm_cluster_permissions_total gauge
olm_cluster_permissions_total $(jq '[.csvs[] | .spec.spec.install.spec.clusterPermissions | length] | add' metrics-olm.json)

# HELP olm_namespace_permissions_total Total namespace permissions across all CSVs
# TYPE olm_namespace_permissions_total gauge  
olm_namespace_permissions_total $(jq '[.csvs[] | .spec.spec.install.spec.permissions | length] | add' metrics-olm.json)

# HELP olm_high_risk_csvs Number of CSVs with wildcard permissions
# TYPE olm_high_risk_csvs gauge
olm_high_risk_csvs $(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*" or .spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*")] | length' metrics-olm.json)

METRICS

echo "OLM metrics exported to $METRICS_FILE"
rm metrics-olm.json
EOF

chmod +x olm-metrics-exporter.sh
```

### Alerting Rules for OLM

```yaml
# Create Prometheus alerting rules for OLM
cat > olm-alerting-rules.yml << 'EOF'
groups:
- name: olm.rules
  rules:
  - alert: OLMCSVFailed
    expr: olm_csvs_failed > 0
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "OLM ClusterServiceVersion(s) failed"
      description: "{{ $value }} ClusterServiceVersion(s) are in Failed state"

  - alert: OLMCSVStuckInstalling  
    expr: olm_csvs_installing > 0
    for: 30m
    labels:
      severity: warning
    annotations:
      summary: "OLM ClusterServiceVersion(s) stuck installing"
      description: "{{ $value }} ClusterServiceVersion(s) have been installing for >30 minutes"

  - alert: OLMHighRiskPermissions
    expr: olm_high_risk_csvs > 0
    for: 0m
    labels:
      severity: critical
    annotations:
      summary: "OLM operators with high-risk permissions detected"
      description: "{{ $value }} ClusterServiceVersion(s) have wildcard (*) permissions"

  - alert: OLMCSVCountChanged
    expr: abs(delta(olm_csvs_total[1h])) > 0
    for: 0m  
    labels:
      severity: info
    annotations:
      summary: "OLM ClusterServiceVersion count changed"
      description: "Number of CSVs changed by {{ $value }} in the last hour"
EOF
```

This comprehensive collection of OLM examples provides:

1. **Basic Operations**: Discovery, analysis, and health monitoring
2. **Advanced Analysis**: RBAC security, resource requirements, and CRD ownership  
3. **Lifecycle Management**: Upgrade planning, verification, and version tracking
4. **Security**: Permission analysis and security context evaluation
5. **Multi-Environment**: Cross-environment comparison and consistency checking
6. **Troubleshooting**: Diagnostic tools for common OLM issues
7. **Monitoring**: Prometheus metrics and alerting integration

These examples enable comprehensive OLM management with the k8s-inventory-cli tool, supporting enterprise-grade operator lifecycle management workflows.
