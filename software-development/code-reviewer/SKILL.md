---
name: code-reviewer
description: "Review completed code against spec, architecture, security."
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [code-review, security, compliance, complexity, edge-cases, verdict]
    related_skills: [software-architecture-design, software-requirements-engineering, requesting-code-review, github-code-review, simplify-code]
---

# Code Reviewer Skill

Guide the complete code review lifecycle for LLM-generated code: from receiving completed code with its task spec, through requirements compliance (RTM-traced), architecture compliance (module boundaries and interface contracts), security scanning (SAST-aligned, OWASP Top 10), style and convention checks, complexity and maintainability assessment (McCabe cyclomatic complexity, Sonar cognitive complexity), edge case gap identification, structured review comments, and a final verdict (approve / request changes / reject). Produces structured artifacts (compliance checklists, review comments, verdict reports) grounded in Michael Fagan's inspection process, the OWASP Code Review Guide, McCabe's cyclomatic complexity (1976), Sonar's cognitive complexity (2018), and the SEI maintainability risk categories. Does not write tests (use `qa-engineer`), design architecture (use `software-architecture-design`), or create task manifests (use `llm-task-engineering`) — it consumes those artifacts to verify the implementation against the specification.

## When to Use

- User asks to review completed code against its task spec, SRS, or architecture document
- User needs to verify that LLM-generated code respects module boundaries and interface contracts
- User wants a security scan of completed code (SAST-aligned vulnerability detection, dependency audit, secret detection)
- User needs a complexity and maintainability assessment of completed code
- User wants to produce structured review comments and a formal verdict (approve / request changes / reject)
- User asks to identify edge cases the code doesn't handle that the Tester may not have covered
- Don't use for: pre-commit self-review of your own changes (use `requesting-code-review`), reviewing other people's PRs on GitHub with inline comments (use `github-code-review`), writing test suites (use `qa-engineer`), or simplifying already-approved code (use `simplify-code`)

## Prerequisites

- Completed code from the implementation harness (Pi) — diff, PR, or file set
- The task spec that generated the code — review is against the spec, not just "does this look good"
- SRS, RTM, and architecture document from upstream roles — for requirements and architecture compliance checks
- Test results from the Tester role (optional but recommended — for cross-referencing coverage)
- No external tools or API keys required — this skill is a structured methodology using Hermes tools (`read_file`, `write_file`, `search_files`, `patch`, `terminal`)
- For security scanning (Task 4): SAST tools may be used if available (e.g., `semgrep`, `bandit`, `gitleaks`); the skill includes grep-based fallback patterns for environments without dedicated SAST tools

## Procedure

The review process is sequential — each task builds on the previous. Follow all ten tasks in order for a complete review; enter at the relevant task for incremental work. Each task references a detailed reference or template file.

### Task 1: Receive Completed Code

Receive the diff, PR, or file set from the implementation harness's output. Must have the task spec that generated this code — review is against the spec, not just "does this look good."

1. **Gather the code changes** — obtain the diff, PR, or file set. Use `terminal` with `git diff` commands. Completion criterion: the full set of changed files is catalogued.
2. **Retrieve the originating task spec** — find the task manifest entry that generated this code. Completion criterion: the task spec is on hand with its scope, output contract, acceptance criteria, and constraints.
3. **Retrieve upstream artifacts** — gather the SRS, RTM, architecture document, and interface contracts referenced by the task spec. Completion criterion: all upstream artifacts referenced by the task spec are available.
4. **Retrieve test results** (if available) — get the test results report and bug reports from the Tester role. Completion criterion: test results are on hand or explicitly marked unavailable.
5. **Create a review queue entry** — record: task ID, code source (diff/PR/files), upstream artifact references, and test result status. Completion criterion: the review queue entry is documented.

Output: Review queue entry.

### Task 2: Requirements Compliance Check

Does the implementation satisfy the SRS requirements mapped to this task? Use the RTM to verify each acceptance criterion is met by the code.

1. **Extract acceptance criteria from the task spec** — list every acceptance criterion with its SRS requirement ID. Completion criterion: every acceptance criterion is listed with its requirement ID.
2. **Map each criterion to code** — for each acceptance criterion, identify the code that implements it and verify the behavior matches the spec. Completion criterion: every acceptance criterion has a code location and a pass/fail assessment.
3. **Check RTM traceability** — verify every requirement ID mapped to this task in the RTM is addressed by the code. Completion criterion: every RTM-mapped requirement ID is accounted for.
4. **Identify unimplemented requirements** — flag any acceptance criterion with no corresponding code. Completion criterion: every unimplemented requirement is flagged.
5. **Identify extra implementations** — flag any code that implements behavior not traced to a requirement (potential scope creep). Completion criterion: every extra implementation is flagged.
6. **Build the compliance checklist** — compile all findings into a structured checklist (see `templates/compliance-checklist.md`). Completion criterion: the checklist covers every acceptance criterion and every RTM-mapped requirement ID.

