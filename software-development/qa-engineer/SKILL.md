---
name: qa-engineer
description: Specify test suites and execution plans from SRS and output contracts.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, qa, test-design, bug-reporting, coverage, regression, llm-testing]
    related_skills: [software-requirements-engineering, llm-task-engineering, test-driven-development, dogfood]
---

# QA Engineer Skill

Guide the complete testing lifecycle for LLM-generated code: from spec-driven test planning, through test case derivation using ISTQB black-box and white-box techniques, to test implementation specification, execution planning, exploratory testing planning, bug reporting, coverage gap analysis, and regression verification planning. Produces structured artifacts (test plans, test specifications, test implementation specs, execution plans, bug reports, coverage gap reports) grounded in ISTQB CTFL v4.0 test design techniques, IEEE 829 test documentation, IEEE 1044 anomaly classification, ISO/IEC/IEEE 29119 test process, and the ISO/IEC 25010 quality model. Does not write requirements (use `software-requirements-engineering`), design architecture (use `software-architecture-design`), or create task manifests (use `llm-task-engineering`) — it consumes those artifacts to verify the implementation against the specification.

**Documentation-only constraint:** This skill produces specification documents only — test implementation specs, execution plans, and bug reports. It does not write executable test code, run tests, or execute test commands. All test implementation and execution is delegated to the coding harness (Pi). Pseudocode and diagramming languages (Mermaid, PlantUML) are permitted within specification documents.

## When to Use

- User asks to design test cases or test suites from an SRS, RTM, or task output contracts
- User needs to specify test implementations before implementation exists (TDD RED phase specification)
- User wants to define a test execution plan for the coding harness to run against completed LLM-generated code
- User needs to produce structured bug reports from defects found during testing
- User wants to cross-reference the RTM with test results to find coverage gaps
- User needs to specify a regression verification plan after a fix is re-dispatched
- Don't use for: requirements elicitation (use `software-requirements-engineering`), architecture design (use `software-architecture-design`), task manifest creation (use `llm-task-engineering`), or exploratory web-app QA only (use `dogfood` — though this skill's Task 7 incorporates exploratory techniques into the testing plan)

## Prerequisites

- An SRS, RTM, and task output contracts from upstream roles — testing cannot begin without specifications to test against
- Completed implementation from the coding harness (Pi) for Tasks 6–10; Tasks 1–5 can proceed pre-implementation (TDD specification)
- No external tools or API keys required — this skill is a structured methodology using Hermes tools (`write_file`, `read_file`, `search_files`, `patch`)
- For test implementation specification (Task 5): the project's test framework should be identified (e.g., `pytest`, `jest`, `go test`). Determine the framework from the project's configuration files. The skill specifies test implementations targeting that framework; Pi implements and executes them

## Procedure

The testing process is sequential but iterative — later tasks may trigger feedback to upstream roles. Follow all ten tasks in order for a new system; enter at the relevant task for incremental work. Each task references a detailed reference or template file.

### Task 1: Analyze SRS and Output Contracts

Read requirements and task specs, NOT the implementation. Reading the implementation first introduces confirmation bias — the tester subconsciously writes tests that validate the code rather than the spec.

1. **Read the SRS end-to-end** — extract all functional requirements, non-functional requirements, and acceptance criteria. Completion criterion: every requirement ID and acceptance criterion is catalogued.
2. **Read the RTM** — identify which requirement IDs map to which modules and which task output contracts. Completion criterion: every requirement ID traces to at least one output contract.
3. **Read each task output contract** — extract the expected function signatures, return types, behavior descriptions, and file structures. Completion criterion: every output contract is catalogued with its public API and behavior spec.
4. **Read the interface contracts** — for integration tests, extract the interface specifications between modules. Completion criterion: every inter-module interface is catalogued.
5. **Build the test planning document** — compile a test plan covering: scope (what will be tested), test levels (unit, integration, system), test types (functional, non-functional), test environment requirements, and entry/exit criteria. Use `templates/test-plan.md`. Completion criterion: the test plan covers every requirement ID and every output contract.

