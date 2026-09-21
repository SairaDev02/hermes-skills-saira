# Environment Configuration Template

## Environments

| Environment | Purpose | Access Policy | Deployment Trigger |
|-------------|---------|---------------|---------------------|
| Development | Local development, feature branches | All developers | Manual / on push |
| Staging | Integration testing, pre-production validation | Developers + CI/CD | Automatic on merge to main |
| Production | Live user traffic | Restricted (on-call + release managers) | Manual approval after staging validation |

## Environment Variables

### Development

| Variable | Type | Description | Example Value |
|----------|------|-------------|----------------|
| DATABASE_URL | string | Database connection string | postgresql://localhost:5432/devdb |
| LOG_LEVEL | enum | Logging verbosity | debug |
| ENABLE_FEATURE_X | boolean | Feature flag | true |
| API_TIMEOUT_MS | integer | API request timeout | 30000 |

### Staging

| Variable | Type | Description | Example Value |
|----------|------|-------------|----------------|
| DATABASE_URL | string | Database connection string | [from vault: staging/database-url] |
| LOG_LEVEL | enum | Logging verbosity | info |
| ENABLE_FEATURE_X | boolean | Feature flag | false |
| API_TIMEOUT_MS | integer | API request timeout | 15000 |

### Production

| Variable | Type | Description | Example Value |
|----------|------|-------------|----------------|
| DATABASE_URL | string | Database connection string | [from vault: production/database-url] |
| LOG_LEVEL | enum | Logging verbosity | warn |
| ENABLE_FEATURE_X | boolean | Feature flag | false |
| API_TIMEOUT_MS | integer | API request timeout | 10000 |

## Secrets Management

### Vault Configuration

| Secret | Environment | Vault Path | Rotation Policy | Access Policy |
|--------|------------|------------|----------------|---------------|
| Database password | Dev | secret/dev/db-password | Every 90 days | All developers |
| Database password | Staging | secret/staging/db-password | Every 90 days | Developers + CI/CD |
| Database password | Production | secret/prod/db-password | Every 90 days | On-call + release managers |
| API key (Stripe) | Production | secret/prod/stripe-key | Every 180 days | Release managers |
| TLS certificate | Production | secret/prod/tls-cert | Every 90 days (Let's Encrypt) | Automated via cert-manager |

### Secrets Segregation Rules

1. Production secrets are stored in a separate vault path with restricted access
2. CI/CD pipelines use environment-scoped service accounts — staging pipeline cannot read production secrets
3. No secret is shared across environments
4. Secret access is logged and audited monthly

## `.env.example`

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# API Keys (stored in vault, not here)
STRIPE_SECRET_KEY=<set-in-vault>
OPENAI_API_KEY=<set-in-vault>

# Feature Flags
ENABLE_FEATURE_X=false

# Logging
LOG_LEVEL=info

# API
API_TIMEOUT_MS=15000

# CORS
CORS_ORIGINS=http://localhost:3000
```

## `.gitignore` Verification

- [ ] `.env` is in `.gitignore`
- [ ] `*.pem`, `*.key`, `*.p12` are in `.gitignore`
- [ ] No secret values appear in any committed file
- [ ] Pre-commit hook (gitleaks) is configured and active
