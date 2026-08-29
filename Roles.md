# Task Definitions for Each Role

These are defined as discrete, sequential units of work — each with its input, output, and dependency on other roles. Ordered by lifecycle position. Feedback paths noted where they exist.

---

## Role 1: Requirements Engineer

**Input:** User's raw problem statement, business goals, stakeholder access
**Output:** SRS document, RTM, feasibility report
**Feeds into:** Architect

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Feasibility study** — assess technical, operational, economic, legal, schedule dimensions | Go/no-go report | Stop here if no-go; saves all downstream effort |
| 2 | **Stakeholder identification** — list every affected party with contact path | Stakeholder register | In LLM context, stakeholders may include the user, the harness operator, and downstream system constraints |
| 3 | **Requirements elicitation** — select and execute techniques (interviews, document analysis, prototyping); record raw needs | Raw requirements list | Flag conflicts and gaps immediately — every gap becomes a downstream hallucination |
| 4 | **Requirements classification** — categorize each as functional, non-functional, constraint, or acceptance criterion | Classified requirements table | Non-functional requirements must be quantified (ISO/IEC 25010 quality model) — "fast" → "responds within 200ms at p95" |
| 5 | **Requirements specification** — write each in EARS syntax, atomic, active voice, "shall" for binding | Formalized requirement entries | Each requirement gets: unique ID, source, MoSCoW priority, status, version, rationale |
| 6 | **Requirements V&V** — run quality attribute checklist (consistent, complete, unambiguous, verifiable, feasible, atomic, traceable, necessary, implementation-free) | V&V results with issue log | Iterate — V&V is not a one-time gate |
| 7 | **RTM construction** — link each requirement to its source, parent/child requirements, design elements, and test cases | Requirements Traceability Matrix | The RTM is the backbone — it's how the Tester and Reviewer verify nothing was missed |
| 8 | **Change management setup** — define how requirement changes are proposed, assessed, approved, and propagated | Change management process doc | Critical for LLM teams: any spec change must propagate to Task Engineer (re-dispatch affected tasks), Tester (update test specs), Reviewer (update acceptance criteria) |

**Feedback path:** If the Architect reports that a requirement is architecturally unimplementable or doesn't decompose cleanly, return to task 5 for revision.

---

### Role 2: Architect

**Input:** Approved SRS, RTM, feasibility report
**Output:** Architecture document, interface contracts, ADRs
**Feeds into:** Task Engineer

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Analyze architectural drivers** — extract functional requirements, quality attributes, and constraints from the SRS | Driver analysis table | Quality attributes (performance, security, scalability) drive pattern selection more than functional reqs |
| 2 | **Select architectural pattern** — choose style(s) appropriate for the drivers (layered, microservices, event-driven, etc.) | Pattern selection with rationale | Record as an ADR |
| 3 | **Module decomposition** — break the system into modules with clear boundaries | Module list with responsibility statements | **LLM-critical:** each module must be implementable within a single LLM context window. If a module is too large, decompose further. The boundary *is* the task interface |
| 4 | **Define interface contracts** — specify signatures, data models, error contracts, and communication protocols between modules | Interface specification document | This is the shared coordination artifact — parallel LLMs produce compatible code only if interfaces are explicit |
| 5 | **Technology selection** — choose languages, frameworks, data stores, libraries | Technology decisions with rationale (ADRs) | Consider LLM familiarity — models produce higher-quality code in well-represented languages and frameworks |
| 6 | **Define cross-cutting concerns** — error handling strategy, logging, authentication, data flow, configuration | Cross-cutting concerns spec | If these aren't specified, each downstream LLM will invent its own — guaranteed inconsistency |
| 7 | **Produce architecture diagrams** — text-based (Mermaid, PlantUML) showing module relationships, data flow, deployment topology | Architecture diagrams | Text-based because LLMs consume and reason about text, not images |
| 8 | **Validate decomposability** — check that each module maps to one or more self-contained tasks that a single LLM can complete without needing context from other modules | Decomposability validation report | If a module requires deep knowledge of another module's internals to implement, the boundary is wrong — re-decompose |

**Feedback path:** If the Task Engineer reports that a module boundary doesn't produce clean task specs (too much shared context needed, ambiguous interfaces), return to task 3.

---

### Role 3: Task Engineer

