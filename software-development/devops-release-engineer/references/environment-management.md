# Environment Management Reference

This reference covers environment configuration, secrets management, and the OWASP-aligned practices for secure DevOps.

## Environment Hierarchy

```
Development (local dev, feature branches)
    ↓
Staging (integration testing, pre-production validation)
    ↓
Production (live user traffic)
```

Optional environments:
- **Preview/Sandbox:** ephemeral environments per pull request (e.g., Vercel preview deployments, Render preview environments)
- **QA:** dedicated quality assurance environment (if staging is used for integration only)
- **Disaster Recovery:** warm standby for production failover

## Twelve-Factor App: Config Principle

**Factor III: Config** — Store config in the environment.

Configuration that varies between deployments (database URLs, API keys, feature flags, log levels) must be extracted from the code and loaded from the environment. Code is the same across all environments; config differs.

- **Code** = committed to version control, identical across environments
- **Config** = environment variables, secrets, differs per environment
- The codebase must not contain environment-specific configuration values

## Secrets Management

### OWASP Secrets Management Cheat Sheet — Key Practices

1. **Never hardcode secrets** in code, configuration files, or scripts. Scan with pre-commit hooks (gitleaks, Talisman) to prevent secrets from entering version control.
2. **Centralize secrets storage** in a dedicated vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GitHub Secrets). A single source of truth for all credentials.
3. **Inject secrets at runtime** via environment variables or vault sidecar. Secrets are never written to disk in plaintext.
4. **Enforce least-privilege access** — each service or pipeline stage accesses only the secrets it needs. Use RBAC to define access policies.
5. **Segregate by environment** — production secrets are not available to development pipelines. Each environment has its own secret scope.
6. **Automate rotation** — define rotation schedules for every secret category. Automated rotation reduces exposure time and human error.
7. **Maintain audit logs** — every secret access is logged with timestamp, accessor, and purpose. Required for compliance (SOC 2, HIPAA, PCI DSS).
8. **Use secure randomness** — pipeline-created secrets must be generated with cryptographic randomness and sufficient length (minimum 256 bits for symmetric keys).
9. **Monitor for secret sprawl** — regularly scan repositories, build logs, and container registries for exposed credentials.
10. **Have an incident response plan** — when a secret is exposed, the response must be: rotate immediately, audit access logs, assess impact, update prevention measures.

### Secrets Management Tool Comparison

| Tool | Type | Best For | Key Feature |
|------|------|----------|-------------|
| HashiCorp Vault | Self-hosted/cloud | Enterprise, multi-cloud | Dynamic secrets, lease-based access |
| AWS Secrets Manager | Cloud (AWS) | AWS-native workloads | Auto-rotation for RDS, Lambda integration |
| Azure Key Vault | Cloud (Azure) | Azure-native workloads | HSM-backed keys, certificate management |
| GitHub Secrets | Platform | GitHub Actions CI/CD | Simple, free for public repos |
| Doppler | SaaS | Teams wanting simplicity | Sync to multiple environments |
| Infisical | Open-source/SaaS | Self-hosted preference | GitOps-native, open-source |
| 1Password CI/CD | SaaS | Teams already using 1Password | Unified credential management |

### `.env.example` Convention

The `.env.example` file documents every environment variable the application expects, with placeholder values. It is committed to version control. The actual `.env` file contains real values and must be in `.gitignore`.

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DATABASE_POOL_SIZE=10

# API Keys (stored in vault, not here)
STRIPE_SECRET_KEY=<set-in-vault>
OPENAI_API_KEY=<set-in-vault>

# Feature Flags
ENABLE_BETA_FEATURES=false

# Logging
LOG_LEVEL=info

# CORS
CORS_ORIGINS=http://localhost:3000
```

### Pre-commit Secret Scanning

Use `gitleaks` or `talisman` as a pre-commit hook to prevent secrets from entering version control:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

## Environment Segregation Rules

1. **Production secrets are never available to non-production pipelines.** Separate GitHub environments, separate Vault paths, separate AWS IAM roles.
2. **CI/CD pipeline permissions are scoped per environment.** A pipeline running in the staging context cannot access production secrets.
3. **Service accounts are environment-specific.** The staging service account cannot authenticate against production resources.
4. **Network isolation where possible.** Production databases are not reachable from staging networks.

## Secret Rotation Policy

| Secret Category | Rotation Frequency | Method |
|----------------|-------------------|--------|
| Database passwords | Every 90 days | Automated via vault or cloud provider |
| API keys (third-party) | Every 180 days or on provider schedule | Manual or automated via provider API |
| TLS certificates | Every 90 days (Let's Encrypt) or per CA | Automated renewal via cert-manager or ACME |
| SSH keys | On personnel change | Manual rotation + audit |
| JWT signing keys | Every 365 days | Manual rotation with key overlap window |
| CI/CD pipeline tokens | Every 90 days | Automated via platform API |
