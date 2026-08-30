---
name: rapid-application-development
description: "Plan and govern iterative RAD delivery with user feedback."
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [rad, prototyping, iterative-development, user-feedback, timeboxing, cutover]
    related_skills: [software-requirements-engineering, software-architecture-design, llm-task-engineering, qa-engineer, devops-release-engineer]
---

# Rapid Application Development Skill

Guide projects that use Rapid Application Development (RAD): lightweight planning, collaborative prototyping, short construction cycles, continuous user feedback, and controlled cutover. This role produces specification and planning documents only; it does not replace requirements engineering, architecture, QA, task engineering, or release engineering, and it does not write executable code, tests, configuration, or scripts.

RAD optimizes for rapid learning and delivery where representative users can participate throughout the project. Use its guardrails to prevent speed from eroding architecture, security, quality, documentation, or operational readiness.

## When to Use

- User asks to plan or govern a project using the RAD model
- A project needs rapid prototypes, frequent user validation, and incremental delivery
- Stakeholders need a RAD feasibility decision, iteration plan, prototype feedback log, or cutover plan
- A team needs to coordinate parallel feature construction without losing a shared product vision
- User feedback is changing requirements and decisions must remain traceable
- Don't use for: detailed SRS authoring (use `software-requirements-engineering`), architecture design (use `software-architecture-design`), dispatchable implementation tasks (use `llm-task-engineering`), test design (use `qa-engineer`), or deployment automation (use `devops-release-engineer`)

## Prerequisites

- A problem statement, business goal, or initial product concept
- Access to representative users or subject-matter experts who can review prototypes throughout the project
- A named decision owner and a cross-functional team with design, engineering, and QA capability
- Known constraints that can affect feasibility: target date, budget, integrations, data, security, privacy, regulatory obligations, and operational environment
- No external tools or API keys are required; use Hermes tools such as `read_file`, `write_file`, `search_files`, and `patch` to produce the artifacts

## Procedure

The RAD process is iterative. Complete Tasks 1–3 before construction; repeat Tasks 4–6 for each feature slice or iteration; complete Tasks 7–8 for cutover and ongoing learning. Revisit earlier tasks when feedback changes the problem, scope, architecture, or acceptance criteria.

### Task 1: Assess RAD Fit and Establish the Charter

Decide whether RAD is appropriate before committing the team to rapid cycles. RAD is a poor default for systems that cannot be modularized, lack available users, require extensive up-front assurance, or have failure consequences that demand a more controlled lifecycle.

1. **Assess suitability** — evaluate time pressure, requirement volatility, UI or workflow uncertainty, modularity, technical familiarity, team experience, user availability, and assurance needs. Completion criterion: each dimension has a fit rating, evidence, and an identified risk.
2. **Define the problem and outcome** — state the user problem, business outcome, target users, success measures, and explicit non-goals. Completion criterion: the charter has one problem statement, measurable outcomes, named users, and a bounded non-goal list.
3. **Set constraints and decision rights** — record budget, target date, integrations, data and compliance constraints, decision owner, escalation path, and stakeholder response expectations. Completion criterion: every constraint has an owner and every major decision has a named approver.
4. **Record the RAD decision** — issue a go, conditional-go, or no-go decision with rationale, assumptions, and review date. Completion criterion: the decision and its conditions are recorded in a dated RAD charter.

Output: RAD charter and feasibility decision.

### Task 2: Create Lightweight Requirements and the Iteration Backlog

RAD does not mean no planning. It means planning enough to start learning while leaving detail to validated feedback. Keep the initial plan lightweight, explicit, and changeable.

1. **Identify stakeholders and representative users** — document user groups, subject-matter experts, business owners, technical owners, and operational stakeholders. Completion criterion: every critical user group has a named representative and a feedback path.
2. **Define the initial product slice** — capture user stories or use cases, primary workflows, assumptions, constraints, and the smallest useful release. Completion criterion: each initial story has a user, outcome, priority, and acceptance intent.
3. **Prioritize the backlog** — rank features by user value, learning value, risk reduction, dependency, and effort. Separate Must, Should, Could, and deferred items. Completion criterion: every backlog item has a priority, rationale, dependency status, and disposition.
4. **Set iteration boundaries** — choose iteration length, prototype and review dates, target release date, work-in-progress limits, and entry/exit criteria. Completion criterion: the backlog contains an ordered sequence of timeboxed slices with capacity and exit criteria.
5. **Route formal requirements** — send binding functional, quality, regulatory, and acceptance requirements to `software-requirements-engineering` when the project needs an SRS or RTM. Completion criterion: every requirement that must survive beyond the iteration is either captured in a formal upstream artifact or explicitly marked as an assumption.