**Input:** Architecture document, interface contracts, SRS, RTM
**Output:** Task manifest — the dispatchable artifact consumed by Pi
**Feeds into:** External harness (Pi), which dispatches to LLMs

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Analyze architecture document** — understand module boundaries, interface contracts, and dependency structure | Module-to-task mapping plan | The architecture defines *what* modules exist; this task defines *how* each module becomes executable work |
| 2 | **Identify implementation units** — map each module to one or more tasks based on complexity | Draft task list | A simple module = one task. A complex module = multiple tasks with clear sub-boundaries |
| 3 | **Define scope boundary for each task** — exact files, modules, and functions this task may touch | Scope field per task | Explicit "what NOT to touch" — prevents an LLM from refactoring adjacent code it wasn't asked to change |
| 4 | **Curate input context for each task** — select the specific design sections, interface contracts, relevant existing code, and style guides the target LLM needs | Context field per task | This is the most critical step. Too much context = diluted signal. Too little = hallucination. The LLM cannot ask for more — what you include is all it gets |
| 5 | **Define output contract for each task** — expected function signatures, return types, behavior description, file structure | Output contract field per task | The Tester uses this to write tests *before* implementation exists |
| 6 | **Map acceptance criteria** — pull relevant requirements from the SRS/RTM and attach to each task | Acceptance criteria field per task | Direct mapping — each task's acceptance criteria must trace to specific SRS requirement IDs |
| 7 | **Build dependency graph** — determine which tasks block others and which can run in parallel | Dependency graph (DAG) | Enables Pi to maximize parallelism without causing integration failures |
| 8 | **Specify constraints per task** — coding standards, patterns to follow, libraries to use, error handling conventions | Constraints field per task | Pull from the architect's cross-cutting concerns spec — ensure every task enforces the same conventions |
| 9 | **Size each task for single-context-window completion** — estimate complexity; if a task is too large, decompose further | Final task sizing check | Heuristic: if the input context + output contract + constraints + expected output code would exceed ~60% of a context window, the task is too large |
| 10 | **Assemble and emit task manifest** — compile all tasks into the structured format Pi consumes | Task manifest (JSON/structured doc) | This is the deliverable. It must be self-contained — Pi will dispatch each task entry as-is to an LLM |

**Feedback paths:**
- If a module won't decompose into single-context-window tasks → feed back to Architect (boundary is wrong)
- If acceptance criteria can't be mapped cleanly → feed back to Requirements Engineer (requirements aren't atomic enough)
- If Pi reports LLM output doesn't match expectations → revise the task spec (gap in context or output contract)

---

### Role 4: Tester / QA Engineer

**Input:** SRS, RTM, task output contracts, completed implementation from Pi
**Output:** Test suites, coverage reports, bug reports
**Feeds into:** Code Reviewer, Task Engineer (for re-dispatch)

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Analyze SRS and output contracts** — read requirements and task specs, NOT the implementation | Test planning doc | Reading the implementation first introduces confirmation bias — the tester subconsciously writes tests that validate the code rather than the spec |
| 2 | **Derive test cases from acceptance criteria** — each acceptance criterion → at least one positive test and one negative test | Test case list | Traceability: each test case maps to an SRS requirement ID via the RTM |
| 3 | **Write test specifications** — unit tests, integration tests, edge cases, boundary conditions, negative tests | Test specification document | Unit tests against output contracts; integration tests against interface contracts |
| 4 | **Define test data and fixtures** — inputs, expected outputs, mock/stub configurations | Test fixtures | Edge cases: empty inputs, null values, max-length strings, concurrent access, timeout behavior |
| 5 | **Write test suites** — implement the test specifications as executable tests (TDD: RED phase) | Test code | In TDD these run and fail before implementation exists; after Pi delivers implementation, they should pass |
| 6 | **Run tests against completed implementation** — execute the test suite on Pi's output | Test results report | Document failures with: failing test, expected vs. actual, reproduction steps |
| 7 | **Exploratory QA** — manually probe the system for issues tests didn't catch (dogfood approach) | Exploratory QA report | LLM code often passes unit tests but fails on integration, state management, and unexpected input combinations |
| 8 | **Produce bug reports** — for each defect: reproduction steps, severity, affected requirement ID, suggested fix area | Bug reports | "Suggested fix area" not "suggested fix" — the tester identifies *where* the problem is, not how to fix it (that's the Task Engineer's job to re-dispatch) |
| 9 | **Coverage gap analysis** — cross-reference RTM with test results to find requirements not covered by any passing test | Coverage gap report | A requirement with no passing test = unverified, regardless of whether the code "works" |
| 10 | **Regression verification** — after a fix is re-dispatched and delivered, re-run the full suite to confirm the fix didn't break anything | Regression test results | LLM fixes frequently introduce new bugs while fixing old ones — the fix optimized for the reported symptom, not the root cause |

**Feedback path:** Bug reports → Task Engineer (re-dispatch with refined context/constraints) → new implementation → Tester re-runs. Coverage gaps → Task Engineer (missing tasks) or Requirements Engineer (untestable requirements).

