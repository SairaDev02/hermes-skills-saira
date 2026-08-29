# ADR Template (Nygard Format)

> Copy this template for each Architecture Decision Record. One decision per file.
> File naming: `ADR-NNNN-<short-kebab-title>.md` in `docs/adr/`.

---

# ADR-NNNN: <Decision Title>

## Status

<proposed | accepted | rejected | deprecated | superseded by ADR-MMMM>

## Context

<Why is this decision needed? What problem are we solving?>

<Reference specific driver IDs from the driver analysis table:>

- **Drivers:** FD-___, QA-___, C-___
- **Constraints:** <list relevant constraints>

<What is the current state? What forces are at play?>

## Decision

<What is the change or choice being made? Write in present tense as if telling a story to a future developer.>

We will <action>.

## Consequences

**Positive:**
- <benefit 1>
- <benefit 2>

**Negative:**
- <drawback 1>
- <drawback 2>

**Neutral / Follow-up:**
- <consequence that is neither good nor bad>
- Follow-up: <action needed as a result of this decision>

---

## ADR Template (MADR Format — for decisions with 3+ viable options)

# ADR-NNNN: <Decision Title>

## Status

<proposed | accepted | rejected | deprecated | superseded by ADR-MMMM>

## Context

<Problem, constraints, and driver IDs — same as Nygard format>

## Options Considered

### Option 1: <Name>

- **Description:** <brief>
- **Pros:**
  - <pro 1>
  - <pro 2>
- **Cons:**
  - <con 1>
  - <con 2>
- **Driver fit:** QA-___ (satisfied), QA-___ (partially), C-___ (violated)

### Option 2: <Name>

- **Description:** <brief>
- **Pros:**
  - <pro 1>
- **Cons:**
  - <con 1>
- **Driver fit:** QA-___ (satisfied), QA-___ (not satisfied)

### Option 3: <Name>

- **Description:** <brief>
- **Pros:**
  - <pro 1>
- **Cons:**
  - <con 1>
- **Driver fit:** QA-___ (satisfied)

## Decision

We chose **Option N** because <one-sentence justification tying back to the highest-priority drivers>.

## Consequences

**Positive:**
- <benefit 1>

**Negative:**
- <drawback 1>

**Neutral / Follow-up:**
- Follow-up: <action needed>
