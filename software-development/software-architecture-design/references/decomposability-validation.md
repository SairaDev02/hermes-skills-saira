# Decomposability Validation Reference

Validation that each module can be implemented as a self-contained task by a single LLM without needing context from other modules' internals. This is Task 8 of the architecture process.

## Validation Checklist

For each module, run these four checks:

### Check 1: Module-to-Task Feasibility

**Question:** Can a developer (or LLM) implement this module given only:
- The module's responsibility statement (from Task 3)
- Its interface contracts (from Task 4) — both sides it implements and consumes
- The cross-cutting concerns spec (from Task 6)
- The relevant SRS requirements (mapped via the RTM)

**Pass criterion:** No knowledge of another module's internal implementation is required. Only the *interface* of other modules is needed, and all interfaces are documented in Task 4.

**Fail action:** The module boundary is wrong. Return to Task 3 and re-decompose so that the cross-module knowledge needed is captured in an interface contract (Task 4) instead of requiring internal access.

### Check 2: Context Sufficiency

**Question:** Does the total input context for this module fit within a reasonable budget?

**Input context for a module =**
- Module responsibility statement (~100 words)
- Interface contracts this module implements (~500-2000 words depending on complexity)
- Interface contracts this module consumes (~500-2000 words)
- Cross-cutting concerns spec (~1000-3000 words)
- Relevant SRS requirements (~500-2000 words)
- Constraints from task manifest (~200-500 words)

**Budget rule:** Total input context should not exceed ~40% of an LLM context window. The remaining 60% is for the LLM's output (implementation code, tests, documentation).

**Heuristic:** If input context + expected output exceeds ~60% of a context window, the module is too large — decompose further.

**Pass criterion:** Estimated total context ≤ 40% of target LLM context window.

**Fail action:** The module is too large or has too many interface dependencies. Return to Task 3 to decompose into smaller modules, or return to Task 4 to simplify the interface surface.

### Check 3: Interface Completeness

**Question:** Does every inter-module dependency have a documented interface contract?

**How to check:** For each module, list every other module it depends on. For each dependency, verify there is a corresponding interface contract in the Task 4 interface specification document that covers:
- Communication pattern (sync, async, in-process)
- Operation signatures (name, parameters, types, return type)
- Data models (request/response schemas)
- Error contracts (error cases, codes, formats)

**Pass criterion:** Zero undocumented dependencies. Every dependency has a complete contract.

**Fail action:** Return to Task 4 to define the missing interface contract before proceeding.

### Check 4: Boundary Clarity

**Question:** Is the module boundary unambiguous — does a developer know exactly what to build and what NOT to touch?

**How to check:** The module's boundary spec (from Task 3) should clearly state:
- What data the module owns
- What behavior the module provides
- What the module does NOT own (explicit exclusion list)
- Which files/modules/functions the implementer may modify

**Pass criterion:** The boundary spec has both inclusion and exclusion lists. No ambiguity about scope.

**Fail action:** Return to Task 3 to clarify the boundary — add explicit exclusion lists.

## Validation Report Format

```markdown
# Decomposability Validation Report

**Date:** <date>
**Architecture version:** <version>
**Validator:** <name/role>

## Summary

| Module | Task Feasibility | Context Sufficiency | Interface Completeness | Boundary Clarity | Overall |
|--------|-----------------|--------------------|-----------------------|-------------------|---------|
| Module A | Pass | Pass | Pass | Pass | **Pass** |
| Module B | Pass | Fail (22k tokens) | Pass | Pass | **Fail → Task 3** |
| Module C | Pass | Pass | Fail (missing IFC-004) | Pass | **Fail → Task 4** |

## Detailed Findings

### Module A: <name>
- **Task feasibility:** Pass — implementable from responsibility statement + IFC-001, IFC-002 + cross-cutting spec + FR-001..FR-005
- **Context sufficiency:** Pass — estimated 8k tokens input, 12k expected output = 20k total (within budget)
- **Interface completeness:** Pass — depends on Module B (IFC-002) and Module D (IFC-005); both fully documented
- **Boundary clarity:** Pass — owns order state machine; does NOT own inventory state, payment processing, or user auth
- **Verdict:** Pass

### Module B: <name>
- **Task feasibility:** Pass
- **Context sufficiency:** Fail — estimated 22k tokens input (interface contracts IFC-003..IFC-008 = 18k, cross-cutting spec = 4k); exceeds 40% budget
- **Interface completeness:** Pass
- **Boundary clarity:** Pass — but module is too large
- **Verdict:** Fail → Return to Task 3. Decompose Module B into B1 and B2, each with fewer interface dependencies.
- **Recommended action:** Split along the reporting vs. processing boundary. B1 handles real-time processing (IFC-003, IFC-004); B2 handles batch reporting (IFC-005..IFC-008).

### Module C: <name>
- **Task feasibility:** Pass
- **Context sufficiency:** Pass
- **Interface completeness:** Fail — depends on Module E but no interface contract exists for this dependency
- **Boundary clarity:** Pass
- **Verdict:** Fail → Return to Task 4. Define interface contract IFC-004 for the Module C → Module E dependency.
- **Recommended action:** Document the communication pattern, signatures, data models, and error contracts for C → E.

## Overall Architecture Verdict

<Pass | Fail with N modules requiring re-decomposition / interface definition>

## Next Steps

- For passing modules: forward to Task Engineer for task manifest creation
- For failing modules: return to the specified task (3 or 4), fix, and re-validate
```

## Key Principle

> If a module requires deep knowledge of another module's internals to implement, the boundary is wrong — re-decompose.

The interface contract is the *only* acceptable form of cross-module knowledge. Internal implementation details are never shared between modules — only contracts are.
