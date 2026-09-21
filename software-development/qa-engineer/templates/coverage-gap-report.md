# Coverage Gap Report Template

> One report per test cycle. Cross-references the RTM with test results
> to find requirements not covered by any passing test. A requirement
> with no passing test is unverified, regardless of whether the code "works."
> See `references/coverage-gap-analysis.md` for the full methodology.

---

## Coverage Gap Report — <Project/Release>

### Report Metadata

| Field | Value |
|-------|-------|
| **Report Date** | <YYYY-MM-DD> |
| **Test Cycle** | <cycle identifier> |
| **SRS Version** | <version> |
| **RTM Version** | <version> |
| **Test Suite Version** | <version or commit hash> |

### Executive Summary

| Metric | Value |
|--------|-------|
| Total requirement IDs in RTM | <N> |
| Requirements verified (≥1 passing test) | <N> |
| Requirements with gaps | <N> |
| Requirements with no tests | <N> |
| **Requirements coverage** | <N / N> = **<%>** |
| Total test cases | <N> |
| Tests executed | <N> |
| Tests passed | <N> |
| Tests failed | <N> |
| Tests skipped | <N> |
| **Test pass rate** | <N / N> = **<%>** |
| Statement coverage (if available) | <%> |
| Branch coverage (if available) | <%> |

### Coverage Matrix

| Requirement ID | Requirement Summary | Test Case IDs | Test Results | Status | Gap Type |
|---------------|--------------------|--------------|--------------|--------|----------|
| FR-001 | <summary> | TC-001, TC-002 | PASS, PASS | ✅ Verified | — |
| FR-002 | <summary> | TC-003 | FAIL | ❌ Gap | Type 2: Failing tests |
| FR-003 | <summary> | — | — | ⬜ No tests | Type 1: Missing test cases |
| NFR-001 | <summary> | TC-012 | SKIP | ⚠️ Skipped | Type 3: Skipped tests |

### Gap Details

#### Gap 1: <Requirement ID> — <Gap Type>

| Field | Value |
|-------|-------|
| **Requirement ID** | <FR-XXX> |
| **Requirement Summary** | <one-line summary> |
| **Gap Type** | Type 1: Missing test cases / Type 2: Failing tests / Type 3: Skipped / Type 4: Missing task / Type 5: Missing requirement |
| **Root Cause** | <why this gap exists> |
| **Recommended Action** | <add test cases / bug report / resolve environment / feedback to Task Engineer / feedback to Requirements Engineer> |
| **Action Owner** | <Tester / Task Engineer / Requirements Engineer> |

> Repeat for each gap.

### Code Coverage Gaps (if available)

| Module/Function | Statement Coverage | Branch Coverage | Mapped Requirement | Status |
|----------------|-------------------|----------------|-------------------|--------|
| <module.function> | <%> | <%> | <FR-XXX> | ❌ Zero coverage |
| <module.function> | 85% | 60% | <FR-XXX> | ⚠️ Low branch coverage |

### Exploratory QA Gaps

| Finding ID | Description | Should Automated Test Have Caught It? | Recommended New Test Case |
|------------|-------------|--------------------------------------|---------------------------|
| <Finding-001> | <description> | Yes / No | <new TC description> |

### Recommendations

1. <Action item 1 — e.g., "Add test cases for FR-003 (Type 1 gap)">
2. <Action item 2 — e.g., "Bug report BUG-005 for FR-002 failure (Type 2 gap)">
3. <Action item 3 — e.g., "Feedback to Task Engineer: FR-004 has no implementation task (Type 4 gap)">
4. <Action item 4 — e.g., "Feedback to Requirements Engineer: exploratory finding Finding-003 has no corresponding SRS requirement (Type 5 gap)">

### Feedback Artifacts

| Feedback To | Requirement ID | Artifact | Status |
|-------------|---------------|----------|--------|
| Task Engineer | FR-004 | <bug report or gap notification> | Pending |
| Requirements Engineer | — (missing) | <new requirement suggestion> | Pending |
