# Scope Boundaries Reference

The methodology for defining exact scope boundaries for each task. This is Task 3 of the task engineering process.

## Why Scope Boundaries Matter

LLM coding agents are proactive — they try to "fix" things they see while working. Without an explicit scope boundary, an LLM that encounters a code smell in an adjacent file will refactor it, even though it wasn't asked to. This creates:

- **Integration conflicts:** Two tasks modify the same file with incompatible changes.
- **Scope creep:** The task produces more changes than expected, making review harder.
- **Hidden dependencies:** A task that "fixed" something in another module creates an undocumented dependency.

The solution is explicit inclusion and exclusion scope per task.

## Scope Specification Format

Each task's scope field has three sections:

### Inclusion Scope

List every file, directory, module, and function the task may create or modify:

```markdown
### Scope: Inclusion

**Files to create:**
- src/modules/payment/processor.ts — payment processing logic
- src/modules/payment/types.ts — payment type definitions

**Files to modify:**
- src/modules/order/service.ts — add call to payment processor (lines ~45-60)
- src/routes/api.ts — register payment endpoint

**Modules to interact with:**
- InventoryService (via IFC-003) — check stock before processing
- NotificationService (via IFC-007) — send payment confirmation
```

### Exclusion Scope

List every file, directory, module, and function the task must NOT touch:

```markdown
### Scope: Exclusion

**Do NOT modify:**
- src/modules/inventory/* — inventory module is owned by TASK-003
- src/modules/auth/* — auth module is owned by TASK-001
- src/modules/notification/* — notification module is owned by TASK-005; interact only via IFC-007
- src/config/* — configuration is owned by TASK-008
- Any file in tests/ — test creation is owned by the Tester role

**Do NOT create:**
- New top-level directories
- New configuration files
- New package.json entries (constraints specify no new dependencies)
```

### Boundary Clarifications

For ambiguous cases, add explicit clarifications:

```markdown
### Scope: Boundary Clarifications

- You MAY read files outside the inclusion scope to understand interfaces, but you may NOT modify them.
- You MAY add helper functions within files in the inclusion scope, but they must be private (not exported).
- You MAY add type imports from other modules, but you may NOT add runtime imports beyond what interface contracts specify.
- If you encounter a bug in an excluded file, document it in the task output — do NOT fix it.
```

## Scope Conflict Detection

After defining scope for all tasks, check for conflicts:

1. **File overlap check:** No two tasks should claim to modify the same file unless one explicitly depends on the other's output. If both need to modify the same file, either merge the tasks or define a clear ordering dependency (Task 7).

2. **Module ownership check:** Each module should have exactly one task that "owns" it (can create/modify its core files). Other tasks may interact with the module via interface contracts but should not modify its files.

3. **Boundary ambiguity check:** For each task, verify the boundary between "may touch" and "must not touch" is unambiguous. If a developer would be unsure whether a file is in scope, add it to the exclusion list explicitly.

## Anti-Patterns

### The Open Scope
"This task implements the user module." — No inclusion list, no exclusion list. The LLM will modify every file it thinks is relevant, including files owned by other tasks.

### The Contradictory Scope
Inclusion: "modify src/shared/utils.ts" + Exclusion: "do not modify src/shared/*" — the LLM cannot resolve the contradiction. Make inclusion and exclusion lists non-overlapping.

### The Over-Broad Exclusion
"Do NOT modify any file outside src/modules/payment/" — This is too broad if the task needs to register a route in src/routes/api.ts. The exclusion should be specific, not a blanket "everything else."

### The Missing "Read But Don't Write" Distinction
The LLM needs to read interface contracts from other modules' files to understand how to call them. If the exclusion says "do not touch src/modules/inventory/*," the LLM may not read it at all, leading to incorrect assumptions. Clarify: "read for interface understanding, do not modify."

## Scope and Dependencies

Scope boundaries directly feed into the dependency graph (Task 7):

- If Task B modifies a file Task A creates → B depends on A.
- If Task B calls an interface Task A implements → B depends on A.
- If Task B and Task C both modify the same file → one depends on the other (define the ordering), or merge them.

Record these dependencies when finalizing scope.
