# Monitoring and Alerting Reference

This reference covers monitoring stack selection, SLO-based alerting, the Google SRE four golden signals, DORA Four Keys, and observability best practices.

## Monitoring Stack Comparison

| Stack | Type | Best For | Key Components |
|-------|------|----------|----------------|
| Prometheus + Grafana | Open-source | Kubernetes, cloud-native | Prometheus (metrics), Grafana (dashboards), Alertmanager (alerts), Loki (logs), Tempo (traces) |
| Datadog | SaaS | Cloud, multi-cloud, full-stack APM | APM, logs, metrics, RUM, synthetic monitoring |
| New Relic | SaaS | APM-focused, Ruby/Java/Python | APM, infrastructure, logs, distributed tracing |
| Sentry | SaaS | Error tracking | Real-time error tracking, release tracking, session replay |
| OpenTelemetry | Open standard | Vendor-neutral observability | Collectors, SDKs, exporters to any backend |
| Hyperping | SaaS | Uptime monitoring, status pages | Uptime checks, SSL monitoring, cron monitoring |
| ELK Stack | Open-source | Log-centric | Elasticsearch, Logstash, Kibana |

## Google SRE Four Golden Signals

These four signals are the minimum set of metrics that must be monitored for any user-facing system:

### Latency
- **What:** Time to service a request
- **Measure:** p50, p95, p99 latency (never average — averages hide tail latency)
- **Alert:** p99 latency exceeds SLO threshold for sustained period
- **Trap:** Track error latency separately from success latency — error responses are often fast, skewing the average down

### Traffic
- **What:** Request volume
- **Measure:** Requests per second, transactions per second, messages per second
- **Alert:** Sudden spike (possible DDoS or viral traffic) or sudden drop (possible upstream failure)
- **Use:** Capacity planning, autoscaling triggers

### Errors
- **What:** Rate of failed requests
- **Measure:** HTTP 5xx rate, exception rate, error log rate
- **Alert:** Error rate exceeds SLO threshold (e.g., > 0.1% over 5 minutes)
- **Trap:** Count client errors (4xx) separately from server errors (5xx) — 4xx is user error, 5xx is your bug

### Saturation
- **What:** Resource utilization — how full the system is
- **Measure:** CPU usage, memory usage, disk I/O, network I/O, queue depth, connection pool usage, cache hit rate
- **Alert:** Utilization exceeds 80% sustained (leave headroom for traffic spikes)
- **Trap:** Saturation often causes latency to increase before errors appear — monitor saturation as a leading indicator

## SLOs and Error Budgets

### SLO Definition

An SLO is a target reliability level, expressed as a percentage:

| SLO | Uptime | Allowed Downtime (30-day month) | Use Case |
|-----|--------|--------------------------------|----------|
| 99% | 99% | 7.2 hours | Internal tools, non-critical |
| 99.9% | 99.9% | 43.2 minutes | User-facing services |
| 99.95% | 99.95% | 21.6 minutes | Critical business services |
| 99.99% | 99.99% | 4.3 minutes | Critical infrastructure, payment systems |
| 99.999% | 99.999% | 26 seconds | Telecom, emergency systems |

### Error Budget

Error budget = 100% - SLO. If SLO is 99.9%, the error budget is 0.1% (43.2 minutes of downtime per month).

**Error budget policy:**
- When error budget is healthy → proceed with releases and feature deployments
- When error budget is depleted → freeze non-critical releases, focus on reliability improvements
- When error budget is at risk (> 50% consumed and > 50% of month remaining) → require additional review for releases

### SLO-Based Alerting

SLO-based alerting reduces alert volume by up to 85% (Google SRE Handbook) by focusing on user impact rather than individual metrics:

- **Burn rate alerts:** Alert when the error budget is being consumed faster than allowed (e.g., 2% of budget in 1 hour = sustained burn rate)
- **Multi-window alerts:** Check burn rate over both short (5 min) and long (1 hour) windows — only alert if both exceed the threshold, reducing false positives from transient spikes
- **Page-worthy:** Error budget will be exhausted within 1 hour at current burn rate
- **Ticket-worthy:** Error budget is being consumed faster than sustainable but not urgently

## DORA Four Keys

The DORA Four Keys measure DevOps performance:

| Metric | Definition | Elite | High | Medium | Low |
|--------|-----------|-------|------|--------|-----|
| Deployment Frequency | How often code is deployed to production | Multiple deploys/day | 1/week | 1/month | < 1/month |
| Lead Time for Changes | Time from commit to production | < 1 hour | 1 day | 1 week | 1 month |
| Change Failure Rate | % of deployments causing failures | 0-15% | 16-30% | 16-30% | > 30% |
| MTTR | Time to recover from production failure | < 1 hour | 1 day | 1 day | 1 week |

**Dashboard:** Track these as time-series metrics. Deployment frequency and lead time measure throughput; change failure rate and MTTR measure stability.

## Alert Severity and Notification

| Severity | Response Time | Examples | Notification Method |
|----------|--------------|----------|---------------------|
| Critical | Immediate | Complete service outage, security breach, data loss | All channels, escalation policy |
| High | 30 minutes | Service partial outage, critical component degradation | Phone call, SMS, Slack |
| Medium | 1-4 hours | Performance degradation, non-critical errors | Team channel, email |
| Low | Next business day | Disk usage at 60%, non-critical warnings | Email, dashboard |

## Alerting Best Practices

1. **Actionable alerts** — every alert must have a documented runbook with the response procedure
2. **Reduce alert fatigue** — SLO-based alerting, multi-window checks, suppress alerts during maintenance windows
3. **Alert on symptoms, not causes** — alert on "users seeing errors" not "CPU at 90%" (the former is the impact, the latter might be fine)
4. **Escalation policies** — define who is paged, in what order, and how to escalate if the primary on-call doesn't respond
5. **Alert annotations** — include the runbook URL, dashboard link, and mitigation steps in the alert annotation
6. **Regular review** — review alert history quarterly: which alerts fired, were they actionable, should thresholds be adjusted

## Observability Pillars

| Pillar | Purpose | Tool Examples |
|--------|---------|---------------|
| Metrics | Alerting, performance trends, capacity planning | Prometheus, Datadog, CloudWatch |
| Logs | Event debugging, error diagnosis, audit trails | Loki, ELK, Datadog Logs |
| Traces | Distributed request analysis, microservice latency | Jaeger, Tempo, OpenTelemetry |

All three are needed for full observability. Metrics tell you *what* is wrong, logs tell you *why*, and traces tell you *where*.
