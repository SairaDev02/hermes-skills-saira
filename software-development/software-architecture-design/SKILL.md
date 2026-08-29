---
name: software-architecture-design
description: Design software architecture from an approved SRS.
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [architecture, design, adr, interfaces, decomposition, drivers]
    related_skills: [software-requirements-engineering, plan, test-driven-development]
---

# Software Architecture Design Skill

Guide the complete architectural design lifecycle: from analyzing architectural drivers extracted from an approved SRS, through pattern selection, module decomposition, interface contract definition, technology selection, cross-cutting concern specification, text-based diagram production, and decomposability validation. Produces structured artifacts (architecture document, ADRs, interface contracts) grounded in SEI Attribute-Driven Design (ADD), the Architecture Tradeoff Analysis Method (ATAM), Michael Nygard's ADR format, the ISO/IEC 25010 quality model, and the C4 model for text-based diagrams. Does not write requirements (use `software-requirements-engineering`) or task manifests (use `plan`) — it produces the architecture that *drives* those downstream activities.

## When to Use

- User asks to design, document, or review software architecture from an approved SRS
- User needs to select an architectural pattern, decompose a system into modules, or define interface contracts
- User wants to produce Architecture Decision Records (ADRs) for technology or pattern choices
- User needs text-based architecture diagrams (Mermaid C4, PlantUML) showing module relationships or deployment topology
- User wants to validate that a module decomposition supports single-context-window implementation (LLM-optimized decomposition)
- Don't use for: requirements elicitation or SRS writing (use `software-requirements-engineering`), task dispatch manifest creation (use `plan`), or code review (use `requesting-code-review`)

## Prerequisites

- An approved SRS, RTM, and feasibility report from the Requirements Engineer role — architecture design cannot begin without approved requirements
- No external tools or API keys required — this skill is a structured methodology using Hermes tools (`write_file`, `read_file`, `search_files`, `patch`)
- For diagram rendering: the user may provide Mermaid or PlantUML tooling, but the skill produces text-based diagram source that any Markdown viewer renders

## Procedure

The architecture process is iterative — later stages may loop back to earlier ones. Follow all eight tasks in order for a new system; enter at the relevant task for incremental work. Each task references a detailed reference or template file.

### Task 1: Analyze Architectural Drivers

Extract functional requirements, quality attributes (non-functional requirements), and constraints from the SRS. Quality attributes (performance, security, scalability, modifiability, availability) drive pattern selection more than functional requirements.

1. **Extract functional drivers** — list the system's primary functional responsibilities from the SRS. Completion criterion: every functional requirement ID in the RTM appears in the driver table.
2. **Extract quality attribute drivers** — map each non-functional requirement to an ISO/IEC 25010 quality characteristic (see `references/architectural-drivers.md`). Quantify: "fast" → "p95 latency < 200ms." Completion criterion: every non-functional requirement has a measurable quality attribute and target.
3. **Extract constraints** — list technology, budget, schedule, regulatory, and team-skill constraints. Completion criterion: every constraint from the SRS is recorded with its source.
4. **Build the driver analysis table** — compile all drivers into a single table (see `templates/driver-analysis-table.md`). Completion criterion: the table has no empty cells and every row traces to an SRS requirement ID.

Output: Driver analysis table. Use `write_file` to save it alongside other project artifacts.

### Task 2: Select Architectural Pattern

Choose the architectural style(s) appropriate for the drivers. Common patterns: layered, microservices, event-driven, hexagonal (ports & adapters), MVC, client-server, pipe-and-filter, space-based.

1. **Map drivers to pattern candidates** — for each quality attribute driver, identify which patterns address it (see `references/architectural-patterns.md`). Completion criterion: each driver has at least one candidate pattern.
2. **Evaluate tradeoffs** — for each candidate, list pros and cons against the driver set. Apply ATAM-style tradeoff analysis: identify sensitivity points (a property that affects more than one quality attribute) and tradeoffs (a property that improves one quality attribute while degrading another). Completion criterion: every candidate has documented tradeoffs.
3. **Select and justify** — choose the pattern (or combination) and record the decision as an ADR (see `references/adr-format.md` and `templates/adr-template.md`). Completion criterion: the ADR has context, decision, status, and consequences sections, and traces to specific driver IDs.

Output: Pattern selection ADR.

### Task 3: Module Decomposition

Break the system into modules with clear boundaries. **LLM-critical:** each module must be implementable within a single LLM context window. If a module is too large, decompose further. The module boundary *is* the task interface — it defines what the Task Engineer can dispatch as a unit.

1. **Identify modules** — using the selected pattern, identify the major modules. Each module has a single responsibility statement (one sentence). Completion criterion: every module has a unique name, a one-sentence responsibility statement, and no two modules share a responsibility.
2. **Define module boundaries** — for each module, list what it owns (data, behavior, state) and what it does NOT own. Completion criterion: every module boundary is explicit; no two modules claim ownership of the same data or behavior.
3. **Check single-context-window feasibility** — estimate the size of each module's implementation (data models, logic, interface surface). If a module's implementation would exceed ~60% of an LLM context window, decompose it into sub-modules. Completion criterion: every module passes the sizing check or has been decomposed.

