# Cross-Cutting Concerns Reference

Cross-cutting concerns affect every module. If they aren't specified, each downstream LLM will invent its own — guaranteed inconsistency. This is the complete checklist for Task 6.

## Complete Checklist

### 1. Error Handling

**What:** How the system detects, reports, and recovers from errors.

**Specify:**
- Error response format (e.g., RFC 7807 Problem Details for REST APIs)
- Error categorization: client errors (4xx), server errors (5xx), business rule violations
- Error codes: unique codes per error type (e.g., `AUTH_001`, `VALIDATION_002`)
- Error propagation: does the caller see the original error or a wrapped error?
- Retry strategy: which errors are retryable, max retries, backoff policy
- Circuit breaker: thresholds for opening/closing, timeout duration

**Owning module:** Error handling middleware / cross-cutting library module.

### 2. Logging

**What:** What to log, at what level, and in what format.

**Specify:**
- Log levels: DEBUG, INFO, WARN, ERROR — when to use each
- Log format: structured (JSON) vs plain text — specify the exact schema
- Required fields: timestamp (ISO 8601), correlation ID, module name, request ID
- What NOT to log: passwords, tokens, PII, full request bodies
- Log destination: stdout (container), file, log aggregation service
- Sampling: high-volume logs (e.g., health checks) — sample rate

**Owning module:** Logging configuration / observability module.

### 3. Authentication

**What:** How the system verifies identity.

**Specify:**
- Auth mechanism: OAuth 2.0, JWT, API keys, session cookies, mTLS
- Token format: JWT claims structure (sub, iss, exp, roles)
- Token lifecycle: issuance, refresh, revocation, expiration
- Auth flow: where auth happens (API gateway, service, both)
- Credential storage: hashing algorithm (Argon2id, bcrypt), where secrets live (vault, not code)

**Owning module:** Auth service / auth middleware.

### 4. Authorization

**What:** How the system enforces what an authenticated identity can do.

**Specify:**
- Authorization model: RBAC, ABAC, resource-based, claims-based
- Permission definitions: list of permissions and their codes
- Enforcement point: where authorization checks happen (gateway, service, data layer)
- Denial handling: what happens on unauthorized access (403, custom error)
- Multi-tenancy: if applicable, how tenant isolation is enforced

**Owning module:** Authz middleware / policy engine.

### 5. Data Validation

**What:** How the system validates input at boundaries.

**Specify:**
- Validation location: API boundary (first line of defense), domain layer (business rules)
- Validation strategy: fail-fast (reject entire input on first error) vs collect-all
- Error reporting: field-level errors with codes
- Schema validation: JSON Schema, OpenAPI spec, or language-specific validators
- Sanitization: what gets stripped/escaped and where

**Owning module:** API gateway validation / domain validation layer.

### 6. Configuration Management

**What:** How the system loads and manages configuration.

**Specify:**
- Config sources: environment variables, config files, config server, vault
- Config hierarchy: defaults → file → env vars → command-line args (later overrides earlier)
- Secrets management: secrets never in code or config files; use vault or env-only
- Config schema: what configuration keys exist, their types, and defaults
- Hot reload: can config change without restart?

**Owning module:** Config service / bootstrap module.

### 7. Observability (Metrics & Tracing)

**What:** How the system exposes its internal state for monitoring.

**Specify:**
- Metrics: what to measure (request count, latency, error rate, resource utilization)
- Metric format: Prometheus, StatsD, CloudWatch
- Distributed tracing: OpenTelemetry, Jaeger, Zipkin — trace propagation headers
- Health checks: liveness (is it running?) vs readiness (is it ready to serve?)
- Dashboards: what dashboards exist and their panels

**Owning module:** Observability middleware / monitoring agent.

### 8. Data Flow & Request Lifecycle

**What:** How a request travels through the system.

**Specify:**
- Request entry point: API gateway, load balancer, direct
- Middleware chain: auth → validation → rate limiting → logging → handler
- Correlation ID: how it's generated, propagated, and logged
- Response lifecycle: response formatting, status code conventions, headers
- Timeout: per-request timeout, per-downstream-call timeout

**Owning module:** Request pipeline / middleware chain.

### 9. Internationalization (i18n) — If Applicable

**What:** How the system supports multiple languages and locales.

**Specify:**
- Supported locales: list
- String externalization: resource bundles, translation files
- Date/time/number formatting: locale-aware
- Character encoding: UTF-8 everywhere
- Direction: LTR/RTL support if needed

**Owning module:** i18n service / localization module.

### 10. Caching — If Applicable

**What:** What data is cached, where, and for how long.

**Specify:**
- Cache layers: client-side, CDN, API gateway, application, database
- Cache invalidation strategy: TTL, event-based, manual
- Cache key structure: how keys are constructed
- Cache storage: Redis, in-memory, CDN edge
- Cache miss behavior: what happens on a miss (load from source, return stale)

**Owning module:** Cache service / caching middleware.

### 11. Rate Limiting & Throttling — If Applicable

**What:** How the system protects itself from overload.

**Specify:**
- Rate limit strategy: token bucket, sliding window, fixed window
- Limits: per-user, per-IP, per-API-key, global
- Response on limit exceeded: 429 Too Many Requests with Retry-After header
- Throttling: graceful degradation vs hard rejection

**Owning module:** Rate limiter middleware / API gateway.

## Specification Template

For each concern, produce a spec entry:

```markdown
### <Concern Name>

**Strategy:** <one-sentence description>
**Pattern:** <pattern or approach used>
**Owning module:** <module name>
**Conventions:**
- <convention 1>
- <convention 2>
**Code constraint for tasks:** <what the Task Engineer must include in task constraints>
```

Every convention must be concrete enough to include verbatim in a task's `constraints` field — if it's vague, the downstream LLM will invent its own version.
