# CI Pipeline Configuration Template

## CI Platform

- **Platform:** [GitHub Actions / GitLab CI / CircleCI / Jenkins]
- **Config file path:** [.github/workflows/ci.yml / .gitlab-ci.yml / .circleci/config.yml / Jenkinsfile]

## Triggers

| Trigger | Branch/Event | Rationale |
|---------|-------------|-----------|
| Push | [branch names or `**`] | [why] |
| Pull request | [target branches] | [why] |
| Schedule | [cron expression] | [why] |
| Tag | [tag pattern] | [why] |

## Stages

### 1. Checkout
- **Tool:** [actions/checkout@v4 / git clone / included]
- **Fetch depth:** [1 for speed / 0 for full history needed]
- **Completion criterion:** Source code is checked out

### 2. Runtime Setup
- **Language:** [Python 3.11 / Node 20 / Go 1.22 / Rust 1.75]
- **Tool:** [actions/setup-python@v5 / actions/setup-node@v4 / etc.]
- **Completion criterion:** Runtime is installed and available

### 3. Dependency Install
- **Package manager:** [pip / npm / yarn / cargo / go mod]
- **Lockfile:** [requirements.txt / package-lock.json / Cargo.lock / go.sum]
- **Cache key:** [hashFiles('**/package-lock.json') / etc.]
- **Completion criterion:** Dependencies installed and cached

### 4. Lint
- **Linter:** [ruff / eslint / golangci-lint / clippy]
- **Command:** [`ruff check .` / `eslint .` / etc.]
- **Fail on:** [any warning / errors only]
- **Completion criterion:** Linter passes with zero errors

### 5. Type Check (if applicable)
- **Tool:** [mypy / tsc / pyright]
- **Command:** [`mypy .` / `tsc --noEmit`]
- **Completion criterion:** Type check passes with zero errors

### 6. Build
- **Command:** [npm run build / python -m build / cargo build --release / go build ./...]
- **Output:** [dist/ / target/ / build/]
- **Completion criterion:** Build produces expected artifacts

### 7. Unit Tests
- **Runner:** [pytest / jest / go test / cargo test]
- **Command:** [`pytest tests/unit/ -v --cov` / `jest --coverage`]
- **Expected:** [all tests pass, coverage > X%]
- **Completion criterion:** All unit tests pass

### 8. Integration Tests
- **Runner:** [pytest / jest / go test]
- **Command:** [`pytest tests/integration/ -v`]
- **Services:** [PostgreSQL, Redis, etc. — list with versions]
- **Completion criterion:** All integration tests pass

### 9. Security Scan
- **SAST:** [semgrep / bandit / none]
- **Dependency audit:** [pip-audit / npm audit / trivy]
- **Secret detection:** [gitleaks / trufflehog / none]
- **Completion criterion:** Security scan completes with zero critical findings

### 10. Coverage Report
- **Tool:** [coverage.py / jest --coverage / codecov]
- **Upload:** [actions/upload-artifact@v4 / codecov-action]
- **Completion criterion:** Coverage report is generated and uploaded

## Concurrency Control

- **Group:** [github.ref / branch name]
- **Cancel in progress:** [true/false]

## Permissions

- **PR checks:** [read-only]
- **Deployment:** [write — only on deployment jobs]