Output: Module list with responsibility statements and boundary specs. See `references/architectural-drivers.md` for decomposition heuristics.

### Task 4: Define Interface Contracts

Specify signatures, data models, error contracts, and communication protocols between modules. This is the shared coordination artifact — parallel LLMs produce compatible code only if interfaces are explicit.

1. **Define communication patterns** — for each inter-module interaction, specify: synchronous (REST/gRPC) vs asynchronous (message queue/event bus) vs in-process (function call). Completion criterion: every inter-module dependency has a communication pattern.
2. **Specify signatures** — for each interface, define the operation name, input parameters (with types), return type, and side effects. Completion criterion: every interface operation has a typed signature.
3. **Define data models** — for each interface, define the request/response data structures (schemas, DTOs, entities). Completion criterion: every data structure referenced in a signature has a defined schema.
4. **Specify error contracts** — for each interface, define the error cases, error codes, and error response format. Completion criterion: every interface operation has documented error behavior.
5. **Document the contract** — compile into an interface specification document (see `templates/interface-contract.md`). Completion criterion: the contract is self-contained — a developer (or LLM) can implement either side of the interface from the contract alone.

Output: Interface specification document.

### Task 5: Technology Selection

Choose languages, frameworks, data stores, and libraries. Consider LLM familiarity — models produce higher-quality code in well-represented languages and frameworks.

1. **Identify technology decision points** — for each module or layer, identify which technology choices are needed (language, framework, data store, message broker, etc.). Completion criterion: every module/layer has its technology decision points listed.
2. **Evaluate candidates** — for each decision point, list 2-3 candidates with pros, cons, and fit against drivers and constraints. Completion criterion: every candidate is evaluated against the driver analysis table from Task 1.
3. **Select and record as ADRs** — choose the technology and write an ADR (see `templates/adr-template.md`). Completion criterion: every technology decision has an ADR tracing to driver IDs and constraints.

Output: Technology decision ADRs.

### Task 6: Define Cross-Cutting Concerns

Specify error handling strategy, logging, authentication, authorization, data flow, configuration, and other concerns that span all modules. If these aren't specified, each downstream LLM will invent its own — guaranteed inconsistency.

1. **Enumerate cross-cutting concerns** — error handling, logging, authentication, authorization, data validation, configuration management, observability (metrics/tracing), internationalization, data flow (request lifecycle). See `references/cross-cutting-concerns.md` for the full checklist. Completion criterion: every concern in the checklist is addressed or explicitly marked N/A with rationale.
2. **Specify each concern** — for each concern, define the strategy, the pattern to use, and the module responsible for providing the capability. Completion criterion: every concern has a strategy statement and an owning module.
3. **Document conventions** — define coding conventions that enforce the cross-cutting strategies (error response format, log message structure, auth token format). Completion criterion: conventions are concrete enough to include in task constraints.

Output: Cross-cutting concerns specification. See `references/cross-cutting-concerns.md` for the full reference.

### Task 7: Produce Architecture Diagrams

Produce text-based diagrams (Mermaid, PlantUML) showing module relationships, data flow, and deployment topology. Text-based because LLMs consume and reason about text, not images.

1. **Context diagram (C4 Level 1)** — show the system as a single box surrounded by users and external systems. Completion criterion: the diagram renders in Mermaid and shows all external actors and systems from the SRS.
2. **Container diagram (C4 Level 2)** — show the deployable/runnable pieces inside the system (services, databases, message queues). Completion criterion: every module from Task 3 appears as a container with its technology from Task 5.
3. **Component diagram (C4 Level 3)** — for complex modules, show internal components. Completion criterion: components map to sub-modules from Task 3's decomposition.
4. **Deployment diagram** — show the deployment topology (servers, regions, networks). Completion criterion: every container maps to a deployment node.
5. **Data flow diagram** — show how data moves through the system for primary use cases. Completion criterion: every primary use case has a data flow path through the architecture.

See `references/c4-diagramming.md` for Mermaid C4 syntax and patterns. Use `write_file` to save diagrams in `.md` files alongside the architecture document.

Output: Architecture diagrams (Mermaid source).

### Task 8: Validate Decomposability

Check that each module maps to one or more self-contained tasks that a single LLM can complete without needing context from other modules. If a module requires deep knowledge of another module's internals to implement, the boundary is wrong — re-decompose.

1. **Module-to-task feasibility check** — for each module, verify that a developer (or LLM) could implement it given only: the module's responsibility statement, its interface contracts, the cross-cutting concerns spec, and the relevant SRS requirements. Completion criterion: every module passes — no module requires knowledge of another module's internal implementation.
2. **Context sufficiency check** — verify that the input context for each module (interface contracts + cross-cutting spec + relevant requirements + constraints) fits within a reasonable context budget. Completion criterion: no module's input context exceeds ~40% of an LLM context window (leaving room for output).
3. **Interface completeness check** — verify that every inter-module dependency is covered by an interface contract from Task 4. Completion criterion: no module has an undocumented dependency.
4. **Produce the decomposability validation report** — document pass/fail for each module with rationale for any failures. For failures, specify which task (3 or 4) to return to. Completion criterion: the report covers every module and has a clear pass/fail verdict.

