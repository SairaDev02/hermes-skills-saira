# Security Review Reference

The methodology for performing security scanning during code review, aligned with the OWASP Top 10, Static Application Security Testing (SAST) principles, and Common Weakness Enumeration (CWE) classifications. Supports Task 4 of the Code Reviewer process.

## OWASP Top 10 (2021) Mapping

The OWASP Top 10 represents the most critical web application security risks. Each risk maps to CWE categories:

| OWASP Category | CWE IDs | What to Check in Code Review |
|----------------|---------|------------------------------|
| A01: Broken Access Control | CWE-200, CWE-201, CWE-352 | Missing authz checks, IDOR, missing CSRF tokens |
| A02: Cryptographic Failures | CWE-259, CWE-327, CWE-331 | Weak crypto, hardcoded keys, plaintext storage |
| A03: Injection | CWE-79, CWE-89, CWE-78 | SQL injection, XSS, command injection |
| A04: Insecure Design | CWE-209, CWE-256, CWE-501 | Missing rate limiting, no threat modeling |
| A05: Security Misconfiguration | CWE-16, CWE-611 | Debug mode on, default credentials, XXE |
| A06: Vulnerable Components | CWE-1104 | Outdated dependencies with known CVEs |
| A07: Auth Failures | CWE-287, CWE-384, CWE-798 | Weak password policy, session fixation, hardcoded credentials |
| A08: Data Integrity Failures | CWE-829, CWE-306 | Untrusted deserialization, unsigned updates |
| A09: Logging Failures | CWE-778, CWE-117 | Missing audit logs, log injection |
| A10: SSRF | CWE-918 | Unvalidated URLs in server-side requests |

## SAST Methodology

Static Application Security Testing (SAST) analyzes source code without executing the application. It parses the code into an Abstract Syntax Tree (AST), builds control flow and data flow graphs, and matches patterns against a rule database mapped to known vulnerability classes (OWASP Top 10, CWE).

### SAST Tools

| Tool | Languages | Focus |
|------|-----------|-------|
| semgrep | Multi-language | Pattern-based, custom rules, low false positive rate |
| bandit | Python | Python-specific security linter |
| gitleaks | Git repos | Secret detection in code and commit history |
| eslint-plugin-security | JavaScript | Node.js security patterns |
| brakeman | Ruby (Rails) | Rails-specific vulnerability scanner |
| gosec | Go | Go security scanner |
| pip-audit | Python | Python dependency vulnerability scanner |
| npm audit | JavaScript | Node.js dependency vulnerability scanner |

### Running SAST Tools

Use `terminal` to run SAST tools against the changed code:

```bash
# Semgrep (multi-language)
semgrep --config auto <changed_files>

# Bandit (Python)
bandit -r <module> -f json

# Gitleaks (secrets)
gitleaks detect --source . --report-path gitleaks-report.json

# pip-audit (Python dependencies)
pip-audit

# npm audit (Node.js dependencies)
npm audit --json
```

## Grep-Based Fallback Patterns

When no SAST tool is available, use grep to scan added lines for common vulnerability patterns. These patterns check only the `+` lines in the diff.

### Hardcoded Secrets (CWE-798)

```bash
git diff --cached | grep "^+" | grep -iE "(api_key|secret|password|token|passwd|api_secret|access_key|private_key)\s*=\s*['\"][^'\"]{6,}['\"]"
```

Flag: Any hardcoded credential with 6+ characters in a string literal.

### Shell Injection (CWE-78)

```bash
git diff --cached | grep "^+" | grep -E "os\.system\(|subprocess\..*shell=True|subprocess\.call\(.*shell=True|os\.popen\("
```

Flag: User input passed to shell execution without sanitization.

### SQL Injection (CWE-89)

```bash
git diff --cached | grep "^+" | grep -E "execute\(f\"|execute\(f'|\.format\(.*SELECT|\.format\(.*INSERT|\.format\(.*UPDATE|\.format\(.*DELETE|%.*SELECT|%.*INSERT|%.*UPDATE|%.*DELETE"
```

