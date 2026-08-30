# Release Process Document Template

## Versioning

- **Scheme:** [Semantic Versioning 2.0.0 / Calendar Versioning]
- **Rationale:** [why this scheme was selected]
- **Version source:** [package.json / pyproject.toml / Cargo.toml / VERSION file]

### SemVer Rules (if SemVer selected)

| Commit Type | Version Bump | Example |
|-------------|-------------|---------|
| `feat:` | MINOR | 1.2.0 → 1.3.0 |
| `fix:` / `perf:` | PATCH | 1.2.0 → 1.2.1 |
| `BREAKING CHANGE:` / `feat!:` | MAJOR | 1.2.0 → 2.0.0 |
| `docs:`, `style:`, `refactor:`, `test:`, `chore:`, `ci:`, `build:` | None | 1.2.0 |

## Commit Convention

- **Standard:** Conventional Commits 1.0.0
- **Format:** `<type>[scope]: <description>`
- **Enforcement:** [commitlint / branch protection rules / pre-commit hook]

### Accepted Types

| Type | Description | Version Impact |
|------|-------------|----------------|
| feat | New feature | MINOR |
| fix | Bug fix | PATCH |
| docs | Documentation | None |
| style | Formatting | None |
| refactor | Code refactor | None |
| perf | Performance improvement | PATCH |
| test | Test changes | None |
| build | Build system | None |
| ci | CI configuration | None |
| chore | Maintenance | None |
| revert | Revert previous commit | None |

### Breaking Changes

- **Marker:** `!` after type/scope (e.g., `feat(auth)!: redesign login`) or `BREAKING CHANGE:` in footer
- **Migration guide:** Required in release notes for every breaking change

## Changelog

- **Format:** Keep a Changelog 1.1.0
- **Generation:** [auto-generated from conventional commits / manually curated]
- **Tool:** [semantic-release / release-please / standard-version / git-cliff]
- **File:** [CHANGELOG.md / docs/CHANGELOG.md]

### Changelog Sections

- **Added** — new features
- **Changed** — changes in existing functionality
- **Deprecated** — soon-to-be removed features
- **Removed** — removed features
- **Fixed** — bug fixes
- **Security** — vulnerability patches (include CVE IDs)

## Release Artifacts

| Artifact | Build Command | Publication Target | Trigger |
|----------|-------------|-------------------|---------|
| Container image | `docker build -t <registry>/<image>:<version> .` | [Docker Hub / ECR / GCR] | Release tag |
| npm package | `npm publish` | [npm registry] | Release tag |
| Python wheel | `python -m build && twine upload dist/*` | [PyPI] | Release tag |
| Binary | `go build -o <binary>-<os>-<arch>` | [GitHub Releases] | Release tag |
| Documentation | `mkdocs build` | [GitHub Pages / Netlify] | Release tag |

## Release Trigger

- **Trigger:** [merge to main / manual tag push / scheduled / release PR merge]
- **Rationale:** [why this trigger was selected]

## Release Pipeline Steps

1. **Analyze commits** — determine version bump from commit messages since last release
2. **Generate changelog** — auto-generate from conventional commits
3. **Bump version** — update version in [package.json / pyproject.toml / etc.]
4. **Create git tag** — `git tag v<version>`
5. **Build artifacts** — container images, packages, binaries
6. **Publish artifacts** — push to registries
7. **Create GitHub Release** — with changelog as release notes
8. **Trigger deployment pipeline** — deploy to staging, then production after validation

## Release Notes Format

### Patch / Minor Release (Auto-Generated)

```markdown
## v1.2.1

### Fixed
- Cache invalidation race condition (#44)

### Added
- User profile settings page (#42) [v1.3.0]
```

### Major Release (Manually Curated)

```markdown
## v2.0.0

### ⚠️ Breaking Changes

The authentication API has been redesigned. See the migration guide below.

#### Migration Guide

**Before (v1.x):**
```python
auth = AuthClient(api_key="...")
token = auth.login(username, password)
```

**After (v2.x):**
```python
auth = AuthClient(credentials=Credentials(api_key="..."))
session = auth.create_session(username, password)
```

### Added
- OAuth 2.1 support (#38)
- User profile settings page (#42)

### Fixed
- Cache invalidation race condition (#44)

### Security
- Patched XSS vulnerability in comment rendering (CVE-2026-1234)
```
