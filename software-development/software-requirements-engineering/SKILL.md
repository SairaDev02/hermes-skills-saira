---
name: software-requirements-engineering
description: Guide the full software requirements engineering lifecycle.
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [requirements, engineering, specification, elicitation, srs, traceability]
    related_skills: [plan, test-driven-development]
---

# Software Requirements Engineering Skill

Guide the complete requirements engineering (RE) lifecycle: feasibility study, elicitation, specification, verification & validation, and management. Produces structured artifacts (SRS, RTM, requirements tables) grounded in IEEE/ISO/IEC 29148, INCOSE, and IREB quality characteristics. Does not implement code or design architecture — it produces the requirements that *drive* those activities.

## When to Use

- User asks to write, review, or validate software requirements or an SRS
- User wants to elicit, analyze, or specify requirements for a new system or feature
- User needs a feasibility study, requirements traceability matrix, or prioritization
- User wants to evaluate requirements quality (ambiguity, testability, completeness)
- Don't use for: architecture design, implementation planning (use `plan` skill), or test case generation (use `test-driven-development` skill)

## Prerequisites

- No external tools or API keys required — this skill is a structured methodology using Hermes tools
- For diagram generation: the user may provide tools like PlantUML, Mermaid, or draw.io, but the skill produces text-based models (ER descriptions, DFD descriptions, data dictionaries) by default

## Procedure

The RE process is iterative — later stages may loop back to earlier ones. Follow all five phases in order for a new project; enter at the relevant phase for incremental work.

### Phase 1: Feasibility Study

Determine whether the project is worth pursuing across five dimensions.

1. **Technical feasibility** — assess whether current hardware, software, and team skills can deliver the system. Completion criterion: a yes/no verdict per dimension with rationale.
2. **Operational feasibility** — assess usability, acceptance by users, and ease of maintenance post-deployment.
3. **Economic feasibility** (most important) — compare projected cost vs. benefit. Include development, operational, and maintenance costs.
4. **Legal feasibility** (least emphasized but required) — verify compliance with laws, regulations, standards, and intellectual property constraints.
5. **Schedule feasibility** — evaluate whether the timeline is realistic given resources and scope.

Output: a feasibility report with a go/no-go recommendation. Use `write_file` to save it alongside other project artifacts.

See `references/feasibility-framework.md` for the full checklist.

### Phase 2: Requirements Elicitation

Gather stakeholder needs, expectations, and domain knowledge. Elicitation does **not** produce formal models — it produces raw, understood requirements.

1. **Identify stakeholders** — list every person/group affected by or influencing the system. Completion criterion: every stakeholder has a name/role and a contact path.
2. **Select techniques** — choose from: interviews, surveys, focus groups, observation, prototyping, brainstorming, Delphi technique, task analysis, document analysis.
3. **Execute elicitation** — conduct the selected techniques. Record every need, constraint, expectation, and assumption.
4. **Document and organize** — group raw requirements by category (functional, non-functional, constraint, domain rule). Flag conflicts and gaps.

See `references/elicitation-techniques.md` for technique selection guidance.

### Phase 3: Requirements Specification

Transform elicited needs into formal, documented requirements. This phase **may trigger re-elicitation** if gaps emerge.

1. **Classify each requirement** as one of:
   - **Functional** — what the system must do (behaviors, inputs/outputs, data processing)
   - **Non-functional** — how well the system must do it (performance, security, usability, reliability, maintainability — see ISO/IEC 25010 quality model)
   - **Constraint** — limitations on the solution space (technology, budget, schedule, regulatory)
   - **Acceptance criterion** — conditions that must be met for the system to be considered complete
2. **Write each requirement** using EARS syntax where applicable (see `references/ears-syntax.md`). Each requirement must be atomic (one requirement per statement), use active voice, and use "shall" for binding obligations.
3. **Assign attributes** — every requirement gets: unique ID, source, priority (MoSCoW), status, version, rationale.
4. **Produce models** as needed: ER diagrams (data entities), DFDs (data flow), FDDs (function decomposition), data dictionaries.
5. **Assemble the SRS** — compile all requirements, models, and supporting information into a Software Requirements Specification document.

Use `templates/srs-template.md` for the document structure and `templates/requirements-table.md` for individual requirement entries.

### Phase 4: Requirements Verification & Validation

