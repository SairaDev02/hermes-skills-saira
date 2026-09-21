# Bug Report Template

> One bug report per defect. The tester identifies WHERE the problem is,
> not HOW to fix it — the fix is the Task Engineer's job to re-dispatch.
> This template defines the structure; fill in all fields.
> See `references/bug-reporting.md` for severity and priority guidance.

---

## BUG-<ID>: <[Component] Brief description>

### Classification

| Field | Value |
|-------|-------|
| **Bug ID** | BUG-<ID> |
| **Title** | <[Component] Brief description> |
| **Severity** | Critical / High / Medium / Low |
| **Severity Rationale** | <Why this severity — based on impact, not frequency> |
| **Priority** | P1 / P2 / P3 / P4 |
| **Priority Rationale** | <Why this priority — frequency, user impact, visibility> |
| **Status** | New |
| **Defect Type** | Functional / Performance / Security / Usability / Compatibility / Reliability / Data |

### Traceability

| Field | Value |
|-------|-------|
| **Affected Requirement ID** | <FR-XXX or NFR-XXX from SRS — or "Missing requirement" if not in SRS> |
| **Affected Module/Function** | <Where the defect originates> |
| **Failing Test Case ID** | <TC-XXX that caught this defect> |
| **Suggested Fix Area** | <Module/function/file — NOT how to fix it> |

### Environment

| Field | Value |
|-------|-------|
| **OS** | <operating system and version> |
| **Runtime** | <language runtime and version> |
| **Test Framework** | <framework and version> |
| **Test Environment** | <environment name — e.g., "staging-01", "local-dev"> |

### Reproduction Steps

1. <Step 1 — specific, minimal, from clean state>
2. <Step 2>
3. <Step 3 — the fewest steps that reliably trigger the defect>

> These steps must be verified by re-execution. A developer must be able
> to follow these and see the defect.

### Expected Result

<What the spec says should happen. Cite the requirement ID and acceptance criterion.>

### Actual Result

<What actually happened. Include exact error message, stack trace, or observed behavior.>

### Evidence

- **Screenshot:** <path or MEDIA: reference>
- **Log excerpt:** <relevant log lines>
- **Stack trace:** <full stack trace if applicable>
- **Video:** <path if screen recording available>

### Workaround (if any)

<If a workaround exists, describe it. If none, write "None".>

### Reporter

| Field | Value |
|-------|-------|
| **Tester** | <name/ID> |
| **Date Reported** | <YYYY-MM-DD> |
| **Exploratory Session** | <Session ID from Task 7, if found during exploration — otherwise "Automated test TC-XXX"> |