---

### Role 5: Code Reviewer

**Input:** Completed code from Pi, architecture document, SRS, RTM, test results
**Output:** Review verdict (approve / request changes / reject), review comments
**Feeds into:** Task Engineer (for re-dispatch), or merge gate

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Receive completed code** — diff, PR, or file set from Pi's output | Review queue entry | Must have the task spec that generated this code — review is against the spec, not just "does this look good" |
| 2 | **Requirements compliance check** — does the implementation satisfy the SRS requirements mapped to this task? | Compliance checklist | Use the RTM to verify each acceptance criterion is met by the code |
| 3 | **Architecture compliance check** — does the code respect module boundaries, interface contracts, and cross-cutting concerns? | Architecture compliance report | Most common LLM failure: an LLM reaches outside its module boundary to "fix" something it wasn't asked to touch |
| 4 | **Security scan** — automated vulnerability detection, dependency audit, secret detection | Security scan results | Use requesting-code-review skill's security gates |
| 5 | **Style and convention check** — does the code follow the constraints specified in the task manifest? | Style check results | Linter output + manual check for pattern adherence |
| 6 | **Complexity and maintainability assessment** — cyclomatic complexity, function length, nesting depth, naming clarity | Complexity report | LLMs tend to write verbose but shallow code — long functions that do little, or deeply nested conditionals that could be flattened |
| 7 | **Edge case gap identification** — are there inputs or states the code doesn't handle that the Tester may not have covered? | Edge case findings | The Reviewer and Tester have complementary blind spots — the Tester tests the spec; the Reviewer reads the code and finds what the spec *missed* |
| 8 | **Produce review comments** — inline comments on specific code locations with severity, issue type, and suggested direction | Review comments | Via gh CLI or REST API for GitHub; structured feedback for Pi re-dispatch otherwise |
| 9 | **Issue verdict** — approve, request changes, or reject | Verdict with rationale | Approve = meets all criteria. Request changes = specific fixable issues. Reject = fundamental approach is wrong, needs re-architecture |
| 10 | **Optional: trigger cleanup** — if approved but code is over-complicated, spawn simplify-code pass | Simplified code | Not a gate — a quality improvement that runs after approval |

**Feedback path:** Request changes → Task Engineer refines task spec → Pi re-dispatches → Reviewer re-reviews. Reject → Architect re-evaluates module design.

---

### Role 6: DevOps / Release Engineer *(situational)*

**Input:** Approved code from Reviewer, architecture deployment diagrams
**Output:** CI/CD pipelines, deployment automation, release artifacts

| # | Task | Output Artifact | Notes |
| --- | ------ | ----------------- | ------- |
| 1 | **Define CI pipeline** — build, test, lint, security scan on every push/merge | CI configuration (GitHub Actions, etc.) | This is the automated guardrail that catches LLM regressions without human review |
| 2 | **Set up deployment pipeline** — staging → production with gates | Deployment config | Gate on: all tests pass, security scan clean, review approved |
| 3 | **Environment management** — dev, staging, production configs, secrets, variables | Environment configs | Secrets in `.env` / vault, never in config — mirrors Hermes's own invariant |
| 4 | **Release process definition** — versioning scheme, changelog generation, release notes | Release process doc | Automate changelog from commit messages / PR titles |
| 5 | **Monitoring and alerting** — health checks, error tracking, performance metrics | Monitoring config | LLM-generated code may have subtle performance issues that only surface under load |
| 6 | **Rollback automation** — one-command revert to previous known-good state | Rollback script/procedure | When an LLM-introduced regression reaches production, rollback speed is the damage limiter |

---

## Cross-Role Feedback Map

```text
Requirements Engineer ─────────────────────────────────────────┐
        │                                                      │
        ▼                                                      │
    Architect ◄──── (boundary won't decompose) ──── Task Engineer
        │                                              │
        ▼                                              │ (task spec gaps)
    Task Engineer ──── (task manifest) ───► Pi (harness) ──► LLMs
        │                                              │
        │ (bug reports)                                ▼
        │                                    Completed code
        ▼                                              │
    Tester ◄──────── (implementation) ─────────────────┤
        │                                              │
        ▼                                              ▼
    Code Reviewer ◄──────── (code + test results) ─────┘
        │
        ▼
    [Approve] → DevOps → Release
    [Request changes] → Task Engineer (refine spec → Pi re-dispatch)
    [Reject] → Architect (re-design)
```

The core insight for skill development: **every feedback path in this diagram should be an explicit, documented artifact — not an implicit "go talk to the other role."** In LLM-based development, coordination is artifact flow. Each arrow should produce a structured document that the receiving role can act on without additional conversation.
