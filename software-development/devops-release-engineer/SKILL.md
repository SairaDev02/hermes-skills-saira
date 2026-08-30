---
name: devops-release-engineer
description: Define CI/CD, deployment, and release specifications.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [devops, ci-cd, deployment, release, monitoring, rollback, environment-management]
    related_skills: [code-reviewer, software-architecture-design, github-pr-workflow, github-code-review]
---

# DevOps / Release Engineer Skill

Guide the complete DevOps and release engineering lifecycle for LLM-generated code: from defining CI pipeline specifications (build, test, lint, security scan), through deployment pipeline specifications (staging to production with gates), environment specifications (dev, staging, production configs, secrets), release process definitions (versioning, changelog automation), monitoring and alerting specifications (health checks, error tracking, performance metrics), and rollback procedure specifications (one-command revert). Produces structured specification documents grounded in the DORA Four Keys (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Restore), the Google SRE Handbook (SLOs, error budgets), OWASP Secrets Management Cheat Sheet, Semantic Versioning 2.0.0, Conventional Commits, Keep a Changelog 1.1.0, the AWS Well-Architected Framework (automated rollback), and the Twelve-Factor App methodology (environment config). Does not review code (use `code-reviewer`), design architecture (use `software-architecture-design`), or write tests (use `qa-engineer`) — it consumes approved code from the Reviewer and architecture deployment diagrams from the Architect to specify the delivery pipeline. The coding harness (Pi) implements these specifications as actual CI/CD configs, deployment manifests, and scripts.

**Documentation-only constraint:** This skill produces specification documents only — CI pipeline specifications, deployment specifications, environment specifications, monitoring specifications, and rollback procedure specifications. It does not write CI/CD config files, deployment manifests, scripts, or any other executable configuration. All implementation is delegated to the coding harness (Pi). Pseudocode and diagramming languages (Mermaid, PlantUML) are permitted within specification documents.

## When to Use

- User asks to specify a CI pipeline (build, test, lint, security scan) for a project
- User needs to define a deployment pipeline specification with staging-to-production gates
- User wants to specify environment management (dev, staging, production) including secrets and configuration
- User needs to define a release process with versioning, changelog generation, and release notes
- User wants to specify monitoring, alerting, health checks, and performance metrics
- User needs to specify a rollback procedure and automation requirements
- Don't use for: code review (use `code-reviewer`), architecture design (use `software-architecture-design`), writing test suites (use `qa-engineer`), or creating task manifests (use `llm-task-engineering`) — DevOps consumes those artifacts to specify the delivery pipeline

## Prerequisites

- Approved code from the Code Reviewer — the DevOps role is situational and only activates after review approval
- Architecture deployment diagrams from the Architect — deployment topology, target environments, infrastructure requirements
- No external tools or API keys required — this skill is a structured methodology using Hermes tools (`write_file`, `read_file`, `search_files`, `patch`)
- For CI pipeline specification (Task 1): the project's CI platform must be identified (e.g., GitHub Actions, GitLab CI, CircleCI). Determine the platform from repository configuration files
- For deployment pipeline specification (Task 2): the target deployment platform must be known (e.g., Kubernetes, AWS, Azure, Vercel, Heroku)
- For environment specification (Task 3): a secrets management solution should be identified (e.g., HashiCorp Vault, AWS Secrets Manager, GitHub Secrets, Azure Key Vault). If none exists, the skill documents the requirement and recommends options
- For monitoring specification (Task 5): the target monitoring stack should be identified (e.g., Prometheus + Grafana, Datadog, New Relic). If none exists, the skill recommends an appropriate stack based on the project's infrastructure

## Procedure

The DevOps process is sequential — each task builds on the previous. Follow all six tasks in order for a complete delivery pipeline specification; enter at the relevant task for incremental work. Each task references a detailed reference or template file.

### Task 1: Specify CI Pipeline

Build, test, lint, and security scan on every push/merge. This is the automated guardrail that catches LLM regressions without human review. This task produces a CI pipeline specification document — Pi implements it as actual CI config files (e.g., `.github/workflows/ci.yml`).

