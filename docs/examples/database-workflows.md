# Database Workflow Examples

This document provides comprehensive examples of using k8s-inventory-cli's database functionality for real-world scenarios.

## Table of Contents

1. [Basic Database Operations](#basic-database-operations)
2. [Multi-Cluster Management](#multi-cluster-management)
3. [Compliance and Auditing](#compliance-and-auditing)
4. [Migration Planning](#migration-planning)
5. [Configuration Drift Detection](#configuration-drift-detection)
6. [Security Analysis](#security-analysis)
7. [Automated Monitoring](#automated-monitoring)
8. [CI/CD Integration](#cicd-integration)

## Basic Database Operations

### Initial Setup and First Snapshot

```bash
# Test cluster connectivity
k8s-inventory cluster test-connection

# Create your first snapshot
k8s-inventory database store --notes "Initial cluster baseline - $(date)"

# Verify the snapshot was created
k8s-inventory database list
```

**Expected Output:**
```
+------+------------------+-----------+--------+-------------+--------+-------------+-------------------------------+
|   ID | Timestamp        | Context   |   CRDs |   Operators |   CSVs | Namespace   | Notes                         |
+======+==================+===========+========+=============+========+=============+===============================+
|    1 | 2025-09-07 19:30 | default   |    143 |           9 |     33 | all         | Initial cluster baseline -... |
+------+------------------+-----------+--------+-------------+--------+-------------+-------------------------------+
```

### Viewing Database Statistics

```bash
# Get comprehensive database statistics
k8s-inventory database stats --output rich
```

**Expected Output:**
```
╭────────────────────────────────────────────────────── Database Info ──────────────────────────────────────────────────────╮
│ Database Path: /Users/user/.k8s-inventory/inventory.db                                                                     │
│ File Size: 13.3MB                                                                                                          │
│ Total Snapshots: 1                                                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────── Data Counts ─────────────────────────────────────────────────────────╮
│ Total CRDs: 143                                                                                                             │
│ Total Operators: 9                                                                                                         │
│ Total CSVs: 33                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Exporting Snapshots for Analysis

```bash
# Export snapshot with complete specifications
k8s-inventory database export 1 --file cluster-snapshot.json

# Export only CRDs for focused analysis  
k8s-inventory database export 1 --crds-only --file crds-analysis.json

# Export in YAML format for human readability
k8s-inventory database export 1 --output yaml --file cluster-snapshot.yaml
```

## Multi-Cluster Management

### Managing Multiple Environments

```bash
# Store snapshots from different environments
k8s-inventory --context prod-cluster database store \
    --notes "Production cluster - $(date +%Y-%m-%d)"

k8s-inventory --context staging-cluster database store \
    --notes "Staging cluster - $(date +%Y-%m-%d)"

k8s-inventory --context dev-cluster database store \
    --notes "Development cluster - $(date +%Y-%m-%d)"

# List snapshots filtered by cluster context
k8s-inventory database list --cluster-context prod-cluster
```

**Expected Output:**
```
+------+------------------+---------------+--------+-------------+--------+-------------+---------------------------+
|   ID | Timestamp        | Context       |   CRDs |   Operators |   CSVs | Namespace   | Notes                     |
+======+==================+===============+========+=============+========+=============+===========================+
|    1 | 2025-09-07 19:30 | prod-cluster  |    143 |           9 |     33 | all         | Production cluster - ...  |
|    2 | 2025-09-07 19:35 | staging-clus  |    128 |           8 |     28 | all         | Staging cluster - ...     |
|    3 | 2025-09-07 19:40 | dev-cluster   |     95 |           5 |     15 | all         | Development cluster - ... |
+------+------------------+---------------+--------+-------------+--------+-------------+---------------------------+
```

### Cross-Environment Comparison

```bash
# Export snapshots for comparison
k8s-inventory database export 1 --file prod-inventory.json
k8s-inventory database export 2 --file staging-inventory.json
k8s-inventory database export 3 --file dev-inventory.json

# Compare CRD counts between environments
echo "=== CRD Comparison ==="
echo "Production: $(jq '.crds | length' prod-inventory.json) CRDs"
echo "Staging:    $(jq '.crds | length' staging-inventory.json) CRDs"
echo "Development: $(jq '.crds | length' dev-inventory.json) CRDs"

# Find CRDs present in prod but not in staging
comm -23 <(jq -r '.crds[].name' prod-inventory.json | sort) \
         <(jq -r '.crds[].name' staging-inventory.json | sort) > prod-only-crds.txt
```

## Compliance and Auditing

### Pre-Audit Baseline

```bash
# Create comprehensive audit baseline
k8s-inventory database store \
    --notes "SOC2 Audit Baseline - $(date +%Y-%m-%d) - Pre-audit snapshot"

# Generate audit-specific exports
k8s-inventory database export 1 --file audit-baseline.json

# Extract security-relevant information
echo "=== Security Analysis for Audit ==="

# Find operators with privileged security contexts
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | 
       "PRIVILEGED: \(.name) in namespace \(.namespace)"' audit-baseline.json

# Find operators without resource limits
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null) | 
       "NO LIMITS: \(.name) in namespace \(.namespace)"' audit-baseline.json

# Extract RBAC permissions from CSVs
jq -r '.csvs[] | 
       "CSV: \(.name) - Permissions: \(.spec.spec.install.spec.permissions | length) - ClusterPermissions: \(.spec.spec.install.spec.clusterPermissions | length)"' audit-baseline.json
```

### Post-Audit Comparison

```bash
# Store post-remediation snapshot
k8s-inventory database store \
    --notes "SOC2 Audit - Post-remediation snapshot - $(date +%Y-%m-%d)"

# Compare audit snapshots
k8s-inventory database export 1 --file pre-audit.json
k8s-inventory database export 2 --file post-audit.json

# Check for security improvements
echo "=== Security Improvements ==="
echo "Pre-audit privileged operators:"
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' pre-audit.json | wc -l

echo "Post-audit privileged operators:"
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | .name' post-audit.json | wc -l
```

## Migration Planning

### Pre-Migration Documentation

```bash
# Document source cluster state
k8s-inventory --context source-cluster database store \
    --notes "Migration Source - EKS v1.28 - $(date +%Y-%m-%d)"

# Export comprehensive migration documentation
k8s-inventory database export 1 --file migration-source-inventory.json

# Generate migration planning report
echo "=== Migration Planning Report ===" > migration-plan.md
echo "Generated: $(date)" >> migration-plan.md
echo "" >> migration-plan.md

echo "## Source Cluster Overview" >> migration-plan.md
echo "- CRDs: $(jq '.crds | length' migration-source-inventory.json)" >> migration-plan.md
echo "- Operators: $(jq '.operators | length' migration-source-inventory.json)" >> migration-plan.md
echo "- OLM CSVs: $(jq '.csvs | length' migration-source-inventory.json)" >> migration-plan.md
echo "" >> migration-plan.md

echo "## Critical CRDs to Migrate" >> migration-plan.md
jq -r '.crds[] | select(.instance_count > 0) | "- \(.name) (\(.kind)) - \(.instance_count) instances"' \
   migration-source-inventory.json >> migration-plan.md
echo "" >> migration-plan.md

echo "## Operators to Reinstall" >> migration-plan.md
jq -r '.operators[] | "- \(.name) (\(.operator_type)) - \(.namespace) - \(.operator_framework // "Manual")"' \
   migration-source-inventory.json >> migration-plan.md
```

### Post-Migration Verification

```bash
# Document target cluster state
k8s-inventory --context target-cluster database store \
    --notes "Migration Target - GKE v1.29 - Post-migration - $(date +%Y-%m-%d)"

# Export target cluster inventory
k8s-inventory database export 2 --file migration-target-inventory.json

# Verify migration completeness
echo "=== Migration Verification ===" > migration-verification.md
echo "Generated: $(date)" >> migration-verification.md
echo "" >> migration-verification.md

# Compare CRD counts
SOURCE_CRDS=$(jq '.crds | length' migration-source-inventory.json)
TARGET_CRDS=$(jq '.crds | length' migration-target-inventory.json)
echo "## CRD Migration Status" >> migration-verification.md
echo "- Source: $SOURCE_CRDS CRDs" >> migration-verification.md  
echo "- Target: $TARGET_CRDS CRDs" >> migration-verification.md
echo "- Status: $( [ $SOURCE_CRDS -eq $TARGET_CRDS ] && echo "✅ COMPLETE" || echo "⚠️  INCOMPLETE" )" >> migration-verification.md
echo "" >> migration-verification.md

# Find missing CRDs
echo "## Missing CRDs" >> migration-verification.md
comm -23 <(jq -r '.crds[].name' migration-source-inventory.json | sort) \
         <(jq -r '.crds[].name' migration-target-inventory.json | sort) | \
while read crd; do echo "- ❌ $crd"; done >> migration-verification.md
```

## Configuration Drift Detection

### Establishing Configuration Baseline

```bash
# Create golden configuration baseline
k8s-inventory database store \
    --notes "Golden Configuration Baseline - Approved by Platform Team - $(date +%Y-%m-%d)"

# Store the baseline ID for future comparisons
echo "1" > .baseline-snapshot-id
```

### Weekly Drift Detection

```bash
# Weekly drift detection script
#!/bin/bash
BASELINE_ID=$(cat .baseline-snapshot-id)
CURRENT_DATE=$(date +%Y-%m-%d)

# Store current state
k8s-inventory database store --notes "Weekly drift check - $CURRENT_DATE"
CURRENT_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')

# Export both snapshots
k8s-inventory database export $BASELINE_ID --file baseline.json
k8s-inventory database export $CURRENT_ID --file current.json

# Generate drift report
echo "=== Configuration Drift Report - $CURRENT_DATE ===" > drift-report.md
echo "" >> drift-report.md

# Compare CRD counts
BASELINE_CRD_COUNT=$(jq '.crds | length' baseline.json)
CURRENT_CRD_COUNT=$(jq '.crds | length' current.json)

echo "## CRD Changes" >> drift-report.md
echo "- Baseline: $BASELINE_CRD_COUNT CRDs" >> drift-report.md
echo "- Current: $CURRENT_CRD_COUNT CRDs" >> drift-report.md
echo "- Change: $(($CURRENT_CRD_COUNT - $BASELINE_CRD_COUNT))" >> drift-report.md
echo "" >> drift-report.md

# Find new CRDs
echo "### New CRDs Added" >> drift-report.md
comm -13 <(jq -r '.crds[].name' baseline.json | sort) \
         <(jq -r '.crds[].name' current.json | sort) | \
while read crd; do echo "- ✅ $crd"; done >> drift-report.md

# Find removed CRDs  
echo "" >> drift-report.md
echo "### CRDs Removed" >> drift-report.md
comm -23 <(jq -r '.crds[].name' baseline.json | sort) \
         <(jq -r '.crds[].name' current.json | sort) | \
while read crd; do echo "- ❌ $crd"; done >> drift-report.md

# Compare operator configurations
echo "" >> drift-report.md
echo "## Operator Configuration Changes" >> drift-report.md

# Check for operator image changes
jq -r '.operators[] | "\(.name)|\(.image)"' baseline.json | sort > baseline-images.txt
jq -r '.operators[] | "\(.name)|\(.image)"' current.json | sort > current-images.txt

echo "### Image Changes" >> drift-report.md
diff baseline-images.txt current-images.txt | grep '^>' | sed 's/^> /- /' >> drift-report.md
```

## Security Analysis

### Security Audit Workflow

```bash
# Store current state for security analysis
k8s-inventory database store \
    --notes "Security Audit - $(date +%Y-%m-%d) - Comprehensive security review"

# Export for detailed security analysis
k8s-inventory database export 1 --file security-audit.json

# Generate security report
echo "=== Security Audit Report - $(date +%Y-%m-%d) ===" > security-report.md
echo "" >> security-report.md

echo "## Privileged Containers Analysis" >> security-report.md
echo "### Operators with Privileged Containers" >> security-report.md
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true) | 
       "- **\(.name)** (namespace: \(.namespace))"' security-audit.json >> security-report.md
echo "" >> security-report.md

echo "### Operators with Host Network Access" >> security-report.md
jq -r '.operators[] | select(.spec.spec.template.spec.hostNetwork == true) | 
       "- **\(.name)** (namespace: \(.namespace))"' security-audit.json >> security-report.md
echo "" >> security-report.md

echo "### Operators without Resource Limits" >> security-report.md
jq -r '.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null) | 
       "- **\(.name)** (namespace: \(.namespace)) - No resource limits set"' security-audit.json >> security-report.md
echo "" >> security-report.md

echo "## RBAC Analysis from OLM CSVs" >> security-report.md
echo "### ClusterPermissions Summary" >> security-report.md
jq -r '.csvs[] | 
       "- **\(.name)**: \(.spec.spec.install.spec.clusterPermissions | length) cluster-level permissions"' \
   security-audit.json >> security-report.md
echo "" >> security-report.md

echo "### High-Risk Permissions" >> security-report.md
# Find CSVs with cluster-admin or dangerous permissions
jq -r '.csvs[] | select(.spec.spec.install.spec.clusterPermissions[]?.rules[]?.resources[]? == "*") | 
       "- **\(.name)**: Has wildcard resource permissions"' security-audit.json >> security-report.md

echo "## Recommendations" >> security-report.md
echo "1. Review all privileged containers and implement least-privilege principle" >> security-report.md
echo "2. Add resource limits to all operators without limits" >> security-report.md  
echo "3. Audit RBAC permissions and implement role-based access control" >> security-report.md
echo "4. Consider using Pod Security Standards for additional security" >> security-report.md
```

### Security Monitoring Setup

```bash
# Create security monitoring script
cat > security-monitor.sh << 'EOF'
#!/bin/bash
# Daily security monitoring

DATE=$(date +%Y-%m-%d)
k8s-inventory database store --notes "Security monitoring - $DATE"

# Get latest snapshot
LATEST_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $LATEST_ID --file daily-security.json

# Check for security violations
PRIVILEGED_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' daily-security.json)
NO_LIMITS_COUNT=$(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' daily-security.json)

if [ $PRIVILEGED_COUNT -gt 0 ] || [ $NO_LIMITS_COUNT -gt 0 ]; then
    echo "SECURITY ALERT - $DATE" | mail -s "K8s Security Issues Detected" security-team@company.com
    echo "Privileged containers: $PRIVILEGED_COUNT" 
    echo "Containers without limits: $NO_LIMITS_COUNT"
fi
EOF

chmod +x security-monitor.sh
```

## Automated Monitoring

### Daily Inventory Collection

```bash
# Create automated daily inventory script
cat > daily-inventory.sh << 'EOF'
#!/bin/bash
# Daily automated inventory collection

DATE=$(date +%Y-%m-%d)
CONTEXTS=("prod-cluster" "staging-cluster" "dev-cluster")

for CONTEXT in "${CONTEXTS[@]}"; do
    echo "Collecting inventory for $CONTEXT..."
    k8s-inventory --context $CONTEXT database store \
        --notes "Automated daily snapshot - $CONTEXT - $DATE"
done

# Cleanup old snapshots (keep 30 days)
k8s-inventory database cleanup --keep 30

# Generate daily summary
echo "=== Daily Inventory Summary - $DATE ===" > daily-summary.txt
k8s-inventory database stats >> daily-summary.txt
echo "" >> daily-summary.txt
echo "Recent snapshots:" >> daily-summary.txt
k8s-inventory database list --limit 10 >> daily-summary.txt
EOF

chmod +x daily-inventory.sh

# Add to crontab for daily execution at 2 AM
echo "0 2 * * * /path/to/daily-inventory.sh" | crontab -
```

### Trend Analysis

```bash
# Weekly trend analysis script
cat > weekly-trends.sh << 'EOF'
#!/bin/bash
# Weekly trend analysis

WEEK_AGO=$(date -d '7 days ago' +%Y-%m-%d)
TODAY=$(date +%Y-%m-%d)

echo "=== Weekly Trends Report - $TODAY ===" > weekly-trends.md
echo "" >> weekly-trends.md

# Get snapshots from the last week for each cluster
for CONTEXT in prod-cluster staging-cluster dev-cluster; do
    echo "## $CONTEXT Trends" >> weekly-trends.md
    
    # Get snapshot IDs from the last week
    SNAPSHOTS=$(k8s-inventory database list --cluster-context $CONTEXT --output json | \
                jq -r '.[] | select(.timestamp >= "'$WEEK_AGO'") | .id')
    
    if [ -n "$SNAPSHOTS" ]; then
        FIRST_ID=$(echo "$SNAPSHOTS" | tail -1)
        LATEST_ID=$(echo "$SNAPSHOTS" | head -1)
        
        # Export snapshots
        k8s-inventory database export $FIRST_ID --file week-start-$CONTEXT.json
        k8s-inventory database export $LATEST_ID --file week-end-$CONTEXT.json
        
        # Calculate changes
        START_CRDS=$(jq '.crds | length' week-start-$CONTEXT.json)
        END_CRDS=$(jq '.crds | length' week-end-$CONTEXT.json)
        CRD_CHANGE=$((END_CRDS - START_CRDS))
        
        START_OPS=$(jq '.operators | length' week-start-$CONTEXT.json)
        END_OPS=$(jq '.operators | length' week-end-$CONTEXT.json)
        OP_CHANGE=$((END_OPS - START_OPS))
        
        echo "- CRDs: $START_CRDS → $END_CRDS (change: $CRD_CHANGE)" >> weekly-trends.md
        echo "- Operators: $START_OPS → $END_OPS (change: $OP_CHANGE)" >> weekly-trends.md
        echo "" >> weekly-trends.md
        
        # Cleanup temp files
        rm week-start-$CONTEXT.json week-end-$CONTEXT.json
    else
        echo "- No snapshots found for the past week" >> weekly-trends.md
        echo "" >> weekly-trends.md
    fi
done
EOF

chmod +x weekly-trends.sh
```

## CI/CD Integration

### GitHub Actions Integration

```yaml
# .github/workflows/inventory-tracking.yml
name: Kubernetes Inventory Tracking

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  inventory:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install k8s-inventory-cli
      run: pipx install k8s-inventory-cli
    
    - name: Configure kubectl
      run: |
        echo "${{ secrets.KUBECONFIG }}" | base64 -d > /tmp/kubeconfig
        export KUBECONFIG=/tmp/kubeconfig
    
    - name: Store inventory snapshot
      env:
        KUBECONFIG: /tmp/kubeconfig
      run: |
        k8s-inventory database store \
          --notes "CI/CD automated snapshot - $(date +%Y-%m-%d) - ${{ github.sha }}"
    
    - name: Generate inventory report
      env:
        KUBECONFIG: /tmp/kubeconfig
      run: |
        # Get latest snapshot
        LATEST_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
        
        # Export inventory
        k8s-inventory database export $LATEST_ID --file inventory-report.json
        
        # Generate summary
        echo "# Kubernetes Inventory Report - $(date)" > inventory-summary.md
        echo "" >> inventory-summary.md
        echo "**Generated by:** GitHub Actions" >> inventory-summary.md
        echo "**Commit:** ${{ github.sha }}" >> inventory-summary.md
        echo "" >> inventory-summary.md
        
        CRD_COUNT=$(jq '.crds | length' inventory-report.json)
        OP_COUNT=$(jq '.operators | length' inventory-report.json)
        CSV_COUNT=$(jq '.csvs | length' inventory-report.json)
        
        echo "## Summary" >> inventory-summary.md
        echo "- **CRDs:** $CRD_COUNT" >> inventory-summary.md
        echo "- **Operators:** $OP_COUNT" >> inventory-summary.md  
        echo "- **OLM CSVs:** $CSV_COUNT" >> inventory-summary.md
    
    - name: Upload database
      uses: actions/upload-artifact@v4
      with:
        name: inventory-database-${{ github.run_number }}
        path: ~/.k8s-inventory/inventory.db
        retention-days: 30
    
    - name: Upload reports
      uses: actions/upload-artifact@v4
      with:
        name: inventory-reports-${{ github.run_number }}
        path: |
          inventory-report.json
          inventory-summary.md
        retention-days: 30
```

### Terraform Integration

```hcl
# terraform/modules/k8s-inventory/main.tf
resource "null_resource" "k8s_inventory" {
  triggers = {
    cluster_endpoint = var.cluster_endpoint
    always_run       = timestamp()
  }

  provisioner "local-exec" {
    command = <<-EOT
      # Configure kubectl for the cluster
      aws eks update-kubeconfig --region ${var.region} --name ${var.cluster_name}
      
      # Store inventory snapshot
      k8s-inventory database store \
        --notes "Terraform deployment - ${var.environment} - $(date +%Y-%m-%d-%H-%M)"
      
      # Export inventory for terraform outputs
      LATEST_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
      k8s-inventory database export $LATEST_ID --file ${var.output_path}/cluster-inventory.json
    EOT
  }

  depends_on = [
    kubernetes_namespace.applications
  ]
}

# Output the inventory summary
data "external" "inventory_summary" {
  program = ["jq", "-n", "--slurpfile", "inventory", "${var.output_path}/cluster-inventory.json", 
             "{crds: ($inventory[0].crds | length), operators: ($inventory[0].operators | length), csvs: ($inventory[0].csvs | length)}"]
  
  depends_on = [null_resource.k8s_inventory]
}

output "inventory_summary" {
  description = "Summary of Kubernetes resources in the cluster"
  value = {
    crds      = data.external.inventory_summary.result["crds"]
    operators = data.external.inventory_summary.result["operators"]
    csvs      = data.external.inventory_summary.result["csvs"]
    snapshot_file = "${var.output_path}/cluster-inventory.json"
  }
}
```

### Monitoring Integration with Prometheus

```bash
# Create Prometheus metrics exporter
cat > inventory-metrics-exporter.sh << 'EOF'
#!/bin/bash
# Export k8s-inventory metrics for Prometheus

# Store current snapshot
k8s-inventory database store --notes "Metrics collection - $(date)"

# Get latest snapshot
LATEST_ID=$(k8s-inventory database list --limit 1 --output json | jq -r '.[0].id')
k8s-inventory database export $LATEST_ID --file metrics-inventory.json

# Generate Prometheus metrics
cat > /var/lib/node_exporter/k8s_inventory.prom << METRICS
# HELP k8s_inventory_crds_total Total number of CRDs in cluster
# TYPE k8s_inventory_crds_total gauge
k8s_inventory_crds_total $(jq '.crds | length' metrics-inventory.json)

# HELP k8s_inventory_operators_total Total number of operators in cluster  
# TYPE k8s_inventory_operators_total gauge
k8s_inventory_operators_total $(jq '.operators | length' metrics-inventory.json)

# HELP k8s_inventory_csvs_total Total number of OLM CSVs in cluster
# TYPE k8s_inventory_csvs_total gauge
k8s_inventory_csvs_total $(jq '.csvs | length' metrics-inventory.json)

# HELP k8s_inventory_privileged_operators Total number of privileged operators
# TYPE k8s_inventory_privileged_operators gauge
k8s_inventory_privileged_operators $(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].securityContext.privileged == true)] | length' metrics-inventory.json)

# HELP k8s_inventory_operators_no_limits Total number of operators without resource limits
# TYPE k8s_inventory_operators_no_limits gauge
k8s_inventory_operators_no_limits $(jq '[.operators[] | select(.spec.spec.template.spec.containers[0].resources.limits == null)] | length' metrics-inventory.json)

# HELP k8s_inventory_database_size_bytes Size of inventory database in bytes
# TYPE k8s_inventory_database_size_bytes gauge
k8s_inventory_database_size_bytes $(stat -c%s ~/.k8s-inventory/inventory.db)
METRICS

echo "Metrics exported to /var/lib/node_exporter/k8s_inventory.prom"
rm metrics-inventory.json
EOF

chmod +x inventory-metrics-exporter.sh

# Add to crontab for regular metrics collection
echo "*/15 * * * * /path/to/inventory-metrics-exporter.sh" | crontab -
```

## Best Practices and Tips

### 1. Snapshot Naming Conventions

```bash
# Use consistent naming patterns
k8s-inventory database store --notes "TYPE-PURPOSE-DATE-DETAILS"

# Examples:
k8s-inventory database store --notes "BASELINE-initial-cluster-setup-$(date +%Y-%m-%d)"
k8s-inventory database store --notes "AUDIT-sox-compliance-pre-$(date +%Y-%m-%d)"
k8s-inventory database store --notes "MIGRATION-source-cluster-$(date +%Y-%m-%d-%H-%M)"
k8s-inventory database store --notes "INCIDENT-post-recovery-$(date +%Y-%m-%d-%H-%M)"
```

### 2. Database Maintenance

```bash
# Regular cleanup script
cat > db-maintenance.sh << 'EOF'
#!/bin/bash
# Database maintenance routine

echo "=== K8s Inventory Database Maintenance - $(date) ==="

# Show current statistics
echo "Current database statistics:"
k8s-inventory database stats

# Clean up old snapshots (keep 30 most recent)
echo "Cleaning up old snapshots..."
k8s-inventory database cleanup --keep 30

# Vacuum database to reclaim space
echo "Vacuuming database..."
sqlite3 ~/.k8s-inventory/inventory.db "VACUUM;"

# Show updated statistics
echo "Updated database statistics:"
k8s-inventory database stats
EOF

chmod +x db-maintenance.sh
```

### 3. Error Handling and Retry Logic

```bash
# Robust snapshot collection with retry
cat > robust-snapshot.sh << 'EOF'
#!/bin/bash
# Robust snapshot collection with retry logic

MAX_RETRIES=3
RETRY_DELAY=30
CONTEXT=${1:-"default"}
NOTES=${2:-"Automated snapshot - $(date)"}

for i in $(seq 1 $MAX_RETRIES); do
    echo "Attempt $i of $MAX_RETRIES for context $CONTEXT"
    
    if k8s-inventory --context $CONTEXT database store --notes "$NOTES"; then
        echo "✅ Successfully stored snapshot for $CONTEXT"
        exit 0
    else
        echo "❌ Failed attempt $i for $CONTEXT"
        if [ $i -lt $MAX_RETRIES ]; then
            echo "Waiting $RETRY_DELAY seconds before retry..."
            sleep $RETRY_DELAY
        fi
    fi
done

echo "🚨 All attempts failed for context $CONTEXT"
exit 1
EOF

chmod +x robust-snapshot.sh
```

## Conclusion

These examples demonstrate the powerful capabilities of k8s-inventory-cli's database functionality for real-world Kubernetes management scenarios. The tool enables comprehensive cluster tracking, compliance monitoring, security analysis, and operational insights through persistent storage of complete resource specifications.

Key benefits demonstrated:

- **Comprehensive Tracking**: Complete cluster state preservation with datetime handling
- **Multi-Environment Management**: Consistent inventory across environments  
- **Security Analysis**: Deep inspection of RBAC, security contexts, and permissions
- **Configuration Drift Detection**: Automated detection of unauthorized changes
- **Compliance Support**: Audit trails and compliance reporting capabilities
- **CI/CD Integration**: Automated inventory collection in deployment pipelines
- **Operational Monitoring**: Trend analysis and alerting for cluster changes

For additional examples and advanced use cases, refer to the complete documentation in the [docs/](../) directory.
