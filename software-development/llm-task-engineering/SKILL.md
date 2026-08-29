---
name: llm-task-engineering
description: Decompose architecture into dispatchable LLM task specs.
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [task-engineering, decomposition, context-curation, task-manifest, llm]
    related_skills: [software-architecture-design, software-requirements-engineering, test-driven-development]
---

# LLM Task Engineering Skill

Transform an approved architecture into a self-contained, dispatchable task manifest that LLM coding agents can execute without additional context. Covers the full pipeline: architecture analysis, implementation-unit identification, scope boundary definition, input-context curation, output-contract definition, acceptance-criteria mapping, dependency-graph construction, constraint specification, single-context-window sizing, and manifest assembly. Produces structured artifacts (task manifest, dependency DAG) grounded in context engineering research (Anthropic, 2025), task decomposition heuristics (OpenAI Codex, 2026), and the ISO/IEC 25010 quality model. Does not design architecture (use `software-architecture-design`) or write requirements (use `software-requirements-engineering`) — it consumes those artifacts to produce executable task specifications.

## When to Use

- User asks to decompose an architecture document into implementation tasks for LLM coding agents
- User needs a task manifest — the dispatchable artifact consumed by a coding harness (Pi, Codex, Claude Code, etc.)
- User wants to curate input context for individual LLM tasks without over- or under-loading the context window
- User needs a dependency DAG showing which tasks block others and which can run in parallel
- User wants to validate that each task fits within a single LLM context window
- Don't use for: architecture design (use `software-architecture-design`), requirements writing (use `software-requirements-engineering`), test generation (use `test-driven-development`), or code review (use `requesting-code-review`)

## Prerequisites

- An approved architecture document, interface contracts, SRS, and RTM from upstream roles — task engineering cannot begin without an architecture to decompose
- No external tools or API keys required — this skill is a structured methodology using Hermes tools (`write_file`, `read_file`, `search_files`, `patch`)
- Familiarity with the target LLM's context window size is needed for Task 9 (sizing). If unknown, assume 128K tokens as a conservative baseline

## Procedure

The task engineering process is sequential but iterative — later tasks may trigger feedback to upstream roles. Follow all ten tasks in order for a new system; enter at the relevant task for incremental work. Each task references a detailed reference or template file.

### Task 1: Analyze Architecture Document

Understand module boundaries, interface contracts, and dependency structure. The architecture defines *what* modules exist; this task defines *how* each module becomes executable work.

1. **Read the architecture document end-to-end** — extract module list, interface contracts, cross-cutting concerns spec, and technology decisions. Completion criterion: every module, interface contract, and cross-cutting concern is catalogued.
2. **Read the RTM** — identify which SRS requirement IDs map to which modules. Completion criterion: every module traces to at least one requirement ID.
3. **Read the decomposability validation report** — note any modules flagged as borderline or requiring attention. Completion criterion: every validation finding is recorded for task-planning use.
4. **Build the module-to-task mapping plan** — for each module, note its complexity (simple, moderate, complex) and estimated task count. Completion criterion: the plan covers every module with an initial task count estimate.

Output: Module-to-task mapping plan. Use `write_file` to save it alongside other project artifacts.

### Task 2: Identify Implementation Units

Map each module to one or more tasks based on complexity. A simple module = one task. A complex module = multiple tasks with clear sub-boundaries.

1. **Decompose each module** — for modules rated "complex" in Task 1, identify sub-boundaries using one of four decomposition axes (see `references/task-sizing.md`): by layer, by feature slice, by phase, or by service. Completion criterion: every complex module has a decomposition rationale.
2. **Draft the task list** — assign a unique ID to each task (e.g., `TASK-001`). For each task, record: title, parent module, one-sentence description. Completion criterion: every task has a unique ID and description, and every module maps to at least one task.
3. **Check for gaps** — verify no module is missing a task and no task exists without a parent module. Completion criterion: the module-to-task map has no orphans in either direction.

Output: Draft task list.

### Task 3: Define Scope Boundary for Each Task

Specify the exact files, modules, and functions this task may touch. Explicit "what NOT to touch" prevents an LLM from refactoring adjacent code it wasn't asked to change.