Output: Test planning document. Use `write_file` to save it alongside other project artifacts.

### Task 2: Derive Test Cases from Acceptance Criteria

Each acceptance criterion must produce at least one positive test and one negative test. Traceability: each test case maps to an SRS requirement ID via the RTM.

1. **Extract acceptance criteria** — for each requirement ID, pull the acceptance criteria from the SRS and the mapped output contract. Completion criterion: every acceptance criterion is listed with its requirement ID.
2. **Derive positive test cases** — for each acceptance criterion, write at least one test case that verifies the criterion is met under valid conditions. Completion criterion: every acceptance criterion has at least one positive test case.
3. **Derive negative test cases** — for each acceptance criterion, write at least one test case that verifies the system handles invalid input or error conditions correctly. Completion criterion: every acceptance criterion has at least one negative test case.
4. **Assign test case IDs** — each test case gets a unique ID (e.g., `TC-001`) and traces to a requirement ID. Completion criterion: every test case has a unique ID, a requirement ID mapping, and a pass/fail condition.
5. **Select test design techniques** — for each test case, identify the appropriate ISTQB technique (see `references/test-design-techniques.md`): equivalence partitioning for input validation, boundary value analysis for numeric ranges, decision table testing for complex business rules, state transition testing for workflow logic. Completion criterion: every test case has a designated technique.

Output: Test case list. Use `templates/test-case.md` for the per-case format.

### Task 3: Write Test Specifications

Transform test cases into detailed test specifications covering unit tests, integration tests, edge cases, boundary conditions, and negative tests. Unit tests are written against output contracts; integration tests against interface contracts.

1. **Write unit test specifications** — for each output contract, specify the unit tests that verify the public API's behavior: normal path, error path, and side effects. Completion criterion: every output contract function has unit test specs covering normal and error paths.
2. **Write integration test specifications** — for each interface contract, specify the integration tests that verify module interactions: correct data flow, error propagation, and contract compliance. Completion criterion: every interface contract has integration test specs.
3. **Specify edge cases and boundary conditions** — using boundary value analysis (see `references/test-design-techniques.md`), identify boundary values for every numeric or ordered input. Specify edge cases: empty inputs, null/None values, max-length strings, concurrent access, timeout behavior. Completion criterion: every input with a boundary has at least one boundary test.
4. **Specify negative tests** — for each function, specify tests for: invalid input types, out-of-range values, malformed data, unauthorized access, resource exhaustion. Completion criterion: every function has negative tests covering at least the categories in `references/test-design-techniques.md`.
5. **Document test conditions** — for each test specification, record the precondition, test steps, expected result, and postcondition. Completion criterion: every test specification has all four elements documented.

See `references/test-design-techniques.md` for the full technique reference.

Output: Test specification document.

### Task 4: Define Test Data and Fixtures

Specify the inputs, expected outputs, and mock/stub configurations needed for test execution. Edge cases must cover: empty inputs, null values, max-length strings, concurrent access, and timeout behavior.

1. **Identify test data requirements** — for each test case, list the input values needed. Use equivalence partitioning to select representative values from each partition. Completion criterion: every test case has specified input values.
2. **Specify expected outputs** — for each test case, define the exact expected output (return value, side effect, state change). Completion criterion: every test case has a precise expected output.
3. **Design mocks and stubs** — for each external dependency (database, API, file system, message queue), specify the mock or stub configuration. Mocks verify interactions; stubs provide canned responses. Completion criterion: every external dependency has a mock/stub specification.
4. **Design test fixtures** — define setup and teardown procedures for each test suite: database seeding, file creation, environment variables, service startup. Completion criterion: every test suite has setup and teardown procedures.
5. **Specify edge-case data** — compile a comprehensive edge-case dataset: empty strings, null/None, zero, negative numbers, max integer, max-length strings, Unicode/special characters, concurrent access scenarios, timeout-inducing inputs. Completion criterion: the edge-case dataset covers every category in `references/test-data-fixtures.md`.

