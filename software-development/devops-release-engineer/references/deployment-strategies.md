# Deployment Strategies Reference

This reference covers the deployment strategies available, their trade-offs, and selection criteria.

## Strategy Comparison

### Rolling Update (Default for Kubernetes)

**How it works:** Replace old pods with new ones gradually. The deployment controller creates new pods, waits for them to pass readiness checks, then terminates old pods.

**Rollback:** `kubectl rollout undo deployment/<name>` reverts to the previous ReplicaSet. Kubernetes retains 10 old ReplicaSets by default (controlled by `revisionHistoryLimit`).

**Pros:**
- No additional infrastructure cost (reuses existing capacity)
- No downtime if readiness probes are configured correctly
- Simple to configure

**Cons:**
- Rollback takes 1-3 minutes (pod recreation cycle)
- Old and new versions run simultaneously during the rollout window
- Cannot run A/B tests or progressive rollouts

**Best for:** Default choice for stateless services on Kubernetes.

### Blue-Green Deployment

**How it works:** Run two identical environments (blue and green). Deploy the new version to the inactive environment, run validation tests, then switch traffic from active to inactive.

**Rollback:** Switch traffic back to the previous active environment. Under 1 minute.

**Pros:**
- Instant rollback (traffic switch, not redeployment)
- Zero downtime
- Full validation before traffic switches

**Cons:**
- Double infrastructure cost (two full environments)
- Database migrations complicate rollback (both versions must be compatible with the schema)
- Requires load balancer or DNS-level traffic switching

**Best for:** Systems where rollback speed is a hard requirement and the team can afford the infrastructure cost. Critical production services.

### Canary Deployment

**How it works:** Roll out the new version to a small subset of users/instances (e.g., 5%), monitor metrics, and gradually increase the percentage if health checks pass.

**Rollback:** Stop the rollout and revert traffic to 100% on the stable version. 1-5 minutes.

**Pros:**
- Limits blast radius (only a small percentage of users are affected by a bad release)
- Metric-based promotion (automatic rollback on SLO breach)
- No additional infrastructure cost beyond the canary instances

**Cons:**
- More complex to configure (traffic splitting, metric analysis)
- Requires a metric analysis system (e.g., Argo Rollouts, Flagger)
- Database migrations must be compatible with both versions during the canary window

**Best for:** High-traffic services where gradual rollout with automated metric-based promotion is valuable. API gateway deployments.

### Feature Flags

**How it works:** Deploy the new code with the feature disabled at runtime. Enable the feature for specific users or percentages via a feature flag service (e.g., LaunchDarkly, Unleash, Flagsmith).

**Rollback:** Toggle the flag off. Seconds.

**Pros:**
- Fastest rollback (runtime toggle, no deployment)
- Decoupled from deployment pipeline
- Enables A/B testing and progressive feature rollout
- Works with any deployment strategy

**Cons:**
- Does not revert code changes — the broken code is still deployed, just disabled
- Requires a feature flag service or in-process flag system
- Technical debt accumulates if old flags are not cleaned up

**Best for:** Application-level bugs that do not require infrastructure changes. Pair with canary for automated rollback based on metrics.

## Selection Criteria

| Criterion | Rolling | Blue-Green | Canary | Feature Flag |
|-----------|---------|------------|--------|--------------|
| Rollback speed | 1-3 min | < 1 min | 1-5 min | Seconds |
| Infrastructure cost | Low | High | Medium | Low |
| Configuration complexity | Low | Medium | High | Medium |
| Blast radius limit | No | Yes (full switch) | Yes (percentage) | Yes (per-feature) |
| Metric-based auto-rollback | No | No | Yes | Yes (with canary) |
| Database migration safety | Requires compat | Requires compat | Requires compat | N/A |

## Decision Flow

1. **Is the service stateless and on Kubernetes?** → Start with rolling update (default, lowest cost)
2. **Is instant rollback a hard requirement?** → Blue-green (if infrastructure budget allows) or feature flag (for application-level rollback)
3. **Is the service high-traffic and metric-driven?** → Canary with automated promotion/rollback
4. **Is the issue a feature-level bug, not an infrastructure issue?** → Feature flag
5. **Can you combine strategies?** → Yes: feature flags inside canary inside blue-green. Each layer adds a rollback mechanism.

## Database Migration Compatibility

All deployment strategies that run old and new versions simultaneously require database migration compatibility:

- **Expand-and-contract pattern:** Add new columns/tables (expand), deploy new code, validate, then remove old columns/tables (contract) in a follow-up migration. The old code version must tolerate the new schema.
- **Forward-only migrations:** Never revert a migration. If a deployment fails, fix forward with a new migration rather than rolling back the database.
- **Backup restore:** Emergency only — restores from backup, causing data loss for any changes made between backup and restore.

## Health Check Requirements

Every deployment strategy requires health checks to validate the new version before traffic is routed to it:

- **Startup probe:** Has the process started? (Kubernetes: `startupProbe`)
- **Readiness probe:** Is the process ready to serve traffic? (Kubernetes: `readinessProbe`) — used by the load balancer to determine traffic routing
- **Liveness probe:** Is the process still healthy? (Kubernetes: `livenessProbe`) — used by the orchestrator to decide whether to restart
- **Deep health check:** Are dependencies (database, cache, message queue) reachable? — endpoint that verifies all external connections

Health checks must have:
- A timeout (don't wait indefinitely)
- A failure threshold (don't fail on first try)
- A success threshold (don't declare healthy on first success)
- A defined expected response (HTTP 200, specific JSON body, TCP connection accepted)
