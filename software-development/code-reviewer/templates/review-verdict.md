# Review Verdict Template

Use this template for the final verdict produced in Task 9. One verdict per review cycle.

---

# Review Verdict: <Task ID>

**Reviewer:** Code Reviewer
**Date:** <YYYY-MM-DD>
**Task Spec:** <task spec reference>
**Code Source:** <diff / PR # / file set reference>
**Test Results:** Available | Unavailable

## Verdict: Approve | Request Changes | Reject

### Summary

<One-to-two sentence summary of the review outcome.>

### Finding Counts

| Severity | Count |
|----------|-------|
| Critical | <N> |
| Warning | <N> |
| Suggestion | <N> |
| **Total** | **<N>** |

### Findings by Category

| Category | Critical | Warning | Suggestion |
|----------|----------|---------|------------|
| Requirements compliance | <N> | <N> | <N> |
| Architecture compliance | <N> | <N> | <N> |
| Security | <N> | <N> | <N> |
| Style and conventions | <N> | <N> | <N> |
| Complexity and maintainability | <N> | <N> | <N> |
| Edge case gaps | <N> | <N> | <N> |

### Rationale

<Detailed rationale for the verdict. Reference specific review comment IDs (RC-XXX).>

- **If Approve:** List any suggestions noted but not blocking. Confirm all compliance checks passed.
- **If Request Changes:** List every critical and warning finding with its RC-ID. Specify which findings feed back to the Task Engineer.
- **If Reject:** List the architectural problems. Specify which module boundary is wrong, which interface contract is violated, and why the code cannot be fixed within the current task scope.

### Feedback Path

| Target | Artifact | Details |
|--------|----------|---------|
| Task Engineer | <list of RC-IDs> | <description of what to re-dispatch> |
| Architect | <list of architectural issues> | <description of what to re-design> |
| Tester | <list of edge case gaps> | <description of test cases to add> |

### Approve Conditions (if applicable)

- [ ] All acceptance criteria met (Task 2)
- [ ] All module boundaries respected (Task 3)
- [ ] All interface contracts satisfied (Task 3)
- [ ] Security scan clean (Task 4)
- [ ] Style and convention checks passed (Task 5)
- [ ] No critical complexity findings (Task 6)
- [ ] All edge case gaps covered by tests or acceptable (Task 7)

### Cleanup Trigger (if approved)

- Complexity findings identified: Yes | No
- Simplify-code pass recommended: Yes | No
- Rationale: <if yes or no, why>
