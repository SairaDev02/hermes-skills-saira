---
name: llm-task-engineering
description: Decompose architecture into self-contained task specs.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [task-engineering, decomposition, context-curation, task-manifest, llm]
    related_skills: [software-architecture-design, software-requirements-engineering, qa-engineer]
---

# LLM Task Engineering Skill

Transform approved architecture and requirements into a self-contained task manifest for a coding harness. This documentation-only role specifies scope, context, outputs, acceptance, constraints, dependencies, and sizing; it does not implement tasks, write tests, or execute commands.

## When to Use

- Decompose modules into dispatchable implementation tasks.
- Build a task manifest, dependency DAG, context package, or output contract.
- Validate task scope, self-containment, and context-window fit.
- Don't use for: architecture, requirements, test implementation, code, or task execution.

## Prerequisites

- Approved architecture, interface contracts, SRS, RTM, cross-cutting concerns, and decomposability report.
- Target harness and context-window size; if unknown, record the assumption instead of presenting it as fact.
- Use `read_file`, `search_files`, `write_file`, and `patch` for artifacts.

## Procedure

Complete all tasks for a new manifest. Re-run affected tasks after decomposition, contract, or requirement changes.

### 1. Map modules to implementation units

Catalog every module, contract, requirement link, and architecture finding. Decompose complex modules by layer, feature slice, phase, or service only when the boundary is coherent. **Done when:** every module maps to one or more uniquely identified tasks and no task is orphaned.

### 2. Define scope and ownership

For each task, list files/modules/functions it may create or modify and an explicit exclusion list. Identify shared-file ownership and required sequencing. **Done when:** every task has inclusion and exclusion scope, and every overlap is coordinated by a dependency or integration owner.

### 3. Curate minimal context

Include only the module responsibility, relevant contracts on both sides, applicable cross-cutting rules, linked requirements, existing code context, and style constraints. Copy required content into the task entry; do not rely on “see also” references. Estimate tokens and keep input context within the chosen budget. **Done when:** each entry contains all necessary context with no irrelevant document dump.

### 4. Define output and acceptance

Specify public signatures and types, behavior on normal and error paths, side effects, expected files, integration points, and implementation-neutral acceptance criteria. Map each criterion to an SRS requirement ID through the RTM. **Done when:** every task has a binary, verifiable done condition and every mapped requirement is covered.

### 5. Build and validate dependencies

Record dependencies caused by interfaces, shared files, data models, migrations, and verification gates. Group independent tasks into parallel waves and represent the graph in Mermaid or the selected structured format. **Done when:** every task has a dependency list, every wave is valid, and the graph is acyclic.

### 6. Apply constraints and size tasks

Propagate cross-cutting conventions, then add task-specific constraints and check for conflicts. Estimate input context, output contract, constraints, and expected output size against the target context window. Decompose tasks above the agreed limit and re-run scope through dependency checks. **Done when:** every task has a sizing verdict, smart-zone flag if used, and consistent constraints.

### 7. Assemble and emit the manifest

Use `templates/task-entry.md`, `templates/task-manifest.md`, and `templates/dependency-dag.md` where present. Include manifest version, source artifact versions, target harness, context-window assumption, task entries, module map, and DAG. **Done when:** every entry is complete, self-contained, versioned, and the manifest format is valid.

## Required task entry

`id`, title, parent module, objective, scope in, scope out, embedded context, output contract, acceptance criteria with requirement IDs, constraints, dependencies, integration checkpoints, estimated context, and status.

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

- Kitchen-sink context or external “see also” dependencies.
- Missing exclusion scope, causing unrequested refactoring.
- Parallelizing tasks with hidden interface, migration, or shared-file dependencies.
- Writing acceptance criteria that cannot be tested or inspected.
- Inventing a target context size instead of recording an assumption.
- Over-decomposing small coherent changes into coordination overhead.
- Updating the architecture or SRS without regenerating affected task entries.

## Verification

- [ ] Every architecture module maps to a task; no task is orphaned.
- [ ] Every task has unique identity, objective, scope in, and scope out.
- [ ] Context is minimal, embedded, and within the stated budget.
- [ ] Output contracts include typed behavior, files, errors, and integration points.
- [ ] Acceptance criteria are binary and trace to SRS IDs via the RTM.
- [ ] The dependency graph is complete, acyclic, and wave-valid.
- [ ] Constraints are consistent with cross-cutting architecture rules.
- [ ] Each task has a sizing verdict and all manifest metadata is present.
- [ ] No task requires an external lookup to understand its assignment.