1. **Define inclusion scope** — for each task, list the files, directories, modules, and functions the task may create or modify. Completion criterion: every task has an explicit inclusion list.
2. **Define exclusion scope** — for each task, list the files, directories, modules, and functions the task must NOT touch, even if they appear related. Completion criterion: every task has an explicit exclusion list.
3. **Check boundary conflicts** — verify no two tasks claim ownership of the same file or function unless one explicitly depends on the other's output. Completion criterion: no uncoordinated scope overlaps.

See `references/scope-boundaries.md` for the scope specification format and anti-patterns.

Output: Scope field per task.

### Task 4: Curate Input Context for Each Task

Select the specific design sections, interface contracts, relevant existing code, and style guides the target LLM needs. This is the most critical step. Too much context = diluted signal and context rot (Anthropic, 2025 — "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases"). Too little = hallucination. The LLM cannot ask for more — what you include is all it gets.

1. **Identify required context components** — for each task, determine which of the following are needed: module responsibility statement, relevant interface contracts (both sides the task implements and consumes), relevant cross-cutting concern conventions, relevant SRS requirements, existing code to extend or integrate with, style guides, technology-specific conventions. Completion criterion: every task has a list of required context components.
2. **Extract and assemble** — pull the actual content for each required component. Trim to the minimal high-signal set — include only the sections of each document that the task needs, not entire documents. Completion criterion: every context component is present and trimmed.
3. **Estimate token cost** — estimate the token count of the assembled context (see `references/context-curation.md` for estimation heuristics). Completion criterion: estimated context tokens are recorded per task.
4. **Apply the context budget rule** — verify the assembled context does not exceed ~40% of the target LLM's context window, leaving 60% for output. If it exceeds, return to step 2 and trim further, or return to Task 2 to decompose the task further. Completion criterion: every task's input context passes the budget check.

See `references/context-curation.md` for the full curation methodology, token estimation, and the context rot rationale.

Output: Context field per task.

### Task 5: Define Output Contract for Each Task

Specify expected function signatures, return types, behavior description, and file structure. The Tester uses this to write tests *before* implementation exists.

1. **Specify expected signatures** — for each task, list the public API the task must produce: function/method names, parameter types, return types. Completion criterion: every task's public API is specified with types.
2. **Specify behavior** — for each function, describe the expected behavior (inputs → outputs, side effects, error cases). Completion criterion: every function has a behavior description covering normal and error paths.
3. **Specify file structure** — list the files the task must create or modify, with expected content per file. Completion criterion: every expected file is listed with a content summary.
4. **Specify integration points** — describe how this task's output connects to other modules via interface contracts. Completion criterion: every interface dependency has a corresponding integration-point description.

See `references/output-contracts.md` for the output contract format and examples.

Output: Output contract field per task.

### Task 6: Map Acceptance Criteria

Pull relevant requirements from the SRS/RTM and attach to each task. Direct mapping — each task's acceptance criteria must trace to specific SRS requirement IDs.

1. **Query the RTM** — for each task, find all SRS requirement IDs that map to the task's parent module. Completion criterion: every task has a list of relevant requirement IDs.
2. **Derive acceptance criteria** — for each requirement ID, write one or more acceptance criteria that verify the requirement is met. Each acceptance criterion must be binary (pass/fail) and verifiable by test or inspection. Completion criterion: every requirement ID has at least one acceptance criterion.
3. **Check traceability** — verify every acceptance criterion traces to a specific requirement ID and every requirement mapped to the task has at least one acceptance criterion. Completion criterion: no orphan criteria and no uncovered requirements.

Output: Acceptance criteria field per task.

### Task 7: Build Dependency Graph

Determine which tasks block others and which can run in parallel. Enables the harness to maximize parallelism without causing integration failures.

1. **Identify dependencies** — for each task, determine which other tasks must complete before this task can start. Dependencies arise from: interface contracts (task B consumes an interface task A produces), shared file modifications (task B modifies a file task A creates), data model dependencies (task B uses a data structure task A defines). Completion criterion: every task has a dependency list (possibly empty).
2. **Identify parallelizable sets** — group tasks that have no dependencies on each other into parallel waves. Completion criterion: every task is assigned to a wave, and no task in a wave depends on another task in the same wave.
3. **Check for cycles** — verify the dependency graph is a DAG (directed acyclic graph). If a cycle exists, tasks have circular dependencies — return to Task 2 to re-decompose. Completion criterion: the graph is acyclic.
4. **Document the DAG** — produce a text-based dependency graph (Mermaid) showing task relationships and parallel waves. Completion criterion: the DAG renders in Mermaid and shows every task.