Output: Lightweight product backlog, iteration roadmap, and assumptions register.

### Task 3: Establish the Collaborative Feedback System

RAD depends on rapid decisions, not merely rapid coding. Define how users participate, how evidence is recorded, and how conflicting feedback is resolved.

1. **Assign team responsibilities** — identify the facilitator, product or business decision owner, representative users, designer, engineers, QA, architect, and operations owner. Completion criterion: every responsibility has one accountable owner and a backup where needed.
2. **Define the feedback cadence** — schedule prototype reviews, usability sessions, iteration demonstrations, defect triage, decision checkpoints, and escalation windows. Completion criterion: the cadence specifies participants, frequency, input artifact, and expected decision.
3. **Define the feedback record** — capture observation, user or stakeholder, scenario, evidence, requested change, severity or value, decision, rationale, owner, and due iteration. Completion criterion: every feedback item can be traced from observation to disposition.
4. **Set decision and change rules** — define who may accept, reject, defer, or trade off a request; require impact assessment for scope, schedule, architecture, security, data, and quality. Completion criterion: the change protocol has an approver, impact fields, and a disposition for every request.
5. **Protect representative participation** — identify unavailable or conflicting stakeholders and provide an explicit substitute or escalation route. Completion criterion: no critical workflow depends on feedback from an unavailable person without a documented mitigation.

Output: Team and stakeholder register, feedback protocol, and decision log format.

### Task 4: Run User Design and Prototype Cycles

Build a prototype that exposes assumptions early. The prototype may be disposable, evolutionary, or a thin vertical slice, but its status and quality level must be explicit.

1. **Select prototype scope and fidelity** — choose the smallest workflow that tests the highest-risk assumption. Label the prototype as exploratory, validation-only, or intended to evolve into production. Completion criterion: the prototype brief names the assumption, users, scenario, fidelity, and success signal.
2. **Produce the prototype specification** — describe screens, workflow states, data needed, integrations represented, known omissions, and observable acceptance signals. Completion criterion: a user can perform the target scenario from the specification without relying on undocumented behavior.
3. **Conduct structured user sessions** — give representative users realistic scenarios and collect observed behavior, comprehension, usability issues, unmet needs, and new constraints. Completion criterion: each session has participants, scenarios, evidence, and a recorded outcome.
4. **Decide what changes** — convert evidence into accepted, rejected, deferred, or clarification-needed backlog changes. Completion criterion: every finding has a disposition, rationale, owner, and target iteration.
5. **Validate downstream impacts** — send changes that affect requirements, architecture, interfaces, quality attributes, or tests to the responsible role. Completion criterion: every accepted change has updated or explicitly revalidated downstream artifacts.

Output: Prototype specification, usability or stakeholder feedback report, and updated backlog.

### Task 5: Coordinate Rapid Construction Iterations

Turn validated prototypes into small, integrated feature slices while preserving explicit boundaries and shared quality rules. Parallel work is allowed only when interfaces and ownership are clear.

1. **Define the iteration goal** — select a coherent user outcome and list the stories, prototype decisions, dependencies, and acceptance criteria included in the slice. Completion criterion: the iteration has one outcome and no unowned work.
2. **Prepare dispatchable work** — ask `llm-task-engineering` to produce bounded task specifications from the approved requirements, architecture, interfaces, and iteration goal. Completion criterion: every implementation slice has scope boundaries, output contract, acceptance criteria, constraints, and dependencies.
3. **Coordinate integration checkpoints** — specify shared interface checks, branch or merge points, demo readiness, and unresolved dependency handling. Completion criterion: every parallel task has an integration owner and a check before user review.
4. **Track scope and quality during construction** — record completed behavior, deferred work, defects, decisions, and changes to assumptions. Completion criterion: the iteration record reconciles every backlog item as accepted, in progress, deferred, blocked, or removed.
5. **Keep the product and architecture coherent** — route structural changes to `software-architecture-design`; do not accept a prototype shortcut as production design without an explicit decision. Completion criterion: all accepted architectural deviations have a documented decision and owner.

