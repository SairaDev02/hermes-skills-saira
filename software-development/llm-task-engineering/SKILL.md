---
name: llm-task-engineering
description: Decompose architecture into self-contained task specs.
version: 0.3.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [task-engineering, decomposition, context-curation, task-manifest, llm]
    related_skills: [software-architecture-design, software-requirements-engineering, qa-engineer]
---

# LLM Task Engineering Skill

Transform approved architecture and requirements into a normalized task manifest and self-contained dispatch bundles for a coding harness. The source manifest minimizes duplication; generated bundles inline the context needed by each task. This documentation-only role specifies scope, context, outputs, acceptance, constraints, dependencies, and sizing; it does not implement tasks, write tests, or execute commands.

## When to Use

- Decompose modules into dispatchable implementation tasks.
- Build a task manifest, dependency DAG, context package, or output contract.
- Validate task scope, self-containment, and context-window fit.
- Don't use for: architecture, requirements, test implementation, code, or task execution.

## Prerequisites

- Approved architecture, interface contracts, SRS, RTM, cross-cutting concerns, and decomposability report.
- Shared project context: `docs/PROJECT-CONSTITUTION.md`, `docs/REFERENCE-INDEX.md`, `docs/GLOSSARY.md`, `docs/ASSUMPTIONS.md`, and `docs/CHANGE-IMPACT-MAP.md`.
- Target harness and context-window size; if unknown, record the assumption instead of presenting it as fact.
- Use `read_file`, `search_files`, `write_file`, and `patch` for artifacts.
- Use the shared root `templates/HANDOFF.md` for the transition to the implementation harness.

## Procedure

Complete all tasks for a new manifest. Re-run affected tasks after decomposition, contract, or requirement changes.

### 1. Map modules to implementation units

Catalog every module, contract, requirement link, and architecture finding. Decompose complex modules by layer, feature slice, phase, or service only when the boundary is coherent. **Done when:** every module maps to one or more uniquely identified tasks and no task is orphaned.

### 2. Define scope and ownership

For each task, list files/modules/functions it may create or modify and an explicit exclusion list. Identify shared-file ownership and required sequencing. **Done when:** every task has inclusion and exclusion scope, and every overlap is coordinated by a dependency or integration owner.

### 3. Curate normalized context

Create reusable, immutable context blocks for module responsibilities, contracts, cross-cutting rules, requirements, existing code, and style constraints. Reference blocks from source task entries; do not duplicate them unnecessarily. **Done when:** every task has a minimal context-block list and the source manifest has no contradictory copies.

### 4. Generate dispatch bundles

Expand each task's context-block list into a self-contained bundle for the harness. The bundle must contain all required context and no unresolved “see also” references. Record the source manifest version and block versions. **Done when:** every bundle can be dispatched without external lookup and can be regenerated deterministically.

The normalized manifest and generated bundles are separate artifacts: maintainers edit the former; the harness consumes the latter.

### 5. Define output and acceptance

Specify public signatures and types, behavior on normal and error paths, side effects, expected files, integration points, and implementation-neutral acceptance criteria. Map each criterion to an SRS requirement ID through the RTM. **Done when:** every task has a binary, verifiable done condition and every mapped requirement is covered.

### 6. Build and validate dependencies

Record dependencies caused by interfaces, shared files, data models, migrations, and verification gates. Group independent tasks into parallel waves and represent the graph in Mermaid or the selected structured format. **Done when:** every task has a dependency list, every wave is valid, and the graph is acyclic.

### 7. Apply constraints and size tasks

Propagate cross-cutting conventions, then add task-specific constraints and check for conflicts. Estimate input context, output contract, constraints, and expected output size against the target context window. Decompose tasks above the agreed limit and re-run scope through dependency checks. **Done when:** every task has a sizing verdict, smart-zone flag if used, and consistent constraints.

### 8. Assemble and emit the manifest

Use `templates/task-entry.md`, `templates/task-manifest.md`, and `templates/dependency-dag.md` where present. Include manifest version, source artifact versions, target harness, context-window assumption, shared context blocks, task entries, module map, DAG, and generated bundle index. **Done when:** the normalized manifest and every generated bundle are complete, versioned, reproducible, and valid.

## Post-dispatch live-QA triage (role boundary)

When the user reports defects from live testing of dispatched implementation work, the Task Engineer does NOT write fixes. The role is: diagnose, hand off, verify.

1. **Diagnose first** — trace the root cause in the worktree with evidence before anything else: failure logs (e.g. the app's diagnostics sink), live probes (curl/API checks), code reads along the failing seam. State root causes with file anchors in the handoff; never hand the harness a blank map. If evidence contradicts the traced cause mid-fix, the harness stops and reports back.
2. **Hand the fix to the coding harness** as a plaintext prompt containing: exact symptoms; a step-0 evidence command the harness must run and quote (so it confirms the diagnosis before touching code); the traced root causes with file paths; minimal fix guidance (pattern to follow, constraints honored); verification commands with expected counts (test suites, linters, builds) that the harness must quote; hard constraints (cross-cutting rules, no new dependencies, touch-only file list, no example/contract edits); commit discipline (one commit, message format, no push); and known-unknowns explicitly marked do-not-chase.
3. **Verify only after the user says fixes are applied** — run independent V&V: full test suites, audits, builds, re-running commands personally and checking counts. Never accept the harness's own verification claims as evidence.
4. **Number the trail** — record each live-QA defect as BUG-N with its root cause and fix commit so regression tests and manifest feedback artifacts stay traceable across rounds.

## Required task entry

`id`, title, parent module, objective, scope in, scope out, context block IDs, output contract, acceptance criteria with requirement IDs, constraints, dependencies, integration checkpoints, estimated context, bundle path/version, and status.

## Quick Reference

| Task | Artifact |
|---|---|
| Mapping | Module-to-task map |
| Boundaries | Scope fields |
| Context | Curated task context |
| Contract | Output specification |
| Acceptance | RTM-linked criteria |
| Coordination | DAG and parallel waves |
| Emission | Versioned manifest |

## Pitfalls

- Kitchen-sink context, duplicated context blocks, or external “see also” dependencies in generated bundles.
- Missing exclusion scope, causing unrequested refactoring.
- Parallelizing tasks with hidden interface, migration, or shared-file dependencies.
- Writing acceptance criteria that cannot be tested or inspected.
- Inventing a target context size instead of recording an assumption.
- Over-decomposing small coherent changes into coordination overhead.
- Updating the architecture or SRS without regenerating affected task entries.
- Fixing live-QA defects directly instead of handing them to the coding harness — the Task Engineer diagnoses and verifies, the harness edits code.

## Verification

- [ ] Every architecture module maps to a task; no task is orphaned.
- [ ] Every task has unique identity, objective, scope in, and scope out.
- [ ] Context blocks are minimal, versioned, non-contradictory, and within the stated budget.
- [ ] Every task has a generated, self-contained dispatch bundle with a source/version index.
- [ ] Output contracts include typed behavior, files, errors, and integration points.
- [ ] Acceptance criteria are binary and trace to SRS IDs via the RTM.
- [ ] The dependency graph is complete, acyclic, and wave-valid.
- [ ] Constraints are consistent with cross-cutting architecture rules.
- [ ] Each task has a sizing verdict and all manifest metadata is present.
- [ ] No task requires an external lookup to understand its assignment.
- [ ] Live-QA defects were handed to the harness via a guided prompt (evidence + root causes + verification gates), and independent V&V ran after the user confirmed the fixes.
