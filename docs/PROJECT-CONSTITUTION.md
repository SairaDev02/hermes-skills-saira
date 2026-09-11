# Project Constitution

Binding project rules for humans, role agents, and implementation agents. More specific approved contracts override general guidance; unresolved conflicts become findings, not silent assumptions.

## Non-negotiable rules

- Preserve public API compatibility unless an approved change record permits a break.
- Never modify files outside task scope without recording a finding.
- Do not add dependencies without an architecture decision or dependency record.
- Use the project error contract at module boundaries.
- Tests must not depend on execution order or shared mutable state.
- Do not commit secrets, credentials, or production data.
- Claims must identify their artifact/version and evidence state.

## Source-of-truth rules

| Concern | Authoritative source |
|---|---|
| Requirements | Project SRS and RTM |
| Decisions | ADRs |
| Interfaces | Versioned interface contracts |
| Task ownership | Normalized task manifest |
| Test IDs and results | QA test matrix and result report |
| Findings and routing | Feedback records |
| Handoffs | Shared handoff template |
| External documentation | `docs/REFERENCE-INDEX.md` |

## Terminology and values

- Use the glossary in `docs/GLOSSARY.md` for domain terms.
- Use canonical field names from approved interface contracts.
- Record timestamps in the project's declared timezone and format.
- Do not infer semantics from opaque identifiers.

## Uncertainty rule

An unknown, conflicting source, or unverified assumption must be recorded in `docs/ASSUMPTIONS.md` or a feedback record. It may not be silently converted into a requirement, implementation decision, or passing result.
