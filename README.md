# Hermes Skills — Software Development Roles

A collection of Hermes Agent skills for the software-development lifecycle. Every specialist role below is documentation-only: it produces planning, specification, review, or evidence artifacts and does not write or execute application code, tests, CI/CD, deployment, or operational scripts. The RAD Engineer is the sole lifecycle exception to this catalog rule; its own skill defines its separate operating boundary.

## Documentation-Only Principle

The Requirements, Architecture, Task Engineering, QA, Code Review, and DevOps/Release skills produce documents only: SRS/RTM, architecture and ADRs, interface contracts, task manifests, test specifications, review reports, and delivery/operations specifications. They may include pseudocode and Mermaid/PlantUML, but they do not create executable artifacts or claim execution without evidence.

## Skills

| # | Skill | Role | Stage | Deliverable boundary |
|---|---|---|---|---|
| 1 | [software-requirements-engineering](software-development/software-requirements-engineering/SKILL.md) | Requirements Engineer | Start | SRS, RTM, feasibility, V&V, and change documents only |
| 2 | [software-architecture-design](software-development/software-architecture-design/SKILL.md) | Architect | Design | Architecture, ADR, interface, diagram, and decomposability documents only |
| 3 | [llm-task-engineering](software-development/llm-task-engineering/SKILL.md) | Task Engineer | Dispatch | Self-contained task manifest and dependency/context specifications only |
| 4 | [qa-engineer](software-development/qa-engineer/SKILL.md) | Tester / QA Engineer | Verification | Test, fixture, execution, exploratory, defect, coverage, and regression documents only |
| 5 | [code-reviewer](software-development/code-reviewer/SKILL.md) | Code Reviewer | Gate | Review evidence, findings, comments, and verdict documents only |
| 6 | [devops-release-engineer](software-development/devops-release-engineer/SKILL.md) | DevOps / Release Engineer | Release | CI/CD, environment, release, monitoring, and rollback specifications only |
| 7 | [rapid-application-development](software-development/rapid-application-development/SKILL.md) | RAD Engineer | Cross-cutting | Separate RAD lifecycle role; its own skill defines its operating boundary |

## Lifecycle Flow

```
Requirements → Architecture → Task Engineering → [implementation harness]
                                      ↓
                              QA + Code Review
                                      ↓
                              DevOps / Release

RAD Engineer ── coordinates evidence and decisions across the lifecycle when selected
```

Each arrow carries a versioned package and uses the shared [handoff template](templates/HANDOFF.md). Findings use the [feedback record](templates/feedback-record.yaml). See [Roles.md](Roles.md) for the role index and routing rules.

## Structure

```
software-development/<role>/
  SKILL.md
  references/
  templates/
templates/
  HANDOFF.md
  feedback-record.yaml
docs/
  PROJECT-CONSTITUTION.md
  REFERENCE-INDEX.md
  GLOSSARY.md
  ASSUMPTIONS.md
  COLLABORATION-PROTOCOL.md
  CHANGE-IMPACT-MAP.md
README.md
Roles.md
```

## License

MIT