See `references/dependency-graphs.md` for DAG construction, cycle detection, and Mermaid syntax. Use `templates/dependency-dag.md` for the graph format.

Output: Dependency graph (DAG).

### Task 8: Specify Constraints per Task

Pull coding standards, patterns to follow, libraries to use, and error handling conventions from the architect's cross-cutting concerns spec. Ensure every task enforces the same conventions.

1. **Extract cross-cutting constraints** — from the cross-cutting concerns spec, identify which conventions apply to each task: error handling format, logging conventions, authentication pattern, coding style, naming conventions, framework version constraints. Completion criterion: every task has a constraints list derived from the cross-cutting spec.
2. **Add task-specific constraints** — for each task, add any task-specific constraints: "no new dependencies beyond X," "follow existing pattern in file Y," "use Z library for this functionality." Completion criterion: every task-specific constraint is recorded.
3. **Check constraint consistency** — verify tasks that share a cross-cutting concern enforce the same convention. Completion criterion: no two tasks specify conflicting conventions for the same concern.

Output: Constraints field per task.

### Task 9: Size Each Task for Single-Context-Window Completion

Estimate complexity; if a task is too large, decompose further. Heuristic: if the input context + output contract + constraints + expected output code would exceed ~60% of a context window, the task is too large.

1. **Estimate total context per task** — sum: input context (from Task 4) + output contract (from Task 5) + constraints (from Task 8) + expected output code (estimated from the output contract). Completion criterion: every task has a total context estimate.
2. **Apply the sizing rule** — if total estimated context > ~60% of the target LLM context window, the task is too large. Decompose it into two or more sub-tasks (return to Task 2). Completion criterion: every task passes the sizing check or has been decomposed.
3. **Apply the smart-zone heuristic** — research (Codex, 2026; Claude Code, 2026) indicates LLM performance is highest in the first ~100K tokens of context. Tasks with estimated total context under 100K tokens will produce higher-quality output. Flag tasks exceeding 100K for extra scrutiny. Completion criterion: every task has a smart-zone flag.
4. **Re-validate decomposition** — if any task was decomposed in step 2, re-run Tasks 3–8 for the new sub-tasks. Completion criterion: all new sub-tasks have complete scope, context, output contract, acceptance criteria, and constraints.

See `references/task-sizing.md` for the full sizing heuristic, token estimation tables, and decomposition axes.

Output: Final task sizing check with pass/fail per task.

### Task 10: Assemble and Emit Task Manifest

Compile all tasks into the structured format the harness consumes. This is the deliverable. It must be self-contained — the harness will dispatch each task entry as-is to an LLM.

1. **Assemble each task entry** — for each task, compile: ID, title, description, scope, input context, output contract, acceptance criteria, constraints, dependencies, estimated context size. Use `templates/task-entry.md` for the per-task format. Completion criterion: every task entry has all fields populated.
2. **Assemble the manifest** — compile all task entries plus the dependency DAG, the module-to-task map, and a metadata header (version, date, architecture version, target LLM, context window size). Use `templates/task-manifest.md` for the manifest format. Completion criterion: the manifest is complete with all task entries and metadata.
3. **Self-containment audit** — for each task entry, verify a developer (or LLM) could complete the task using ONLY the information in that entry — no external lookups, no "see also" references to other tasks. Completion criterion: every task entry is self-contained.
4. **Emit** — write the manifest to a file using `write_file`. If the harness expects JSON, convert the structured document to JSON. Completion criterion: the manifest file exists and is valid.

Output: Task manifest (structured document or JSON). See `templates/task-manifest.md` and `templates/task-entry.md`.

## Feedback Paths

- **To Architect:** If a module won't decompose into single-context-window tasks, feed back to the Architect — the module boundary is wrong. The feedback must specify: which module, why it won't decompose (estimated context size vs. limit), and the suggested decomposition direction.
- **To Requirements Engineer:** If acceptance criteria can't be mapped cleanly (requirements aren't atomic enough), feed back to the Requirements Engineer. The feedback must specify: which requirement ID, why it's not atomic, and the suggested split.
- **Self-correction:** If the LLM output doesn't match expectations, revise the task spec — the gap is in the context or output contract. Document the gap, the revision, and the re-dispatch.

