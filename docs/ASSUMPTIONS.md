# Assumptions and Unknowns

Record uncertainty that could affect requirements, design, implementation, testing, or release. An assumption is not binding until accepted by the responsible owner.

| ID | Assumption or question | Impact | Owner | Status | Evidence/resolution |
|---|---|---|---|---|---|
| ASM-000 | `<assumption or unresolved question>` | `<affected area>` | `<role/person>` | open | `<link or note>` |

## Status vocabulary

`open` · `accepted` · `rejected` · `superseded` · `verified`

## Rules

- Tasks depending on an open assumption are `CONDITIONAL`, not `READY`.
- Acceptance records who accepted the assumption and which version it applies to.
- A resolved assumption that changes behavior creates a change record and propagates through the handoff chain.
