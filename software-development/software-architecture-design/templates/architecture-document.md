# Architecture Document Template

> The architecture document is the master deliverable of the Architect role.
> It compiles all task outputs into a single, self-contained reference.
> Use this template to structure the final document. Each section references the detailed artifact produced in its task.

---

# Architecture Document: <System Name>

**Version:** 0.1.0
**Date:** <date>
**Author:** <name/role>
**Status:** <draft | under review | approved>

**Source artifacts:**
- SRS: <path or reference>
- RTM: <path or reference>
- Feasibility report: <path or reference>

---

## 1. Architectural Drivers

> Output of Task 1. See `templates/driver-analysis-table.md` for the full table.

### 1.1 Functional Drivers

<Insert functional driver summary or link to driver analysis table>

### 1.2 Quality Attribute Drivers

<Insert quality attribute driver summary or link to driver analysis table>

### 1.3 Constraints

<Insert constraint summary or link to driver analysis table>

### 1.4 Tradeoff Analysis

<Insert tradeoff analysis summary>

---

## 2. Architectural Pattern

> Output of Task 2. Reference the ADR for the full rationale.

**Selected pattern:** <pattern name(s)>
**ADR:** ADR-___ (see `docs/adr/ADR-NNNN-*.md`)

**Rationale summary:**
<2-3 sentence summary of why this pattern was chosen, referencing the key quality attribute drivers it addresses.>

**Tradeoffs accepted:**
<Summary of the primary tradeoffs and why they are acceptable given the drivers.>

---

## 3. Module Decomposition

> Output of Task 3.

### Module Summary

| Module ID | Module Name | Responsibility Statement | Owns | Does NOT Own |
|-----------|-------------|--------------------------|------|--------------|
| M-01 | <name> | <one-sentence responsibility> | <data/behavior/state> | <explicit exclusions> |
| M-02 | | | | |
| M-03 | | | | |

### Context-Window Feasibility

| Module ID | Estimated Implementation Size | Single-Context-Window? | Notes |
|-----------|-------------------------------|------------------------|-------|
| M-01 | <S / M / L> | Yes | |
| M-02 | | | |

---

## 4. Interface Contracts

> Output of Task 4. Each interface has a detailed contract document.

### Interface Summary

| Interface ID | Provider Module | Consumer Module(s) | Communication Pattern | Contract Document |
|-------------|----------------|--------------------|-----------------------|-------------------|
| IFC-001 | M-01 | M-02, M-03 | <REST / gRPC / Event / In-process> | `docs/interfaces/IFC-001-*.md` |
| IFC-002 | | | | |

---

## 5. Technology Decisions

> Output of Task 5. Each decision is an ADR.

### Technology Summary

| Decision Point | Module(s) | Selected Technology | ADR |
|---------------|-----------|--------------------|-----|
| Language | M-01, M-02 | <language> | ADR-___ |
| Framework | M-01 | <framework> | ADR-___ |
| Data store | M-03 | <database> | ADR-___ |
| Message broker | M-04 | <broker> | ADR-___ |
| <other> | | | |

---

## 6. Cross-Cutting Concerns

> Output of Task 6. See `references/cross-cutting-concerns.md` for the full checklist.

| Concern | Strategy | Owning Module | Code Constraint for Tasks |
|---------|---------|--------------|--------------------------|
| Error handling | <strategy> | <module> | <convention for task constraints> |
| Logging | | | |
| Authentication | | | |
| Authorization | | | |
| Data validation | | | |
| Configuration | | | |
| Observability | | | |
| Data flow | | | |
| <others as applicable> | | | |

---

## 7. Architecture Diagrams

> Output of Task 7. All diagrams are text-based (Mermaid).

### 7.1 System Context Diagram (C4 Level 1)

<Insert Mermaid C4Context diagram source>

### 7.2 Container Diagram (C4 Level 2)

<Insert Mermaid C4Container diagram source>

### 7.3 Component Diagrams (C4 Level 3)

<For each complex module, insert Mermaid C4Component diagram source>

### 7.4 Deployment Diagram

<Insert Mermaid C4Deployment diagram source>

### 7.5 Data Flow Diagram

<Insert Mermaid flowchart showing data flow for primary use cases>

---

## 8. Decomposability Validation

> Output of Task 8.

### Validation Summary

| Module | Task Feasibility | Context Sufficiency | Interface Completeness | Boundary Clarity | Verdict |
|--------|-----------------|--------------------|-----------------------|-------------------|---------|
| M-01 | Pass | Pass | Pass | Pass | **Pass** |
| M-02 | Pass | Pass | Pass | Pass | **Pass** |

**Overall verdict:** <Pass | Fail with N modules requiring re-work>

<Full validation report: see `docs/validation-report.md`>

---

## 9. Feedback Paths

### To Requirements Engineer

<If any requirement was found architecturally unimplementable, document: requirement ID, the architectural constraint, and suggested revision direction.>

| Requirement ID | Issue | Architectural Constraint | Suggested Revision |
|---------------|-------|--------------------------|-------------------|
| FR-___ | <issue> | <constraint> | <suggestion> |

### From Task Engineer (Anticipated)

<Known boundary or interface concerns that may require Task 3 or Task 4 revision if the Task Engineer encounters problems:>

| Module | Concern | Fallback Action |
|--------|---------|-----------------|
| M-___ | <concern> | <return to Task 3/4> |

---

## Document Checklist

- [ ] Section 1 — Driver analysis table has no empty cells; all drivers trace to SRS IDs
- [ ] Section 2 — Pattern ADR exists with documented tradeoffs
- [ ] Section 3 — Every module has a responsibility statement and explicit boundaries
- [ ] Section 3 — Every module passes the single-context-window check
- [ ] Section 4 — Every inter-module interaction has an interface contract
- [ ] Section 5 — Every technology decision has an ADR tracing to drivers
- [ ] Section 6 — Every cross-cutting concern is addressed or marked N/A
- [ ] Section 7 — Context, container, component, deployment, and data flow diagrams exist
- [ ] Section 7 — All diagrams are text-based (Mermaid)
- [ ] Section 8 — Every module has a pass/fail verdict in the validation report
- [ ] Section 9 — Feedback paths to Requirements Engineer and from Task Engineer are documented
