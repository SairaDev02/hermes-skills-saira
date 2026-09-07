# Technical Reference Index

This registry points to external technical documentation used by the project. Prefer official, versioned sources. Do not copy whole manuals into the repository.

## Rules

- Give every reference a stable `REF-` ID.
- Prefer primary/official documentation, standards, and source repositories.
- Record the applicable technology version and access date.
- Mark links `current`, `deprecated`, `uncertain`, or `needs-review`.
- Summarize the project-specific rule or decision separately; a URL alone is not an implementation instruction.
- Add only references relevant to a task bundle or architectural decision.

## Registry

| ID | Technology/product | Topic | URL | Version | Accessed | Authority | Status | Use when |
|---|---|---|---|---|---|---|---|---|
| REF-000 | `<technology>` | `<topic>` | `<official URL>` | `<version>` | `<YYYY-MM-DD>` | official/standard/source | needs-review | `<task or decision>` |

## Reference use in artifacts

Tasks and handoffs may cite IDs without repeating URLs:

```yaml
references:
  - id: REF-000
    applies_to: "<specific rule or API>"
    required_version: "<version or range>"
```

When a reference changes, create a change record if the affected behavior, contract, or task changes.
