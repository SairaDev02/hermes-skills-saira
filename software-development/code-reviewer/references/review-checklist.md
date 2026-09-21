# Review Checklist Reference

The methodology for systematically checking code compliance against requirements, architecture, style, and conventions. Supports Tasks 2, 3, and 5 of the Code Reviewer process. Grounded in Michael Fagan's inspection process (1976) and modern code review practices.

## Fagan Inspection Process (Adapted)

Michael Fagan developed the formal code inspection process at IBM in the mid-1970s. The process has five phases, adapted here for LLM-generated code review:

| Phase | Fagan Original | Code Reviewer Adaptation |
|-------|--------------|--------------------------|
| 1. Overview | Author briefs inspectors on the artifact | Reviewer reads the task spec and upstream artifacts |
| 2. Preparation | Inspectors study the artifact individually | Reviewer reads the diff and changed files |
| 3. Inspection | Team meets to find defects | Reviewer runs Tasks 2–7 (compliance, security, style, complexity, edge cases) |
| 4. Rework | Author fixes issues | Task Engineer re-dispatches with refined spec |
| 5. Follow-up | Moderator verifies fixes | Reviewer re-reviews re-dispatched code (Task 1 re-entry) |

Key Fagan principle: **the reviewer's job is to find defects, not to fix them.** The reviewer identifies *where* the problem is and *what* the issue is — the fix direction is the boundary; the actual fix is the Task Engineer's job.

## Requirements Compliance Check (Task 2)

### Step-by-Step

1. **Extract acceptance criteria** from the task spec — each criterion has an SRS requirement ID.
2. **Map each criterion to code** — identify the function(s), class(es), or module(s) that implement it.
3. **Verify behavioral match** — does the code's actual behavior match the spec's expected behavior?
4. **Check RTM traceability** — every requirement ID in the RTM mapped to this task must be addressed.
5. **Flag unimplemented requirements** — acceptance criteria with no corresponding code.
6. **Flag extra implementations** — code that implements behavior not traced to any requirement (scope creep).

### Compliance Checklist Categories

| Category | Check | Pass Criterion |
|----------|-------|----------------|
| Functional requirement | Does the code implement the required behavior? | Code behavior matches spec exactly |
| Acceptance criterion | Is each acceptance criterion met? | Every criterion has a passing code assessment |
| RTM traceability | Is every mapped requirement ID addressed? | Zero unaddressed requirement IDs |
| Scope adherence | Does the code only implement what's in the spec? | No extra behavior beyond spec |
| Constraint compliance | Does the code follow task spec constraints? | Every constraint is met |

## Architecture Compliance Check (Task 3)

### Module Boundary Compliance

The most common LLM failure in code generation: an LLM reaches outside its module boundary to "fix" something it wasn't asked to touch. This often produces silent integration failures when other modules are combined.

1. **Extract the scope field** from the task spec — it lists exactly which files, modules, and functions this task may touch.
2. **List all changed files** from the diff.
3. **Cross-reference** — every changed file must appear in the scope field. Any file not in the scope is an out-of-scope modification.
4. **Check function-level scope** — even within an in-scope file, verify the code only modifies functions listed in the scope. Modifications to functions not in the scope are boundary violations.
5. **Flag violations** — document each out-of-scope change with: file path, function name, and the scope boundary it violates.

### Interface Contract Compliance

For each interface the code touches (as a producer or consumer):

1. **Signature match** — does the function signature match the interface contract (name, parameters, types, return type)?
2. **Data model match** — do the request/response data structures match the contract schemas?
3. **Error contract match** — does the code produce the documented error codes and error response formats?
4. **Protocol match** — does the code use the communication protocol specified in the contract (REST, gRPC, in-process call)?

### Cross-Cutting Concerns Compliance

Check the code against the cross-cutting concerns spec from the architecture document:

| Concern | Check |
|---------|-------|
| Error handling | Does the code follow the specified error handling strategy? |
| Logging | Does the code use the specified logging format and level? |
| Authentication | Does the code follow the specified auth pattern? |
| Authorization | Does the code enforce the specified access control? |
| Data validation | Does the code validate input per the specified strategy? |
| Configuration | Does the code read config from the specified source? |

## Style and Convention Check (Task 5)

### Linter Detection

Detect the project language and run the appropriate linter:

| Language | Linter | Command |
|----------|--------|---------|
| Python | ruff | `ruff check .` |
| Python | pylint | `pylint <module>` |
| JavaScript/TypeScript | eslint | `npx eslint .` |
| Rust | clippy | `cargo clippy -- -D warnings` |
| Go | go vet | `go vet ./...` |
| Java | checkstyle / spotbugs | per project config |

### Coding Standards Check

Verify the code follows the coding standards from the task spec's constraints field:

- **Naming conventions** — variable, function, class, file naming per the project's convention
- **File structure** — imports, exports, module organization per the project's pattern
- **Import organization** — ordering, grouping, no unused imports
- **Documentation** — public APIs documented, non-obvious logic has comments explaining "why"

### Debug Artifact Detection

Scan for leftover debug artifacts in the changed code:

```bash
# Debug statements
git diff --cached | grep "^+" | grep -E "print\(|console\.log|debugger|System\.out\.print"
# TODOs and FIXMEs
git diff --cached | grep "^+" | grep -E "TODO|FIXME|HACK|XXX"
# Commented-out code
git diff --cached | grep "^+" | grep -E "^\s*//.*[a-zA-Z]" | grep -vE "^\s*//\s*(http|https|eslint|tslint|prettier|@)"
```

## Verdict Decision Matrix

| Condition | Verdict | Rationale |
|-----------|---------|----------|
| Zero critical, zero warnings (suggestions only) | **Approve** | Code meets all criteria; suggestions are non-blocking improvements |
| Any critical or warning, fixable within task scope | **Request changes** | Specific issues can be fixed by re-dispatching with refined context |
| Fundamental approach is wrong, not fixable within task scope | **Reject** | The code needs re-architecture — feed back to Architect |

### Verdict Rationale Requirements

- **Approve:** List any suggestions that were noted but not blocking. Confirm all compliance checks passed.
- **Request changes:** List every critical and warning finding with its review comment ID. Specify which findings feed back to the Task Engineer.
- **Reject:** List the architectural problems. Specify which module boundary is wrong, which interface contract is violated, and why the code cannot be fixed within the current task scope. Feed back to the Architect.
