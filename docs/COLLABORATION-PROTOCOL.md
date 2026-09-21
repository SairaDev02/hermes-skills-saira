# Developer–LLM Collaboration Protocol

## Agent start sequence

1. Read the applicable handoff.
2. Read `docs/PROJECT-CONSTITUTION.md`, `docs/GLOSSARY.md`, and referenced contracts.
3. Resolve referenced `REF-` IDs and `ASM-` IDs.
4. Confirm task scope, exclusions, output contract, and evidence requirements.
5. Ask only when ambiguity changes implementation or acceptance; otherwise record a bounded assumption.

## Agent working rules

- Do not infer unresolved behavior from neighboring code.
- Do not silently expand scope or rewrite upstream specifications.
- Record uncertainty, scope conflicts, and contract mismatches as findings.
- Preserve stable IDs and report every changed file.
- Run the declared verification commands and report exact results.
- Distinguish planned, implemented, and verified behavior.

## Developer response options

- **Clarify:** answer the question and identify affected IDs.
- **Approve assumption:** accept a named assumption with scope and version.
- **Narrow scope:** remove the affected behavior from the task.
- **Change specification:** create a change record and propagate it.
- **Return task:** reject the task until a blocking ambiguity is resolved.

## Completion report

Every implementation handoff reports:

- source revision and changed files;
- requirements, contracts, and task IDs addressed;
- commands run and exact result summary;
- known failures, skips, and environment limits;
- open findings and assumptions;
- claim state for each acceptance criterion.
