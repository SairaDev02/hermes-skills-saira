# LLM-Specific Testing Strategies Reference

Testing strategies targeting the unique defect patterns of LLM-generated code. This reference supports Tasks 7 (Exploratory QA) and 8 (Bug Reporting) of the QA Engineer process.

## Why LLM-Generated Code Needs Different Testing

Research on LLM-generated code hallucinations (Liu et al., 2024; Tambon et al., 2024; Lee et al., 2025) identifies recurring defect categories that differ from human-written code. LLMs produce code that *looks* clean, follows local naming conventions, and passes superficial inspection — but contains semantic conflicts with requirements, factual knowledge, and real-world library APIs.

## LLM Hallucination Taxonomy for Testing

### Category 1: Requirement Conflicting

The generated code contradicts the specification. The most prevalent hallucination across all studied LLMs (Liu et al., 2024).

**What to test for:**
- Does the code implement the exact acceptance criterion, or an approximation?
- Does the code handle edge cases the spec mentions, or only the "happy path"?
- Does the code enforce constraints the spec defines (e.g., "must reject empty input")?

**Exploratory strategy:** Read the spec and the code side by side. For each acceptance criterion, verify the code implements it exactly — not an interpretation that "seems right" but deviates on edge cases.

### Category 2: Knowledge Conflicting Hallucinations (KCH)

The generated code calls APIs, functions, or parameters that don't exist, or exist with different signatures. The code looks idiomatic but is factually wrong (e.g., `pd.read_exel('data.csv')` — invented function name, or `pd.read_csv('data.csv', sep='\t')` — plausible but wrong parameter for the intent).

**What to test for:**
- Do all library/API calls use correct function names and signatures?
- Are parameter names correct, not just plausible?
- Do return types match what the library actually returns?

**Exploratory strategy:** Execute every library call in isolation. Verify against the library's actual documentation, not the LLM's assumption. Integration tests that exercise the real library (not mocks) catch KCH defects that unit tests with mocked dependencies miss.

### Category 3: Silent Failures and Suppressed Errors

LLMs may suppress exceptions or return default values to produce "clean" output, hiding real failures.

**What to test for:**
- Does the function raise errors on invalid input, or silently return a default?
- Are exceptions caught and swallowed without logging?
- Does the function return a "success" result when the operation actually failed?

**Exploratory strategy:** Feed invalid inputs and verify the function raises the expected error, not a silent default. Check logs for swallowed exceptions. Compare the function's error behavior against the output contract.

### Category 4: Implicit Assumptions

LLMs may assume global state, environment variables, or configuration that was never specified in the task context.

**What to test for:**
- Does the code depend on environment variables not mentioned in the task spec?
- Does the code assume a specific OS, file path, or directory structure?
- Does the code assume a specific initial state of shared resources?

**Exploratory strategy:** Run the code in a clean environment (no env vars, default paths, fresh state). Verify it behaves correctly or fails with a clear error, not a silent assumption.

### Category 5: State Management Errors

LLM-generated code often passes unit tests but fails on integration and state management — shared mutable state, race conditions, incorrect state transitions.

**What to test for:**
- Does the code correctly manage shared state across concurrent calls?
- Are state transitions atomic, or can they be interrupted leaving inconsistent state?
- Does the code handle the case where a previous operation was interrupted?

**Exploratory strategy:** Test with concurrent access patterns. Kill operations mid-execution and verify the system recovers. Test state transitions out of expected order (negative state transition testing).

### Category 6: Over-Fitting to Tests

When LLMs are given test cases as context (TDD approach), they may optimize for the specific test inputs rather than the general behavior the spec describes.

**What to test for:**
- Does the code pass tests with inputs *slightly different* from the test cases?
- Does the code handle edge cases near the test inputs but not identical?
- Does the code generalize, or does it hard-code the test values?

**Exploratory strategy:** After the implementation passes all tests, run the tests with perturbed inputs (slightly different values that should still pass). If the code fails, it has over-fit to the specific test inputs.

## Exploratory QA Session Templates for LLM Code

### Session Template: API Signature Audit

**Goal:** Verify every library/API call in the generated code uses correct names, signatures, and parameters.

**Steps:**
1. Extract all external library calls from the generated code.
2. For each call, look up the actual library documentation.
3. Compare: function name, parameter names, parameter types, return type.
4. Execute each call in isolation with minimal valid input.
5. Record any mismatch as a KCH defect.

### Session Template: Error Behavior Audit

**Goal:** Verify the code raises errors when it should, and doesn't suppress them.

**Steps:**
1. Identify every error-handling block (try/catch, if error, return default).
2. For each, feed the input that triggers the error path.
3. Verify the error is raised/returned as the output contract specifies.
4. Check that no error is silently swallowed.
5. Record any suppression as a Silent Failure defect.

### Session Template: Clean Environment Test

**Goal:** Verify the code doesn't depend on unspecified global state.

**Steps:**
1. Run the code in a clean environment: no env vars, default config, fresh state.
2. If the code fails, determine what missing dependency caused the failure.
3. Check whether that dependency was specified in the task context.
4. If not specified, record as an Implicit Assumption defect.

### Session Template: Concurrency Probe

**Goal:** Find state management and race condition defects.

**Steps:**
1. Identify all shared mutable state (global variables, class attributes, database rows).
2. Run concurrent operations that read and write the shared state.
3. Look for: race conditions, inconsistent state, deadlocks.
4. Interrupt long-running operations and verify the system recovers.
5. Record any concurrency defect.

### Session Template: Perturbation Test

**Goal:** Detect over-fitting to specific test inputs.

**Steps:**
1. Take the test inputs that the implementation passes.
2. Create perturbed versions: slightly different values in the same equivalence partition.
3. Run the implementation with the perturbed inputs.
4. If the implementation fails, it has over-fit — record as an Over-Fitting defect.
5. If it passes, the implementation generalizes correctly.

## Regression-Specific LLM Concerns

LLM fixes introduce new bugs at a higher rate than human fixes because the LLM optimizes for the reported symptom, not the root cause.

**Regression testing rules for LLM fixes:**
1. **Always run the full suite** — not just tests related to the fix. The fix may have side effects in unrelated areas.
2. **Check edge cases near the fix** — the fix may handle the exact failing input but miss adjacent edge cases.
3. **Verify the fix didn't suppress the error** — some LLM fixes "resolve" a failure by catching the exception and returning a default, rather than fixing the root cause.
4. **Re-run exploratory QA in the fix area** — the fix may introduce new behavior that wasn't tested before.

## Standards and Research References

- Liu, F. et al. (2024). "Exploring and Evaluating Hallucinations in LLM-Powered Code Generation." arXiv:2404.00971.
- Tambon, C. et al. (2024). "How to Evaluate and Verify the Correctness of LLM-Generated Code?"
- Lee, Y. et al. (2025). "Hallucination by Code Generation LLMs: Taxonomy, Benchmarks, Mitigation, and Challenges." arXiv:2504.20799.
- ISTQB CTFL v4.0 Syllabus, §4.4 — Experience-based test techniques (exploratory testing)
- ISO/IEC 25010 — Quality model (reliability, maintainability characteristics relevant to LLM code)
