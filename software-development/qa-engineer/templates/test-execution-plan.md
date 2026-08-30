# Test Execution Plan Template

> This document specifies how the coding harness (Pi) should execute
> the implemented test suite and triage results. It does not execute
> tests itself — it defines the execution scope, order, environment,
> expected results, and reporting format.

---

## Execution Scope and Order

### Unit Tests

| Order | Test ID | Test File | Target Function | Expected Result |
|-------|---------|-----------|-----------------|-----------------|
| 1 | TC-001 | tests/unit/test_auth.py | test_login_valid | Pass (post-impl) / Fail (RED) |
| 2 | TC-002 | tests/unit/test_auth.py | test_login_invalid_password | Pass (post-impl) / Fail (RED) |
| ... | ... | ... | ... | ... |

### Integration Tests

| Order | Test ID | Test File | Target Function | Expected Result |
|-------|---------|-----------|-----------------|-----------------|
| 1 | TC-050 | tests/integration/test_api.py | test_create_order_flow | Pass (post-impl) / Fail (RED) |
| ... | ... | ... | ... | ... |

## Execution Environment Requirements

| Requirement | Value | Source |
|-------------|-------|--------|
| Language runtime | <Python 3.11 / Node 20 / etc.> | Project config |
| Test framework | <pytest / jest / etc.> | Task 5 specification |
| Dependencies | <list from lockfile> | Project lockfile |
| Environment variables | <list required vars> | Task 4 fixtures |
| Test database | <type, version, connection string pattern> | Task 4 fixtures |
| Mock services | <list of mock/stub configurations> | Task 4 fixtures |
| Coverage tool | <coverage.py / jest --coverage / etc.> | Project config |

## Expected Results Summary

| Phase | Total Tests | Expected Pass | Expected Fail | Expected Error |
|-------|-------------|---------------|---------------|----------------|
| RED (pre-implementation) | <N> | 0 | <N> | <M> |
| GREEN (post-implementation) | <N> | <N> | 0 | 0 |

## Failure Triage Rules

### Classification: Real Defect

A failure is a **real defect** if ALL of the following are true:
- The test specification (Task 3) is correct
- The test data and fixtures (Task 4) are correct
- The test implementation (Task 5 spec) is correct
- The implementation does not produce the expected output

→ Action: Produce a bug report (Task 8)

### Classification: Test Bug

A failure is a **test bug** if ANY of the following are true:
- The test asserts against implementation details rather than the spec
- The test depends on execution order of other tests
- The test uses incorrect test data (does not match Task 4 specification)
- The test mocks the wrong interface or uses incorrect mock configuration
- The test function signature does not match the implementation spec (Task 5)

→ Action: Revise the test implementation to match the spec, then re-run

### Classification: Environment Issue

A failure is an **environment issue** if ANY of the following are true:
- The test framework is not installed or is the wrong version
- A required dependency is missing
- A required environment variable is not set
- The test database is not available or not seeded
- A mock service is not running or is misconfigured

→ Action: Fix the environment, then re-run

## Test Bug Identification Checklist

For each failing test, verify:
- [ ] Test asserts against the output contract (Task 3 spec), not implementation internals
- [ ] Test does not depend on another test's side effects or execution order
- [ ] Test data matches the Task 4 specification exactly
- [ ] Mock/stub configuration matches the Task 4 specification
- [ ] Test function name and signature match the Task 5 implementation spec

## Results Reporting Format

Pi must produce a test results report with the following structure:

### Summary

| Field | Value |
|-------|-------|
| Total tests | <N> |
| Passed | <N> |
| Failed | <N> |
| Skipped | <N> |
| Pass rate | <N>% |
| Duration | <seconds> |
| Phase | RED / GREEN / Regression |

### Per-Failure Details

For each failure:

| Field | Value |
|-------|-------|
| Test ID | TC-<ID> |
| Test function | <function name> |
| Test file | <file path> |
| Expected result | <from Task 3 spec> |
| Actual result | <observed output/error> |
| Triage classification | Real defect / Test bug / Environment issue |
| Triage rationale | <why this classification was chosen> |
| Reproduction steps | <minimal steps to reproduce the failure> |
