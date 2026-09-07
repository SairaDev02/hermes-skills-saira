# Task Entry Template

> One normalized entry per task. It references versioned context blocks.
> The generated dispatch bundle, not this source entry, must be self-contained.
> This template defines the structure; fill in all fields.

---

## Task <TASK-ID>: <Title>

### Source context

- Constitution: `docs/PROJECT-CONSTITUTION.md`
- References: `REF-000` — applies to `<rule/API>`
- Assumptions: `ASM-000` — status `<status>`

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

### Context Blocks

> List the immutable, versioned blocks used to generate this task's bundle.
> The bundle generator expands these blocks before dispatch.

| Block ID | Version | Purpose |
|---|---|---|
| CTX-001 | 1.0 | <module responsibility or contract> |

#### Context Block Expansion Preview (optional)

<Generated bundle may inline the selected blocks here for review; this is derived output, not authoritative source content.>

The normalized entry stores context block IDs only. The bundle generator expands those blocks into the dispatch artifact, including the applicable module responsibility, interfaces, requirements, conventions, existing-code excerpts, and constraints. Do not maintain a second hand-edited copy here.

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

### Claim state and evidence

| Acceptance item | State | Evidence required |
|---|---|---|
| AC-1 | PLANNED | `<command, test, inspection, or stakeholder evidence>` |

Allowed states: `PLANNED`, `IMPLEMENTED`, `VERIFIED`, `BLOCKED`, `DISPUTED`, `STALE`.

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
