# Deployment Configuration Template

## Deployment Platform

- **Platform:** [Kubernetes / AWS ECS / Azure App Service / Vercel / Heroku / Docker Compose]
- **Deployment strategy:** [Rolling / Blue-Green / Canary / Feature Flag]
- **Strategy rationale:** [why this strategy was selected]

## Environment Promotion Flow

```
Dev → Staging → Production
```

| Environment | Entry Criteria | Exit Criteria |
|-------------|---------------|---------------|
| Dev | Code compiles, unit tests pass | CI pipeline green |
| Staging | CI pipeline green, all tests pass | Deployment gates pass, health checks green |
| Production | Staging validated, manual approval | Deployment healthy for [duration] |

## Deployment Gates

| Gate | Type | Pass Criteria |
|------|------|---------------|
| CI checks | Automatic | All CI stages pass |
| Security scan | Automatic | Zero critical/high vulnerabilities |
| Test coverage | Automatic | Coverage > [X]% |
| Code review | Automatic | PR approved by reviewer |
| Manual approval | Manual | [Role] approves production deployment |

## Deployment Steps

### 1. Build Artifact
- **Command:** [docker build / npm run build / go build]
- **Output:** [image:tag / dist/ / binary]
- **Verification:** [image scans clean / build produces expected files]

### 2. Environment Provisioning
- **Tool:** [Terraform / Helm / kubectl / CloudFormation]
- **Config:** [terraform.tfvars / values.yaml / kustomization.yaml]
- **Verification:** [infrastructure is healthy and ready]

### 3. Configuration Injection
- **Method:** [environment variables / config maps / vault sidecar]
- **Secrets source:** [HashiCorp Vault / AWS Secrets Manager / GitHub Secrets]
- **Verification:** [all config values are set, no missing secrets]

### 4. Deploy
- **Command:** [kubectl apply / helm upgrade / vercel --prod / docker compose up]
- **Strategy:** [rolling update / blue-green switch / canary 5% → 100%]
- **Verification:** [deployment reaches desired state]

### 5. Health Check Verification
- **Endpoint:** [/health / /ready / /healthz]
- **Expected response:** [HTTP 200, body: {"status":"ok"}]
- **Timeout:** [60 seconds]
- **Failure behavior:** [abort deployment, trigger rollback]

### 6. Traffic Switch (if applicable)
- **Method:** [DNS switch / load balancer weight / slot swap / traffic percentage]
- **Verification:** [traffic is flowing to the new version]

## Health Checks

| Probe Type | Endpoint | Expected Response | Timeout | Failure Threshold | Success Threshold |
|------------|----------|-------------------|---------|-------------------|-------------------|
| Startup | /startup | HTTP 200 | 300s | 30 failures | 1 success |
| Readiness | /ready | HTTP 200 | 5s | 3 failures | 1 success |
| Liveness | /health | HTTP 200 | 5s | 3 failures | 1 success |
| Deep | /health/deep | HTTP 200 + all deps | 10s | 3 failures | 1 success |

## Rollback

- **Mechanism:** [kubectl rollout undo / slot swap back / canary abort / redeploy previous]
- **Trigger:** [automatic on health check failure / manual one-command]
- **Rollback script:** [path/to/rollback.sh]
- **Recovery time:** [estimated time]
