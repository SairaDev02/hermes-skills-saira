# Lifecycle Role Index

The specialist roles are documentation-only. Each role produces a versioned artifact package and a structured handoff; implementation and execution belong to the assigned harness or operator. The RAD Engineer is governed separately and is intentionally not covered here.

## Shared handoff contract

All role transitions use [`templates/HANDOFF.md`](templates/HANDOFF.md). Findings and feedback use [`templates/feedback-record.yaml`](templates/feedback-record.yaml). Shared project context lives in [`docs/`](docs/): constitution, references, glossary, assumptions, collaboration protocol, and change-impact map. These are the authoritative coordination rules; role skills describe only role-specific work.

## Roles

| # | Role | Input | Output package | Next owner | Skill |
|---:|---|---|---|---|---|
| 1 | Requirements Engineer | Problem, goals, constraints, stakeholder evidence | Requirements baseline: SRS, RTM, feasibility decision, change records | Architect | [Skill](software-development/software-requirements-engineering/SKILL.md) |
| 2 | Architect | Approved requirements baseline | Architecture boundary baseline: drivers, ADRs, modules, contracts, cross-cutting rules, diagrams | Task Engineer | [Skill](software-development/software-architecture-design/SKILL.md) |
| 3 | Task Engineer | Architecture boundary baseline and requirements | Normalized task manifest plus self-contained dispatch bundles | Implementation harness | [Skill](software-development/llm-task-engineering/SKILL.md) |
| 4 | QA Engineer | Requirements, contracts, task outputs, implementation evidence | QA design package; later evidence and coverage package | Harness, then Code Reviewer | [Skill](software-development/qa-engineer/SKILL.md) |
| 5 | Code Reviewer | Versioned code, task spec, QA evidence, review basis | Review package and gate verdict | DevOps / Release or Task Engineer | [Skill](software-development/code-reviewer/SKILL.md) |
| 6 | DevOps / Release Engineer | Approved code, review gate, deployment constraints, QA evidence | Delivery and operational readiness package | Release operator / service owner | [Skill](software-development/devops-release-engineer/SKILL.md) |

## Handoff readiness

A handoff is `READY`, `CONDITIONAL`, or `BLOCKED`. The receiver must be able to work from the package without an undocumented conversation. Every handoff identifies artifact versions, open findings, changed IDs, ownership, and receiver acceptance criteria.

## Feedback routing

Use a feedback record instead of informal “talk to the other role” instructions:

```text
Requirements → Architect: requirement or driver clarification
Architect → Task Engineer: boundary or contract defect
Task Engineer → Architect/Requirements: decomposition or traceability gap
QA → Task Engineer: implementation or task-spec defect
QA → Requirements: untestable or uncovered requirement
Review → Task Engineer: fixable code finding
Review → Architect: re-architecture finding
Release → owning role: delivery or operational readiness gap
```

The receiving role closes the record or creates a superseding record. Do not silently edit an upstream baseline.

## Project closure

Closure is not a role; it is a checklist applied by the service owner (with the DevOps / Release Engineer as acting coordinator) once delivery is accepted and the lifecycle's final handoff is `READY`. Closure confirms the project's documentation-only contracts actually ended cleanly — nothing stays open by default.

Before closing a project, verify:

- Every feedback record is closed or superseded; none silently expired.
- Every entry in `docs/ASSUMPTIONS.md` is resolved, or explicitly archived with its unresolved state noted.
- All handoff packages and artifact versions are final, versioned, and archived under their owning role.
- The change-impact map is empty of pending follow-ups.
- Lessons learned are written as candidate inputs to the Requirements Engineer for the next project — never as edits to a closed baseline.

Closure output is a single [`templates/CLOSURE.md`](templates/CLOSURE.md) record, filed with the project's handoff packages. The next project's role 1 consumes only that record; nothing else from the closed project is authoritative.