1. **Identify the CI platform** — determine the project's CI platform from repository configuration files (`.github/workflows/`, `.gitlab-ci.yml`, `.circleci/config.yml`, `Jenkinsfile`). If none exists, recommend one appropriate for the project's hosting (GitHub Actions for GitHub repos, GitLab CI for GitLab repos). Completion criterion: the CI platform is identified and documented.
2. **Specify build stage** — document the build step: language runtime setup, dependency installation, compilation or transpilation. Identify the project's build command from `package.json`, `pyproject.toml`, `Makefile`, `Cargo.toml`, or equivalent. Completion criterion: the build command and runtime version are documented.
3. **Specify test stage** — document the test execution step: unit tests, integration tests, and test coverage reporting. Pull the test runner from the Tester's test suite (Task 5 of `qa-engineer`). Completion criterion: the test command, expected exit behavior, and coverage reporting are documented.
4. **Specify lint stage** — document the linting step: code style enforcement, type checking, import sorting. Identify the project's linter configuration (`.eslintrc`, `ruff.toml`, `.golangci.yml`, `clippy.toml`). Completion criterion: the lint command and expected behavior are documented.
5. **Specify security scan stage** — document the security scanning step: SAST (static analysis), dependency audit, secret detection. Pull the security scanning patterns from `code-reviewer`'s security review methodology. Identify available tools (`semgrep`, `bandit`, `gitleaks`, `pip-audit`, `npm audit`, `trivy`). Completion criterion: the security scan commands and expected behavior are documented.
6. **Specify trigger conditions** — document when the pipeline runs: on every push (for all branches or specific branches), on pull requests, on merges to the main branch, on tags, on a schedule (nightly). Completion criterion: every trigger condition is documented with its rationale.
7. **Specify caching strategy** — document dependency caching to reduce pipeline execution time: cache directories for package managers (`~/.cache/pip`, `node_modules`, `~/.cargo/registry`). Completion criterion: the caching strategy covers every dependency manager used by the project.
8. **Assemble the CI pipeline specification** — compile all stage specifications into a CI pipeline specification document. Use `templates/ci-pipeline-config.md` as the structuring template. See `references/ci-pipeline-design.md` for the full CI pipeline design methodology, stage ordering, and platform-specific patterns. Completion criterion: the CI pipeline specification document is complete and covers every stage.

Output: CI pipeline specification document. Pi implements this as the CI configuration file (e.g., `.github/workflows/ci.yml`).

### Task 2: Specify Deployment Pipeline

Staging to production with gates. Gate on: all tests pass, security scan clean, review approved. This task produces a deployment pipeline specification document — Pi implements it as actual deployment config files (e.g., Kubernetes manifests, Terraform modules, deploy workflows).