Output: Iteration plan, dispatchable task inputs, integration checkpoint record, and iteration status report.

### Task 6: Perform Continuous Verification and Feedback

Testing and feedback are part of every iteration, not a final gate. Verify that the increment works, is usable, and still solves the intended problem.

1. **Derive verification scope** — ask `qa-engineer` to map iteration acceptance criteria to functional, negative, usability, workflow, integration, security, performance, and recovery checks as applicable. Completion criterion: every acceptance criterion has a verification method and owner.
2. **Run a review-ready increment gate** — require the defined checks, user demonstration, defect triage, and evidence before accepting an increment. Completion criterion: the increment has a pass/fail decision for each gate with linked evidence.
3. **Compare outcomes with user needs** — evaluate observed user behavior and success measures against the charter, not only against implementation correctness. Completion criterion: every iteration records whether the increment improved the target outcome and what evidence supports the judgment.
4. **Manage defects and gaps** — classify defects, assign severity and owner, link them to requirements or assumptions, and decide fix-now, defer, or reject. Completion criterion: every finding has a disposition, rationale, and regression or follow-up condition.
5. **Update the plan** — revise backlog order, assumptions, prototype decisions, and roadmap based on evidence. Completion criterion: the next iteration starts from a versioned backlog and decision log that reflects the completed review.

Output: Iteration verification report, user feedback report, defect disposition log, and revised backlog.

### Task 7: Prepare and Govern Cutover

Cutover moves a validated increment or release into live use. Continuous feedback reduces risk but does not replace release readiness, acceptance, migration, training, observability, or rollback planning.

1. **Define cutover scope and readiness criteria** — identify included features, excluded features, open defects, acceptance status, data and security checks, operational SLOs, and approval owners. Completion criterion: every release item has a readiness status and every open risk has an owner and treatment.
2. **Specify deployment and migration** — ask `devops-release-engineer` to produce deployment, environment, monitoring, and rollback specifications. Completion criterion: the cutover plan names environments, sequence, health checks, migration approach, rollback trigger, and verification step.
3. **Plan user acceptance and adoption** — specify final representative-user scenarios, training, support materials, communication, accessibility checks, and support escalation. Completion criterion: UAT, training, and support responsibilities are assigned with completion evidence.
4. **Run the go/no-go review** — review acceptance evidence, unresolved defects, security and compliance obligations, data integrity, support readiness, and rollback readiness. Completion criterion: the decision owner records go, conditional-go, or no-go with explicit conditions.
5. **Record cutover outcomes** — document actual deployment timing, incidents, deviations, user feedback, and follow-up work. Completion criterion: the cutover report reconciles the plan with observed results and opens owners for every follow-up.

Output: Cutover readiness checklist, go/no-go record, and cutover report.

### Task 8: Capture Post-Cutover Learning and Sustain the Product

RAD ends an iteration or release with learning, not with an assumption that the product is finished.

1. **Collect post-release evidence** — gather user feedback, adoption, task success, support requests, defects, performance, reliability, and other charter measures. Completion criterion: every success measure has an observed value, time window, and data source or is marked unavailable.
2. **Run a retrospective** — identify what accelerated learning, what caused rework, which assumptions were wrong, and which coordination rules need revision. Completion criterion: each retrospective finding has an owner and an action or explicit rejection.
3. **Reprioritize the improvement backlog** — convert validated learning into new features, fixes, experiments, documentation, or retirement decisions. Completion criterion: each item has evidence, priority, owner, and target decision point.
4. **Handoff maintainability artifacts** — ensure architecture decisions, interfaces, requirements, tests, operational procedures, known limitations, and support ownership are retained. Completion criterion: the handoff inventory has no missing artifact category for the deployed scope.
5. **Decide whether to continue RAD** — reassess user availability, product uncertainty, scale, risk, and maintenance needs. Completion criterion: the next lifecycle mode is recorded as continue RAD, transition to a more structured cadence, or retire the product, with rationale.

Output: Post-cutover review, retrospective, improvement backlog, and maintenance handoff record.

## Feedback Paths

