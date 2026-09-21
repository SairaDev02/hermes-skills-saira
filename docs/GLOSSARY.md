# Project Glossary

Use these definitions consistently across requirements, architecture, tasks, tests, reviews, and release records. Add a term when ambiguity could change implementation or verification.

| Term | Definition | Do not confuse with | Canonical source | Owner |
|---|---|---|---|---|
| `<term>` | `<precise meaning>` | `<nearby term>` | `<artifact/ID>` | `<role>` |

## Naming and units

- Field names must match the applicable interface contract.
- Units must be written explicitly; do not mix milliseconds and seconds.
- Timestamps must state timezone and serialization format.
- IDs are opaque unless a contract explicitly defines their structure.