1. **Identify the deployment platform** — determine the target deployment platform from the architecture deployment diagrams. Completion criterion: the deployment platform, runtime, and target environments are documented.
2. **Specify environment promotion flow** — document the promotion path: dev to staging to production (or the project's equivalent). Each environment must have explicit entry and exit criteria. Completion criterion: every environment in the promotion flow has documented entry and exit criteria.
3. **Specify deployment gates** — document the gates that must pass before promotion: all CI checks pass, security scan clean, code review approved, test coverage above threshold, manual approval (for production). Completion criterion: every gate is documented with its pass/fail criteria and whether it is automatic or manual.
4. **Select deployment strategy** — choose the deployment strategy appropriate for the project: rolling update (default for Kubernetes), blue-green (for instant rollback capability), canary (for progressive rollout with metric-based promotion), feature flags (for runtime feature toggling). See `references/deployment-strategies.md` for the full strategy comparison and selection criteria. Completion criterion: the deployment strategy is selected with rationale.
5. **Specify deployment steps** — document the deployment workflow: artifact building, environment provisioning, configuration injection, health check verification, traffic switching. Completion criterion: every deployment step is documented in order with its verification check.
6. **Specify health checks** — document the health check endpoints and expected responses that validate a successful deployment. Specify startup, readiness, and liveness probes for containerized deployments. Completion criterion: every health check is documented with its endpoint, expected response, and failure behavior.
7. **Assemble the deployment pipeline specification** — compile all step specifications into a deployment pipeline specification document. Use `templates/deployment-config.md` as the structuring template. Completion criterion: the deployment pipeline specification document is complete and covers every step and health check.

Output: Deployment pipeline specification document. Pi implements this as deployment config files (e.g., Kubernetes manifests, Terraform modules, GitHub Actions deploy workflows).

### Task 3: Specify Environment Management

Dev, staging, production configs, secrets, variables. Secrets in `.env` or vault, never in config — mirrors Hermes's own invariant. This task produces an environment specification document — Pi implements it as actual config files (`.env.example`, vault policies, environment-specific config files).

1. **Enumerate environments** — list every environment the project requires: development, staging, production (and optionally preview/sandbox environments). Completion criterion: every environment is documented with its purpose and access policy.
2. **Specify environment variables per environment** — for each environment, list every configuration variable the application needs: database URLs, API endpoints, feature flags, logging level, CORS origins. Follow the Twelve-Factor App principle: config belongs in the environment, not the code. Completion criterion: every environment has a documented set of environment variables with their types and descriptions.
3. **Specify secrets management strategy** — document where secrets are stored and how they are accessed. Recommend a secrets vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GitHub Secrets) as the single source of truth. Never hardcode secrets in config files, environment files committed to version control, or Docker images. See `references/environment-management.md` for the full secrets management methodology, OWASP-aligned practices, and tool comparison. Completion criterion: the secrets management strategy covers every secret in every environment.
4. **Specify environment segregation** — ensure secrets intended for production are not available to development pipelines. Each environment has its own secret scope with distinct access policies. Completion criterion: every environment's secret scope is documented with its access policy.
5. **Specify secret rotation policy** — document how and when secrets are rotated: automated rotation schedules, key rotation procedures, and emergency rotation procedures. Completion criterion: every secret category has a documented rotation policy.
6. **Specify `.env.example` contents** — document every environment variable the application expects, with placeholder values and descriptions, to be committed to version control. Specify that the actual `.env` file must be in `.gitignore`. Completion criterion: the `.env.example` specification covers every environment variable and notes that `.env` must be in `.gitignore`.
7. **Assemble the environment specification** — compile all environment definitions into a structured document. Use `templates/environment-config.md` as the structuring template. Completion criterion: the environment specification document covers every environment, variable, secret, and access policy.

Output: Environment specification document. Pi implements this as config files (`.env.example`, vault policies, environment-specific config files).

### Task 4: Release Process Definition

Versioning scheme, changelog generation, release notes. Automate changelog from commit messages / PR titles. This task is already documentation-only — it produces a release process document that describes the process, not executable config.

1. **Select versioning scheme** — choose the versioning scheme appropriate for the project: Semantic Versioning (SemVer 2.0.0) for libraries and frameworks (MAJOR.MINOR.PATCH), Calendar Versioning (CalVer) for applications and distributions with rolling releases (YYYY.MM.PATCH). See `references/release-process.md` for the full versioning scheme comparison. Completion criterion: the versioning scheme is selected with rationale.
2. **Define conventional commit enforcement** — specify the commit message convention that enables automated version bumping and changelog generation: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `perf:`, `test:`, `chore:`, `BREAKING CHANGE:`). Define commit linting via commitlint, pre-commit hooks, or GitHub branch protection rules. Completion criterion: the commit convention is documented with its enforcement mechanism.
3. **Define changelog format** — specify the changelog format: Keep a Changelog 1.1.0 sections (Added, Changed, Deprecated, Removed, Fixed, Security). Specify whether the changelog is auto-generated from conventional commits (via `semantic-release`, `release-please`, `standard-version`, `git-cliff`) or manually curated. Completion criterion: the changelog format and generation method are documented.
4. **Define release artifact pipeline** — specify what artifacts are produced on release: container images, package registry publications (npm, PyPI, Maven), binary releases, documentation site updates. Completion criterion: every release artifact is documented with its publication target.
5. **Define release trigger** — specify what triggers a release: merge to main (continuous delivery), manual tag push, scheduled release (weekly/monthly), or release PR merge (release-please pattern). Completion criterion: the release trigger is documented with its rationale.
6. **Define release notes format** — specify the format for release notes: auto-generated from changelog, manually curated for major releases, or a combination. Include migration guidance for breaking changes. Completion criterion: the release notes format is documented with its generation method.
7. **Assemble the release process document** — compile all definitions into a structured release process document. Use `templates/release-process-doc.md` as the structuring template. Completion criterion: the release process document covers versioning, commit conventions, changelog, artifacts, triggers, and release notes.