See `references/review-checklist.md` for the full compliance check methodology.

Output: Compliance checklist.

### Task 3: Architecture Compliance Check

Does the code respect module boundaries, interface contracts, and cross-cutting concerns? The most common LLM failure: an LLM reaches outside its module boundary to "fix" something it wasn't asked to touch.

1. **Verify module boundary compliance** — check that the code only modifies files, modules, and functions within the task spec's scope. Use `search_files` to cross-reference changed files against the scope field. Completion criterion: every changed file is within the declared scope.
2. **Check for out-of-scope modifications** — flag any changes to files, modules, or functions not listed in the task spec's scope field. Completion criterion: every out-of-scope change is flagged with the file path and the scope boundary it violates.
3. **Verify interface contract compliance** — for each interface the code touches, verify the implementation matches the interface contract (signatures, data models, error contracts). Completion criterion: every interfaced operation matches its contract.
4. **Check cross-cutting concerns** — verify the code follows the cross-cutting concerns spec (error handling strategy, logging format, auth pattern, configuration approach). Completion criterion: every applicable cross-cutting concern is checked.
5. **Produce the architecture compliance report** — compile all findings. Completion criterion: the report covers module boundaries, interface contracts, and cross-cutting concerns.

Output: Architecture compliance report.

### Task 4: Security Scan

Automated vulnerability detection, dependency audit, and secret detection. Use SAST tools if available; fall back to grep-based pattern matching.

1. **Run SAST tools** (if available) — run any available static analysis security tools against the changed code. Use `terminal` to invoke tools like `semgrep`, `bandit`, or `gitleaks`. Completion criterion: SAST results are captured or marked unavailable.
2. **Run grep-based security patterns** — scan added lines for common vulnerability patterns. Use `terminal` with grep commands from `references/security-review.md`. Check for: hardcoded secrets, shell injection, SQL injection, XSS, path traversal, unsafe deserialization, dangerous eval/exec. Completion criterion: every pattern category is scanned.
3. **Dependency audit** — check for known vulnerabilities in dependencies. Use `terminal` to run `pip audit`, `npm audit`, or equivalent. Completion criterion: dependency audit is run or marked unavailable.
4. **Secret detection** — scan for hardcoded API keys, passwords, tokens, and credentials in the diff. Completion criterion: secret detection is run with zero false negatives for common patterns.
5. **Compile security scan results** — document all findings with severity, CWE ID (where applicable), file location, and the vulnerable code snippet. Completion criterion: every finding is documented with CWE classification.

See `references/security-review.md` for the full SAST methodology, OWASP Top 10 mapping, grep patterns, and CWE references.

Output: Security scan results.

### Task 5: Style and Convention Check

Does the code follow the constraints specified in the task manifest? Linter output plus manual check for pattern adherence.

1. **Run linters** (if available) — detect the project language and run the appropriate linter. Use `terminal` to invoke `ruff`, `eslint`, `clippy`, `golangci-lint`, or equivalent. Capture the failure count. Completion criterion: linter output is captured or marked unavailable.
2. **Check coding standards** — verify the code follows the coding standards specified in the task spec's constraints field (naming conventions, file structure, import organization). Completion criterion: every constraint from the task spec is checked.
3. **Check pattern adherence** — verify the code follows the architectural patterns specified in the task spec (e.g., if the spec says "use repository pattern," verify the code uses it). Completion criterion: every specified pattern is verified.
4. **Check for debug artifacts** — scan for leftover debug statements, TODOs, commented-out code, and console logs. Completion criterion: zero debug artifacts remain in the changed code.
5. **Compile style check results** — document all findings with severity, file location, and the specific constraint violated. Completion criterion: every finding traces to a specific constraint from the task spec.

Output: Style check results.

### Task 6: Complexity and Maintainability Assessment

Assess cyclomatic complexity, cognitive complexity, function length, nesting depth, and naming clarity. LLMs tend to write verbose but shallow code — long functions that do little, or deeply nested conditionals that could be flattened.