## Quick Reference

| Task | Key Output | Reference / Template |
|------|------------|---------------------|
| 1. Architecture analysis | Module-to-task mapping plan | — |
| 2. Implementation units | Draft task list | — |
| 3. Scope boundaries | Scope field per task | `references/scope-boundaries.md` |
| 4. Context curation | Context field per task | `references/context-curation.md` |
| 5. Output contracts | Output contract field per task | `references/output-contracts.md` |
| 6. Acceptance criteria | Acceptance criteria field per task | — |
| 7. Dependency graph | DAG (Mermaid) | `references/dependency-graphs.md`, `templates/dependency-dag.md` |
| 8. Constraints | Constraints field per task | — |
| 9. Sizing check | Sizing verdict per task | `references/task-sizing.md` |
| 10. Manifest assembly | Task manifest | `templates/task-manifest.md`, `templates/task-entry.md` |

### Task sizing quick rules

- Input context ≤ 40% of context window (leaves room for output)
- Total estimated context (input + output + constraints) ≤ 60% of context window
- Smart zone: under ~100K tokens total for highest output quality
- If a task exceeds 60%, decompose along layer, feature slice, phase, or service axis
- "Done when" clause must be present — if you can't write one, the task is too vague

## Pitfalls

1. **Kitchen-sink context.** Stuffing an entire architecture document, full interface specs, and all requirements into a single task's context. The LLM processes irrelevant context and produces unfocused output (Anthropic, 2025 — "context rot"). Trim to the minimal high-signal set per task.
2. **Implicit "see also" references.** A task entry that says "see architecture document section 4.2" is not self-contained — the LLM cannot look it up. Include the relevant content directly in the task's context field.
3. **Missing exclusion scope.** Without an explicit "do NOT touch" list, the LLM will refactor adjacent code it wasn't asked to change, creating integration conflicts. Always specify exclusions (Task 3).
4. **No "done when" clause.** A task without a concrete, programmatically verifiable acceptance criterion is too vague to dispatch. The agent can't confirm "done" without it (Codex, 2026).
5. **Premature parallelization.** Spawning tasks in parallel that have sequential dependencies. Task B needs Task A's output but starts before it's available, leading to hallucinated assumptions. Map dependencies explicitly (Task 7) and only parallelize tasks with no edges between them.
6. **Over-decomposition.** Breaking a three-file change into ten tasks introduces coordination overhead that exceeds the benefit. Rule of thumb: if you would review the change as a single PR, it's probably a single task.
7. **Inconsistent cross-cutting constraints.** Task A says "use structured JSON logging" and Task B says "use plain text logging." Both touch the logging concern but produce incompatible code. Pull constraints from the cross-cutting spec and check consistency (Task 8).
8. **Assuming the LLM can ask for more.** It cannot. Everything the LLM needs must be in the task entry. Missing context = hallucination. There is no "let me check the docs" fallback.
9. **Sizing by gut feeling.** "This looks small enough" without estimating tokens. Use the token estimation heuristics in `references/task-sizing.md` — context rot is real and measurable.
10. **Skipping the self-containment audit.** A manifest that looks complete but has entries with "see also" references or missing context will fail at dispatch time. Run the audit (Task 10, step 3) before emitting.

## Verification

- [ ] Every module from the architecture document maps to at least one task
- [ ] Every task has a unique ID, title, description, and parent module
- [ ] Every task has an explicit inclusion scope AND exclusion scope
- [ ] Every task's input context is trimmed to the minimal high-signal set
- [ ] Every task's input context passes the 40% budget check
- [ ] Every task's total estimated context passes the 60% sizing check
- [ ] Every task has an output contract with typed signatures and behavior descriptions
- [ ] Every task's acceptance criteria trace to specific SRS requirement IDs via the RTM
- [ ] The dependency graph is a DAG (no cycles) and shows parallel waves
- [ ] Every task's constraints are consistent with the cross-cutting concerns spec
- [ ] Every task entry is self-contained (no external lookups required)
- [ ] The manifest has a metadata header with version, architecture version, and target LLM
- [ ] Feedback paths to Architect and Requirements Engineer are documented as structured artifacts
