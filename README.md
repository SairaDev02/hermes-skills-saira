# Hermes Skills — Software Development Roles

A collection of Hermes Agent skills for the full software development lifecycle. Each role produces specification and planning documents only — Hermes does not write executable code. All implementation and execution is delegated to the coding harness (Pi).

## Documentation-Only Principle

Hermes produces specification and planning documents only — SRS, RTM, architecture docs, ADRs, interface contracts, task manifests, test specs, test execution plans, CI/CD specs, deployment specs, monitoring specs, rollback procedure specs, bug reports, review verdicts, and release process docs. Hermes does not write executable code, test code, CI/CD config files, deployment manifests, or scripts. Pseudocode and diagramming languages (Mermaid, PlantUML) are permitted within specification documents.

## Skills

| # | Skill | Role | Lifecycle Stage | Description |
|---|-------|------|-----------------|-------------|
| 1 | [software-requirements-engineering](software-development/software-requirements-engineering/SKILL.md) | Requirements Engineer | Start | Full requirements lifecycle: feasibility study, stakeholder identification, elicitation, EARS-syntax specification, V&V, RTM construction, change management |
| 2 | [software-architecture-design](software-development/software-architecture-design/SKILL.md) | Architect | Design | Architectural driver analysis, pattern selection, module decomposition, interface contracts, technology selection, cross-cutting concerns, text-based diagrams |
| 3 | [llm-task-engineering](software-development/llm-task-engineering/SKILL.md) | Task Engineer | Dispatch | Decompose architecture into dispatchable LLM task specs with curated context, output contracts, acceptance criteria, dependency DAG, and single-context-window sizing |
| 4 | [qa-engineer](software-development/qa-engineer/SKILL.md) | Tester / QA Engineer | Verification | Spec-driven test planning, test case derivation (ISTQB), test implementation specification (pseudocode), execution plans, exploratory testing plans, bug reporting, coverage gap analysis |
| 5 | [code-reviewer](software-development/code-reviewer/SKILL.md) | Code Reviewer | Gate | Requirements compliance, architecture compliance, security scan (OWASP), style checks, complexity assessment (McCabe, Sonar), edge case gap identification, verdict (approve/request changes/reject) |
| 6 | [devops-release-engineer](software-development/devops-release-engineer/SKILL.md) | DevOps / Release Engineer | Release | CI/CD pipeline specifications, deployment specifications, environment specifications, release process docs, monitoring specifications, rollback procedure specifications |
| 7 | [rapid-application-development](software-development/rapid-application-development/SKILL.md) | Rapid Application Development Facilitator | Method / Iteration | RAD fit decisions, lightweight backlogs, prototype cycles, user feedback, iteration coordination, continuous verification, and cutover readiness |

## Lifecycle Flow

```
Requirements Engineer → Architect → Task Engineer → [Pi: LLM implementation]
                                                      ↓
                                            Tester + Code Reviewer
                                                      ↓
                                              DevOps → Release
```

Each arrow produces a structured artifact the receiving role can act on without additional conversation. See [Roles.md](Roles.md) for full task definitions, feedback paths, and cross-role coordination.

## Structure

```
software-development/
  software-requirements-engineering/
    SKILL.md
    references/
    templates/
  software-architecture-design/
    SKILL.md
    references/
    templates/
  llm-task-engineering/
    SKILL.md
    references/
    templates/
  qa-engineer/
    SKILL.md
    references/
    templates/
  code-reviewer/
    SKILL.md
    references/
    templates/
  devops-release-engineer/
    SKILL.md
    references/
    templates/
  rapid-application-development/
    SKILL.md
    references/
Roles.md
```

## License

MIT
