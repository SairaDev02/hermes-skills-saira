# RAD Methodology Reference

This reference summarizes the source basis for the `rapid-application-development` skill. It is a methodology aid, not a substitute for project-specific requirements, architecture, testing, security, compliance, or release decisions.

## Core model

Rapid Application Development (RAD) emphasizes speed, iterative prototyping, short development cycles, and continuous user feedback instead of exhaustive upfront planning. The skill uses the commonly described four-phase model:

1. **Requirements planning** — define the problem, users, important features, constraints, and initial scope without attempting to freeze every detail.
2. **User design** — build and review mockups, prototypes, workflows, and models with representative users; incorporate evidence into the evolving design.
3. **Construction** — implement and integrate small, prioritized slices through iterative development, testing, and feedback.
4. **Cutover** — complete acceptance, migration, training, deployment, monitoring, and support readiness before live use.

Testing and feedback are treated as continuous activities across the phases. RAD is most defensible when the project is modular, the team is experienced, the technology is familiar, and representative users can participate regularly. The method becomes risky when stakeholder access is weak, scope is uncontrolled, architecture is neglected, documentation is discarded, or system scale and assurance needs exceed the team's lightweight controls.

## Source notes

- **GeeksforGeeks** describes RAD as iterative and incremental, identifies requirements planning, user design, construction, and cutover, and highlights active user involvement, prototyping, short cycles, modularity, and the need for skilled coordination. [Source](https://www.geeksforgeeks.org/software-engineering/software-engineering-rapid-application-development-model-rad/)
- **IBM** describes RAD as short iterations that produce working application parts for user feedback. It emphasizes lightweight planning, user-interface-driven validation, parallel construction, continuous functional/usability/workflow/performance testing, and cutover activities such as migration and training. It also identifies risks including scope creep, weak documentation, loss of architectural focus, and poor fit for critical or large-scale systems. [Source](https://www.ibm.com/think/topics/rapid-application-development)
- **EBSCO Research Starters** attributes the formalization of the named method to James Martin's 1991 book and emphasizes iterative development, prototyping, current development tools, and small collaborative teams. [Source](https://www.ebsco.com/research-starters/computer-science/rapid-application-development-rad)
- **James Martin**, *Rapid Application Development* (1991), is the primary bibliographic reference for the named method. [Publication record](https://openlibrary.org/books/OL1854364M/Rapid_application_development)

## Application to Hermes role artifacts

The role translates the model into documents that downstream roles can act on without additional conversation:

- RAD charter and feasibility decision
- Lightweight backlog, roadmap, and assumptions register
- Stakeholder, feedback, and decision records
- Prototype and usability feedback reports
- Iteration plans and bounded dispatch inputs
- Verification, defect disposition, and coverage-impact records
- Cutover readiness, go/no-go, and cutover reports
- Retrospective, improvement backlog, and maintenance handoff

The role remains documentation-only. The coding harness implements approved task specifications, and the QA and DevOps roles implement or execute their respective specifications.