- **To Requirements Engineer:** Prototype evidence that changes a binding requirement, exposes ambiguity, or creates an untestable acceptance condition becomes a structured change request with evidence and affected IDs.
- **To Architect:** Prototype or construction findings that cross module boundaries, change quality attributes, or create integration risk become an architecture feedback record with the affected decision and proposed review point.
- **To Task Engineer:** An iteration slice that is too large, lacks a clear output contract, or fails integration becomes a re-dispatch request containing the slice boundary, missing context, and revised acceptance criteria.
- **To QA Engineer:** Every accepted feature change and feedback-derived workflow change becomes a test-impact record; uncovered behavior becomes a coverage-gap input.
- **To DevOps / Release Engineer:** A cutover-ready increment becomes a release input containing scope, verification evidence, environment needs, migration risks, monitoring criteria, and rollback conditions.
- **From downstream roles:** Requirements, architecture, task, QA, review, or release findings must update the RAD decision log and backlog rather than remaining as informal conversation.

## Quick Reference

| Task | Key Output | Downstream Role or Reference |
|------|-----------|------------------------------|
| 1. Assess RAD fit and charter | RAD charter and feasibility decision | `software-requirements-engineering` |
| 2. Lightweight requirements and backlog | Backlog, roadmap, assumptions register | `software-requirements-engineering` |
| 3. Feedback system | Stakeholder register, feedback protocol, decision log | — |
| 4. User design and prototypes | Prototype specification and feedback report | `software-architecture-design` |
| 5. Rapid construction | Iteration plan and dispatch inputs | `llm-task-engineering` |
| 6. Continuous verification | Verification and defect disposition reports | `qa-engineer` |
| 7. Cutover | Readiness checklist, go/no-go record, cutover report | `devops-release-engineer` |
| 8. Post-cutover learning | Retrospective, improvement backlog, handoff record | All affected roles |

## RAD Guardrails

- Keep initial planning lightweight, but never omit constraints, acceptance intent, risk ownership, or decision records.
- Treat prototypes as evidence. Mark whether each prototype is disposable, validation-only, or intended to evolve into production.
- Use representative users, realistic scenarios, and observed behavior; sponsor approval alone is not user validation.
- Timebox iterations and process new requests through impact analysis; continuous feedback does not mean unlimited scope.
- Preserve architecture, security, privacy, data integrity, accessibility, testing, observability, and operational readiness as explicit gates.
- Prefer familiar, modular technologies and reusable components only when they meet the project's quality and maintainability needs.
- Do not infer production readiness from prototype success. Require separate implementation, verification, and cutover evidence.
- For safety-critical, highly regulated, very large, or tightly coupled systems, record why RAD controls are sufficient or select a more appropriate lifecycle.

## Verification

- [ ] RAD fit has been assessed across user availability, modularity, uncertainty, time, team capability, technology, and assurance needs
- [ ] The charter defines the problem, target users, measurable outcomes, constraints, non-goals, decision owner, and RAD decision
- [ ] The initial backlog has priorities, acceptance intent, dependencies, assumptions, and timeboxed iteration boundaries
- [ ] Stakeholder participation, feedback cadence, decision rights, and feedback records are explicit
- [ ] Every prototype has a scope, fidelity, intended quality level, target scenario, and success signal
- [ ] Every feedback item has evidence, disposition, rationale, owner, and target iteration
- [ ] Each construction slice has bounded dispatch inputs, integration ownership, and a recorded status
- [ ] Every accepted change has an impact review across requirements, architecture, tests, schedule, and operations as applicable
- [ ] Every iteration has verification evidence, user-outcome evidence, defect dispositions, and a revised backlog
- [ ] Cutover readiness covers acceptance, security, data, migration, training, monitoring, support, and rollback
- [ ] Post-cutover measures, retrospective actions, maintenance handoff, and next-lifecycle decision are recorded
- [ ] Feedback paths to Requirements, Architect, Task Engineer, QA, and DevOps roles are structured artifacts

## Sources

- GeeksforGeeks, “Rapid Application Development Model (RAD) - Software Engineering,” https://www.geeksforgeeks.org/software-engineering/software-engineering-rapid-application-development-model-rad/
- IBM, “What is rapid application development?”, https://www.ibm.com/think/topics/rapid-application-development
- EBSCO Research Starters, “Rapid application development (RAD),” https://www.ebsco.com/research-starters/computer-science/rapid-application-development-rad
- James Martin, *Rapid Application Development* (1991), publication record: https://openlibrary.org/books/OL1854364M/Rapid_application_development
