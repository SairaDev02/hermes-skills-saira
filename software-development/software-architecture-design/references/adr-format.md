# ADR Format Reference

Architecture Decision Records (ADRs) capture a single architectural decision and its rationale. Based on Michael Nygard's format from "Documenting Architecture Decisions" (2011).

## Why ADRs

> "A new person coming on to a project may be perplexed, baffled, delighted, or infuriated by some past decision. Without understanding the rationale or consequences, this person has only two choices: blindly accept the decision or blindly change it."
> — Michael Nygard

ADRs make architectural decisions **explicit, immutable, and discoverable**. They replace tribal knowledge with versioned documents.

## Nygard Format (Recommended)

Each ADR is a single Markdown file named `ADR-NNNN-short-title.md` (e.g., `ADR-0001-use-event-driven-architecture.md`), stored in a `docs/adr/` directory.

### Structure

```markdown
# ADR-NNNN: <Title>

## Status
<proposed | accepted | rejected | deprecated | superseded by ADR-MMMM>

## Context
<Why is this decision needed? What problem are we solving? What constraints are in play? Reference specific driver IDs from the driver analysis table.>

## Decision
<What is the change or choice being made? Write in present tense as if telling a story to a future developer.>

## Consequences
<What are the results? Include positive effects, negative effects, and neutral effects. List follow-up tasks or risks.>
```

### Example

```markdown
# ADR-0001: Adopt Event-Driven Architecture for Order Processing

## Status
Accepted

## Context
The SRS requires (FR-014) order processing with p95 throughput of 5000 orders/sec and
(NFR-007) decoupled scaling of order validation and fulfillment. The current synchronous
layered design (ADR-0000) cannot meet the throughput driver because the validation and
fulfillment layers are coupled. Driver IDs: NFR-007 (performance), NFR-012 (scalability).

## Decision
We will adopt an event-driven architecture for the order processing subsystem. Order
intake publishes an OrderReceived event to a message broker (Kafka). The Validation
and Fulfillment services subscribe independently and scale based on their own throughput.

## Consequences
Positive:
- Validation and Fulfillment scale independently (NFR-012 satisfied)
- Throughput target achievable — broker handles 50K+ events/sec
- New subscribers (e.g., Analytics) added without modifying existing services

Negative:
- Eventual consistency — order status is not immediately consistent
- Debugging is harder — must trace event chains across services
- Operational complexity — Kafka cluster adds infrastructure burden

Neutral:
- Existing synchronous endpoints for queries remain (CQRS pattern)
- Follow-up: define event schema contracts (Task 4)
- Follow-up: add distributed tracing (cross-cutting concern, Task 6)
```

## ADR Lifecycle

```
proposed → accepted → (deprecated | superseded)
                ↓
            rejected
```

- **Proposed:** Written but not yet reviewed
- **Accepted:** Reviewed and adopted; the decision is in force
- **Rejected:** Considered and rejected; the rejection rationale is as valuable as an acceptance
- **Deprecated:** Was accepted but no longer in force (replaced by a new approach)
- **Superseded:** Replaced by a newer ADR — link to the replacing ADR

**Never delete ADRs.** A rejected or superseded ADR is valuable history. It tells future developers what was considered and why it was not pursued.

## MADR Format (Alternative)

For decisions requiring explicit option comparison, use the Markdown Architectural Decision Record (MADR) format — an extension of Nygard that adds structured option analysis:

```markdown
# ADR-NNNN: <Title>

## Status
Accepted

## Context
<Problem and constraints. Reference driver IDs.>

## Options Considered

### Option 1: <Name>
- **Description:** <brief>
- **Pros:** <list>
- **Cons:** <list>
- **Driver fit:** <which quality attributes are satisfied, which are not>

### Option 2: <Name>
- **Description:** <brief>
- **Pros:** <list>
- **Cons:** <list>
- **Driver fit:** <which quality attributes are satisfied, which are not>

## Decision
<Selected option and one-sentence justification>

## Consequences
<As above>
```

Use MADR when there are 3+ viable options with non-obvious tradeoffs. Use Nygard when the decision is straightforward and the rationale fits in one page.

## ADR Rules

1. **One decision per ADR.** Never bundle multiple decisions.
2. **Number sequentially.** ADR-0001, ADR-0002, etc. Never renumber.
3. **Trace to drivers.** Every ADR's Context section references specific driver IDs from the driver analysis table (Task 1).
4. **Write for the future.** The audience is a developer joining the project in 2 years who needs to understand *why* this choice was made.
5. **Keep it small.** Nygard: "Large documents are never kept up to date. Small, modular documents have at least a chance at being updated." Target 1-2 pages.
6. **Never delete.** Supersede with a link; keep the history.

## Sources

- Michael Nygard, "Documenting Architecture Decisions," 2011 (https://adr.github.io)
- joelparkerhenderson/architecture-decision-record GitHub repository (16.7k stars)
- MADR — Markdown Architectural Decision Records (https://adr.github.io/madr/)
