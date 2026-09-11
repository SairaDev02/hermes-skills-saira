---
name: software-requirements-engineering
description: Guide requirements from discovery through traceability.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [requirements, engineering, specification, elicitation, srs, traceability]
    related_skills: [software-architecture-design, qa-engineer]
---

# Software Requirements Engineering Skill

Produce implementation-neutral requirements artifacts from discovery through change control. This documentation-only role records feasibility, stakeholder needs, measurable requirements, validation evidence, and traceability; it does not design architecture, create implementation tasks, or write code.

## When to Use

- Create or revise an SRS, requirements table, RTM, feasibility report, or change record.
- Elicit, classify, prioritize, validate, or quality-review requirements.
- Analyze the impact of a proposed requirement change.
- Don't use for: architecture, task manifests, test specifications, code, or executable configuration.

## Prerequisites

- Problem statement, business goals, constraints, and available stakeholder evidence.
- Existing requirements and change history for incremental work.
- Shared project context: `docs/PROJECT-CONSTITUTION.md`, `docs/REFERENCE-INDEX.md`, `docs/GLOSSARY.md`, `docs/ASSUMPTIONS.md`, and `docs/CHANGE-IMPACT-MAP.md`.
- Use `read_file`, `search_files`, `write_file`, and `patch` for project artifacts.

## Procedure

Use all phases for a new initiative; enter at the affected phase for an incremental change. Record evidence and disposition at each phase.

### 1. Feasibility

Assess technical, operational, economic, legal, and schedule feasibility. Record assumptions, evidence, risks, mitigations, and a go, conditional-go, or no-go recommendation. **Done when:** each dimension has a verdict and rationale, and every material risk has an owner or explicit acceptance.

### 2. Stakeholders and elicitation

Identify affected users, owners, operators, regulators, and system dependencies. Select suitable techniques—interviews, observation, document analysis, workshops, surveys, prototyping, or task analysis—and record raw needs, conflicts, assumptions, and gaps. **Done when:** every critical stakeholder has a role, evidence source, and feedback path; unresolved gaps are logged.

### 3. Specification

Classify each need as functional, quality/non-functional, constraint, domain rule, or acceptance criterion. Write atomic, active-voice requirements using EARS where useful. Assign a stable ID, source, priority, status, version, rationale, and verification method. Quantify quality targets; avoid implementation choices unless they are explicit constraints. Assemble the SRS with `templates/srs-template.md` and entries from `templates/requirements-table.md`. **Done when:** every entry is atomic, testable, uniquely identified, sourced, prioritized, and included in the SRS.

### 4. Verification and validation

Verify the set for consistency, completeness, unambiguity, feasibility, atomicity, necessity, verifiability, traceability, and implementation independence. Validate with stakeholders using review, walkthrough, prototype, or simulation evidence. Record each issue, disposition, approver, and follow-up. **Done when:** no unresolved blocker remains hidden as a TBD, and stakeholder validation evidence is attached or its absence is explicitly recorded.

### 5. Traceability and management

Build the RTM with `templates/rtm-template.md`, linking each requirement to its source, parent/child items, architecture element, task, test, and verification evidence. For every change request, record impact on scope, architecture, interfaces, quality, tests, schedule, cost, and release; then record approval, rejection, or deferral. **Done when:** no requirement or downstream artifact is orphaned, and the change log identifies all affected owners.

## Handoff

Use the shared root `templates/HANDOFF.md` for the requirements baseline handoff. Include the feasibility decision, baseline version, unresolved assumptions, changed requirement IDs, verification methods, and stakeholder validation status.

## Required artifact shapes

- **Requirement:** ID, statement, type, source, priority, rationale, status, version, acceptance/verification method, trace links.
- **Change record:** ID, requested change, reason, affected IDs, impact, options, decision, approver, effective version.
- **V&V issue:** ID, criterion, evidence, finding, severity, disposition, owner, due date.
- **RTM row:** requirement ID, source, parent/child, architecture/task/test links, verification status.

## Quick Reference

| Need | Artifact |
|---|---|
| Feasibility | Go/no-go report |
| Discovery | Stakeholder register and raw requirements |
| Specification | SRS and requirements table |
| Quality review | V&V issue log |
| Traceability | RTM and change log |

### Writing rules

- One obligation per requirement; avoid chained “and/or”.
- Use `shall` for mandatory, `should` for recommended, and `may` for optional behavior.
- Quantify latency, capacity, availability, security, usability, and other quality targets.
- Describe what is needed, not an unapproved implementation.
- Use stable terminology and IDs across all artifacts.

## Pitfalls

- Treating every request as Must-have; force an explicit trade-off.
- Hiding ambiguity behind passive voice or vague terms such as “fast” or “user-friendly”.
- Mixing a solution choice into a need without labeling it as a constraint.
- Declaring completeness while TBDs, conflicts, or missing stakeholders remain.
- Claiming validation or stakeholder agreement without recorded evidence.
- Updating the SRS but not the RTM, change log, or downstream impact records.

## Verification

- [ ] Feasibility has evidence-backed verdicts for all five dimensions.
- [ ] Every critical stakeholder has a role and feedback path.
- [ ] Every requirement has the required fields, a source, priority, and verification method.
- [ ] Requirements are atomic, measurable where applicable, consistent, and implementation-neutral.
- [ ] Stakeholder validation evidence or an explicit evidence gap is recorded.
- [ ] RTM links requirements to downstream design, tasks, tests, and results.
- [ ] Change records include impact, decision, approver, and propagation status.
- [ ] No unresolved blocker is hidden in a placeholder.