1. **Measure cyclomatic complexity** — run complexity analysis tools if available (`radon cc` for Python, `complexity-report` for JS, etc.). If no tool is available, manually count decision points per function. Flag functions with cyclomatic complexity > 10 (McCabe's threshold, corroborated by NIST Structured Testing). Completion criterion: every function in the changed code has a complexity assessment.
2. **Assess cognitive complexity** — evaluate nesting depth and logical flow complexity. Flag functions with deep nesting (> 3 levels) or convoluted conditional logic that a human would struggle to follow. Use the cognitive complexity principles from `references/complexity-metrics.md`. Completion criterion: every function is assessed for cognitive load.
3. **Check function length** — flag functions exceeding 50 lines (excluding comments and blank lines). Long functions often indicate mixed responsibilities. Completion criterion: every function is measured.
4. **Check naming clarity** — verify function, variable, and class names clearly describe their purpose. Flag vague names (`data`, `process`, `handle`, `tmp`), misleading names, and inconsistent naming conventions. Completion criterion: every public identifier in the changed code is assessed.
5. **Assess DRY violations** — identify duplicated logic that should be extracted. Flag copy-pasted code blocks and near-identical function bodies. Completion criterion: every duplication is flagged with both locations.
6. **Produce the complexity report** — compile all findings using the SEI risk categories (see `references/complexity-metrics.md`). Completion criterion: the report covers every function with complexity, length, nesting, naming, and DRY assessments.

Output: Complexity report.

### Task 7: Edge Case Gap Identification

Are there inputs or states the code doesn't handle that the Tester may not have covered? The Reviewer and Tester have complementary blind spots — the Tester tests the spec; the Reviewer reads the code and finds what the spec *missed*.

1. **Read the code for unhandled paths** — trace each function's control flow for missing error handling, uncaught exceptions, and unhandled return values. Completion criterion: every function is traced for unhandled paths.
2. **Identify missing input validation** — check for inputs that are used without validation (null checks, range checks, type checks, format checks). Completion criterion: every user-facing input is checked for validation.
3. **Identify missing boundary handling** — check for edge cases: empty collections, zero/negative values, max-length inputs, Unicode/special characters, concurrent access, timeout behavior. Completion criterion: every boundary category from `references/edge-case-analysis.md` is checked.
4. **Cross-reference with test results** — for each edge case gap found, check whether the Tester's test suite covers it. If not, it's a coverage gap to feed back. Completion criterion: every edge case gap is classified as "covered by tests" or "uncovered — feed back to Tester."
5. **Identify state management issues** — check for race conditions, stale state, missing cleanup, and incorrect state transitions. Completion criterion: every stateful operation is checked.
6. **Compile edge case findings** — document each finding with: the code location, the unhandled input/state, the potential impact, and whether the test suite covers it. Completion criterion: every finding is documented.

See `references/edge-case-analysis.md` for the full edge case taxonomy and identification methodology.

Output: Edge case findings.

### Task 8: Produce Review Comments

Inline comments on specific code locations with severity, issue type, and suggested direction. Via `gh` CLI or REST API for GitHub; structured feedback for re-dispatch otherwise.

1. **Consolidate all findings** — merge findings from Tasks 2–7 into a single comment list. Completion criterion: every finding from every task is included.
2. **Assign severity to each comment** — use the severity scale: Critical (security, data loss, spec violation), Warning (maintainability, style, missing edge case handling), Suggestion (improvement, non-blocking). Completion criterion: every comment has a severity.
3. **Assign issue type** — classify each comment: requirements, architecture, security, style, complexity, edge-case. Completion criterion: every comment has an issue type.
4. **Write the suggested direction** — for each comment, describe the direction the fix should take (not the fix itself — the fix is the Task Engineer's job to re-dispatch). Completion criterion: every comment has a suggested direction.
5. **Locate each comment precisely** — attach file path and line number to every comment. For GitHub PRs, prepare inline comments using the `github-code-review` skill's API patterns. Completion criterion: every comment has a precise code location.
6. **Format the review comments** — use `templates/review-comment.md` for the per-comment format. For GitHub, use the `github-code-review` skill's inline comment patterns. For re-dispatch, produce structured feedback the Task Engineer can act on. Completion criterion: every comment is formatted and located.

Output: Review comments.

### Task 9: Issue Verdict

Approve, request changes, or reject. Approve = meets all criteria. Request changes = specific fixable issues. Reject = fundamental approach is wrong, needs re-architecture.

1. **Aggregate critical findings** — count Critical-severity comments from Task 8. Completion criterion: the critical count is exact.
2. **Aggregate warnings** — count Warning-severity comments. Completion criterion: the warning count is exact.
3. **Determine the verdict** — apply the decision matrix from `references/review-checklist.md`. Approve: zero critical, zero warnings (suggestions only). Request changes: any critical or warning that is fixable within the current task scope. Reject: the fundamental approach is wrong — the code cannot be fixed within the current task scope and needs re-architecture (feed back to Architect). Completion criterion: the verdict is determined with rationale.
4. **Write the verdict report** — document the verdict, the rationale, the count of findings by severity, and the specific issues that must be addressed (for request changes) or the architectural problems (for reject). Use `templates/review-verdict.md`. Completion criterion: the verdict report is complete with rationale and counts.
5. **Document the feedback path** — for request changes: specify which findings feed back to the Task Engineer for re-dispatch. For reject: specify which architectural problems feed back to the Architect. Completion criterion: the feedback path is documented as a structured artifact.

Output: Verdict with rationale.

### Task 10: Optional — Trigger Cleanup

If approved but the code is over-complicated, spawn a `simplify-code` pass. Not a gate — a quality improvement that runs after approval.

1. **Assess complexity post-approval** — if the verdict is approve and Task 6 identified complexity findings (Warning or Suggestion severity), evaluate whether a cleanup pass would meaningfully improve the code. Completion criterion: a yes/no decision is made with rationale.
2. **Trigger simplify-code** — if yes, invoke the `simplify-code` skill on the approved code. Completion criterion: the simplify-code pass is triggered or explicitly skipped with rationale.
3. **Re-verify after cleanup** — after the simplify-code pass, re-run Tasks 2–5 to confirm the simplification didn't break compliance, security, or style. Completion criterion: all re-verification checks pass.

Output: Simplified code (optional).

## Feedback Paths

- **To Task Engineer (request changes):** Each review comment with severity Critical or Warning feeds back to the Task Engineer as a structured artifact: the comment, the code location, the issue type, the suggested direction, and the originating task spec. The Task Engineer refines the task spec and re-dispatches.
- **To Architect (reject):** If the verdict is reject, the feedback to the Architect must specify: which module boundary is wrong, which interface contract is violated, and why the code cannot be fixed within the current task scope. The Architect re-evaluates the module design.
- **To Tester (edge case gaps):** Edge case gaps from Task 7 that are not covered by the test suite feed back to the Tester as structured artifacts: the code location, the unhandled input/state, and the recommended new test case. The Tester adds the test case and re-runs.
- **From Task Engineer (re-dispatch):** After a fix is re-dispatched and delivered, the Reviewer re-reviews (re-enter at Task 1 with the new code). The re-dispatch notification must include: the review comment IDs being addressed, the changed files, and the new diff.

## Quick Reference

| Task | Key Output | Reference / Template |
|------|------------|---------------------|
| 1. Receive completed code | Review queue entry | — |
| 2. Requirements compliance | Compliance checklist | `references/review-checklist.md`, `templates/compliance-checklist.md` |
| 3. Architecture compliance | Architecture compliance report | `references/review-checklist.md` |
| 4. Security scan | Security scan results | `references/security-review.md` |
| 5. Style and convention check | Style check results | `references/review-checklist.md` |
| 6. Complexity assessment | Complexity report | `references/complexity-metrics.md` |
| 7. Edge case gap identification | Edge case findings | `references/edge-case-analysis.md` |
| 8. Produce review comments | Review comments | `templates/review-comment.md` |
| 9. Issue verdict | Verdict with rationale | `templates/review-verdict.md` |
| 10. Optional cleanup | Simplified code | — |

### Verdict decision matrix

| Condition | Verdict |
|-----------|---------|
| Zero critical, zero warnings (suggestions only) | **Approve** |
| Any critical or warning, fixable within task scope | **Request changes** |
| Fundamental approach wrong, not fixable within task scope | **Reject** |

### Severity scale

| Severity | Definition | Examples |
|----------|-----------|----------|
| Critical | Security vulnerability, data loss, spec violation | SQL injection, unhandled crash path, missing requirement |
| Warning | Maintainability, style, missing edge case handling | Function too complex, missing null check, naming violation |
| Suggestion | Improvement, non-blocking | DRY refactoring, better naming, minor simplification |

### Complexity thresholds

| Metric | Threshold | Source |
|--------|-----------|--------|
| Cyclomatic complexity | > 10 = flag, > 15 = flag with justification required | McCabe (1976), NIST Structured Testing |
| Cognitive complexity | Nesting > 3 levels = flag | Sonar cognitive complexity (2018) |
| Function length | > 50 lines (excl. comments) = flag | SEI maintainability guidelines |
| SEI risk category | 1–10 = low risk, 11–20 = moderate, 21–50 = high, 51+ = very high | SEI / Klocwork |

## Verification

- [ ] Every acceptance criterion from the task spec has a code location and a pass/fail assessment
- [ ] Every RTM-mapped requirement ID is accounted for in the compliance checklist
- [ ] Every changed file is verified to be within the task spec's declared scope
- [ ] Every interface the code touches is verified against its interface contract
- [ ] Every applicable cross-cutting concern is checked
- [ ] Security scan covers all pattern categories (secrets, injection, XSS, traversal, deserialization, eval/exec)
- [ ] Dependency audit is run or marked unavailable
- [ ] Every function in the changed code has a complexity, length, nesting, and naming assessment
- [ ] Every edge case category is checked and cross-referenced with test coverage
- [ ] Every review comment has severity, issue type, suggested direction, and precise code location
- [ ] The verdict is determined with rationale and documented in the verdict report
- [ ] Feedback paths to Task Engineer, Architect, and Tester are documented as structured artifacts
