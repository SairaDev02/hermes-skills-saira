# Edge Case Analysis Reference

The methodology for identifying inputs, states, and code paths that the implementation doesn't handle — gaps the Tester's spec-driven tests may not have covered. The Reviewer and Tester have complementary blind spots: the Tester tests the spec; the Reviewer reads the code and finds what the spec *missed*. Supports Task 7 of the Code Reviewer process.

## Edge Case Taxonomy

### 1. Input Boundary Cases

| Category | What to Check | Common LLM Failure |
|----------|---------------|---------------------|
| Empty inputs | Empty string `""`, empty list `[]`, empty dict `{}`, empty file | No guard clause; function proceeds and crashes on empty |
| Null/None/nil | `None`, `null`, `undefined`, `nil` passed where object expected | Missing null check; dereference error |
| Zero / negative | `0`, `-1`, negative values for numeric parameters | Off-by-one in boundary; division by zero |
| Max values | `MAX_INT`, `MAX_FLOAT`, `2^31 - 1`, `2^63 - 1` | Integer overflow; silent truncation |
| Max-length strings | Strings at or beyond configured maximum length | No length validation; buffer/storage overflow |
| Unicode / special chars | Emoji, zero-width chars, RTL markers, null bytes `\x00`, control characters | Encoding mismatch; injection via special chars |
| Type mismatch | String passed where int expected, float where int expected | No type coercion/guard; unexpected behavior |
| Malformed input | Invalid JSON, broken XML, non-UTF-8 bytes | Parser crashes instead of returning error |

### 2. State and Concurrency Cases

| Category | What to Check | Common LLM Failure |
|----------|---------------|---------------------|
| Race conditions | Shared mutable state accessed concurrently without locks | No mutex/lock; data corruption under concurrency |
| Stale state | Cached values not invalidated after update | Cache returns stale data; user sees old state |
| Missing cleanup | Resources (files, connections, memory) not released on error path | Resource leak on exception; file descriptor exhaustion |
| State transitions | Invalid state transitions not rejected | FSM accepts illegal transition; inconsistent state |
| Initialization order | Module depends on state not yet initialized | Null reference; undefined behavior |
| Re-entrancy | Function called again while still executing from previous call | Stack overflow; corrupted state |

### 3. Error Path Cases

| Category | What to Check | Common LLM Failure |
|----------|---------------|---------------------|
| Uncaught exceptions | Exception thrown but not caught in the calling code | Crash; unhandled promise rejection |
| Missing error return | Function returns error code but caller doesn't check | Silent failure; wrong result propagated |
| Partial failure | Multi-step operation fails midway — is state consistent? | Half-written data; inconsistent database state |
| Timeout behavior | Network/IO operation hangs — is there a timeout? | Infinite hang; no timeout configured |
| Retry without backoff | Failed operation retried immediately and indefinitely | Retry storm; cascading failure |
| Error message leakage | Error response includes stack traces or internal details | Information disclosure to attacker |

### 4. Resource Cases

| Category | What to Check | Common LLM Failure |
|----------|---------------|---------------------|
| Memory exhaustion | Large input processed without streaming/batching | OOM kill |
| Disk space | File operations don't check available disk space | Write fails silently; data loss |
| Connection pool | Database/API connections not returned to pool | Pool exhaustion; service unavailable |
| File descriptor | Files opened but not closed on all paths (including error paths) | FD exhaustion; EMFILE |
| Thread pool | Async tasks submitted without bound | Thread pool starvation |

### 5. Security-Adjacent Edge Cases

| Category | What to Check | Common LLM Failure |
|----------|---------------|---------------------|
| Input sanitization gaps | User input used in SQL, HTML, shell, or file path without validation | Injection vulnerability |
| Auth bypass edge cases | Empty user ID, null session, expired token with grace period | Auth bypass |
| Privilege escalation | User can access resource by ID guessing (IDOR) | Missing ownership check |
| Rate limiting absence | Sensitive endpoint has no rate limit | Brute force; enumeration |

## Identification Methodology

### Step 1: Trace Control Flow

For each function in the changed code:

1. **Map all branches** — identify every `if`, `else`, `switch`, `try/catch`, loop. Each branch is a potential edge case.
2. **Identify unhandled branches** — branches that have no error handling or no default case. A missing `else` or `default` is an unhandled state.
3. **Check guard clauses** — verify each function has guard clauses for: null/None inputs, empty collections, invalid types, out-of-range values.

### Step 2: Trace Data Flow

For each input in the changed code:

1. **Trace from source to sink** — where does user input enter, and where is it used? Every sink (SQL query, HTML render, shell command, file path, network request) is a potential vulnerability point.
2. **Check validation at boundaries** — is input validated at the point of entry (API handler, CLI argument parser, file reader)?
3. **Check sanitization at sinks** — is input sanitized before being used in a dangerous sink?

### Step 3: Trace Error Paths

For each error-handling block in the changed code:

1. **Verify catch completeness** — does the `catch` block handle all expected exception types, or only a subset?
2. **Verify cleanup on all paths** — on both success and error paths, are resources properly released?
3. **Verify error propagation** — does the error propagate correctly to the caller, or is it silently swallowed?
4. **Verify error information** — does the error response leak internal details (stack traces, SQL queries, file paths)?

### Step 4: Cross-Reference with Test Results

For each edge case gap found:

1. **Check if a test covers it** — search the test suite for tests that exercise this input/state.
2. **Classify coverage** — "covered by tests" or "uncovered — feed back to Tester."
3. **Recommend new test cases** — for uncovered gaps, describe the test case the Tester should add: input, expected behavior, and why it matters.

## Edge Case Finding Documentation

For each edge case finding, document:

| Field | Description |
|-------|-------------|
| Code Location | File path and line number |
| Category | Input boundary / State / Error path / Resource / Security-adjacent |
| Unhandled Input/State | The specific input or state that is not handled |
| Potential Impact | What happens if this input/state occurs (crash, data corruption, security vulnerability, silent failure) |
| Test Coverage | Covered by tests / Uncovered |
| Recommended Test Case | If uncovered, the test case the Tester should add |
| Severity | Critical / Warning / Suggestion |

### Severity Assignment for Edge Cases

| Severity | Condition | Example |
|----------|-----------|---------|
| Critical | Unhandled input can cause data loss, security breach, or system crash | Null dereference on user input causes crash; missing authz allows IDOR |
| Warning | Unhandled input causes degraded behavior or silent failure | Missing empty-list guard returns wrong result; no timeout on network call |
| Suggestion | Unhandled input is unlikely but possible; defensive programming recommended | No max-length check on string input; no rate limiting on non-sensitive endpoint |
