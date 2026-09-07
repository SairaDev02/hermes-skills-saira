---
name: qa-engineer
description: Specify tests and QA evidence from requirements.
version: 0.3.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, qa, test-design, bug-reporting, coverage, regression, llm-testing]
    related_skills: [software-requirements-engineering, software-architecture-design, llm-task-engineering]
---

# QA Engineer Skill

Produce a compact QA design package and, after implementation, an evidence package for LLM-generated software. QA derives tests from requirements and contracts, defines fixtures and execution plans, and reviews actual results for defects, coverage, and regression. It does not write executable tests, run tests, or modify implementation.

## Documentation-only boundary

Outputs are test plans, test cases, test specifications, fixture specifications, execution plans, exploratory plans, bug reports, coverage-gap reports, and regression plans. Pseudocode and Mermaid/PlantUML are allowed inside those documents. Execution evidence must come from the assigned harness or operator; never infer a pass from missing output.

## When to Use

- Design tests from an SRS, RTM, interface contract, or task output contract.
- Specify TDD test implementations, fixtures, execution, exploratory sessions, or regression checks.
- Analyze test results for defects, traceability, and coverage gaps.
- Don't use for: executable test code, test execution, requirements, architecture, task manifests, or code review.

## Prerequisites

- SRS, RTM, architecture/interface contracts, and task output contracts.
- Shared project context: `docs/PROJECT-CONSTITUTION.md`, `docs/REFERENCE-INDEX.md`, `docs/GLOSSARY.md`, `docs/ASSUMPTIONS.md`, and `docs/CHANGE-IMPACT-MAP.md`.
- Completed implementation and actual test/exploratory results for evidence-based Tasks 7–10.
- Project test framework and environment details, or an explicit unknown/recommendation.
- Use `read_file`, `search_files`, `write_file`, and `patch` for documents.
- Use the shared root `templates/HANDOFF.md` for both the design handoff to the harness and the evidence handoff to Code Review.

## Procedure

### 1. Build the test basis

Read the specification before implementation. Catalog requirements, acceptance criteria, output contracts, interfaces, quality targets, and test-level scope. **Done when:** every testable requirement and contract has a traceable test basis.

### 2. Derive test cases

For every acceptance criterion, define at least one proving case and add negative, boundary, equivalence-partition, decision-table, state-transition, or risk-based cases according to applicability and risk. Give each a stable ID, preconditions, steps, expected result, technique, and requirement link. **Done when:** every criterion is proven and omitted case types have a rationale.

### 3. Specify data, fixtures, and implementation

Define representative and edge-case data, expected outputs, mocks/stubs, setup/teardown, isolation, and test file structure. Provide pseudocode and assertion specifications for the harness, not executable code. **Done when:** every test case has reproducible data, environment assumptions, and an implementation-neutral procedure.

### 4. Specify execution and exploration

Define test order, environment, expected results, failure triage, reporting fields, and RED/GREEN expectations. Add time-boxed exploratory sessions for integration, state, concurrency, recovery, API/UI, and untested risk areas. **Done when:** the harness can execute the plan and classify each result as pass, defect, test issue, or environment issue.

### 5. Report defects and coverage

For each actual finding, record evidence, minimal reproduction, severity, priority, affected requirement, fix area, owner, and status. Use the shared `templates/feedback-record.yaml` shape for cross-role findings. Build a requirement-to-test-result matrix and flag unmapped, failing, skipped, and code-path gaps. **Done when:** every finding is evidence-backed and every RTM requirement has a coverage disposition.

### 6. Specify regression verification

For each fix, name the confirming test, full-suite scope, regression analysis, over-fitting checks, focused exploration, and report format. **Done when:** the plan verifies both the reported behavior and collateral impact, with no claimed execution result absent evidence.

## Handoff

Use the shared root `templates/HANDOFF.md` twice when needed: once for the design package to the implementation harness, and once for evidence and coverage to Code Review. Do not mix planned results with observed results.

## Required artifact shapes

- **Test case:** ID, requirement, risk, technique, preconditions, data, steps, expected result, pass rule.
- **Fixture:** dependency, setup, teardown, isolation, representative data, edge data.
- **Defect:** ID, evidence, reproduction, expected/actual, severity, priority, requirement, fix area, status.
- **Coverage row:** requirement, tests, results, code-path evidence, gap, disposition.
- **Regression gate:** fix evidence, suite scope, result, residual risk, approver.

## Package structure

Use one compact package unless a project needs separate review:

```text
qa/
  TEST-PLAN.md       # basis, scope, strategy, entry/exit rules
  TEST-MATRIX.md     # cases, fixtures, requirement links, and results
  FINDINGS.md        # defects, coverage gaps, regression disposition
  HANDOFF.md         # shared handoff template
```

Separate implementation and execution sections when their evidence states differ. The design handoff goes to the harness; the evidence handoff goes to Code Review.

## Pitfalls

- Reading implementation first and designing tests around its behavior.
- Requiring a negative test for a criterion where no invalid boundary exists without documenting the rationale.
- Treating skipped or failing tests as coverage.
- Reporting a defect without reproducible evidence or requirement impact.
- Confusing a test bug or environment failure with an implementation defect.
- Claiming tests ran when only a plan was produced.

## Verification

- [ ] Every requirement and acceptance criterion has a traceable test disposition.
- [ ] Every criterion has a proving case; applicable invalid, boundary, state, and risk cases are included or justified.
- [ ] Fixtures, mocks, setup, teardown, and isolation are specified.
- [ ] Implementation and execution documents contain pseudocode and reporting rules, not executable code.
- [ ] Exploratory sessions have scope, scenarios, evidence format, and time box.
- [ ] Every defect has evidence, reproduction, severity, priority, requirement, and fix area.
- [ ] Coverage distinguishes passing, failing, skipped, unmapped, and unverified.
- [ ] Regression covers the fix, full suite, over-fitting, and focused exploration.
- [ ] No execution result is asserted without an actual result artifact.
