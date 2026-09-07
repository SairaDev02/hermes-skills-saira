---
name: software-architecture-design
description: Design architecture from approved requirements.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [architecture, design, adr, interfaces, decomposition, drivers]
    related_skills: [software-requirements-engineering, llm-task-engineering, qa-engineer]
---

# Software Architecture Design Skill

Produce an implementation-ready architecture package from approved requirements. This role defines drivers, boundaries, interfaces, technology decisions, cross-cutting rules, diagrams, and decomposability evidence; it does not write application code or task manifests.

## When to Use

- Design or review architecture from an approved SRS, RTM, and feasibility decision.
- Select patterns or technologies, define module boundaries, or specify interfaces.
- Produce ADRs, text-based diagrams, or a decomposability report.
- Don't use for: requirements authoring, implementation tasks, executable code, or code review.

## Prerequisites

- Approved SRS, RTM, feasibility report, and known deployment constraints.
- Shared project context: `docs/PROJECT-CONSTITUTION.md`, `docs/REFERENCE-INDEX.md`, `docs/GLOSSARY.md`, `docs/ASSUMPTIONS.md`, and `docs/CHANGE-IMPACT-MAP.md`.
- Use `read_file`, `search_files`, `write_file`, and `patch` for artifacts.
- Produce Mermaid or PlantUML source rather than image-only diagrams.

## Procedure

Complete the tasks in order for a new system; revisit earlier tasks when validation exposes a boundary or driver problem.

### 1. Analyze architectural drivers

Extract functional drivers, measurable quality attributes, constraints, and deployment concerns. Link every driver to requirement IDs and identify sensitivity points and tradeoffs. **Done when:** the driver table has no orphan requirements, unquantified quality targets, or unowned constraints.

### 2. Select patterns and technologies

Compare candidate architectural styles against the driver set. Record one decision per ADR with context, alternatives, decision, consequences, status, and trace links. Select technologies only after the pattern decision and evaluate fit, constraints, operational cost, security, and team familiarity. **Done when:** every consequential pattern and technology choice has an ADR with rejected alternatives and rationale.

### 3. Decompose modules

Define each module's responsibility, owned data/state, public surface, exclusions, dependencies, and likely implementation size. Keep boundaries independently understandable and sized for a single task context. **Done when:** every module has one accountable responsibility, no conflicting ownership exists, and oversized modules are decomposed.

### 4. Define interface contracts

For every dependency, specify communication mode, operation signatures, schemas, validation, side effects, idempotency, versioning, timeouts, retries, and error contracts. **Done when:** either side can implement or integrate from the contract without undocumented assumptions.

### 5. Specify cross-cutting concerns

Define error handling, logging, authentication, authorization, validation, configuration, observability, privacy, accessibility, data flow, and resilience. Assign an owner and concrete convention for each concern, or mark it N/A with rationale. **Done when:** downstream task constraints can be copied from one authoritative specification.

### 6. Produce and validate diagrams

Create context, container, component where needed, deployment, and primary data-flow diagrams in Mermaid or PlantUML. Keep names consistent with modules and ADRs. **Done when:** diagrams render as text and every actor, module, dependency, and deployment node has a traceable source.

### 7. Validate decomposability

For every module, check that a task can implement it using only its responsibility, contracts, applicable cross-cutting rules, and relevant requirements. Check context budget, undocumented dependencies, ownership overlap, and feedback from Task Engineering. **Done when:** the report has a pass/fail verdict for every module and a precise return point for each failure.

## Handoff

Use the shared root `templates/HANDOFF.md` for the architecture boundary baseline. Include module ownership, interface/ADR versions, cross-cutting rules, decomposability status, unresolved risks, and explicit constraints for Task Engineering.

## Required artifact shapes

- **Driver:** ID, source requirement, category, measurable target, evidence, risk.
- **ADR:** ID, title, status, context, options, decision, consequences, driver/constraint links.
- **Module:** ID, responsibility, ownership, exclusions, interfaces, dependencies, size verdict.
- **Interface:** operation, types/schema, errors, side effects, reliability/versioning rules, owners.
- **Validation finding:** module/contract, evidence, severity, verdict, remediation, owner.

## Quick Reference

| Task | Artifact |
|---|---|
| Drivers | Driver analysis table |
| Decisions | ADR set |
| Boundaries | Module and ownership map |
| Coordination | Interface contract |
| Consistency | Cross-cutting concerns spec |
| Communication | Text diagrams |
| Readiness | Decomposability report |

## Pitfalls

- Choosing a framework before identifying architectural drivers.
- Treating diagrams as decoration rather than traceable coordination artifacts.
- Leaving interface behavior, errors, retries, or ownership implicit.
- Keeping modules too large for independent task execution.
- Adding layers or services without a current requirement or quality driver.
- Updating an ADR or module list without updating contracts, diagrams, and validation evidence.

## Verification

- [ ] Every SRS driver and constraint appears in the driver analysis.
- [ ] Quality attributes have measurable targets and trace links.
- [ ] Every consequential decision has an ADR with alternatives and consequences.
- [ ] Module responsibilities and data ownership do not conflict.
- [ ] Every inter-module dependency has a complete interface contract.
- [ ] Cross-cutting concerns are addressed or explicitly marked N/A.
- [ ] Required diagrams are text-based, renderable, and consistent.
- [ ] Every module has a decomposability verdict and remediation path if needed.
