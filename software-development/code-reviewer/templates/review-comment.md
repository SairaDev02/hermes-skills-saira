# Review Comment Template

Use this template for each inline review comment produced in Task 8. One comment per issue.

---

## Comment ID: RC-<number>

**File:** `<file_path>`
**Line:** `<line_number>`
**Severity:** Critical | Warning | Suggestion
**Issue Type:** Requirements | Architecture | Security | Style | Complexity | Edge-case
**Source Task:** Task 2 | Task 3 | Task 4 | Task 5 | Task 6 | Task 7

### Code Snippet

```
<3-5 lines of code context surrounding the issue>
```

### Description

<What the issue is and why it matters. Be specific: reference the spec, contract, or convention violated.>

### Suggested Direction

<The direction the fix should take — NOT the fix itself. The Task Engineer re-dispatches with this guidance. Example: "Add null check for user_id parameter before database query" or "Extract repeated validation logic into a shared utility function.">

### CWE ID (if security)

<CWE-XX — only for security findings>

### Related Test Case (if edge-case)

<TC-XXX — only if there is an existing test case, or "New test case recommended: <description>" if uncovered>
