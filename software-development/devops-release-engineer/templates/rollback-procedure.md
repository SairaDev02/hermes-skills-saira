# Rollback Procedure Specification Template

> This document specifies the rollback procedure for the coding harness (Pi)
> to implement. It does not contain executable scripts — it specifies the
> rollback mechanism, triggers, script requirements as pseudocode, and
> testing procedure. Pi implements the actual rollback script from this spec.

---

## Rollback Mechanism

- **Platform:** [Kubernetes / AWS / Azure / Vercel / Docker Compose]
- **Mechanism:** [kubectl rollout undo / slot swap / canary abort / redeploy previous]
- **Recovery time:** [estimated time]

## Rollback Script Requirements

### Script Interface

| Field | Value |
|-------|-------|
| **Script name** | rollback.sh / rollback.py / <other> |
| **Arguments** | `[environment]` — e.g., `production`, `staging` (default: `production`) |
| **Exit code 0** | Rollback successful, health checks passed |
| **Exit code 1** | Rollback failed — manual intervention required |
| **Environment vars** | `DEPLOYMENT_NAME`, `NAMESPACE`, `HEALTH_CHECK_URL` |

### Script Logic (Pseudocode)

```
# Rollback script pseudocode — Pi implements this as executable code

FUNCTION rollback(environment):
    SET deployment = GET_ENV("DEPLOYMENT_NAME", default="app")
    SET namespace = GET_ENV("NAMESPACE", default="default")
    SET health_url = GET_ENV("HEALTH_CHECK_URL", default="http://localhost/health")

    PRINT "Rolling back deployment/" + deployment + " in " + environment + "..."

    # Execute rollback
    EXECUTE rollback_command_for_platform(deployment, namespace)

    # Wait for rollout to complete
    IF rollout_status(deployment, namespace, timeout=300s) SUCCEEDS:
        PRINT "✅ Rollback successful — " + deployment + " reverted to previous revision"
    ELSE:
        PRINT "❌ Rollback failed — manual intervention required"
        NOTIFY on-call team
        EXIT 1

    # Verify health checks
    IF http_check(health_url) SUCCEEDS:
        PRINT "✅ Health check passed"
    ELSE:
        PRINT "⚠️ Health check failed — service may not be healthy after rollback"
        NOTIFY on-call team
        EXIT 1

    PRINT "Rollback complete. Previous version is now serving traffic."
    EXIT 0
```

### Platform-Specific Rollback Command Specification

| Platform | Command | Verification |
|----------|---------|--------------|
| Kubernetes | `kubectl rollout undo deployment/<name> -n <namespace>` | `kubectl rollout status deployment/<name> --timeout=300s` |
| Blue-Green | Switch traffic back to previous active environment | Health check on previous environment |
| Canary | Revert traffic percentage to 0% for new version | Traffic metrics confirm 0% to new version |
| Artifact redeploy | Redeploy previous container image tag | `kubectl rollout status` or equivalent |
| Terraform | `terraform apply` with previous state | `terraform plan` shows no drift |

## Rollback Triggers

| Trigger | Threshold | Evaluation Window | Action |
|---------|-----------|-------------------|--------|
| Health check failure rate | > [5%] | [2 min] | [Automatic] |
| Error rate (5xx) | > [2%] | [2 min] | [Automatic] |
| p99 latency | > [500ms] | [2 min] | [Automatic] |
| Deployment timeout | > [15 min] | — | [Automatic] |
| Manual trigger | — | — | `rollback.sh production` |

## Database Rollback Strategy

- **Strategy:** [expand-and-contract / forward-only / backup restore]
- **Rationale:** [why this strategy was selected]
- **Data-loss risk:** [none / low / high — explanation]

### Migration Compatibility Check

Before deploying, verify:

- [ ] New code is compatible with the previous database schema (if rollback is possible)
- [ ] No destructive migrations (DROP COLUMN, DROP TABLE) in the same deployment as code changes
- [ ] Destructive migrations are scheduled as a follow-up deployment after the new code is validated
- [ ] Database backup is taken before production deployment

## Rollback Testing Procedure

| Frequency | What to Test | Environment |
|-----------|-------------|------------|
| Every staging deployment | Deploy → validate → rollback → validate | Staging |
| Quarterly | Full rollback drill | Staging |
| Before major releases | Rollback in production-mirror | Pre-prod |
| After infrastructure changes | Rollback with new infra config | Staging |

### Test Checklist

- [ ] Rollback script executes without errors
- [ ] Previous version is serving traffic after rollback
- [ ] Health checks pass after rollback
- [ ] No data loss occurred (for database-impacting changes)
- [ ] Rollback completes within the estimated recovery time
- [ ] Team is notified after rollback (alert, Slack message)

## Post-Rollback Procedure

1. **Notify the team** — post in [incident channel]:
   ```
   ⚠️ ROLLBACK: [service] rolled back from [vX.Y.Z] to [vX.Y.Z-1]
   Reason: [failure description]
   Time: [timestamp]
   ```
2. **Verify health** — confirm health checks pass and traffic is flowing
3. **Create incident report** — document:
   - Failing version: [vX.Y.Z]
   - Failure symptoms: [description]
   - Rollback mechanism used: [mechanism]
   - Recovery time: [actual time]
   - User impact: [description and duration]
4. **Identify root cause** — investigate the deployment failure
5. **Fix forward** — deploy a fixed version (not the broken version)
6. **Update rollback script** — if the rollback revealed a gap, update and re-test
7. **Review rollback metrics** — track rollback frequency; high frequency indicates upstream quality issues

## Rollback vs Roll Forward Decision

| Criterion | Roll Back | Roll Forward |
|-----------|----------|--------------|
| Database schema change? | No (data loss risk) | Yes |
| Code-only bug? | Yes (if fast rollback) | Yes (if fix is ready) |
| Feature flag can disable? | Use flag instead | — |
| Hours since deployment? | < 1 hour: yes | > 24 hours: yes |
| Dependent services affected? | No: yes | Yes: yes (need coordination) |
