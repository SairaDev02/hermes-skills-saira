# Rollback Automation Reference

This reference covers rollback mechanisms, trigger criteria, database rollback strategies, and testing procedures.

## Rollback Mechanisms by Platform

### Kubernetes — Rolling Update

```bash
# Rollback to the previous deployment
kubectl rollout undo deployment/<name> -n <namespace>

# Rollback to a specific revision
kubectl rollout undo deployment/<name> -n <namespace> --to-revision=3

# Check rollout status
kubectl rollout status deployment/<name> -n <namespace>

# View rollout history
kubectl rollout history deployment/<name> -n <namespace>
```

Kubernetes retains 10 old ReplicaSets by default (controlled by `revisionHistoryLimit` in the deployment spec). Setting `revisionHistoryLimit: 0` disables rollback — a trap worth avoiding.

**Recovery time:** 1-3 minutes (pod termination and recreation cycle).

### Kubernetes — Blue-Green (with Argo Rollouts)

```bash
# Argo Rollouts: revert to stable
kubectl argo rollouts undo rollout/<name> -n <namespace>

# Or promote/abort via Argo Rollouts
kubectl argo rollouts abort rollout/<name> -n <namespace>
```

**Recovery time:** < 1 minute (traffic switch, no pod recreation needed if the old environment is still running).

### Canary (with Argo Rollouts / Flagger)

```bash
# Abort canary and revert traffic to stable
kubectl argo rollouts abort rollout/<name> -n <namespace>
```

Flagger automatically reverts traffic when analysis metrics breach thresholds. No manual intervention needed.

**Recovery time:** 1-5 minutes (traffic percentage reverts to 0% on the new version).

### Cloud Platforms

| Platform | Rollback Command | Recovery Time |
|----------|-----------------|---------------|
| AWS Elastic Beanstalk | `eb deploy --version <version-label>` | 5-15 minutes |
| AWS Lambda | Update alias to point to previous version | < 1 minute |
| Azure Web Apps | Swap deployment slots back | < 1 minute |
| Vercel | `vercel --prod --prev` (or dashboard rollback) | < 1 minute |
| Heroku | `heroku rollback` | 1-3 minutes |
| Docker Compose | Re-deploy previous image tag | 1-5 minutes |

### Standard Redeployment

If no native rollback mechanism exists, redeploy the previous artifact:

```bash
# Pull the previous image and restart
docker pull <registry>/<image>:<previous-tag>
docker stop <container-name>
docker run -d --name <container-name> <registry>/<image>:<previous-tag>
```

**Recovery time:** 5-15 minutes (full redeployment cycle).

### Feature Flag Rollback

```bash
# Toggle feature flag off (via flag service API or dashboard)
curl -X PATCH https://api.launchdarkly.com/api/v2/flags/<env>/<flag-key> \
  -H "Authorization: <token>" \
  -d '{"patches":[{"op":"replace","path":"/environments/<env>/on","value":false}]}'
```

**Recovery time:** Seconds (runtime toggle, no deployment needed).

## Rollback Triggers

Define specific, measurable conditions that trigger an automatic rollback:

| Trigger | Threshold | Evaluation Window | Action |
|---------|-----------|-------------------|--------|
| Health check failure rate | > 5% | 2 minutes | Automatic rollback |
| Error rate (5xx) | > 2% | 2 minutes | Automatic rollback |
| p99 latency | > 500ms | 2 minutes | Automatic rollback |
| Deployment timeout | > 15 minutes | — | Automatic rollback |
| SLO burn rate | > 2% of budget in 1 hour | 1 hour | Alert + manual decision |
| Alert: service down | Critical alert firing | 60 seconds | Alert + manual rollback |

### Automatic vs Manual Rollback

| Type | When to Use | Risk |
|------|-------------|------|
| Automatic | Well-tested rollback path, clear trigger thresholds, non-destructive rollback (traffic switch, kubectl undo) | Reverting a deployment that would have self-healed |
| Manual | Database migrations involved, rollback path untested, ambiguous failure signals | Delayed recovery while waiting for human decision |

**Recommendation:** Start with manual rollback. Once the rollback path is tested and reliable, automate it with specific trigger conditions. (AWS Well-Architected Framework, OPS06-BP04)

## Database Rollback Strategies

### Expand-and-Contract Pattern

The safest database migration pattern for environments that run old and new versions simultaneously:

```
Step 1: EXPAND — Add new columns/tables (backward-compatible)
  ALTER TABLE users ADD COLUMN email_verified BOOLEAN DEFAULT true;

Step 2: DEPLOY — Deploy new code version that uses the new schema
  (old version still works — it ignores the new column)

Step 3: VALIDATE — Verify the new version works correctly with the new schema

Step 4: CONTRACT — Remove old columns/tables (only after new version is stable)
  ALTER TABLE users DROP COLUMN email_unverified;
```

**Rollback:** Between steps 1 and 4, the old code version remains compatible with the schema. Rolling back the application code does not require rolling back the database.

### Forward-Only Migrations

Never revert a database migration. If a deployment fails:

1. Roll back the application code
2. Write a new migration that fixes the issue (do not revert the original migration)
3. Deploy the fix

**Rationale:** Reverting a migration that added data or modified existing data risks data loss. Forward-only migrations ensure the database is always moving forward.

### Backup Restore (Emergency Only)

Restoring from a database backup is a disaster recovery action, not a routine rollback:

- **Risk:** All data changes since the backup are lost
- **Use case:** Data corruption, accidental deletion, catastrophic schema failure
- **Recovery point objective (RPO):** Determined by backup frequency (e.g., 15 minutes for PITR, 24 hours for daily snapshots)

## Rollback Decision Criteria

Before rolling back, assess:

1. **Was there a database schema change?** If yes, consider rolling forward instead — database rollbacks risk data loss
2. **How long has the new version been live?** If users have been actively using it for hours, rollback may cause user-visible disruption (lost sessions, stale data)
3. **Is the failure a code bug or a config issue?** Config fixes may be faster than a full rollback
4. **Can a feature flag disable the broken feature?** This is faster than a rollback for feature-level bugs
5. **Are there dependent services that would break with a rollback?** If the new version's API contract changed, rolling back may break callers

## Rollback Testing

| Frequency | What to Test | Where |
|-----------|-------------|-------|
| Every deployment | Rollback after staging deployment | Staging |
| Quarterly | Full rollback drill (deploy → validate → rollback → validate) | Staging |
| Before major releases | Rollback in a production-mirror environment | Pre-prod |
| After infrastructure changes | Rollback with new infrastructure config | Staging |

**Anti-pattern:** Writing a rollback script and never testing it. Untested rollback scripts fail in production when they are needed most.

## Post-Rollback Procedure

1. **Notify the team** — post in the incident channel with: what was rolled back, the version rolled back to, and the reason
2. **Verify health** — confirm health checks pass and traffic is flowing to the stable version
3. **Create an incident report** — document: the failing version, the failure symptoms, the rollback mechanism used, the recovery time
4. **Identify root cause** — investigate why the deployment failed; do not re-deploy until the root cause is identified
5. **Fix forward** — deploy a fixed version (not the broken version); the fix must address the root cause, not just the symptom
6. **Update the rollback script** — if the rollback revealed a gap in the procedure, update the script and re-test in staging
7. **Review rollback metrics** — track rollback frequency as a DORA-adjacent metric; high rollback frequency indicates a quality issue upstream (CI gates, testing, review)