V&V is **iterative** and continues throughout the lifecycle — not a one-time gate.

1. **Verification** (are we building the *thing right*?) — review each requirement and the full set against quality characteristics:
   - Consistent: no two requirements conflict; same term used for same concept throughout
   - Complete: no TBDs; set covers all stakeholder needs without further amplification
   - Unambiguous: each requirement has exactly one interpretation
   - Verifiable: each requirement can be proven (test, demonstration, inspection, analysis)
   - Feasible: each requirement is achievable within constraints
   - Singular/atomic: each requirement contains exactly one obligation
   - Traceable: each requirement links to its source and to downstream artifacts
   - Necessary: removing it creates a deficiency
   - Implementation-free: describes *what*, not *how*
2. **Validation** (are we building the *right thing*?) — confirm with stakeholders that requirements match their actual needs. Techniques: reviews, walkthroughs, prototyping, simulation.
3. **Record V&V results** — document every issue found, its resolution, and the disposition (accepted, revised, deferred).

See `references/requirement-quality-attributes.md` for the full quality attribute checklist.

### Phase 5: Requirements Management

Manage changing requirements throughout the lifecycle.

1. **Change tracking** — for every change request: identify source, assess impact (affected requirements, design, tests, schedule, cost), approve or reject, and record the decision.
2. **Version control** — maintain versioned requirement documents with change history.
3. **Traceability** — maintain a Requirements Traceability Matrix (RTM) linking each requirement to: its source (stakeholder need), its parent/child requirements, design elements, test cases, and verification results.
4. **Prioritization** — apply MoSCoW (Must have, Should have, Could have, Won't have this time) or another prioritization scheme. Must-haves should not exceed 60% of total effort.
5. **Communication** — ensure all stakeholders are informed of requirement changes, status, and decisions.

Use `templates/rtm-template.md` for the traceability matrix.

## Quick Reference

| Phase | Key Output | Template |
|------|-----------|----------|
| Feasibility | Go/no-go report | `references/feasibility-framework.md` |
| Elicitation | Raw requirements list | `references/elicitation-techniques.md` |
| Specification | SRS document | `templates/srs-template.md` |
| V&V | Quality review results | `references/requirement-quality-attributes.md` |
| Management | RTM + change log | `templates/rtm-template.md` |

### Requirement writing quick rules

- One requirement per statement (atomic — no "and"/"or" chaining)
- Use "shall" for mandatory, "should" for recommended, "may" for optional
- Active voice: "The system shall..." not "It shall be..."
- EARS patterns for complex conditions (see `references/ears-syntax.md`)
- Every requirement has a unique ID and is traceable to its source
- No implementation details — describe *what*, not *how*
- Avoid vague terms ("fast", "user-friendly", "robust") — quantify everything

## Pitfalls

1. **Everything is a Must-have.** MoSCoW collapses if >60% is Must. Force trade-offs.
2. **Confusing functional with non-functional.** Functional = what the system does; non-functional = how well it does it. If it addresses a quality attribute, it's non-functional.
3. **Passive voice hides accountability.** "The system shall be secured" — who secures it? Use active voice: "The system shall enforce authentication..."
4. **Vague quantifiers.** "The system shall respond quickly" is unverifiable. Specify: "The system shall respond within 200ms at 95th percentile."
5. **Implementation bias.** "The system shall use Redis for caching" is a constraint disguised as a requirement. Reframe as: "The system shall cache frequently accessed data with sub-millisecond retrieval latency."
6. **Skipping V&V.** Requirements that pass a quick self-review still need stakeholder validation and consistency checks across the full set.
7. **Forgetting implicit requirements.** Session management, error handling, browser compatibility, data persistence — these are real requirements even if no stakeholder mentioned them.
8. **EARS overuse.** Not every requirement needs EARS. If a requirement has more than three preconditions, use a different format (table, diagram, or structured prose).

## Verification

- [ ] Every requirement has a unique ID, source, and priority
- [ ] Every functional requirement maps to at least one acceptance criterion
- [ ] Every requirement passes the quality attribute checklist (see `references/requirement-quality-attributes.md`)
- [ ] The RTM has no orphan requirements (every requirement links to a source and a test)
- [ ] No two requirements conflict (consistency check across the full set)
- [ ] No TBDs or placeholders remain in the SRS
- [ ] Stakeholders have validated the requirements (not just the author)
