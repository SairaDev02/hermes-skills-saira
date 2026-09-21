# CI Pipeline Design Reference

This reference covers the design methodology for CI pipelines, stage ordering, platform-specific patterns, and LLM-specific considerations.

## Design Principles

1. **Fail fast** — order stages from fastest to slowest. Lint and type-check before full test suites. A syntax error should fail in seconds, not minutes.
2. **Fail clearly** — every failure must produce actionable output: the failing step, the error message, and the file/line responsible. LLM-generated code often fails in non-obvious ways; the pipeline output is the diagnostic.
3. **Cache aggressively** — dependency installation is the slowest non-test step. Cache package manager directories (`~/.cache/pip`, `node_modules`, `~/.cargo/registry`, `~/.gradle/caches`) keyed on lockfile hash.
4. **Isolate environments** — each stage runs in a clean container or VM. No state carries over between runs. LLM-generated code may have hidden side effects; isolation prevents false passes.
5. **Gate merges, not branches** — CI runs on pull requests and blocks merge on failure. Direct pushes to the main branch should be blocked by branch protection rules.

## Standard Stage Order

```
1. Checkout (actions/checkout@v4 with fetch-depth: 1 for speed; fetch-depth: 0 for tools needing full history)
2. Runtime setup (language version, toolchain)
3. Dependency install (cached)
4. Lint (fastest — syntax, style, import order)
5. Type check (if applicable — TypeScript, mypy, golangci-lint)
6. Build (compile, transpile, bundle)
7. Unit tests (fast, isolated)
8. Integration tests (slower, may need services)
9. Security scan (SAST, dependency audit, secret detection)
10. Coverage report (generate and upload as artifact)
```

## Platform-Specific Patterns

### GitHub Actions

- Workflows live in `.github/workflows/*.yml`
- Use `actions/checkout@v4`, `actions/setup-node@v4`, `actions/setup-python@v5`, `actions/setup-go@v5` for runtime setup
- Cache with `actions/cache@v4` using `hashFiles()` keys
- Use `services` for integration test dependencies (PostgreSQL, Redis, etc.)
- Matrix strategy for multi-version testing: `strategy.matrix.os: [ubuntu-latest, windows-latest]`, `strategy.matrix.python-version: ["3.11", "3.12"]`
- Use `concurrency` groups to cancel superseded runs on the same branch
- Secrets via `secrets.CONTEXT` — never echo or log secrets
- Use `permissions` block to apply least-privilege (read-only for PRs, write for deployment)

### GitLab CI

- Configuration in `.gitlab-ci.yml`
- Use `image:` to specify container per job
- Cache with `cache:key` and `paths`
- `services` block for integration dependencies
- `only:` / `rules:` for trigger control
- `environment` for deployment tracking
- `include` for shared pipeline definitions across repos

### CircleCI

- Configuration in `.circleci/config.yml`
- Use orbs for reusable commands (`circleci/python-orb`, `circleci/node-orb`)
- `cache` keys with checksums
- `machine` executor for Docker-in-Docker
- `workflows` for parallel job orchestration

## LLM-Specific Considerations

LLM-generated code has distinct failure patterns that the CI pipeline must catch:

1. **Scope creep** — LLM may modify files outside the task scope. Add a step that diffs changed files against the task spec's scope field and fails on out-of-scope modifications.
2. **Inconsistent conventions** — each LLM session may produce different coding styles. Lint rules must be strict and non-negotiable; they are the only consistent enforcement.
3. **Dependency drift** — LLM may add new dependencies. The pipeline should detect uncommitted changes to lockfiles and flag them for review.
4. **Silent failures** — LLM code often catches exceptions and returns default values instead of propagating errors. Add test coverage thresholds to ensure error paths are exercised.
5. **Debug artifacts** — LLM may leave `print()`, `console.log()`, TODO comments, or commented-out code. Add a check that scans for debug artifacts and fails if found.

## SAST and Dependency Audit Tools

| Tool | Language | Purpose |
|------|----------|---------|
| semgrep | Multi | Pattern-based SAST with custom rules |
| bandit | Python | Python-specific SAST |
| gitleaks | Multi | Secret detection in git history and diffs |
| pip-audit | Python | Python dependency vulnerability audit |
| npm audit | JavaScript | npm dependency vulnerability audit |
| trivy | Multi | Container image and filesystem vulnerability scan |
| snyk | Multi | Commercial SAST + dependency audit |

If no SAST tools are available, use grep-based fallback patterns (see `code-reviewer`'s `references/security-review.md` for the grep patterns).

## Caching Best Practices

- Key caches on lockfile hashes: `key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}`
- Use restore-keys for partial cache hits: `restore-keys: ${{ runner.os }}-pip-`
- Cache the build output directory if builds are expensive
- Do NOT cache test output or coverage reports — these must be regenerated every run
- Set cache timeout to fail the build if cache operations hang

## Concurrency Control

- Use concurrency groups to cancel in-progress runs when a new commit is pushed to the same branch
- GitHub Actions: `concurrency: { group: ${{ github.ref }}, cancel-in-progress: true }`
- This saves CI minutes and prevents stale results from masking newer failures
