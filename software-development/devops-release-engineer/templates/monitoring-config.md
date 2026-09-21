# Monitoring Configuration Template

## Monitoring Stack

- **Platform:** [Prometheus + Grafana / Datadog / New Relic / Sentry / OpenTelemetry]
- **Selection rationale:** [why this stack was selected]

## Health Checks

| Probe Type | Endpoint | Expected Response | Timeout | Failure Threshold | Success Threshold |
|------------|----------|-------------------|---------|-------------------|-------------------|
| Startup | [/startup] | [HTTP 200] | [300s] | [30] | [1] |
| Readiness | [/ready] | [HTTP 200] | [5s] | [3] | [1] |
| Liveness | [/health] | [HTTP 200] | [5s] | [3] | [1] |
| Deep | [/health/deep] | [HTTP 200 + deps verified] | [10s] | [3] | [1] |

## Application Metrics (Golden Signals)

### Latency

| Metric | Source | Aggregation | Alert Threshold |
|--------|--------|-------------|----------------|
| http_request_duration_seconds | [Prometheus histogram / APM] | p50, p95, p99 | p99 > [500ms] for 2 min |
| grpc_request_duration_seconds | [Prometheus histogram] | p50, p95, p99 | p99 > [200ms] for 2 min |

### Traffic

| Metric | Source | Aggregation | Alert Threshold |
|--------|--------|-------------|----------------|
| http_requests_total | [Prometheus counter] | rate per second | Spike > [3x baseline] |
| active_connections | [app gauge] | current value | > [max_connections * 0.8] |

### Errors

| Metric | Source | Aggregation | Alert Threshold |
|--------|--------|-------------|----------------|
| http_requests_errors_total | [Prometheus counter] | rate (5xx) | > [0.1%] of total for 2 min |
| exceptions_total | [app counter / Sentry] | rate per second | > [1/sec] for 5 min |

### Saturation

| Metric | Source | Aggregation | Alert Threshold |
|--------|--------|-------------|----------------|
| cpu_usage_percent | [node exporter / cloud metrics] | current | > [80%] for 5 min |
| memory_usage_percent | [node exporter / cloud metrics] | current | > [85%] for 5 min |
| disk_usage_percent | [node exporter / cloud metrics] | current | > [80%] for 10 min |
| queue_depth | [app gauge / message broker] | current | > [1000] for 5 min |
| db_connection_pool_usage | [app gauge] | current | > [80%] for 5 min |

## Infrastructure Metrics

| Metric | Source | Alert Threshold |
|--------|--------|----------------|
| container_restarts_total | [kube-state-metrics] | > [3] in 10 min |
| pod_status_failed | [kube-state-metrics] | > [0] for 2 min |
| node_cpu_usage | [node exporter] | > [85%] for 10 min |
| node_memory_usage | [node exporter] | > [90%] for 5 min |
| disk_io_wait | [node exporter] | > [20%] for 5 min |

## SLOs and Error Budgets

| Service | SLO | Target | Error Budget (30-day month) | Measurement Method |
|---------|-----|--------|------------------------------|-------------------|
| [API Gateway] | Availability | 99.9% | 43.2 min downtime | Uptime probe + synthetic check |
| [API Gateway] | Latency (p99) | < 500ms | — | Prometheus histogram p99 over 5 min |
| [API Gateway] | Error rate | < 0.1% | — | 5xx rate / total request rate |

### Error Budget Policy

- **Healthy budget:** Proceed with releases and feature deployments
- **At risk (>50% consumed, >50% of period remaining):** Additional review required for releases
- **Depleted:** Freeze non-critical releases; focus on reliability improvements

## Alerting Rules

| Alert Name | Severity | Trigger Condition | Evaluation Window | Notification Channel | Runbook |
|------------|----------|-------------------|-------------------|----------------------|---------|
| ServiceDown | Critical | up == 0 | 60s | [PagerDuty + Slack] | [runbook URL] |
| HighErrorRate | Critical | error_rate > 2% | 2 min | [PagerDuty + Slack] | [runbook URL] |
| HighLatencyP99 | High | p99 > 500ms | 2 min | [Slack] | [runbook URL] |
| DiskSpaceWarning | Medium | disk > 80% | 10 min | [Slack + Email] | [runbook URL] |
| DeploymentCompleted | Low | deployment_created == 1 | — | [Slack] | — |

## Dashboards

### Service Overview Dashboard
- **Panels:** Request rate, error rate, p50/p95/p99 latency, saturation (CPU, memory, queue depth)
- **Data source:** [Prometheus / Datadog]
- **Refresh interval:** [10s]

### Infrastructure Overview Dashboard
- **Panels:** Node CPU, memory, disk, network; pod status; container restarts
- **Data source:** [node exporter / cloud metrics]
- **Refresh interval:** [30s]

### DORA Four Keys Dashboard
- **Panels:** Deployment frequency (count per day), Lead time for changes (commit to deploy), Change failure rate (% of deployments causing incidents), MTTR (incident open to resolved)
- **Data source:** [CI/CD platform API + incident tracker API]
- **Refresh interval:** [1h]