Output: Release process document.

### Task 5: Specify Monitoring and Alerting

Health checks, error tracking, performance metrics. LLM-generated code may have subtle performance issues that only surface under load. This task produces a monitoring specification document — Pi implements it as actual monitoring config files (e.g., Prometheus alerting rules, Grafana dashboard JSON, Datadog monitor definitions).

1. **Identify the monitoring stack** — determine the target monitoring platform from the project's infrastructure (Prometheus + Grafana for Kubernetes, Datadog for cloud, New Relic for APM, Sentry for error tracking). If none exists, recommend one based on the infrastructure. See `references/monitoring-alerting.md` for the full monitoring stack comparison and selection criteria. Completion criterion: the monitoring stack is identified or recommended with rationale.
2. **Specify health checks** — document the health check endpoints and their expected responses: liveness (is the process running?), readiness (is the process ready to serve traffic?), and deep health checks (are dependencies — database, cache, message queue — reachable?). Completion criterion: every health check endpoint is documented with its expected response and failure behavior.
3. **Specify application metrics** — document the application-level metrics to collect: request rate, error rate, latency percentiles (p50, p95, p99), throughput, queue depth, cache hit rate. Follow the Google SRE four golden signals (latency, traffic, errors, saturation). Completion criterion: every golden signal has at least one metric defined for it.
4. **Specify infrastructure metrics** — document the infrastructure-level metrics to collect: CPU usage, memory usage, disk I/O, network I/O, container restart count, pod status. Completion criterion: every infrastructure metric is documented with its source (node exporter, cloud metrics API, etc.).
5. **Specify SLOs and error budgets** — document the Service Level Objectives for the system: availability target (e.g., 99.9% uptime), latency target (e.g., p99 < 500ms), error rate target (e.g., < 0.1%). Derive the error budget from the SLO (e.g., 99.9% = 43.2 minutes of downtime per month). Completion criterion: every SLO has a documented target, measurement method, and error budget.
6. **Specify alerting rules** — document the alerting rules based on SLOs and error budgets: page-worthy alerts (SLO burn rate exceeded, service down), ticket-worthy alerts (error budget depleting, latency degradation), and informational alerts (deployment completed, scale-up event). Follow SLO-based alerting to reduce alert noise. Completion criterion: every alert has a documented trigger condition, severity, and notification channel.
7. **Specify dashboards** — document the dashboards to create: service overview (golden signals), infrastructure overview (resource usage), deployment tracker (release frequency, change failure rate, MTTR — the DORA Four Keys). Completion criterion: every dashboard is documented with its panels and data sources.
8. **Assemble the monitoring specification** — compile all definitions into a structured monitoring specification document. Use `templates/monitoring-config.md` as the structuring template. Completion criterion: the monitoring specification document covers health checks, metrics, SLOs, alerts, and dashboards.

Output: Monitoring specification document. Pi implements this as monitoring config files (e.g., Prometheus alerting rules, Grafana dashboard JSON, Datadog monitor definitions).

### Task 6: Specify Rollback Procedure

