# Bug Reporting Reference

The methodology for classifying, documenting, and tracking defects using IEEE 1044 anomaly classification and the ISTQB defect lifecycle. This reference supports Task 8 of the QA Engineer process.

## Defect Terminology (ISTQB)

| Term | Definition |
|------|-----------|
| **Error** | A human mistake (e.g., developer wrote `>` instead of `>=`) |
| **Defect (fault)** | The flaw in the code resulting from the error |
| **Failure** | The observable incorrect behavior when the defect executes |
| **Bug** | Informal term for defect — use "defect" in formal documentation |
| **Anomaly** | Any event that requires investigation (IEEE 1044 term) |

A defect can exist without causing a failure (if the code path is never executed). A failure requires a defect to be present. Testing finds failures; debugging finds defects.

## Severity Classification (IEEE 1044)

Severity measures the *impact* of the defect on the system.

| Severity | Definition | Examples |
|----------|-----------|----------|
| **Critical** | System is unusable; data loss; security breach | Crash on startup, database corruption, authentication bypass |
| **High** | Major function failure; no workaround available | Payment processing fails, login broken, data not saved |
| **Medium** | Function failure with a workaround available | Search returns wrong results (manual filter works), feature degraded but usable |
| **Low** | Cosmetic; minor; documentation error | Typo in UI, misaligned element, incorrect help text |

### Severity Assignment Rules

1. **Severity is about impact, not frequency.** A defect that occurs rarely but causes data loss is Critical.
2. **Severity is not negotiable based on effort to fix.** A Critical defect that's a one-line fix is still Critical.
3. **Severity does not change with priority.** A cosmetic typo on the homepage may be High priority but Low severity.
4. **Assign severity based on worst-case impact.** If the defect *can* cause data loss, it's Critical even if it usually doesn't.

## Priority Classification

Priority measures the *urgency* of fixing the defect.

| Priority | Definition | Typical Action |
|----------|-----------|----------------|
| **P1 — Fix immediately** | Blocks testing or release; affects critical path | Fix before any other work |
| **P2 — Fix this sprint** | Significant impact; workaround exists but is painful | Schedule in current sprint |
| **P3 — Fix next sprint** | Minor impact; workaround is acceptable | Backlog |
| **P4 — Fix when convenient** | Cosmetic, documentation, no user impact | Backlog, low priority |

### Priority Assignment Rules

1. **Priority considers frequency, impact, and visibility.** A Low-severity typo on the homepage may be P1 if it affects brand perception.
2. **Priority is set by the product owner or test lead, not the tester alone.** The tester recommends; the owner decides.
3. **Priority can change.** As the release approaches, priority may increase for must-fix defects.

## Severity vs Priority Matrix

| | Low Severity | Medium Severity | High Severity | Critical Severity |
|-|-------------|-----------------|---------------|-------------------|
| **P1 (Immediate)** | Homepage typo before launch | — | — | All critical defects |
| **P2 (This sprint)** | — | Feature degradation in common path | Feature broken in common path | — |
| **P3 (Next sprint)** | Internal typo | Feature degradation in rare path | Feature broken in rare path | — |
| **P4 (When convenient)** | Internal doc typo | Cosmetic in admin panel | — | — |

## ISTQB Defect Lifecycle

```text
New → Assigned → Open → Fixed → Verified → Closed
                ↑                     ↓
                └── Reopened ←────────┘
                     ↑
                     └── Rejected (duplicate / not a defect / won't fix)
```

| State | Description |
|-------|-------------|
| **New** | Defect logged by tester, not yet triaged |
| **Assigned** | Defect assigned to a developer |
| **Open** | Developer is working on the fix |
| **Fixed** | Developer has implemented a fix; awaiting verification |
| **Verified** | Tester has confirmed the fix resolves the defect |
| **Closed** | Defect is resolved and no further action needed |
| **Reopened** | Defect recurred after a fix; sent back to developer |
| **Rejected** | Defect is not valid (duplicate, not a defect, won't fix) |
| **Deferred** | Defect acknowledged but postponed to a future release |

## Bug Report Format

Every bug report must contain the following fields. The report is the primary feedback artifact to the Task Engineer — it must be self-contained.

### Required Fields

| Field | Description |
|-------|-------------|
| **Bug ID** | Unique identifier (e.g., `BUG-001`) |
| **Title** | One-line summary: `[Component] Brief description` |
| **Severity** | Critical / High / Medium / Low (with rationale) |
| **Priority** | P1 / P2 / P3 / P4 (with rationale) |
| **Status** | Current lifecycle state (initially: New) |
| **Affected Requirement ID** | SRS requirement ID from the RTM (or "Missing requirement" if not in SRS) |
| **Affected Module/Function** | Where the defect originates (fix area, not fix) |
| **Environment** | OS, browser, runtime version, test environment name |
| **Reproduction Steps** | Numbered, minimal, specific — a developer can follow these and see the defect |
| **Expected Result** | What the spec says should happen (cite the requirement ID) |
| **Actual Result** | What actually happened (include error message, stack trace, screenshot) |
| **Evidence** | Screenshots, log excerpts, stack traces, video recordings |
| **Suggested Fix Area** | Which module/function/file contains the defect — NOT how to fix it |
| **Reporter** | Tester name/ID |
| **Date Reported** | Date of discovery |

### Reproduction Steps Rules

1. **Minimal** — the fewest steps that reliably trigger the defect.
2. **Specific** — each step must be unambiguous (click THIS button, enter THIS value).
3. **Verified** — the tester must have reproduced the defect at least twice using these steps.
4. **From clean state** — steps start from a known-good state (fresh session, clean database).

### What NOT to Include

- **Suggested fix** — the tester identifies *where* the problem is, not how to fix it. The fix is the Task Engineer's job.
- **Speculation about cause** — report the observed behavior, not guesses about why it happens.
- **"Probably" / "might be"** — the bug report must be non-speculative. State observed facts.
- **Other defects** — one defect per report. If two defects are related, cross-reference by Bug ID.

## Defect Classification by Type

| Type | Description | Example |
|------|-------------|---------|
| **Functional** | System doesn't do what the spec says | Returns wrong value for valid input |
| **Performance** | System is too slow, uses too much memory | API response > 500ms when spec says < 200ms |
| **Security** | System allows unauthorized access or data leak | API returns data without authentication |
| **Usability** | System is confusing or hard to use | Error message doesn't explain how to fix the input |
| **Compatibility** | System fails in a specific environment | Works in Chrome, fails in Firefox |
| **Reliability** | System fails intermittently | Crashes under concurrent load |
| **Data** | System corrupts or loses data | Save operation drops fields silently |

## Standards References

- IEEE Std 1044-2009 — Standard for Classification of Software Anomalies
- IEEE Std 829-2008 — Standard for Software Test Documentation (Anomaly Report)
- ISO/IEC/IEEE 29119-3:2021 — Test documentation (defect reporting)
- ISTQB CTFL v4.0 Syllabus, §5.5 — Defect Management