See `references/test-data-fixtures.md` for the full fixture methodology, edge-case taxonomy, and mock/stub patterns.

Output: Test fixtures specification.

### Task 5: Specify Test Suite Implementation

Produce a test implementation specification document that the coding harness (Pi) implements as executable test code. This specifies *what* the test code should do, not the code itself — test function signatures, test logic as pseudocode, assertion specifications, and file structure. In TDD, these specifications are written before implementation exists; Pi implements them as executable tests (RED phase), and after implementation is delivered, they should pass (GREEN phase).

1. **Select the test framework** — identify the project's test runner from configuration files (`pytest` for Python, `jest` for JavaScript/TypeScript, `go test` for Go, `JUnit` for Java). If none exists, recommend one appropriate for the project's language. Completion criterion: the test framework is identified and documented.
2. **Specify unit test implementations** — for each unit test specification from Task 3, produce: the test function signature (name, parameters, return type), the test logic as pseudocode (arrange-act-assert blocks), and the assertion specification (what to assert, expected value, comparison method). Use `templates/test-implementation-spec.md`. Completion criterion: every unit test specification has a corresponding implementation spec with pseudocode.
3. **Specify integration test implementations** — for each integration test specification from Task 3, produce the test function signature, pseudocode logic (including mock/stub setup from Task 4), and assertion specification. Completion criterion: every integration test specification has a corresponding implementation spec with pseudocode.
4. **Specify test file structure** — define the directory layout for test files: where unit tests, integration tests, fixtures, and helpers should be placed. Specify naming conventions for test files and test functions. Completion criterion: the file structure and naming conventions are documented.
5. **Specify RED phase verification criteria** — define what constitutes a successful RED phase: all specified tests should fail or error because no implementation exists. Specify how to identify tests that pass erroneously (testing the wrong thing). Completion criterion: RED phase verification criteria are documented.
6. **Specify test quality criteria** — define quality checks for the implemented tests: each test is independent (no test depends on another's execution order), each test has a single assertion focus, and test names describe the behavior being tested. Completion criterion: test quality criteria are documented for Pi to verify against.

Output: Test implementation specification document. Use `write_file` to save it alongside other project artifacts. Pi implements this specification as executable test code.

### Task 6: Define Test Execution Plan

Produce a test execution plan document that the coding harness (Pi) follows to execute the implemented test suite against completed code. This specifies *how* tests should be executed and *how* results should be triaged — not the execution itself.

1. **Specify execution scope and order** — list all test IDs to execute, grouped by test level (unit, integration) and in execution order (independent tests first, dependency-ordered tests after). Completion criterion: every test ID from Tasks 2–5 is listed with its execution group and order.
2. **Specify execution environment requirements** — document the runtime environment Pi must provide: language version, dependencies, environment variables, test database, mock services. Pull from the test plan (Task 1) and fixture specifications (Task 4). Completion criterion: every environment requirement is documented.
3. **Specify expected results per test** — for each test ID, restate the expected result (pass or fail) and the expected output (pass: assertion holds; fail: specific error message or assertion failure). For TDD RED phase, all tests should fail. For post-implementation GREEN phase, all tests should pass. Completion criterion: every test ID has a documented expected result.
4. **Define failure triage criteria** — specify how Pi should classify each failure as: real defect (implementation doesn't meet the spec), test bug (test is wrong), or environment issue (test infrastructure failure). Provide decision rules for each classification. Completion criterion: every failure category has documented triage rules.
5. **Define test bug identification rules** — specify how Pi should identify tests classified as test bugs: test asserts against implementation details rather than spec, test depends on execution order, test uses incorrect test data, test mocks the wrong interface. Completion criterion: test bug identification rules are documented.
6. **Specify results reporting format** — define the structure of the test results report Pi must produce: total tests, passed, failed, skipped, pass rate, and per-failure details (test ID, expected vs. actual, triage classification, reproduction steps). Use `templates/test-execution-plan.md`. Completion criterion: the results reporting format is fully specified.

Output: Test execution plan document. Pi follows this plan to execute tests and produce a test results report.

### Task 7: Specify Exploratory Testing Plan

Produce an exploratory testing plan that Pi's testers follow to probe the system for issues that automated tests didn't catch. LLM-generated code often passes unit tests but fails on integration, state management, and unexpected input combinations.

1. **Define exploration scope** — identify areas not covered by automated tests: cross-module interactions, state transitions under load, concurrent access patterns, error recovery paths, and UI/API edge cases. Completion criterion: the exploration scope covers every area not fully covered by automated tests.
2. **Specify exploration sessions** — for each scope area, define a time-boxed exploration session (30–60 minutes) with: the target area, exploration techniques to apply (see `references/llm-testing-strategies.md`), specific scenarios to probe, and inputs to try. For web applications, reference the `dogfood` skill's methodology: navigate, interact, check for console errors, test with valid and invalid inputs, scroll through content, test navigation flows. For non-web systems, specify API or CLI exercises with unexpected inputs. Completion criterion: every scope area has at least one specified exploration session.
3. **Specify finding documentation format** — define how Pi should document each finding: the scenario, steps to reproduce, expected behavior, actual behavior, and evidence (screenshot, log output, stack trace). Completion criterion: the finding documentation format is fully specified.
4. **Specify cross-reference criteria** — define how Pi should cross-reference each finding with automated tests: check whether an existing test should have caught it. If yes, flag as a test gap for Task 9. If no, flag as a coverage gap for Task 9 and recommend a new test case for Task 2. Completion criterion: cross-reference criteria are documented.

See `references/llm-testing-strategies.md` for LLM-specific exploratory strategies targeting common hallucination patterns.

Output: Exploratory testing plan document. Pi's testers execute this plan and produce an exploratory QA report.

### Task 8: Produce Bug Reports

For each defect reported by Pi's testing (from Task 6 execution results or Task 7 exploratory findings), produce a structured bug report with reproduction steps, severity, affected requirement ID, and suggested fix area. The tester identifies *where* the problem is, not how to fix it — the fix is the Task Engineer's job to re-dispatch.

1. **Assign severity** — for each defect, assign a severity using the IEEE 1044 classification (see `references/bug-reporting.md`): Critical (system unusable, data loss), High (major function failure, no workaround), Medium (function failure with workaround), Low (cosmetic, minor). Completion criterion: every defect has a severity assignment with rationale.
2. **Assign priority** — determine the urgency of fixing: how often the defect occurs, its impact on users, and its visibility. Completion criterion: every defect has a priority assignment with rationale.
3. **Write reproduction steps** — document the minimal sequence of actions that reliably triggers the defect. Each step must be specific enough for a developer to reproduce. Completion criterion: every defect has reproducible steps verified by Pi's testing.
4. **Map to requirement ID** — identify which SRS requirement the defect affects, using the RTM. If the defect affects a requirement not in the SRS, flag it as a missing requirement (feedback to Requirements Engineer). Completion criterion: every defect maps to a requirement ID or is flagged as a missing requirement.
5. **Identify the fix area** — specify which module, function, or file the defect originates in. Do not suggest a fix — identify the location. Completion criterion: every defect has a fix-area identification.
6. **Compile the bug report** — use `templates/bug-report.md` to produce a structured report for each defect. Completion criterion: every bug report has all template fields populated.

See `references/bug-reporting.md` for the full IEEE 1044 severity classification, ISTQB defect lifecycle, and report format.

Output: Bug reports (one per defect).

### Task 9: Coverage Gap Analysis

Cross-reference the RTM with test results (provided by Pi from Task 6 execution and Task 7 exploratory findings) to find requirements not covered by any passing test. A requirement with no passing test is unverified, regardless of whether the code "works."

1. **Build the coverage matrix** — for each requirement ID in the RTM, list all test case IDs that map to it (from Task 2) and their pass/fail status (from Pi's test results report). Completion criterion: every requirement ID in the RTM appears in the coverage matrix.
2. **Identify uncovered requirements** — flag any requirement ID with: no test cases mapped, or all mapped test cases failed, or all mapped test cases skipped. Completion criterion: every uncovered requirement is flagged with its reason.
3. **Identify uncovered code paths** — specify that Pi should cross-reference line/branch coverage (from tools like `coverage.py`, `jest --coverage`) with the test results. Flag any function or branch with zero coverage. Completion criterion: every uncovered code path is flagged.
4. **Identify test quality gaps** — for each exploratory finding from Task 7 that wasn't caught by automated tests, determine whether a new test case should be added. Completion criterion: every exploratory gap has a recommended new test case.
5. **Produce the coverage gap report** — compile all uncovered requirements, uncovered code paths, and test quality gaps into a structured report. Use `templates/coverage-gap-report.md`. Completion criterion: the report covers every gap category and traces each gap to a requirement ID or code path.

See `references/coverage-gap-analysis.md` for the full methodology, coverage metrics, and gap classification.

Output: Coverage gap report.

### Task 10: Specify Regression Verification Plan

Produce a regression verification plan that Pi follows after a fix is re-dispatched and delivered. LLM fixes frequently introduce new bugs while fixing old ones — the fix optimized for the reported symptom, not the root cause.

1. **Specify fix verification** — for each bug report from Task 8, specify which test Pi should re-run to confirm the fix resolves the reported defect. Define the pass criterion: the specific test that caught the defect must now pass. Completion criterion: every fixed defect has a specified verification test and pass criterion.
2. **Specify full regression suite re-execution** — define that Pi must re-execute the entire test suite (all unit and integration tests), not just the tests related to the fix. List all test IDs to include. Completion criterion: the full regression test list is documented.
3. **Define regression analysis criteria** — specify how Pi should analyze new failures: for any test that passed before the fix but fails after, document which test failed, what the fix changed, and whether the regression is related to the fix or independent. Completion criterion: regression analysis criteria are documented.
4. **Define over-fitting check criteria** — specify how Pi should verify the fix didn't just make the specific failing test pass without addressing the root cause: check whether the fix handles the edge cases identified in Task 4, not just the exact input that triggered the original defect. List the specific edge cases to verify. Completion criterion: over-fitting check criteria with specific edge cases are documented.
5. **Specify post-fix exploratory session scope** — define a focused exploratory session for Pi to conduct in the area where the fix was applied, checking for new issues introduced by the fix. Reference the exploration techniques from Task 7. Completion criterion: every fix area has a specified post-fix exploratory session scope.
6. **Specify test suite update criteria** — define when Pi should add new test cases identified during regression (from Task 9's gap analysis or from new edge cases discovered during exploratory QA). Specify the update process and verification criteria. Completion criterion: test suite update criteria are documented.
7. **Define regression report format** — specify the structure of the regression test results report Pi must produce: tests run, passed, failed, regressions found, over-fitting verdicts, and exploratory findings. Completion criterion: the regression report format is fully specified.

Output: Regression verification plan document. Pi follows this plan after re-dispatch and produces a regression test results report.

## Feedback Paths

- **To Task Engineer (bug reports):** Each bug report from Task 8 feeds back to the Task Engineer with: the defect's fix area, the failing test, expected vs. actual behavior, and the affected requirement ID. The Task Engineer re-dispatches with refined context/constraints. The feedback must be a structured artifact — the bug report itself.
- **To Task Engineer (coverage gaps):** Coverage gaps from Task 9 that indicate missing tasks (requirements with no corresponding implementation task) feed back to the Task Engineer. The feedback must specify: which requirement ID is uncovered, whether no task exists or the task's output contract is incomplete.
- **To Requirements Engineer (untestable requirements):** Coverage gaps that indicate a requirement is untestable (too vague, no acceptance criterion, not atomic) feed back to the Requirements Engineer. The feedback must specify: which requirement ID, why it's untestable, and the suggested revision.
- **From Task Engineer (re-dispatch):** After a fix is re-dispatched and delivered, Pi follows the regression verification plan (Task 10). The re-dispatch notification must include: the bug report ID, the fix area, and the expected behavior.

## Quick Reference

| Task | Key Output | Reference / Template |
|------|------------|---------------------|
| 1. Analyze SRS & contracts | Test planning document | `templates/test-plan.md` |
| 2. Derive test cases | Test case list | `references/test-design-techniques.md`, `templates/test-case.md` |
| 3. Write test specs | Test specification document | `references/test-design-techniques.md` |
| 4. Test data & fixtures | Test fixtures specification | `references/test-data-fixtures.md` |
| 5. Specify test suite implementation | Test implementation specification | `templates/test-implementation-spec.md` |
| 6. Define test execution plan | Test execution plan | `templates/test-execution-plan.md` |
| 7. Specify exploratory testing plan | Exploratory testing plan | `references/llm-testing-strategies.md` |
| 8. Bug reports | Bug reports (one per defect) | `references/bug-reporting.md`, `templates/bug-report.md` |
| 9. Coverage gap analysis | Coverage gap report | `references/coverage-gap-analysis.md`, `templates/coverage-gap-report.md` |
| 10. Specify regression verification plan | Regression verification plan | — |

### Test design technique quick rules

- Equivalence partitioning: one representative value per partition (including invalid partitions)
- Boundary value analysis: test the boundary and its adjacent neighbor (2-value BVA); for rigor, add the inner neighbor (3-value BVA)
- Decision table testing: one test per column (rule); 100% coverage = all feasible rules exercised
- State transition testing: cover all valid transitions, all states, and all invalid transitions (negative testing)
- Statement coverage: every executable statement exercised by at least one test
- Branch coverage: every branch (true and false) exercised — stronger than statement coverage
- Error guessing: supplement systematic techniques with experience-based guesses in known problem areas
- Exploratory testing: time-boxed sessions targeting areas not covered by automated tests

### Bug severity quick reference (IEEE 1044)

| Severity | Definition |
|----------|-----------|
| Critical | System unusable, data loss, security breach |
| High | Major function failure, no workaround |
| Medium | Function failure with workaround available |
| Low | Cosmetic, minor, documentation error |

## Verification

- [ ] Every SRS requirement ID appears in the test planning document
- [ ] Every acceptance criterion has at least one positive test case and one negative test case
- [ ] Every test case has a unique ID and traces to a requirement ID via the RTM
- [ ] Every test case has a designated ISTQB test design technique
- [ ] Every output contract function has unit test specifications (normal and error paths)
- [ ] Every interface contract has integration test specifications
- [ ] Every input with a boundary has at least one boundary value test
- [ ] Every external dependency has a mock or stub specification
- [ ] The test implementation specification covers every test case with pseudocode and assertion specs
- [ ] The test execution plan specifies every test ID with expected results and triage criteria
- [ ] Every bug report has severity, priority, reproduction steps, requirement ID, and fix area
- [ ] The coverage matrix covers every requirement ID in the RTM
- [ ] Every uncovered requirement is flagged with its reason
- [ ] The regression verification plan specifies full suite re-execution and over-fitting check criteria
- [ ] Feedback paths to Task Engineer and Requirements Engineer are documented as structured artifacts
