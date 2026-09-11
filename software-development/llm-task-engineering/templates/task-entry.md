# Task Entry Template

> One entry per task. Each entry must be self-contained — the LLM receives
> only this entry and cannot look up external references.
> This template defines the structure; fill in all fields.

---

## Task <TASK-ID>: <Title>

### Description

<One to three sentences describing what this task implements.>

### Parent Module

<Module name from architecture document>

### Scope

**Inclusion (may create or modify):**

- <file or directory paths>
- <files to modify with approximate location>

**Exclusion (must NOT touch):**

- <file or directory paths owned by other tasks>
- <modules to interact with only via interface contracts>

**Boundary Clarifications:**

- <any ambiguous cases resolved — e.g., "may read but not modify X">

### Input Context

> This is ALL the context the LLM receives. It cannot ask for more.
> Trim to the minimal high-signal set. See `references/context-curation.md`.

#### Module Responsibility

<One-sentence responsibility statement from architecture document>

#### Interface Contracts (Implementing)

<Full text of interface contracts this task implements — trimmed to relevant operations>

#### Interface Contracts (Consuming)

<Signatures and data models only for interfaces this task calls as a client>

#### Requirements

<SRS requirement entries mapped to this task via the RTM — verbatim text>

#### Conventions

<Relevant cross-cutting concern conventions — verbatim from the spec>

#### Existing Code

<Code sections the task will extend or integrate with — trimmed to relevant functions>

#### Constraints

<Coding standards, patterns, libraries, error handling rules — both cross-cutting and task-specific>

### Output Contract

#### Public API

<Function/method signatures with types, type definitions, interface implementations>

```typescript
// Example — replace with actual language and signatures
function exampleFunction(param: Type): ReturnType;
```

#### Behavior

<For each function: normal path, error paths, side effects, explicit non-effects>

#### File Structure

<Every file the task creates or modifies, with expected content summary>

#### Integration Points

<How this task's output connects to other modules — interface IDs, event names, etc.>

### Acceptance Criteria

> Each criterion must be binary (pass/fail) and trace to an SRS requirement ID.

- [ ] **AC-1 (FR-XXX):** <criterion description — e.g., "processPayment returns PaymentResult with status 'success' for valid inputs">
- [ ] **AC-2 (FR-XXX):** <criterion description — e.g., "processPayment throws ValidationError for orders with total ≤ 0">
- [ ] **AC-3 (NFR-XXX):** <criterion description — e.g., "processPayment completes within 500ms at p95">

**Done when:** <concrete, programmatically verifiable completion clause — e.g., "all acceptance criteria pass, `npm test` is clean, `npm run lint` is clean">

### Dependencies

**Depends on:**

- <TASK-ID> — reason: <interface contract / file creation / data model>
- <TASK-ID> — reason: <...>

**Blocks:**

- <TASK-ID> — reason: <why this task must complete before the other can start>

### Estimated Context

| Component | Estimated Tokens |
|-----------|-----------------|
| Input context | ~<N>K |
| Output contract | ~<N>K |
| Constraints | ~<N>K |
| Expected output | ~<N>K |
| **Total** | **~<N>K** |

| Check | Threshold | Status |
|-------|-----------|--------|
| Input ≤ 40% of window | <N>K / <budget>K | ✅ / ❌ |
| Total ≤ 60% of window | <N>K / <budget>K | ✅ / ❌ |
| Smart zone (< 100K) | <N>K | ✅ / ⚠️ |
