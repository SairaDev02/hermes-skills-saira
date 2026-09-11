# Release Process Reference

This reference covers versioning schemes, conventional commits, changelog automation, and release artifact management.

## Versioning Schemes

### Semantic Versioning (SemVer 2.0.0)

Format: `MAJOR.MINOR.PATCH`

| Component | When to Increment | Example | Consumer Impact |
|-----------|-------------------|---------|------------------|
| MAJOR | Breaking API changes | 1.0.0 → 2.0.0 | Must update integration code |
| MINOR | New features (backward-compatible) | 1.2.0 → 1.3.0 | Safe to upgrade, new features available |
| PATCH | Bug fixes (backward-compatible) | 1.3.1 → 1.3.2 | Safe to upgrade, fixes only |

**Pre-release labels:** `2.0.0-alpha.1`, `1.3.0-rc.2`, `2.0.0-beta.3`
**Build metadata:** `1.2.3+build.42` (ignored for precedence)

**When to use SemVer:** Libraries, frameworks, APIs, any project where backwards compatibility is a consumer concern.

### Calendar Versioning (CalVer)

Format: `YYYY.MM.PATCH` or `YYYY.MM.MICRO`

| Project | Format | Example |
|---------|--------|---------|
| Ubuntu | YY.MM | 24.04 |
| pip | YY.N | 24.0 |
| Terraform | MAJOR.MINOR.PATCH (monthly) | 1.7.0 |
| Black | YY.MM.MICRO | 24.3.0 |

**When to use CalVer:** Applications, distributions, tools with rolling releases where "backwards compatibility" is not the primary concern.

## Conventional Commits

Format: `<type>[optional scope]: <description>\n\n[optional body]\n\n[optional footer(s)]`

| Type | SemVer Impact | Description |
|------|---------------|-------------|
| `feat` | MINOR | New feature |
| `fix` | PATCH | Bug fix |
| `docs` | None | Documentation only |
| `style` | None | Formatting, whitespace |
| `refactor` | None | Code change that neither fixes nor adds |
| `perf` | PATCH | Performance improvement |
| `test` | None | Adding or fixing tests |
| `build` | None | Build system or dependencies |
| `ci` | None | CI configuration |
| `chore` | None | Other maintenance |
| `revert` | None | Reverting a previous commit |

**Breaking changes:** `feat(auth)!: redesign login flow` or `BREAKING CHANGE: auth API redesigned` in the footer.

**Enforcement:** Use `commitlint` with `@commitlint/config-conventional`:

```json
{
  "extends": ["@commitlint/config-conventional"]
}
```

Add as a pre-commit hook or enforce via GitHub branch protection rules.

## Changelog Automation

### Keep a Changelog 1.1.0 Format

```markdown
# Changelog

## [Unreleased]

## [1.2.0] - 2026-01-15

### Added
- User profile settings page (#42)

### Changed
- Authentication flow now uses OAuth 2.1 (#38)

### Deprecated
- Legacy API v1 endpoints will be removed in v2.0 (#40)

### Removed
- Deprecated `getUserById` method (#35)

### Fixed
- Race condition in cache invalidation (#44)

### Security
- Patched XSS vulnerability in comment rendering (CVE-2026-1234)
```

### Automation Tools

| Tool | Approach | Best For |
|------|----------|----------|
| semantic-release | Fully automated: analyzes commits, bumps version, generates changelog, creates GitHub release, publishes to registry | Hands-off CI/CD publishing (npm, PyPI) |
| release-please (Google) | Creates a "Release PR" that accumulates changes; merging it triggers the release | Google-style release workflow |
| standard-version | Generates changelog and bumps version; leaves publishing to you | Projects that want control over publishing |
| git-cliff | Generates changelog from conventional commits; configurable format | Rust/Go projects, custom changelog formats |
| changesets | Developer-authored change descriptions; merges into a release | Monorepos with human-readable changelogs |
| conventional-changelog | Parses git log, generates CHANGELOG.md | Simple single-package repos |

### semantic-release Configuration Example

```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    ["@semantic-release/changelog", { "changelogFile": "CHANGELOG.md" }],
    "@semantic-release/npm",
    ["@semantic-release/git", {
      "assets": ["package.json", "CHANGELOG.md"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }],
    "@semantic-release/github"
  ]
}
```

**Critical:** `fetch-depth: 0` is mandatory in the checkout step because semantic-release needs full git history to find the last tag.

## Release Artifacts

Identify what artifacts are produced on release:

| Artifact Type | Publication Target | Example |
|---------------|-------------------|---------|
| Container image | Docker Hub, ECR, GCR | `docker build -t app:v1.2.0 .` |
| npm package | npm registry | `npm publish` |
| Python wheel | PyPI | `python -m build && twine upload dist/*` |
| Go binary | GitHub Releases | `go build -o app-linux-amd64` |
| Java JAR | Maven Central | `mvn deploy` |
| Documentation site | GitHub Pages, Netlify | `mkdocs build && mkdocs gh-deploy` |

## Release Triggers

| Trigger | When | Use Case |
|---------|------|-----------|
| Merge to main | Continuous delivery | Every merged PR triggers a release |
| Manual tag push | On-demand | `git tag v1.2.0 && git push origin v1.2.0` |
| Scheduled | Weekly/monthly | Cron-triggered release for fixed cadence |
| Release PR merge | release-please pattern | Accumulate changes, merge the release PR to trigger |

## Release Notes Best Practices

1. **Auto-generate from conventional commits** for patch and minor releases
2. **Manually curate for major releases** — breaking changes need migration guidance
3. **Include migration steps** for breaking changes — before, after, and the rationale
4. **Link to PRs and issues** — each changelog entry references its PR number
5. **Write for a technical audience** — no marketing language
6. **Include security advisories** — CVE IDs, affected versions, and patch versions
