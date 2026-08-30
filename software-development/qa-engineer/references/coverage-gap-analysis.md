# Coverage Gap Analysis Reference

The methodology for cross-referencing the Requirements Traceability Matrix (RTM) with test results to find requirements not covered by any passing test. This reference supports Task 9 of the QA Engineer process.

## Core Principle

A requirement with no passing test is **unverified**, regardless of whether the code "works." The RTM is the backbone — it links each requirement to its test cases, and the test results tell us which requirements are actually verified.

## Coverage Dimensions

Coverage is multi-dimensional. A system can have high coverage in one dimension and zero in another.

| Dimension | What It Measures | How It's Measured |
|-----------|-----------------|-------------------|
| **Requirements coverage** | % of SRS requirement IDs with at least one passing test | (req IDs with passing tests / total req IDs) × 100 |
| **Test case coverage** | % of test cases that have been executed | (tests executed / total tests) × 100 |
| **Code coverage (statement)** | % of executable statements exercised by tests | (statements hit / total statements) × 100 |
| **Code coverage (branch)** | % of branches exercised by tests | (branches hit / total branches) × 100 |
| **Boundary coverage** | % of identified boundary values tested | (boundaries tested / total boundaries) × 100 |
| **Transition coverage** | % of state transitions tested | (transitions tested / total transitions) × 100 |

## The Coverage Matrix

The coverage matrix is the primary artifact. It cross-references every requirement ID in the RTM with its test cases and their results.

### Matrix Structure

| Requirement ID | Requirement Summary | Test Case IDs | Test Results | Status |
|---------------|--------------------|--------------|--------------|--------|
| FR-001 | User can register with email | TC-001, TC-002, TC-003 | PASS, PASS, PASS | ✅ Verified |
| FR-002 | System validates email format | TC-004, TC-005 | PASS, FAIL | ❌ Gap |
| FR-003 | System sends confirmation email | — | — | ⬜ No tests |
| NFR-001 | API responds within 200ms p95 | TC-012 | SKIP | ⚠️ Skipped |

### Status Values

| Status | Meaning | Action Required |
|--------|---------|----------------|
| ✅ Verified | At least one test mapped, all passing | None |
| ❌ Gap | Tests mapped but at least one failing | Bug report (Task 8) → fix → regression (Task 10) |
| ⬜ No tests | No test cases mapped to this requirement | New test cases (Task 2) or missing task feedback to Task Engineer |
| ⚠️ Skipped | Tests exist but were skipped (environment, dependency) | Resolve blocker, re-run tests |
| 🔶 Partial | Some test cases passing, some failing | Bug report for failures; remaining tests are verified |

## Gap Classification

### Type 1: Missing Test Cases (No Tests Mapped)

A requirement in the RTM has no test cases mapped to it. This means the test planning (Task 1) or test case derivation (Task 2) missed this requirement.

**Root cause:** Incomplete test planning or test case derivation.

**Action:**
- If the requirement is testable → add test cases (return to Task 2).
- If the requirement is untestable (too vague, no acceptance criterion, not atomic) → feedback to Requirements Engineer with: requirement ID, why it's untestable, suggested revision.

### Type 2: Failing Tests (Tests Mapped, All/Some Failing)

Test cases are mapped to the requirement, but at least one is failing. The requirement is not verified because the implementation doesn't meet the spec.

**Root cause:** Implementation defect (most common) or test bug.

**Action:**
- If the failure is a real defect → bug report (Task 8) → fix → regression (Task 10).
- If the failure is a test bug → fix the test (Task 6, step 4).

### Type 3: Skipped Tests

Test cases are mapped but were skipped during execution. The requirement is not verified because the test was never run.

**Root cause:** Environment issue (missing dependency, service unavailable), or test infrastructure problem.

**Action:**
- Resolve the blocker (start the dependency service, fix the test infrastructure).
- Re-run the skipped tests.

### Type 4: Missing Implementation Task

A requirement in the RTM has no corresponding implementation task in the task manifest. The requirement was never implemented.

**Root cause:** The Task Engineer missed this requirement when creating the task manifest.

**Action:**
- Feedback to Task Engineer: specify which requirement ID is uncovered, and that no task exists for it.

### Type 5: Missing Requirement

An exploratory finding (Task 7) reveals a defect that doesn't map to any SRS requirement. The requirement was never specified.

**Root cause:** The Requirements Engineer missed a requirement during elicitation.

**Action:**
- Feedback to Requirements Engineer: specify the observed behavior, why it should be a requirement, and the suggested requirement text.

## Coverage Metrics Calculation

### Requirements Coverage Rate

```
Requirements Coverage = (Requirement IDs with ≥1 passing test / Total requirement IDs in RTM) × 100
```

### Test Execution Rate

```
Test Execution = (Tests executed / Total tests) × 100
```

### Test Pass Rate

```
Test Pass Rate = (Tests passed / Tests executed) × 100
```

### Code Coverage (when available)

```
Statement Coverage = (Statements exercised / Total executable statements) × 100
Branch Coverage = (Branches exercised / Total branches) × 100
```

## Coverage Targets

| Coverage Type | Minimum Target | Ideal |
|---------------|---------------|------|
| Requirements coverage | 100% | 100% |
| Test execution rate | 95% | 100% |
| Test pass rate | 95% | 100% |
| Statement coverage | 80% | 90%+ |
| Branch coverage | 70% | 85%+ |
| Boundary coverage | 100% | 100% |

**Note:** 100% code coverage does NOT mean 100% requirements coverage. A system can have every line of code tested but still have untested requirements if the tests don't map to the spec. Requirements coverage is the primary metric; code coverage is supplementary.

## Gap Analysis Procedure

### Step 1: Build the Coverage Matrix

For each requirement ID in the RTM:

1. Find all test case IDs mapped to this requirement (from Task 2).
2. Find the pass/fail/skip status for each test case (from Task 6).
3. Record the status: Verified, Gap, No tests, Skipped, or Partial.

### Step 2: Classify Each Gap

For each requirement that is not ✅ Verified:

1. Determine the gap type (Type 1–5 above).
2. Record the root cause.
3. Record the recommended action.

### Step 3: Cross-Reference with Code Coverage

If code coverage tools are available:

1. Identify functions/branches with zero coverage.
2. Map these to the requirement IDs they implement (via the architecture document).
3. Flag any requirement whose implementation has zero code coverage as a Type 2 gap.

### Step 4: Cross-Reference with Exploratory Findings

For each finding from Task 7 (Exploratory QA):

1. Check if an automated test should have caught this issue.
2. If yes → the test has a gap (revise the test or add a new one).
3. If no → the test suite has a coverage gap (add a new test case).

### Step 5: Produce the Coverage Gap Report

Compile all gaps into a structured report using `templates/coverage-gap-report.md`.

## Standards References

- ISO/IEC/IEEE 29119-2:2021 — Test process (coverage measurement)
- ISO/IEC/IEEE 29119-3:2021 — Test documentation (coverage reports)
- ISTQB CTFL v4.0 Syllabus, §5.3 — Test monitoring and control
- IEEE Std 829-2008 — Test summary report