One-command revert to previous known-good state. When an LLM-introduced regression reaches production, rollback speed is the damage limiter. This task produces a rollback procedure specification document — Pi implements it as an actual rollback script and associated automation.

1. **Identify the rollback mechanism** — determine the rollback mechanism available on the deployment platform: `kubectl rollout undo` (Kubernetes), blue-green traffic switch, canary rollout revert, previous artifact redeployment, Terraform state revert. See `references/rollback-automation.md` for the full rollback mechanism comparison and selection criteria. Completion criterion: the rollback mechanism is identified with its target platform.
2. **Specify rollback triggers** — document the conditions that trigger an automatic rollback: health check failure rate exceeds threshold (e.g., > 5% over 2 minutes), error rate exceeds threshold (e.g., > 2% over 2 minutes), p99 latency exceeds threshold (e.g., > 500ms over 2 minutes), deployment timeout. Define whether the trigger is automatic (monitoring-initiated) or manual (one-command). Completion criterion: every rollback trigger has a documented condition, threshold, and evaluation window.
3. **Specify database rollback strategy** — if the deployment includes database migrations, document the database rollback approach: expand-and-contract pattern (add new schema first, deploy new code, validate, then remove old schema in a follow-up migration), database backup restore (emergency only — data loss risk), forward-only migrations (no rollback, fix forward). Completion criterion: the database rollback strategy is documented with its data-loss risk assessment.
4. **Specify rollback script requirements** — document the requirements for the rollback script that Pi must implement: identify the previous known-good version, execute the rollback, verify health checks pass, and notify the team. Specify the script interface (command-line arguments, expected exit codes), the rollback steps as pseudocode, and the notification mechanism. Use `templates/rollback-procedure.md` as the structuring template. Completion criterion: the rollback script requirements specification is complete with pseudocode, interface, and verification steps.
5. **Specify rollback testing procedure** — document how the rollback is tested: schedule regular rollback drills in staging (at least quarterly), test after every deployment in staging, verify the rollback script works with the current deployment pipeline. Completion criterion: the rollback testing procedure is documented with its schedule and verification criteria.
6. **Specify post-rollback procedure** — document the steps after a rollback: notify the team, create an incident report, identify the root cause, fix forward (deploy a fixed version, not re-deploy the broken one), update the rollback script if the rollback revealed a gap. Completion criterion: the post-rollback procedure is documented with every step and its owner.
7. **Assemble the rollback procedure specification** — compile all definitions into a structured rollback procedure specification document. Use `templates/rollback-procedure.md` as the structuring template. Completion criterion: the rollback procedure specification covers mechanism, triggers, database strategy, script requirements, testing, and post-rollback steps.

Output: Rollback procedure specification document. Pi implements this as a rollback script and associated automation.

## Feedback Paths

- **From Code Reviewer (approval):** The Reviewer's approval verdict triggers the DevOps role. The feedback must include: the approved code artifact (diff, PR, or file set), the task spec, and the architecture deployment diagrams. DevOps consumes these to specify the delivery pipeline.
- **From Architect (deployment diagrams):** The architecture deployment diagrams define the target environments, deployment topology, and infrastructure requirements. If the deployment diagrams are missing or insufficient, feed back to the Architect with specific gaps (e.g., no staging environment defined, no health check endpoints specified).
- **To Code Reviewer (pipeline as guardrail):** The CI pipeline specification defines the automated checks that the Reviewer's manual review complements. If the CI pipeline catches an issue the Reviewer missed, feed back to the Reviewer to add the check to their review checklist.
- **To Task Engineer (pipeline failures):** If the CI pipeline or deployment fails due to a code issue, the failure report feeds back to the Task Engineer for re-dispatch. The feedback must include: the failing stage, the error output, the expected behavior, and the originating task spec.

## Quick Reference