Flag: SQL queries built with string formatting instead of parameterized statements.

### XSS — Cross-Site Scripting (CWE-79)

```bash
git diff --cached | grep "^+" | grep -E "innerHTML|dangerouslySetInnerHTML|document\.write\(|eval\("
```

Flag: User input rendered as HTML without escaping.

### Path Traversal (CWE-22)

```bash
git diff --cached | grep "^+" | grep -E "\.\./\.\./|os\.path\.join\(.*\.\.|open\(.*\+.*request|open\(.*input"
```

Flag: File paths constructed from user input without validation.

### Unsafe Deserialization (CWE-502)

```bash
git diff --cached | grep "^+" | grep -E "pickle\.loads?\(|yaml\.load\((?!Loader=SafeLoader)|marshal\.loads?\(|eval\(|exec\("
```

Flag: Deserialization of untrusted data without safe loaders.

### Dangerous eval/exec (CWE-95)

```bash
git diff --cached | grep "^+" | grep -E "\beval\(|\bexec\(|new Function\(|window\.eval\("
```

Flag: Dynamic code execution with user input.

### SSRF — Server-Side Request Forgery (CWE-918)

```bash
git diff --cached | grep "^+" | grep -E "requests\.get\(.*input|urllib\.request\.urlopen\(.*input|http\.Get\(.*input|fetch\(.*input"
```

Flag: Server-side HTTP requests with URLs from user input without validation.

## Dependency Audit

Check for known vulnerabilities in project dependencies:

```bash
# Python
pip-audit 2>&1 | tail -20

# Node.js
npm audit --json 2>&1 | tail -20

# Go
govulncheck ./... 2>&1 | tail -20

# Ruby
bundle audit 2>&1 | tail -20
```

Flag: Any dependency with a known CVE. Document the CVE ID, the package name, the installed version, and the fixed version.

## Secret Detection Patterns

Beyond the hardcoded secrets grep, check for:

| Pattern | Regex | Risk |
|---------|------|------|
| AWS Access Key | `AKIA[0-9A-Z]{16}` | AWS credential exposure |
| AWS Secret Key | `[0-9a-zA-Z/+]{40}` near AWS context | AWS credential exposure |
| GitHub Token | `ghp_[0-9a-zA-Z]{36}` | GitHub credential exposure |
| Generic API Key | `[a-zA-Z]{3,}_[kK]ey\s*=\s*['\"][^'\"]{16,}['\"]` | Generic API key |
| Private Key Block | `-----BEGIN.*PRIVATE KEY-----` | Private key in source |
| JWT | `eyJ[0-9a-zA-Z_-]+\.[0-9a-zA-Z_-]+\.[0-9a-zA-Z_-]+` | JWT token in source |
| Database URL with credentials | `[a-zA-Z]+://[^:]+:[^@]+@` | Database credentials in URL |

## Security Finding Documentation

For each security finding, document:

| Field | Description |
|-------|-------------|
| Severity | Critical / High / Medium / Low |
| CWE ID | Common Weakness Enumeration identifier |
| OWASP Category | OWASP Top 10 category (A01–A10) |
| File | File path |
| Line | Line number |
| Code Snippet | The vulnerable code (3–5 lines of context) |
| Description | What the vulnerability is and why it matters |
| Suggested Direction | The direction the fix should take (not the fix itself) |

### Security Severity Scale

| Severity | Definition | Examples |
|----------|-----------|----------|
| Critical | Remotely exploitable, leads to data breach or RCE | SQL injection, command injection, hardcoded production secrets |
| High | Exploitable with some access, serious impact | XSS stored, path traversal, missing authz on sensitive endpoint |
| Medium | Requires specific conditions to exploit | Missing rate limiting, weak crypto, verbose error messages |
| Low | Defense in depth, hard to exploit directly | Missing security headers, log injection, information disclosure |
