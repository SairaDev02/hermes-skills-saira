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

Each arrow should produce a structured artifact that the receiving role can act on without an undocumented conversation. See [Roles.md](Roles.md) for role inputs, outputs, tasks, and feedback paths.

## Structure

```
software-development/<role>/
  SKILL.md
  references/
  templates/
README.md
Roles.md
```

## License

MIT