| Task | Key Output | Reference / Template |
|------|------------|---------------------|
| 1. Specify CI pipeline | CI pipeline specification | `references/ci-pipeline-design.md`, `templates/ci-pipeline-config.md` |
| 2. Specify deployment pipeline | Deployment pipeline specification | `references/deployment-strategies.md`, `templates/deployment-config.md` |
| 3. Specify environment management | Environment specification | `references/environment-management.md`, `templates/environment-config.md` |
| 4. Release process definition | Release process doc | `references/release-process.md`, `templates/release-process-doc.md` |
| 5. Specify monitoring and alerting | Monitoring specification | `references/monitoring-alerting.md`, `templates/monitoring-config.md` |
| 6. Specify rollback procedure | Rollback procedure specification | `references/rollback-automation.md`, `templates/rollback-procedure.md` |

### DORA Four Keys

| Metric | Definition | Elite Tier |
|--------|-----------|------------|
| Deployment Frequency | How often code is deployed to production | Multiple deploys per day |
| Lead Time for Changes | Time from commit to production deployment | Less than one hour |
| Change Failure Rate | Percentage of deployments causing failures | 0-15% |
| Mean Time to Restore (MTTR) | Time to recover from a production failure | Less than one hour |

### Google SRE Four Golden Signals

| Signal | What to Measure | Example Metric |
|--------|----------------|----------------|
| Latency | Request processing time | p50, p95, p99 latency |
| Traffic | Request volume | Requests per second |
| Errors | Error rate | HTTP 5xx percentage |
| Saturation | Resource utilization | CPU, memory, disk, queue depth |

### Deployment strategy quick comparison

| Strategy | Rollback Speed | Infrastructure Cost | Best For |
|----------|---------------|-------------------|----------|
| Rolling update | 1-3 min (kubectl undo) | Low (reuses capacity) | Default for Kubernetes |
| Blue-green | < 1 min (traffic switch) | High (duplicate environment) | Instant rollback requirement |
| Canary | 1-5 min (revert traffic %) | Medium (extra instances) | Progressive rollout with metric gates |
| Feature flag | Seconds (toggle off) | Low | Runtime feature control |

### SemVer quick rules

- `feat:` commit → MINOR bump (1.2.0 → 1.3.0)
- `fix:` / `perf:` commit → PATCH bump (1.2.0 → 1.2.1)
- `BREAKING CHANGE:` or `feat!:` → MAJOR bump (1.2.0 → 2.0.0)
- `docs:`, `style:`, `refactor:`, `test:`, `chore:`, `ci:`, `build:` → No bump
- Pre-release: `2.0.0-alpha.1`, `1.3.0-rc.2`
- Build metadata: `1.2.3+build.42` (ignored for precedence)

### Secrets management quick rules

- Never hardcode secrets in code, config files, or Docker images
- Use a vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GitHub Secrets)
- Inject secrets at runtime via environment variables or vault sidecar
- Segregate by environment: dev secrets never available to prod pipelines
- Rotate automatically on a schedule
- Scan for leaked secrets with gitleaks or equivalent pre-commit hooks
- Maintain audit logs for all secret access

## Verification

- [ ] The CI pipeline specification defines build, test, lint, and security scan stages with trigger conditions
- [ ] The deployment pipeline specification defines staging-to-production promotion with explicit gates
- [ ] Every environment (dev, staging, production) has documented variables, secrets, and access policies
- [ ] No secrets are specified to be hardcoded in config files or committed to version control
- [ ] The `.env.example` specification covers every environment variable and notes that `.env` must be in `.gitignore`
- [ ] The release process defines a versioning scheme, commit convention, changelog format, and release artifacts
- [ ] The monitoring specification covers the four golden signals (latency, traffic, errors, saturation)
- [ ] Every SLO has a documented target, measurement method, and error budget
- [ ] Every alert has a trigger condition, severity, and notification channel
- [ ] The rollback procedure specification defines the mechanism, triggers, script requirements (as pseudocode), and testing procedure
- [ ] The database rollback strategy is documented with its data-loss risk assessment
- [ ] Feedback paths to Code Reviewer, Architect, and Task Engineer are documented as structured artifacts
