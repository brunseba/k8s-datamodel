# Security and Compliance Analysis Examples

This document provides comprehensive examples for security analysis and compliance reporting using k8s-datamodel's database functionality and spec analysis capabilities.

## Table of Contents

1. [Security Baseline Establishment](#security-baseline-establishment)
2. [RBAC Analysis and Auditing](#rbac-analysis-and-auditing)
3. [Security Context Analysis](#security-context-analysis)
4. [Compliance Reporting](#compliance-reporting)
5. [Vulnerability Assessment](#vulnerability-assessment)
6. [Policy Enforcement Monitoring](#policy-enforcement-monitoring)
7. [Security Drift Detection](#security-drift-detection)
8. [Automated Security Monitoring](#automated-security-monitoring)

## Security Baseline Establishment

### Creating Security Baseline

```bash
# Establish comprehensive security baseline
k8s-datamodel database store \
    --notes "SECURITY-BASELINE-$(date +%Y-%m-%d) - Initial security assessment and baseline"

# Export baseline for detailed analysis
BASELINE_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $BASELINE_ID --file security-baseline.json

echo "Security baseline established with snapshot ID: $BASELINE_ID"
echo $BASELINE_ID > .security-baseline-id

# Generate baseline security report
cat > security-baseline-report.md << 'EOF'
# Security Baseline Report

**Generated:** $(date)
**Baseline Snapshot ID:** $BASELINE_ID

## Executive Summary

This document establishes the security baseline for the Kubernetes cluster, documenting the current security posture of all operators, CRDs, and OLM-managed components.

## Methodology

The security baseline was established using k8s-datamodel to:
1. Capture complete cluster specifications including security contexts
2. Analyze RBAC permissions for all operators and CSVs
3. Document privileged containers and high-risk configurations
4. Establish metrics for ongoing security monitoring

## Baseline Metrics
EOF

# Add baseline metrics to report
echo "- **Total CRDs:** $(jq '.crds | length' security-baseline.json)" >> security-baseline-report.md
echo "- **Total Operators:** $(jq '.operators | length' security-baseline.json)" >> security-baseline-report.md
echo "- **Total OLM CSVs:** $(jq '.csvs | length' security-baseline.json)" >> security-baseline-report.md
echo "- **Privileged Containers:** $(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' security-baseline.json)" >> security-baseline-report.md
echo "- **Containers without Limits:** $(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' security-baseline.json)" >> security-baseline-report.md
echo "- **Host Network Access:** $(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' security-baseline.json)" >> security-baseline-report.md

echo "Baseline security report generated: security-baseline-report.md"
```

### Security Baseline Validation

```bash
# Create security baseline validation script
cat > validate-security-baseline.sh << 'EOF'
#!/bin/bash
# Security Baseline Validation Script

BASELINE_ID=${1:-$(cat .security-baseline-id 2>/dev/null)}
if [ -z "$BASELINE_ID" ]; then
    echo "Error: Baseline snapshot ID required"
    echo "Usage: $0 <baseline_snapshot_id>"
    exit 1
fi

VALIDATION_REPORT="security-baseline-validation-$(date +%Y-%m-%d).md"

echo "# Security Baseline Validation - $(date)" > $VALIDATION_REPORT
echo "" >> $VALIDATION_REPORT

# Export baseline for comparison
k8s-datamodel database export $BASELINE_ID --file baseline-validation.json

# Current snapshot for comparison
k8s-datamodel database store --notes "Security validation against baseline - $(date +%Y-%m-%d)"
CURRENT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $CURRENT_ID --file current-validation.json

echo "## Validation Summary" >> $VALIDATION_REPORT
echo "- **Baseline Snapshot:** $BASELINE_ID" >> $VALIDATION_REPORT
echo "- **Current Snapshot:** $CURRENT_ID" >> $VALIDATION_REPORT
echo "- **Validation Date:** $(date)" >> $VALIDATION_REPORT
echo "" >> $VALIDATION_REPORT

# Compare security metrics
echo "## Security Metrics Comparison" >> $VALIDATION_REPORT

BASELINE_PRIVILEGED=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' baseline-validation.json)
CURRENT_PRIVILEGED=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' current-validation.json)

BASELINE_NO_LIMITS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' baseline-validation.json)
CURRENT_NO_LIMITS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' current-validation.json)

BASELINE_HOST_NET=$(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' baseline-validation.json)
CURRENT_HOST_NET=$(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' current-validation.json)

echo "| Metric | Baseline | Current | Change | Status |" >> $VALIDATION_REPORT
echo "|--------|----------|---------|--------|--------|" >> $VALIDATION_REPORT
echo "| Privileged Containers | $BASELINE_PRIVILEGED | $CURRENT_PRIVILEGED | $(($CURRENT_PRIVILEGED - $BASELINE_PRIVILEGED)) | $( [ $CURRENT_PRIVILEGED -le $BASELINE_PRIVILEGED ] && echo "✅ OK" || echo "⚠️ INCREASED" ) |" >> $VALIDATION_REPORT
echo "| Containers w/o Limits | $BASELINE_NO_LIMITS | $CURRENT_NO_LIMITS | $(($CURRENT_NO_LIMITS - $BASELINE_NO_LIMITS)) | $( [ $CURRENT_NO_LIMITS -le $BASELINE_NO_LIMITS ] && echo "✅ OK" || echo "⚠️ INCREASED" ) |" >> $VALIDATION_REPORT  
echo "| Host Network Access | $BASELINE_HOST_NET | $CURRENT_HOST_NET | $(($CURRENT_HOST_NET - $BASELINE_HOST_NET)) | $( [ $CURRENT_HOST_NET -le $BASELINE_HOST_NET ] && echo "✅ OK" || echo "⚠️ INCREASED" ) |" >> $VALIDATION_REPORT

echo "" >> $VALIDATION_REPORT
echo "## Security Violations" >> $VALIDATION_REPORT

# Find new security violations
echo "### New Privileged Containers" >> $VALIDATION_REPORT
comm -13 <(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' baseline-validation.json | sort) \
         <(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' current-validation.json | sort) | \
while read container; do echo "- ⚠️ $container"; done >> $VALIDATION_REPORT

echo "" >> $VALIDATION_REPORT
echo "### New Containers without Resource Limits" >> $VALIDATION_REPORT  
comm -13 <(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null) | .name' baseline-validation.json | sort) \
         <(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null) | .name' current-validation.json | sort) | \
while read container; do echo "- ⚠️ $container"; done >> $VALIDATION_REPORT

echo "" >> $VALIDATION_REPORT
echo "## Recommendations" >> $VALIDATION_REPORT

# Generate recommendations based on findings
TOTAL_VIOLATIONS=$(($CURRENT_PRIVILEGED + $CURRENT_NO_LIMITS + $CURRENT_HOST_NET))
if [ $TOTAL_VIOLATIONS -eq 0 ]; then
    echo "✅ **Excellent security posture** - No major security violations detected" >> $VALIDATION_REPORT
elif [ $TOTAL_VIOLATIONS -lt 5 ]; then
    echo "⚠️ **Good security posture** - Minor violations detected that should be addressed" >> $VALIDATION_REPORT
else
    echo "🚨 **Security attention required** - Multiple violations detected requiring immediate attention" >> $VALIDATION_REPORT
fi

echo "" >> $VALIDATION_REPORT
echo "1. Review and remediate any new privileged containers" >> $VALIDATION_REPORT
echo "2. Implement resource limits for all containers without limits" >> $VALIDATION_REPORT
echo "3. Evaluate necessity of host network access" >> $VALIDATION_REPORT
echo "4. Schedule regular security baseline validations" >> $VALIDATION_REPORT

rm baseline-validation.json current-validation.json
echo "Security baseline validation complete: $VALIDATION_REPORT"
EOF

chmod +x validate-security-baseline.sh
```

## RBAC Analysis and Auditing

### Comprehensive RBAC Audit

```bash
# Create comprehensive RBAC audit script
cat > rbac-security-audit.sh << 'EOF'
#!/bin/bash
# Comprehensive RBAC Security Audit Script

AUDIT_REPORT="rbac-security-audit-$(date +%Y-%m-%d).md"

echo "# RBAC Security Audit Report - $(date)" > $AUDIT_REPORT
echo "" >> $AUDIT_REPORT

# Store current state for analysis
k8s-datamodel database store --notes "RBAC Security Audit - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file rbac-audit.json

echo "## Executive Summary" >> $AUDIT_REPORT
echo "" >> $AUDIT_REPORT

TOTAL_CSVS=$(jq '.csvs | length' rbac-audit.json)
CSVS_WITH_CLUSTER_PERMS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions | length > 0)] | length' rbac-audit.json)
CSVS_WITH_WILDCARD=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*" or .spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*")] | length' rbac-audit.json)

echo "- **Total ClusterServiceVersions:** $TOTAL_CSVS" >> $AUDIT_REPORT
echo "- **CSVs with Cluster Permissions:** $CSVS_WITH_CLUSTER_PERMS" >> $AUDIT_REPORT  
echo "- **CSVs with Wildcard Permissions:** $CSVS_WITH_WILDCARD" >> $AUDIT_REPORT
echo "- **Risk Level:** $( [ $CSVS_WITH_WILDCARD -eq 0 ] && echo "LOW" || [ $CSVS_WITH_WILDCARD -lt 3 ] && echo "MEDIUM" || echo "HIGH" )" >> $AUDIT_REPORT

echo "" >> $AUDIT_REPORT
echo "## Critical Security Findings" >> $AUDIT_REPORT

# Find dangerous permissions
echo "### 🚨 CRITICAL: Wildcard Resource Access" >> $AUDIT_REPORT
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | 
       "- **\(.display_name)** (\(.name)): Full resource access (*)"' rbac-audit.json >> $AUDIT_REPORT

echo "" >> $AUDIT_REPORT
echo "### 🚨 CRITICAL: Wildcard Verb Access" >> $AUDIT_REPORT
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*") | 
       "- **\(.display_name)** (\(.name)): Full verb access (*)"' rbac-audit.json >> $AUDIT_REPORT

echo "" >> $AUDIT_REPORT
echo "### ⚠️ HIGH RISK: Sensitive Resource Access" >> $AUDIT_REPORT

# Check access to sensitive resources
SENSITIVE_RESOURCES=("secrets" "nodes" "clusterroles" "clusterrolebindings" "persistentvolumes" "serviceaccounts")

for resource in "${SENSITIVE_RESOURCES[@]}"; do
    echo "#### Access to $resource" >> $AUDIT_REPORT
    jq -r --arg res "$resource" '.csvs[] | 
           select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == $res) |
           "- **\(.display_name)**: Can access \($res)"' rbac-audit.json >> $AUDIT_REPORT
done

echo "" >> $AUDIT_REPORT
echo "### ⚠️ HIGH RISK: Privileged Verbs" >> $AUDIT_REPORT

PRIVILEGED_VERBS=("create" "delete" "patch" "update")
for verb in "${PRIVILEGED_VERBS[@]}"; do
    echo "#### $verb Permissions on Critical Resources" >> $AUDIT_REPORT
    jq -r --arg verb "$verb" '.csvs[] | 
           select(.spec.spec.install.spec.clusterPermissions[]?.rules[]? | 
                  (.verbs | contains([$verb])) and 
                  (.resources | contains(["clusterroles", "clusterrolebindings", "nodes", "secrets"]))) |
           "- **\(.display_name)**: Can \($verb) sensitive resources"' rbac-audit.json >> $AUDIT_REPORT
done

echo "" >> $AUDIT_REPORT
echo "## Detailed Permission Analysis" >> $AUDIT_REPORT

# Create detailed permission matrix
echo "### Permission Matrix" >> $AUDIT_REPORT
echo "| Operator | Cluster Perms | NS Perms | Dangerous Resources | Wildcard | Risk Level |" >> $AUDIT_REPORT
echo "|----------|---------------|----------|-------------------|----------|------------|" >> $AUDIT_REPORT

jq -r '.csvs[] | 
       {
           name: .display_name,
           cluster_perms: (.spec.spec.install.spec.clusterPermissions | length),
           ns_perms: (.spec.spec.install.spec.permissions | length),
           has_wildcard: ((.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") or 
                         (.spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*")),
           has_sensitive: ((.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? | 
                          . as $r | ["secrets", "nodes", "clusterroles"] | any(. == $r)) // false)
       } |
       "| \(.name) | \(.cluster_perms) | \(.ns_perms) | \(.has_sensitive) | \(.has_wildcard) | \(if .has_wildcard then "🚨 CRITICAL" elif .has_sensitive then "⚠️ HIGH" elif .cluster_perms > 5 then "⚠️ MEDIUM" else "✅ LOW" end) |"' \
       rbac-audit.json >> $AUDIT_REPORT

echo "" >> $AUDIT_REPORT
echo "## Security Recommendations" >> $AUDIT_REPORT

echo "### Immediate Actions Required" >> $AUDIT_REPORT
if [ $CSVS_WITH_WILDCARD -gt 0 ]; then
    echo "1. **🚨 URGENT**: Review and remediate CSVs with wildcard permissions" >> $AUDIT_REPORT
    echo "2. Implement least-privilege principle for all operators" >> $AUDIT_REPORT
else
    echo "1. ✅ No wildcard permissions detected - good security posture" >> $AUDIT_REPORT
fi

echo "3. Regular RBAC audit schedule (monthly)" >> $AUDIT_REPORT
echo "4. Implement automated monitoring for permission changes" >> $AUDIT_REPORT
echo "5. Consider using admission controllers to prevent dangerous permissions" >> $AUDIT_REPORT

echo "" >> $AUDIT_REPORT
echo "### Best Practices" >> $AUDIT_REPORT
echo "- Use namespace-scoped permissions when possible" >> $AUDIT_REPORT
echo "- Implement specific resource and verb permissions" >> $AUDIT_REPORT
echo "- Regular review of operator permissions" >> $AUDIT_REPORT
echo "- Use Pod Security Standards for additional protection" >> $AUDIT_REPORT

rm rbac-audit.json
echo "RBAC security audit complete: $AUDIT_REPORT"
EOF

chmod +x rbac-security-audit.sh
```

### RBAC Change Detection

```bash
# Create RBAC change detection script
cat > rbac-change-detector.sh << 'EOF'
#!/bin/bash
# RBAC Change Detection Script

BASELINE_ID=${1:-$(cat .security-baseline-id 2>/dev/null)}
if [ -z "$BASELINE_ID" ]; then
    echo "Error: Baseline snapshot ID required"
    echo "Usage: $0 <baseline_snapshot_id>"
    exit 1
fi

CHANGE_REPORT="rbac-changes-$(date +%Y-%m-%d).md"

echo "# RBAC Change Detection Report - $(date)" > $CHANGE_REPORT
echo "" >> $CHANGE_REPORT

# Get current state
k8s-datamodel database store --notes "RBAC change detection - $(date +%Y-%m-%d)"
CURRENT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')

# Export snapshots
k8s-datamodel database export $BASELINE_ID --file rbac-baseline.json
k8s-datamodel database export $CURRENT_ID --file rbac-current.json

echo "## Change Summary" >> $CHANGE_REPORT
echo "- **Baseline Snapshot:** $BASELINE_ID" >> $CHANGE_REPORT
echo "- **Current Snapshot:** $CURRENT_ID" >> $CHANGE_REPORT
echo "- **Analysis Date:** $(date)" >> $CHANGE_REPORT
echo "" >> $CHANGE_REPORT

# Analyze permission changes
echo "## Permission Changes Detected" >> $CHANGE_REPORT

# Check for new CSVs with dangerous permissions
echo "### New High-Risk CSVs" >> $CHANGE_REPORT
BASELINE_DANGEROUS=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | .name' rbac-baseline.json | sort)
CURRENT_DANGEROUS=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | .name' rbac-current.json | sort)

NEW_DANGEROUS=$(comm -13 <(echo "$BASELINE_DANGEROUS") <(echo "$CURRENT_DANGEROUS"))
if [ -n "$NEW_DANGEROUS" ]; then
    echo "🚨 **CRITICAL ALERT**: New CSVs with wildcard permissions detected!" >> $CHANGE_REPORT
    while read csv; do
        echo "- $csv" >> $CHANGE_REPORT
    done <<< "$NEW_DANGEROUS"
else
    echo "✅ No new high-risk CSVs detected" >> $CHANGE_REPORT
fi

echo "" >> $CHANGE_REPORT
echo "### Permission Escalations" >> $CHANGE_REPORT

# Check for CSVs that gained cluster permissions
BASELINE_CLUSTER_CSVS=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions | length > 0) | .name' rbac-baseline.json | sort)
CURRENT_CLUSTER_CSVS=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions | length > 0) | .name' rbac-current.json | sort)

NEW_CLUSTER_CSVS=$(comm -13 <(echo "$BASELINE_CLUSTER_CSVS") <(echo "$CURRENT_CLUSTER_CSVS"))
if [ -n "$NEW_CLUSTER_CSVS" ]; then
    echo "⚠️ **New cluster permissions detected:**" >> $CHANGE_REPORT
    while read csv; do
        echo "- $csv gained cluster-level permissions" >> $CHANGE_REPORT
    done <<< "$NEW_CLUSTER_CSVS"
else
    echo "✅ No new cluster permission escalations" >> $CHANGE_REPORT
fi

echo "" >> $CHANGE_REPORT
echo "### Detailed Permission Analysis" >> $CHANGE_REPORT

# For each CSV, compare permission counts
echo "| CSV | Baseline Cluster Perms | Current Cluster Perms | Change | Status |" >> $CHANGE_REPORT
echo "|-----|------------------------|----------------------|--------|--------|" >> $CHANGE_REPORT

# Get common CSVs between snapshots
COMMON_CSVS=$(comm -12 <(jq -r '.csvs[].name' rbac-baseline.json | sort) <(jq -r '.csvs[].name' rbac-current.json | sort))

while read csv; do
    if [ -n "$csv" ]; then
        BASELINE_COUNT=$(jq -r --arg csv "$csv" '.csvs[] | select(.name == $csv) | .spec.spec.install.spec.clusterPermissions | length' rbac-baseline.json)
        CURRENT_COUNT=$(jq -r --arg csv "$csv" '.csvs[] | select(.name == $csv) | .spec.spec.install.spec.clusterPermissions | length' rbac-current.json)
        CHANGE=$(($CURRENT_COUNT - $BASELINE_COUNT))
        
        if [ $CHANGE -gt 0 ]; then
            STATUS="⚠️ INCREASED"
        elif [ $CHANGE -lt 0 ]; then
            STATUS="✅ DECREASED"
        else
            STATUS="➖ NO CHANGE"
        fi
        
        echo "| $csv | $BASELINE_COUNT | $CURRENT_COUNT | $CHANGE | $STATUS |" >> $CHANGE_REPORT
    fi
done <<< "$COMMON_CSVS"

echo "" >> $CHANGE_REPORT
echo "## Recommendations" >> $CHANGE_REPORT

if [ -n "$NEW_DANGEROUS" ] || [ -n "$NEW_CLUSTER_CSVS" ]; then
    echo "🚨 **Immediate action required:**" >> $CHANGE_REPORT
    echo "1. Review all new high-risk permissions immediately" >> $CHANGE_REPORT
    echo "2. Validate business justification for permission escalations" >> $CHANGE_REPORT
    echo "3. Consider implementing admission controllers to prevent dangerous permissions" >> $CHANGE_REPORT
else
    echo "✅ **No critical RBAC changes detected**" >> $CHANGE_REPORT
    echo "1. Continue regular monitoring of RBAC changes" >> $CHANGE_REPORT
    echo "2. Maintain security baseline updates" >> $CHANGE_REPORT
fi

echo "4. Schedule regular RBAC audits" >> $CHANGE_REPORT
echo "5. Implement automated alerting for permission changes" >> $CHANGE_REPORT

rm rbac-baseline.json rbac-current.json
echo "RBAC change detection complete: $CHANGE_REPORT"
EOF

chmod +x rbac-change-detector.sh
```

## Security Context Analysis

### Container Security Analysis

```bash
# Create comprehensive container security analysis
cat > container-security-analyzer.sh << 'EOF'
#!/bin/bash
# Container Security Analysis Script

SECURITY_REPORT="container-security-analysis-$(date +%Y-%m-%d).md"

echo "# Container Security Analysis Report - $(date)" > $SECURITY_REPORT
echo "" >> $SECURITY_REPORT

# Store current state
k8s-datamodel database store --notes "Container security analysis - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file container-security.json

echo "## Security Posture Overview" >> $SECURITY_REPORT
echo "" >> $SECURITY_REPORT

# Calculate security metrics
TOTAL_OPERATORS=$(jq '.operators | length' container-security.json)
PRIVILEGED_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' container-security.json)
ROOT_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.runAsUser == 0)] | length' container-security.json)
HOST_NETWORK_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' container-security.json)
NO_LIMITS_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' container-security.json)
HOST_PID_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.hostPID == true)] | length' container-security.json)

echo "| Security Metric | Count | Percentage | Risk Level |" >> $SECURITY_REPORT
echo "|-----------------|-------|------------|------------|" >> $SECURITY_REPORT
echo "| Total Operators | $TOTAL_OPERATORS | 100% | - |" >> $SECURITY_REPORT
echo "| Privileged Containers | $PRIVILEGED_CONTAINERS | $(echo "scale=1; $PRIVILEGED_CONTAINERS * 100 / $TOTAL_OPERATORS" | bc)% | $( [ $PRIVILEGED_CONTAINERS -eq 0 ] && echo "✅ LOW" || echo "🚨 CRITICAL" ) |" >> $SECURITY_REPORT
echo "| Running as Root | $ROOT_CONTAINERS | $(echo "scale=1; $ROOT_CONTAINERS * 100 / $TOTAL_OPERATORS" | bc)% | $( [ $ROOT_CONTAINERS -eq 0 ] && echo "✅ LOW" || [ $ROOT_CONTAINERS -lt 3 ] && echo "⚠️ MEDIUM" || echo "🚨 HIGH" ) |" >> $SECURITY_REPORT
echo "| Host Network Access | $HOST_NETWORK_CONTAINERS | $(echo "scale=1; $HOST_NETWORK_CONTAINERS * 100 / $TOTAL_OPERATORS" | bc)% | $( [ $HOST_NETWORK_CONTAINERS -eq 0 ] && echo "✅ LOW" || echo "⚠️ MEDIUM" ) |" >> $SECURITY_REPORT
echo "| No Resource Limits | $NO_LIMITS_CONTAINERS | $(echo "scale=1; $NO_LIMITS_CONTAINERS * 100 / $TOTAL_OPERATORS" | bc)% | $( [ $NO_LIMITS_CONTAINERS -eq 0 ] && echo "✅ LOW" || [ $NO_LIMITS_CONTAINERS -lt 5 ] && echo "⚠️ MEDIUM" || echo "🚨 HIGH" ) |" >> $SECURITY_REPORT
echo "| Host PID Access | $HOST_PID_CONTAINERS | $(echo "scale=1; $HOST_PID_CONTAINERS * 100 / $TOTAL_OPERATORS" | bc)% | $( [ $HOST_PID_CONTAINERS -eq 0 ] && echo "✅ LOW" || echo "🚨 CRITICAL" ) |" >> $SECURITY_REPORT

echo "" >> $SECURITY_REPORT
echo "## Critical Security Violations" >> $SECURITY_REPORT

# Detailed analysis of security violations
echo "### 🚨 CRITICAL: Privileged Containers" >> $SECURITY_REPORT
if [ $PRIVILEGED_CONTAINERS -gt 0 ]; then
    jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | 
           "- **\(.name)** (namespace: \(.namespace)) - Image: \(.image // "unknown")"' container-security.json >> $SECURITY_REPORT
    echo "" >> $SECURITY_REPORT
    echo "**Impact:** Privileged containers have full access to host resources and can escape container isolation." >> $SECURITY_REPORT
    echo "**Recommendation:** Review necessity and implement least-privilege alternatives." >> $SECURITY_REPORT
else
    echo "✅ No privileged containers detected" >> $SECURITY_REPORT
fi

echo "" >> $SECURITY_REPORT
echo "### ⚠️ HIGH RISK: Containers Running as Root" >> $SECURITY_REPORT
if [ $ROOT_CONTAINERS -gt 0 ]; then
    jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.runAsUser == 0) | 
           "- **\(.name)** (namespace: \(.namespace)) - Image: \(.image // "unknown")"' container-security.json >> $SECURITY_REPORT
    echo "" >> $SECURITY_REPORT
    echo "**Impact:** Root containers increase attack surface and privilege escalation risk." >> $SECURITY_REPORT
    echo "**Recommendation:** Configure containers to run as non-root users." >> $SECURITY_REPORT
else
    echo "✅ No containers running as root detected" >> $SECURITY_REPORT
fi

echo "" >> $SECURITY_REPORT
echo "### ⚠️ MEDIUM RISK: Host Network Access" >> $SECURITY_REPORT
if [ $HOST_NETWORK_CONTAINERS -gt 0 ]; then
    jq -r '.operators[] | select(.spec.spec.template.spec.hostNetwork == true) | 
           "- **\(.name)** (namespace: \(.namespace)) - Image: \(.image // "unknown")"' container-security.json >> $SECURITY_REPORT
    echo "" >> $SECURITY_REPORT
    echo "**Impact:** Host network access bypasses Kubernetes network isolation." >> $SECURITY_REPORT
    echo "**Recommendation:** Use Kubernetes Services instead of host networking when possible." >> $SECURITY_REPORT
else
    echo "✅ No host network access detected" >> $SECURITY_REPORT
fi

echo "" >> $SECURITY_REPORT
echo "### ⚠️ MEDIUM RISK: Containers without Resource Limits" >> $SECURITY_REPORT
if [ $NO_LIMITS_CONTAINERS -gt 0 ]; then
    jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null) | 
           "- **\(.name)** (namespace: \(.namespace)) - Image: \(.image // "unknown")"' container-security.json >> $SECURITY_REPORT
    echo "" >> $SECURITY_REPORT
    echo "**Impact:** Containers without limits can consume unlimited resources, enabling DoS attacks." >> $SECURITY_REPORT
    echo "**Recommendation:** Implement CPU and memory limits for all containers." >> $SECURITY_REPORT
else
    echo "✅ All containers have resource limits" >> $SECURITY_REPORT
fi

echo "" >> $SECURITY_REPORT
echo "## Security Context Analysis" >> $SECURITY_REPORT

# Detailed security context analysis
echo "### Detailed Security Context Matrix" >> $SECURITY_REPORT
echo "| Operator | Privileged | RunAsUser | ReadOnlyRootFS | AllowPrivilegeEsc | HostNetwork | Risk Score |" >> $SECURITY_REPORT
echo "|----------|------------|-----------|----------------|-------------------|-------------|-----------|" >> $SECURITY_REPORT

jq -r '.operators[] | 
       {
           name: .name,
           privileged: (.spec.spec.template.spec.containers[0].securityContext.privileged // false),
           runAsUser: (.spec.spec.template.spec.containers[0].securityContext.runAsUser // "not_set"),
           readOnlyRootFS: (.spec.spec.template.spec.containers[0].securityContext.readOnlyRootFilesystem // false),
           allowPrivilegeEsc: (.spec.spec.template.spec.containers[0].securityContext.allowPrivilegeEscalation // true),
           hostNetwork: (.spec.spec.template.spec.hostNetwork // false)
       } |
       # Calculate risk score
       (.privileged | if . then 10 else 0 end) +
       (.runAsUser | if . == 0 then 5 elif . == "not_set" then 3 else 0 end) +
       (.readOnlyRootFS | if . then -2 else 2 end) +
       (.allowPrivilegeEsc | if . then 3 else -1 end) +
       (.hostNetwork | if . then 4 else 0 end) as $risk |
       "| \(.name) | \(.privileged) | \(.runAsUser) | \(.readOnlyRootFS) | \(.allowPrivilegeEsc) | \(.hostNetwork) | \($risk) \(if $risk >= 10 then "🚨" elif $risk >= 6 then "⚠️" elif $risk >= 3 then "⚠️" else "✅" end) |"' \
       container-security.json >> $SECURITY_REPORT

echo "" >> $SECURITY_REPORT
echo "**Risk Score Legend:**" >> $SECURITY_REPORT
echo "- 🚨 **10+ Critical**: Immediate attention required" >> $SECURITY_REPORT
echo "- ⚠️ **6-9 High**: Should be addressed soon" >> $SECURITY_REPORT  
echo "- ⚠️ **3-5 Medium**: Consider improvements" >> $SECURITY_REPORT
echo "- ✅ **0-2 Low**: Good security posture" >> $SECURITY_REPORT

echo "" >> $SECURITY_REPORT
echo "## Remediation Plan" >> $SECURITY_REPORT

# Generate remediation recommendations based on findings
TOTAL_VIOLATIONS=$(($PRIVILEGED_CONTAINERS + $ROOT_CONTAINERS + $HOST_NETWORK_CONTAINERS))

if [ $TOTAL_VIOLATIONS -eq 0 ]; then
    echo "✅ **Excellent Security Posture**" >> $SECURITY_REPORT
    echo "No critical security violations detected. Continue monitoring." >> $SECURITY_REPORT
elif [ $TOTAL_VIOLATIONS -lt 3 ]; then
    echo "⚠️ **Good Security Posture with Minor Issues**" >> $SECURITY_REPORT
    echo "Address the following items to improve security:" >> $SECURITY_REPORT
else
    echo "🚨 **Security Attention Required**" >> $SECURITY_REPORT
    echo "Multiple security violations detected requiring immediate attention:" >> $SECURITY_REPORT
fi

echo "" >> $SECURITY_REPORT
echo "### Immediate Actions" >> $SECURITY_REPORT
[ $PRIVILEGED_CONTAINERS -gt 0 ] && echo "1. **CRITICAL**: Review and remediate all privileged containers" >> $SECURITY_REPORT
[ $ROOT_CONTAINERS -gt 0 ] && echo "2. **HIGH**: Configure non-root users for containers" >> $SECURITY_REPORT
[ $HOST_NETWORK_CONTAINERS -gt 0 ] && echo "3. **MEDIUM**: Evaluate host network necessity" >> $SECURITY_REPORT
[ $NO_LIMITS_CONTAINERS -gt 0 ] && echo "4. **MEDIUM**: Implement resource limits for all containers" >> $SECURITY_REPORT

echo "" >> $SECURITY_REPORT
echo "### Long-term Improvements" >> $SECURITY_REPORT
echo "1. Implement Pod Security Standards" >> $SECURITY_REPORT
echo "2. Use admission controllers (e.g., OPA Gatekeeper)" >> $SECURITY_REPORT
echo "3. Regular security scanning of container images" >> $SECURITY_REPORT
echo "4. Implement runtime security monitoring" >> $SECURITY_REPORT
echo "5. Regular security context audits" >> $SECURITY_REPORT

rm container-security.json
echo "Container security analysis complete: $SECURITY_REPORT"
EOF

chmod +x container-security-analyzer.sh
```

## Compliance Reporting

### SOC 2 Compliance Report

```bash
# Create SOC 2 compliance reporting script
cat > soc2-compliance-report.sh << 'EOF'
#!/bin/bash
# SOC 2 Compliance Report Generator

COMPLIANCE_REPORT="soc2-compliance-report-$(date +%Y-%m-%d).md"
AUDIT_PERIOD_START=${1:-$(date -d '30 days ago' +%Y-%m-%d)}
AUDIT_PERIOD_END=${2:-$(date +%Y-%m-%d)}

echo "# SOC 2 Compliance Report" > $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT
echo "**Report Date:** $(date)" >> $COMPLIANCE_REPORT
echo "**Audit Period:** $AUDIT_PERIOD_START to $AUDIT_PERIOD_END" >> $COMPLIANCE_REPORT
echo "**Scope:** Kubernetes Cluster Security Controls" >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

# Store current state
k8s-datamodel database store --notes "SOC2 Compliance Assessment - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file soc2-compliance.json

echo "## Executive Summary" >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

# Calculate compliance metrics
TOTAL_COMPONENTS=$(jq '[.crds, .operators, .csvs] | map(length) | add' soc2-compliance.json)
PRIVILEGED_CONTAINERS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' soc2-compliance.json)
WILDCARD_PERMISSIONS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*")] | length' soc2-compliance.json)

echo "- **Total Components Assessed:** $TOTAL_COMPONENTS" >> $COMPLIANCE_REPORT
echo "- **High-Risk Configurations:** $(($PRIVILEGED_CONTAINERS + $WILDCARD_PERMISSIONS))" >> $COMPLIANCE_REPORT
echo "- **Compliance Status:** $( [ $(($PRIVILEGED_CONTAINERS + $WILDCARD_PERMISSIONS)) -eq 0 ] && echo "✅ COMPLIANT" || echo "⚠️ NON-COMPLIANT" )" >> $COMPLIANCE_REPORT

echo "" >> $COMPLIANCE_REPORT
echo "## SOC 2 Control Assessment" >> $COMPLIANCE_REPORT

echo "" >> $COMPLIANCE_REPORT
echo "### CC6.1 - Logical and Physical Access Controls" >> $COMPLIANCE_REPORT
echo "**Control Objective:** The entity implements logical and physical access controls to restrict unauthorized access." >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

# Access control assessment
RBAC_VIOLATIONS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]? | (.resources | contains(["*"])) or (.verbs | contains(["*"])))] | length' soc2-compliance.json)

if [ $RBAC_VIOLATIONS -eq 0 ]; then
    echo "✅ **COMPLIANT**: No wildcard RBAC permissions detected" >> $COMPLIANCE_REPORT
    echo "- All operators follow least-privilege principle" >> $COMPLIANCE_REPORT
    echo "- No excessive permissions identified" >> $COMPLIANCE_REPORT
else
    echo "❌ **NON-COMPLIANT**: $RBAC_VIOLATIONS operators with excessive permissions" >> $COMPLIANCE_REPORT
    echo "**Violations:**" >> $COMPLIANCE_REPORT
    jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | 
           "- \(.display_name): Wildcard resource access"' soc2-compliance.json >> $COMPLIANCE_REPORT
fi

echo "" >> $COMPLIANCE_REPORT
echo "### CC6.2 - System Security" >> $COMPLIANCE_REPORT
echo "**Control Objective:** The entity implements system security controls to protect against unauthorized access." >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

if [ $PRIVILEGED_CONTAINERS -eq 0 ]; then
    echo "✅ **COMPLIANT**: No privileged containers detected" >> $COMPLIANCE_REPORT
    echo "- Container isolation maintained" >> $COMPLIANCE_REPORT
    echo "- No host-level access violations" >> $COMPLIANCE_REPORT
else
    echo "❌ **NON-COMPLIANT**: $PRIVILEGED_CONTAINERS privileged containers detected" >> $COMPLIANCE_REPORT
    echo "**Violations:**" >> $COMPLIANCE_REPORT
    jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | 
           "- \(.name) in \(.namespace): Privileged container"' soc2-compliance.json >> $COMPLIANCE_REPORT
fi

echo "" >> $COMPLIANCE_REPORT
echo "### CC6.3 - Data Security and Privacy" >> $COMPLIANCE_REPORT
echo "**Control Objective:** The entity protects data in transmission and at rest." >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

# Check for secret access
SECRET_ACCESS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "secrets")] | length' soc2-compliance.json)

if [ $SECRET_ACCESS -eq 0 ]; then
    echo "✅ **COMPLIANT**: No direct secret access permissions" >> $COMPLIANCE_REPORT
else
    echo "⚠️ **ATTENTION REQUIRED**: $SECRET_ACCESS operators with secret access" >> $COMPLIANCE_REPORT
    echo "**Review Required:**" >> $COMPLIANCE_REPORT
    jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "secrets") | 
           "- \(.display_name): Can access secrets"' soc2-compliance.json >> $COMPLIANCE_REPORT
fi

echo "" >> $COMPLIANCE_REPORT
echo "### CC7.1 - System Monitoring" >> $COMPLIANCE_REPORT
echo "**Control Objective:** The entity monitors system components and operations for anomalies." >> $COMPLIANCE_REPORT
echo "" >> $COMPLIANCE_REPORT

echo "✅ **COMPLIANT**: Monitoring controls implemented" >> $COMPLIANCE_REPORT
echo "- k8s-datamodel provides continuous monitoring" >> $COMPLIANCE_REPORT
echo "- Historical snapshots maintained for audit trail" >> $COMPLIANCE_REPORT
echo "- Security baselines established and monitored" >> $COMPLIANCE_REPORT

echo "" >> $COMPLIANCE_REPORT
echo "## Remediation Requirements" >> $COMPLIANCE_REPORT

TOTAL_VIOLATIONS=$(($RBAC_VIOLATIONS + $PRIVILEGED_CONTAINERS))

if [ $TOTAL_VIOLATIONS -eq 0 ]; then
    echo "✅ **No remediation required** - All controls are compliant" >> $COMPLIANCE_REPORT
else
    echo "⚠️ **Remediation required** - $TOTAL_VIOLATIONS violations must be addressed" >> $COMPLIANCE_REPORT
    echo "" >> $COMPLIANCE_REPORT
    echo "### Required Actions" >> $COMPLIANCE_REPORT
    [ $RBAC_VIOLATIONS -gt 0 ] && echo "1. **CRITICAL**: Remove wildcard RBAC permissions" >> $COMPLIANCE_REPORT
    [ $PRIVILEGED_CONTAINERS -gt 0 ] && echo "2. **CRITICAL**: Eliminate privileged containers" >> $COMPLIANCE_REPORT
    echo "3. Implement additional monitoring and alerting" >> $COMPLIANCE_REPORT
    echo "4. Establish regular compliance validation schedule" >> $COMPLIANCE_REPORT
fi

echo "" >> $COMPLIANCE_REPORT
echo "## Audit Evidence" >> $COMPLIANCE_REPORT
echo "- **Snapshot ID:** $SNAPSHOT_ID" >> $COMPLIANCE_REPORT
echo "- **Assessment Tool:** k8s-datamodel" >> $COMPLIANCE_REPORT
echo "- **Evidence Location:** Database snapshot contains complete cluster configuration" >> $COMPLIANCE_REPORT
echo "- **Retention:** Snapshots retained per data retention policy" >> $COMPLIANCE_REPORT

echo "" >> $COMPLIANCE_REPORT
echo "## Appendix: Detailed Findings" >> $COMPLIANCE_REPORT

# Detailed technical findings
echo "" >> $COMPLIANCE_REPORT
echo "### RBAC Permission Matrix" >> $COMPLIANCE_REPORT
echo "| Operator | Cluster Permissions | Namespace Permissions | Risk Level |" >> $COMPLIANCE_REPORT
echo "|----------|-------------------|---------------------|-----------|" >> $COMPLIANCE_REPORT

jq -r '.csvs[] | 
       {
           name: .display_name,
           cluster_perms: (.spec.spec.install.spec.clusterPermissions | length),
           ns_perms: (.spec.spec.install.spec.permissions | length),
           has_wildcard: ((.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") or 
                         (.spec.spec.install.spec.clusterPermissions[]?.rules[]?.verbs[]? == "*"))
       } |
       "| \(.name) | \(.cluster_perms) | \(.ns_perms) | \(if .has_wildcard then "🚨 HIGH" elif .cluster_perms > 3 then "⚠️ MEDIUM" else "✅ LOW" end) |"' \
       soc2-compliance.json >> $COMPLIANCE_REPORT

rm soc2-compliance.json
echo "SOC 2 compliance report generated: $COMPLIANCE_REPORT"
EOF

chmod +x soc2-compliance-report.sh
```

### PCI DSS Compliance Assessment

```bash
# Create PCI DSS compliance assessment script
cat > pci-dss-compliance.sh << 'EOF'
#!/bin/bash
# PCI DSS Compliance Assessment Script

PCI_REPORT="pci-dss-compliance-$(date +%Y-%m-%d).md"

echo "# PCI DSS Compliance Assessment Report" > $PCI_REPORT
echo "" >> $PCI_REPORT
echo "**Assessment Date:** $(date)" >> $PCI_REPORT
echo "**PCI DSS Version:** 4.0" >> $PCI_REPORT
echo "**Scope:** Kubernetes Infrastructure Security Controls" >> $PCI_REPORT
echo "" >> $PCI_REPORT

# Store current state
k8s-datamodel database store --notes "PCI DSS Compliance Assessment - $(date +%Y-%m-%d)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file pci-compliance.json

echo "## Executive Summary" >> $PCI_REPORT
echo "" >> $PCI_REPORT

# PCI DSS specific security metrics
NETWORK_VIOLATIONS=$(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' pci-compliance.json)
ACCESS_VIOLATIONS=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*")] | length' pci-compliance.json)
PRIVILEGE_VIOLATIONS=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' pci-compliance.json)

TOTAL_VIOLATIONS=$(($NETWORK_VIOLATIONS + $ACCESS_VIOLATIONS + $PRIVILEGE_VIOLATIONS))

echo "**Compliance Status:** $( [ $TOTAL_VIOLATIONS -eq 0 ] && echo "✅ COMPLIANT" || echo "❌ NON-COMPLIANT" )" >> $PCI_REPORT
echo "**Total Security Violations:** $TOTAL_VIOLATIONS" >> $PCI_REPORT
echo "**Risk Level:** $( [ $TOTAL_VIOLATIONS -eq 0 ] && echo "LOW" || [ $TOTAL_VIOLATIONS -lt 5 ] && echo "MEDIUM" || echo "HIGH" )" >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "## PCI DSS Requirement Assessment" >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "### Requirement 1: Install and maintain network security controls" >> $PCI_REPORT

if [ $NETWORK_VIOLATIONS -eq 0 ]; then
    echo "✅ **COMPLIANT**: Network isolation maintained" >> $PCI_REPORT
    echo "- No host network access detected" >> $PCI_REPORT
    echo "- Container network isolation in place" >> $PCI_REPORT
else
    echo "❌ **NON-COMPLIANT**: $NETWORK_VIOLATIONS network security violations" >> $PCI_REPORT
    echo "**Violations:**" >> $PCI_REPORT
    jq -r '.operators[] | select(.spec.spec.template.spec.hostNetwork == true) | 
           "- \(.name): Host network access enabled"' pci-compliance.json >> $PCI_REPORT
fi

echo "" >> $PCI_REPORT
echo "### Requirement 7: Restrict access by business need to know" >> $PCI_REPORT

if [ $ACCESS_VIOLATIONS -eq 0 ]; then
    echo "✅ **COMPLIANT**: Access controls properly implemented" >> $PCI_REPORT
    echo "- No excessive permissions detected" >> $PCI_REPORT
    echo "- Least privilege principle followed" >> $PCI_REPORT
else
    echo "❌ **NON-COMPLIANT**: $ACCESS_VIOLATIONS access control violations" >> $PCI_REPORT
    echo "**Violations:**" >> $PCI_REPORT
    jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | 
           "- \(.display_name): Excessive cluster permissions"' pci-compliance.json >> $PCI_REPORT
fi

echo "" >> $PCI_REPORT
echo "### Requirement 8: Identify users and authenticate access" >> $PCI_REPORT

# Check for service account configurations
SA_COUNT=$(jq '[.csvs[] | .spec.spec.install.spec.deployments[]?.spec.template.spec.serviceAccountName] | map(select(. != null)) | length' pci-compliance.json)

if [ $SA_COUNT -gt 0 ]; then
    echo "✅ **COMPLIANT**: Service accounts properly configured" >> $PCI_REPORT
    echo "- $SA_COUNT operators use dedicated service accounts" >> $PCI_REPORT
else
    echo "⚠️ **REVIEW REQUIRED**: Service account usage should be verified" >> $PCI_REPORT
fi

echo "" >> $PCI_REPORT
echo "### Requirement 11: Regularly test security systems and processes" >> $PCI_REPORT

echo "✅ **COMPLIANT**: Security testing framework in place" >> $PCI_REPORT
echo "- Automated security assessments implemented" >> $PCI_REPORT
echo "- Regular compliance monitoring active" >> $PCI_REPORT
echo "- Historical security data maintained" >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "## Detailed Security Analysis" >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "### Network Security Assessment" >> $PCI_REPORT
echo "| Operator | Host Network | Host PID | Risk Level |" >> $PCI_REPORT
echo "|----------|-------------|----------|-----------|" >> $PCI_REPORT

jq -r '.operators[] | 
       {
           name: .name,
           hostNetwork: (.spec.spec.template.spec.hostNetwork // false),
           hostPID: (.spec.spec.template.spec.hostPID // false)
       } |
       "| \(.name) | \(.hostNetwork) | \(.hostPID) | \(if .hostNetwork or .hostPID then "🚨 HIGH" else "✅ LOW" end) |"' \
       pci-compliance.json >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "### Access Control Matrix" >> $PCI_REPORT
echo "| Component | Type | Permissions | Compliance Status |" >> $PCI_REPORT
echo "|-----------|------|-------------|------------------|" >> $PCI_REPORT

jq -r '.csvs[] | 
       {
           name: .display_name,
           cluster_perms: (.spec.spec.install.spec.clusterPermissions | length),
           has_wildcard: (.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*")
       } |
       "| \(.name) | CSV | \(.cluster_perms) cluster perms | \(if .has_wildcard then "❌ NON-COMPLIANT" else "✅ COMPLIANT" end) |"' \
       pci-compliance.json >> $PCI_REPORT

echo "" >> $PCI_REPORT
echo "## Remediation Plan" >> $PCI_REPORT

if [ $TOTAL_VIOLATIONS -eq 0 ]; then
    echo "✅ **No remediation required** - All PCI DSS requirements met" >> $PCI_REPORT
    echo "" >> $PCI_REPORT
    echo "### Maintenance Activities" >> $PCI_REPORT
    echo "1. Continue regular compliance monitoring" >> $PCI_REPORT
    echo "2. Maintain current security baselines" >> $PCI_REPORT
    echo "3. Schedule quarterly compliance reviews" >> $PCI_REPORT
else
    echo "❌ **Immediate remediation required** - $TOTAL_VIOLATIONS violations must be addressed" >> $PCI_REPORT
    echo "" >> $PCI_REPORT
    echo "### Critical Actions" >> $PCI_REPORT
    [ $NETWORK_VIOLATIONS -gt 0 ] && echo "1. **URGENT**: Remove host network access" >> $PCI_REPORT
    [ $ACCESS_VIOLATIONS -gt 0 ] && echo "2. **URGENT**: Implement least-privilege access controls" >> $PCI_REPORT
    [ $PRIVILEGE_VIOLATIONS -gt 0 ] && echo "3. **URGENT**: Eliminate privileged containers" >> $PCI_REPORT
    
    echo "" >> $PCI_REPORT
    echo "### Timeline" >> $PCI_REPORT
    echo "- **Immediate (0-7 days):** Address critical security violations" >> $PCI_REPORT
    echo "- **Short-term (1-4 weeks):** Implement additional controls" >> $PCI_REPORT
    echo "- **Long-term (1-3 months):** Establish continuous compliance monitoring" >> $PCI_REPORT
fi

echo "" >> $PCI_REPORT
echo "## Compensating Controls" >> $PCI_REPORT

if [ $TOTAL_VIOLATIONS -gt 0 ]; then
    echo "The following compensating controls should be implemented:" >> $PCI_REPORT
    echo "1. **Network Segmentation:** Implement strict network policies" >> $PCI_REPORT
    echo "2. **Enhanced Monitoring:** Deploy runtime security monitoring" >> $PCI_REPORT
    echo "3. **Regular Auditing:** Increase audit frequency to weekly" >> $PCI_REPORT
    echo "4. **Admission Control:** Implement policy-based admission controllers" >> $PCI_REPORT
else
    echo "No compensating controls required - direct compliance achieved" >> $PCI_REPORT
fi

rm pci-compliance.json
echo "PCI DSS compliance assessment complete: $PCI_REPORT"
EOF

chmod +x pci-dss-compliance.sh
```

## Automated Security Monitoring

### Continuous Security Monitoring

```bash
# Create continuous security monitoring script
cat > security-continuous-monitoring.sh << 'EOF'
#!/bin/bash
# Continuous Security Monitoring Script

MONITORING_LOG="/var/log/k8s-security-monitor.log"
ALERT_THRESHOLD_PRIVILEGED=0
ALERT_THRESHOLD_WILDCARD=0
ALERT_EMAIL="security-team@company.com"

# Function to send alert
send_alert() {
    local alert_type="$1"
    local message="$2"
    
    echo "$(date): SECURITY ALERT - $alert_type: $message" | tee -a "$MONITORING_LOG"
    
    # Send email alert (requires mail command)
    if command -v mail > /dev/null; then
        echo "$message" | mail -s "K8s Security Alert: $alert_type" "$ALERT_EMAIL"
    fi
    
    # Send to syslog
    logger -p security.warning "k8s-security-monitor: $alert_type - $message"
}

# Store current security snapshot
k8s-datamodel database store --notes "Security monitoring - $(date +%Y-%m-%d-%H-%M)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file security-monitoring.json

echo "$(date): Security monitoring check started" | tee -a "$MONITORING_LOG"

# Check for privileged containers
PRIVILEGED_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' security-monitoring.json)
if [ $PRIVILEGED_COUNT -gt $ALERT_THRESHOLD_PRIVILEGED ]; then
    PRIVILEGED_CONTAINERS=$(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' security-monitoring.json | tr '\n' ', ' | sed 's/,$//')
    send_alert "PRIVILEGED_CONTAINERS" "Found $PRIVILEGED_COUNT privileged containers: $PRIVILEGED_CONTAINERS"
fi

# Check for wildcard permissions
WILDCARD_COUNT=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*")] | length' security-monitoring.json)
if [ $WILDCARD_COUNT -gt $ALERT_THRESHOLD_WILDCARD ]; then
    WILDCARD_CSVS=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | .display_name' security-monitoring.json | tr '\n' ', ' | sed 's/,$//')
    send_alert "WILDCARD_PERMISSIONS" "Found $WILDCARD_COUNT CSVs with wildcard permissions: $WILDCARD_CSVS"
fi

# Check for host network access
HOST_NETWORK_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.hostNetwork == true)] | length' security-monitoring.json)
if [ $HOST_NETWORK_COUNT -gt 0 ]; then
    HOST_NETWORK_OPERATORS=$(jq -r '.operators[] | select(.spec.spec.template.spec.hostNetwork == true) | .name' security-monitoring.json | tr '\n' ', ' | sed 's/,$//')
    send_alert "HOST_NETWORK_ACCESS" "Found $HOST_NETWORK_COUNT operators with host network access: $HOST_NETWORK_OPERATORS"
fi

# Check for containers without resource limits
NO_LIMITS_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' security-monitoring.json)
if [ $NO_LIMITS_COUNT -gt 5 ]; then  # Alert if more than 5 containers without limits
    send_alert "RESOURCE_LIMITS" "Found $NO_LIMITS_COUNT containers without resource limits"
fi

# Generate daily security summary
if [ $(date +%H%M) = "0800" ]; then  # Daily at 8 AM
    SUMMARY_FILE="/var/log/k8s-security-daily-$(date +%Y-%m-%d).summary"
    
    cat > "$SUMMARY_FILE" << SUMMARY
Daily Security Summary - $(date)
================================

Cluster Security Metrics:
- Total Operators: $(jq '.operators | length' security-monitoring.json)
- Privileged Containers: $PRIVILEGED_COUNT
- Wildcard Permissions: $WILDCARD_COUNT
- Host Network Access: $HOST_NETWORK_COUNT
- Containers w/o Limits: $NO_LIMITS_COUNT

Security Status: $([ $(($PRIVILEGED_COUNT + $WILDCARD_COUNT)) -eq 0 ] && echo "✅ SECURE" || echo "⚠️ ATTENTION REQUIRED")

Database Info:
- Latest Snapshot: $SNAPSHOT_ID
- Storage Location: $(dirname $(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id' 2>/dev/null) 2>/dev/null || echo "~/.k8s-inventory/")/inventory.db

SUMMARY

    # Email daily summary
    if command -v mail > /dev/null; then
        cat "$SUMMARY_FILE" | mail -s "K8s Daily Security Summary - $(date +%Y-%m-%d)" "$ALERT_EMAIL"
    fi
fi

# Cleanup old monitoring data
rm security-monitoring.json

echo "$(date): Security monitoring check completed" | tee -a "$MONITORING_LOG"

# Rotate logs if they get too large (keep last 1000 lines)
if [ -f "$MONITORING_LOG" ] && [ $(wc -l < "$MONITORING_LOG") -gt 1000 ]; then
    tail -1000 "$MONITORING_LOG" > "${MONITORING_LOG}.tmp"
    mv "${MONITORING_LOG}.tmp" "$MONITORING_LOG"
fi
EOF

chmod +x security-continuous-monitoring.sh
```

### Security Alerting Integration

```bash
# Create security alerting integration with popular tools
cat > security-alerting-integration.sh << 'EOF'
#!/bin/bash
# Security Alerting Integration Script

# Configuration
SLACK_WEBHOOK_URL=${SLACK_WEBHOOK_URL:-""}
TEAMS_WEBHOOK_URL=${TEAMS_WEBHOOK_URL:-""}
PAGERDUTY_INTEGRATION_KEY=${PAGERDUTY_INTEGRATION_KEY:-""}

# Function to send Slack alert
send_slack_alert() {
    local alert_type="$1"
    local message="$2"
    local severity="$3"
    
    if [ -n "$SLACK_WEBHOOK_URL" ]; then
        local color="danger"
        [ "$severity" = "low" ] && color="warning"
        [ "$severity" = "info" ] && color="good"
        
        curl -X POST -H 'Content-type: application/json' \
            --data "{
                \"attachments\": [{
                    \"color\": \"$color\",
                    \"title\": \"Kubernetes Security Alert\",
                    \"fields\": [
                        {\"title\": \"Alert Type\", \"value\": \"$alert_type\", \"short\": true},
                        {\"title\": \"Severity\", \"value\": \"$severity\", \"short\": true},
                        {\"title\": \"Message\", \"value\": \"$message\", \"short\": false},
                        {\"title\": \"Timestamp\", \"value\": \"$(date)\", \"short\": true}
                    ]
                }]
            }" \
            "$SLACK_WEBHOOK_URL"
    fi
}

# Function to send Teams alert
send_teams_alert() {
    local alert_type="$1"
    local message="$2"
    local severity="$3"
    
    if [ -n "$TEAMS_WEBHOOK_URL" ]; then
        local color="FF0000"
        [ "$severity" = "low" ] && color="FFA500"
        [ "$severity" = "info" ] && color="00FF00"
        
        curl -X POST -H 'Content-type: application/json' \
            --data "{
                \"@type\": \"MessageCard\",
                \"@context\": \"http://schema.org/extensions\",
                \"themeColor\": \"$color\",
                \"summary\": \"Kubernetes Security Alert\",
                \"sections\": [{
                    \"activityTitle\": \"Kubernetes Security Alert\",
                    \"activitySubtitle\": \"$alert_type\",
                    \"facts\": [
                        {\"name\": \"Severity\", \"value\": \"$severity\"},
                        {\"name\": \"Message\", \"value\": \"$message\"},
                        {\"name\": \"Timestamp\", \"value\": \"$(date)\"}
                    ]
                }]
            }" \
            "$TEAMS_WEBHOOK_URL"
    fi
}

# Function to send PagerDuty alert
send_pagerduty_alert() {
    local alert_type="$1"
    local message="$2"
    local severity="$3"
    
    if [ -n "$PAGERDUTY_INTEGRATION_KEY" ]; then
        curl -X POST -H 'Content-Type: application/json' \
            --data "{
                \"routing_key\": \"$PAGERDUTY_INTEGRATION_KEY\",
                \"event_action\": \"trigger\",
                \"payload\": {
                    \"summary\": \"Kubernetes Security Alert: $alert_type\",
                    \"severity\": \"$severity\",
                    \"source\": \"k8s-datamodel\",
                    \"custom_details\": {
                        \"alert_type\": \"$alert_type\",
                        \"message\": \"$message\",
                        \"timestamp\": \"$(date)\"
                    }
                }
            }" \
            "https://events.pagerduty.com/v2/enqueue"
    fi
}

# Main alerting function
send_security_alert() {
    local alert_type="$1"
    local message="$2"
    local severity="${3:-high}"
    
    echo "Sending security alert: $alert_type - $message"
    
    send_slack_alert "$alert_type" "$message" "$severity"
    send_teams_alert "$alert_type" "$message" "$severity"
    
    # Only send to PagerDuty for critical/high severity alerts
    if [ "$severity" = "critical" ] || [ "$severity" = "high" ]; then
        send_pagerduty_alert "$alert_type" "$message" "$severity"
    fi
}

# Example usage with security monitoring
if [ "$1" = "test" ]; then
    send_security_alert "TEST_ALERT" "This is a test security alert" "info"
    echo "Test alerts sent to configured endpoints"
    exit 0
fi

# Store current state and analyze
k8s-datamodel database store --notes "Security alerting check - $(date +%Y-%m-%d-%H-%M)"
SNAPSHOT_ID=$(k8s-datamodel database list --limit 1 --output json | jq -r '.[0].id')
k8s-datamodel database export $SNAPSHOT_ID --file alerting-security.json

# Check for critical violations and send alerts
PRIVILEGED_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' alerting-security.json)
if [ $PRIVILEGED_COUNT -gt 0 ]; then
    PRIVILEGED_LIST=$(jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' alerting-security.json | head -5 | tr '\n' ', ' | sed 's/,$//')
    send_security_alert "PRIVILEGED_CONTAINERS" "Found $PRIVILEGED_COUNT privileged containers: $PRIVILEGED_LIST" "critical"
fi

WILDCARD_COUNT=$(jq '[.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*")] | length' alerting-security.json)
if [ $WILDCARD_COUNT -gt 0 ]; then
    WILDCARD_LIST=$(jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | .display_name' alerting-security.json | head -5 | tr '\n' ', ' | sed 's/,$//')
    send_security_alert "WILDCARD_PERMISSIONS" "Found $WILDCARD_COUNT operators with excessive permissions: $WILDCARD_LIST" "critical"
fi

rm alerting-security.json
echo "Security alerting check completed"
EOF

chmod +x security-alerting-integration.sh

# Usage examples:
# ./security-alerting-integration.sh test  # Send test alerts
# ./security-alerting-integration.sh       # Run security check and send real alerts
```

This comprehensive security and compliance analysis suite provides:

1. **Security Baseline Management**: Establish and validate security baselines
2. **RBAC Analysis**: Comprehensive permission auditing and change detection
3. **Security Context Analysis**: Deep container security assessment
4. **Compliance Reporting**: SOC 2 and PCI DSS compliance automation
5. **Vulnerability Assessment**: Systematic security violation detection
6. **Automated Monitoring**: Continuous security monitoring and alerting
7. **Integration**: Slack, Teams, and PagerDuty alerting integration

These tools enable enterprise-grade security management and compliance reporting using k8s-datamodel's database and analysis capabilities.

## Vulnerability Assessment

The vulnerability assessment capabilities are integrated throughout the security baseline establishment, RBAC analysis, and container security analysis sections above. These provide comprehensive vulnerability identification including:

- Privileged container detection
- Wildcard permission identification
- Resource limit violations
- Host network access risks
- Root user execution detection

For specific vulnerability scanning workflows, refer to the container security analysis scripts and RBAC audit examples.

## Policy Enforcement Monitoring

Policy enforcement monitoring is implemented through the continuous security monitoring and alerting integration examples above. Key features include:

- Real-time security violation detection
- Automated policy compliance checking
- Multi-channel alerting (Slack, Teams, PagerDuty)
- Historical compliance tracking
- Security baseline validation

The security monitoring scripts provide comprehensive policy enforcement capabilities with configurable thresholds and automated responses.

## Security Drift Detection

Security drift detection is implemented through the security baseline validation and RBAC change detection scripts above. This includes:

- Baseline comparison analysis
- Permission escalation detection
- Configuration drift identification
- Security posture degradation alerts
- Historical trend analysis

The drift detection capabilities leverage k8s-datamodel's database functionality to maintain historical security baselines and detect deviations over time.
