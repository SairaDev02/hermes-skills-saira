# Compliance Checklist Template

Use this template for the requirements compliance check produced in Task 2. One checklist per task under review.

---

# Requirements Compliance Checklist: <Task ID>

**Reviewer:** Code Reviewer
**Date:** <YYYY-MM-DD>
**Task Spec:** <task spec reference>
**SRS Reference:** <SRS document reference>
**RTM Reference:** <RTM document reference>

## Acceptance Criteria Compliance

| # | Requirement ID | Acceptance Criterion | Code Location (file:line) | Status | Notes |
|---|----------------|---------------------|--------------------------|--------|-------|
| 1 | <REQ-001> | <criterion text> | <file>:<line> | Pass | — |
| 2 | <REQ-002> | <criterion text> | <file>:<line> | Fail | <description of failure> |
| 3 | <REQ-003> | <criterion text> | Not found | Unimplemented | <no corresponding code> |

### Status Values

- **Pass** — code implements the criterion correctly
- **Fail** — code implements the criterion incorrectly
- **Unimplemented** — no code found for this criterion
- **Partial** — code implements some but not all of the criterion

## RTM Traceability

| Requirement ID | RTM Mapping | Code Found? | Status |
|----------------|-------------|-------------|--------|
| <REQ-001> | <module/function> | Yes | Pass |
| <REQ-002> | <module/function> | Yes | Fail |
| <REQ-003> | <module/function> | No | Unimplemented |

## Scope Compliance

| Changed File | In Scope? | Scope Boundary |
|-------------|-----------|----------------|
| <file> | Yes | Within task scope |
| <file> | No | Out of scope — modifies <module> not in task spec |

## Extra Implementations (Scope Creep)

| # | Code Location | Behavior | Traced to Requirement? | Action |
|---|--------------|----------|----------------------|--------|
| 1 | <file>:<line> | <description> | No | Flag for removal or requirements update |

## Constraint Compliance

| # | Constraint (from task spec) | Status | Notes |
|---|---------------------------|--------|-------|
| 1 | <constraint text> | Pass | — |
| 2 | <constraint text> | Fail | <description of violation> |

## Summary

| Check | Pass | Fail | Unimplemented | N/A |
|-------|------|------|----------------|-----|
| Acceptance criteria | <N> | <N> | <N> | <N> |
| RTM traceability | <N> | <N> | <N> | <N> |
| Scope compliance | <N> | <N> | — | — |
| Constraint compliance | <N> | <N> | — | <N> |

**Overall compliance verdict:** Pass | Fail