See `references/decomposability-validation.md` for the validation checklist and report template.

Output: Decomposability validation report.

## Feedback Paths

- **To Requirements Engineer:** If a requirement is architecturally unimplementable or doesn't decompose cleanly, flag it for revision. The feedback must be a structured artifact: requirement ID, the architectural constraint that blocks it, and the suggested revision direction.
- **From Task Engineer:** If the Task Engineer reports that a module boundary doesn't produce clean task specs (too much shared context needed, ambiguous interfaces), return to Task 3 (module decomposition). The feedback from Task Engineer must specify which module, what context is missing, and what interface is ambiguous.

## Quick Reference

| Task | Key Output | Reference / Template |
|------|------------|---------------------|
| 1. Driver analysis | Driver analysis table | `templates/driver-analysis-table.md`, `references/architectural-drivers.md` |
| 2. Pattern selection | Pattern selection ADR | `references/architectural-patterns.md`, `templates/adr-template.md` |
| 3. Module decomposition | Module list with boundaries | `references/architectural-drivers.md` |
| 4. Interface contracts | Interface spec document | `templates/interface-contract.md` |
| 5. Technology selection | Technology ADRs | `templates/adr-template.md` |
| 6. Cross-cutting concerns | Cross-cutting concerns spec | `references/cross-cutting-concerns.md` |
| 7. Architecture diagrams | Mermaid C4 diagrams | `references/c4-diagramming.md` |
| 8. Decomposability validation | Validation report | `references/decomposability-validation.md`, `templates/architecture-document.md` |

### ADR quick rules

- One decision per ADR — never bundle multiple decisions
- Status: proposed → accepted (or rejected, deprecated, superseded)
- Use the Nygard format: Title, Status, Context, Decision, Consequences
- Every ADR traces to specific driver IDs from the driver analysis table
- See `references/adr-format.md` for format guidance

## Pitfalls

1. **Functional requirements driving pattern selection.** Quality attributes drive architecture, not features. A system with strict latency requirements needs a different pattern than one with strict modifiability requirements, even if they have identical functional requirements. Always start from the quality attribute drivers in Task 1.
2. **Modules too large for a single context window.** The LLM-critical sizing constraint in Task 3 is not a suggestion — a module that exceeds ~60% of a context window will produce lower-quality code because the LLM loses signal to noise. Decompose aggressively.
3. **Implicit interface assumptions.** If two modules communicate but the interface isn't written down, each downstream LLM will assume a different contract. The result is integration failures that only surface when the modules are combined. Every inter-module interaction needs an explicit contract (Task 4).
4. **Unspecified cross-cutting concerns.** "We'll figure out logging later" means each module invents its own logging format, error response shape, and auth pattern. Specify cross-cutting concerns in Task 6 before any implementation begins.
5. **Image-based diagrams.** Architecture diagrams saved as PNG/SVG images cannot be consumed by downstream LLMs. Always produce text-based diagrams (Mermaid, PlantUML) that render in Markdown and can be read as text.
6. **Skipping decomposability validation.** Task 8 catches boundary errors before they become task-spec problems. If the Task Engineer can't produce a clean task spec, the root cause is usually a module boundary that requires cross-module internal knowledge — which Task 8 would have caught.
7. **Technology selection before pattern selection.** Choosing a framework before choosing an architectural pattern constrains the architecture to the framework's opinion. Select patterns first (Task 2), then choose technologies that fit the pattern (Task 5).
8. **ADRs without tradeoff analysis.** An ADR that says "we chose X because it's the best" is useless to a future developer. Document the alternatives considered and why they were rejected — this is the core value of an ADR.
9. **Over-architecting.** YAGNI applies to architecture too. Don't add modules, layers, or patterns for hypothetical future requirements. Every architectural element should trace to a current driver from the SRS.

## Verification

- [ ] Every functional requirement ID in the RTM appears in the driver analysis table
- [ ] Every quality attribute driver is quantified and maps to an ISO/IEC 25010 characteristic
- [ ] Every constraint from the SRS is recorded in the driver analysis table
- [ ] The selected architectural pattern has an ADR with documented tradeoffs
- [ ] Every module has a unique name, a one-sentence responsibility statement, and explicit boundaries
- [ ] Every module passes the single-context-window feasibility check
- [ ] Every inter-module interaction has an explicit interface contract (signatures, data models, error contracts)
- [ ] Every technology decision has an ADR tracing to driver IDs and constraints
- [ ] Every cross-cutting concern in the checklist is addressed or explicitly marked N/A with rationale
- [ ] Architecture diagrams exist for: context, container, component (if complex), deployment, and data flow
- [ ] All diagrams are text-based (Mermaid or PlantUML) and render in Markdown
- [ ] The decomposability validation report covers every module with a pass/fail verdict
- [ ] No module requires knowledge of another module's internal implementation to implement
- [ ] Feedback paths to Requirements Engineer and from Task Engineer are documented as structured artifacts
