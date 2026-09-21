# Requirements Traceability Matrix (RTM) Template

The RTM links each requirement to its source, downstream artifacts, and verification
results. Maintained throughout the lifecycle.

## Purpose

- Ensure every requirement is traced to a source (stakeholder need)
- Ensure every requirement is traced to a verification artifact (test, review, demo)
- Identify orphan requirements (no source) and uncovered needs (no requirement)
- Support impact analysis for change requests

## RTM Structure

### Primary RTM (Bidirectional)

| Req ID | Requirement Summary | Source | Priority | Status | Design Element | Test Case ID | Verification Method | Verification Result | Notes |
|--------|-------------------|--------|----------|--------|---------------|-------------|--------------------|--------------------|-------|
| FR-01 | User login with email/password | Stakeholder: Product Owner | Must | Validated | AUTH-001 | TC-001 | Test | Pass | |
| FR-02 | Password reset via email link | Stakeholder: Support Team | Should | Draft | AUTH-002 | TC-002, TC-003 | Test | Pending | |
| NFR-P01 | API response ≤200ms P95 | Stakeholder: DevOps Lead | Must | Reviewed | ARCH-PERF | TC-PERF-001 | Test | Pending | |
| NFR-R01 | 99.9% monthly uptime | SLA Contract | Must | Validated | ARCH-HA | TC-REL-001 | Analysis | Pass | |

### Column Definitions

| Column | Description |
|--------|-------------|
| **Req ID** | Unique requirement identifier (FR-XX, NFR-XX, C-XX) |
| **Requirement Summary** | Brief description (1 line) of the requirement |
| **Source** | Where the requirement came from (stakeholder name, document, regulation) |
| **Priority** | MoSCoW: Must / Should / Could / Won't (this time) |
| **Status** | Draft → Reviewed → Validated → Approved → Implemented → Verified |
| **Design Element** | Architecture or design component that implements this requirement |
| **Test Case ID** | Link to the test case(s) that verify this requirement |
| **Verification Method** | Test / Analysis / Demonstration / Inspection |
| **Verification Result** | Pending / Pass / Fail / Blocked |
| **Notes** | Caveats, dependencies, change requests |

## Forward Traceability (Requirements → Outputs)

Confirms that every requirement has a design element and test case:

| Req ID | Design Element | Test Case ID | Verified? |
|--------|---------------|-------------|-----------|
| FR-01 | | | |
| FR-02 | | | |
| | | | |

**Coverage check:** Every Req ID should have a Design Element and at least one Test Case ID.
Flag any row with missing values.

## Backward Traceability (Outputs → Requirements)

Confirms that every design element and test case traces back to a requirement:

| Design Element | Req ID | Orphan? |
|---------------|--------|---------|
| AUTH-001 | FR-01 | |
| AUTH-002 | FR-02 | |
| ARCH-007 | ??? | ⚠ ORPHAN — no requirement |

**Coverage check:** Every Design Element should map to at least one Req ID.
Flag orphans for resolution (add a missing requirement or remove the design element).

## Change Impact Matrix

Used when a change request is received. Map the affected requirements to all
downstream artifacts:

| Change Request | Affected Req IDs | Affected Design Elements | Affected Test Cases | Impact Assessment | Decision |
|---------------|-----------------|------------------------|--------------------|--------------------|---------|
| CR-001: Add social login | FR-01, FR-03 | AUTH-001 | TC-001, TC-005 | Medium — new auth flow, update existing tests | Approved |
| CR-002: | | | | | |

## Coverage Summary Dashboard

| Metric | Count | Status |
|--------|-------|--------|
| Total Requirements | | |
| Requirements with Test Cases | | |
| Requirements without Test Cases | | ⚠ Gap |
| Test Cases Passed | | |
| Test Cases Failed | | |
| Test Cases Pending | | |
| Orphan Requirements (no source) | | ⚠ |
| Orphan Design Elements (no requirement) | | ⚠ |
| TBDs / Placeholders | | ⚠ |

## RTM Maintenance Rules

1. **Update on every change** — when a requirement changes, update its row and all
   linked rows immediately.
2. **No orphans** — every requirement must have a source and a test case. Every design
   element must trace to a requirement. Flag and resolve orphans within the same sprint.
3. **Status workflow** — Draft → Reviewed → Validated → Approved → Implemented →
   Verified. A requirement cannot be marked Verified until its test case passes.
4. **Version the RTM** — keep the RTM under version control alongside the SRS. Record
   changes in a change log.
5. **Review regularly** — the RTM should be reviewed at least at each major milestone
   and sprint boundary.
