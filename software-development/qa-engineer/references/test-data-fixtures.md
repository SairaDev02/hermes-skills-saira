# Test Data and Fixtures Reference

The methodology for designing test data, edge-case datasets, and mock/stub configurations. This reference supports Task 4 of the QA Engineer process.

## Test Data Design Principles

Test data must be designed with the same rigor as test cases — it is the input that triggers the behavior the test verifies. Poorly designed test data passes tests that miss real defects.

### Data Design Process

1. **Map inputs to equivalence partitions** — for each input parameter, identify valid and invalid partitions (see `references/test-design-techniques.md`).
2. **Select representative values** — one value per partition for EP; boundary values for BVA.
3. **Add edge-case values** — values from the edge-case taxonomy below.
4. **Specify expected outputs** — for each input combination, define the exact expected output.
5. **Design fixtures** — define setup/teardown procedures for each test suite.

## Edge-Case Taxonomy

A comprehensive edge-case dataset must cover every category below. Each category represents a class of inputs that commonly triggers defects, especially in LLM-generated code.

### Empty and Null Inputs

| Category | Test Values | Why It Matters |
|----------|-------------|----------------|
| Empty string | `""` | String operations may not handle zero-length |
| Empty list/array | `[]` | Iteration and indexing may fail on empty collections |
| Empty dict/map | `{}` | Key lookups and iteration may behave unexpectedly |
| None/null | `None`, `null`, `nil` | Null dereference is the most common runtime error |
| Empty file | 0 bytes | File readers may hang or return undefined |
| Empty JSON | `{}` or `[]` | Deserialization may produce unexpected types |

### Boundary Values

| Category | Test Values | Why It Matters |
|----------|-------------|----------------|
| Zero | `0`, `0.0`, `-0.0` | Division by zero, sign handling |
| Negative | `-1`, `-MAX` | Off-by-one, unsigned conversion |
| Max integer | `2147483647` (32-bit), `9223372036854775807` (64-bit) | Integer overflow |
| Min integer | `-2147483648`, `-9223372036854775808` | Underflow |
| Max-length string | String of `MAX_LEN` characters | Buffer truncation, validation bypass |
| Over-length string | String of `MAX_LEN + 1` characters | Boundary validation |
| First element | Index `0` | Zero-based indexing errors |
| Last element | Index `len - 1` | Off-by-one errors |

### Type and Format Edge Cases

| Category | Test Values | Why It Matters |
|----------|-------------|----------------|
| Wrong type | String where int expected | Type coercion, unexpected casting |
| Boolean as int | `True` as `1`, `False` as `0` | Truthy/falsy confusion |
| Floating point | `0.1 + 0.2` (≠ `0.3`) | Floating point precision |
| NaN | `float('nan')` | Comparison failures |
| Infinity | `float('inf')`, `float('-inf')` | Arithmetic edge cases |
| Date/time boundary | Midnight UTC, leap second, DST transition | Timezone and calendar errors |
| Unicode | Emojis, combining characters, RTL text, zero-width | Encoding and display issues |
| Special characters | `'`, `"`, `\`, `;`, `--`, `<script>` | SQL injection, XSS, path traversal |

### Concurrency and State

| Category | Test Scenario | Why It Matters |
|----------|---------------|----------------|
| Concurrent access | Multiple threads/processes accessing same resource | Race conditions, deadlocks |
| Timeout behavior | Operation that exceeds timeout limit | Hanging, resource leaks |
| Interrupted operation | Operation killed mid-execution | Partial state, corrupted data |
| State transition during operation | State changes while a long operation runs | Inconsistent state |
| Resource exhaustion | Out of memory, disk full, connection pool exhausted | Graceful degradation |

### LLM-Specific Edge Cases

| Category | Test Scenario | Why It Matters |
|----------|---------------|----------------|
| API signature mismatch | Call with parameters not in the output contract | LLMs may hallucinate parameters |
| Nonexistent library function | Call a function that doesn't exist in the library | LLMs invent plausible-looking APIs |
| Wrong return type | Function returns a type different from the contract | LLMs may return a similar but wrong type |
| Implicit assumptions | Code assumes a global state or environment variable | LLMs may assume context not provided |
| Silent failure | Function returns a default instead of raising an error | LLMs may suppress errors for "clean" output |

## Mock and Stub Design

### Mocks vs Stubs vs Fakes vs Spies

| Test Double | Purpose | Behavior |
|-------------|---------|----------|
| **Stub** | Provide canned responses | Returns predefined values; no interaction verification |
| **Mock** | Verify interactions | Pre-programmed with expectations; verifies the SUT called it correctly |
| **Fake** | Simplified working implementation | Has working logic but cut corners (e.g., in-memory database) |
| **Spy** | Record interactions | Wraps real object; records calls for later assertion |

### When to Use Each

- **Stub:** When the test needs the dependency to return specific values but doesn't care how it was called.
- **Mock:** When the test must verify the SUT called the dependency with specific parameters, in a specific order, or a specific number of times.
- **Fake:** When the test needs a working implementation that's faster or simpler than the real one (e.g., in-memory cache instead of Redis).
- **Spy:** When the test needs to verify interactions with a real object without replacing it.

### Mock Design Principles

1. **Mock at the boundary** — mock external services (databases, APIs, file systems), not internal modules. Mocking internal modules couples tests to implementation details.
2. **One mock per dependency** — each external dependency gets exactly one mock. Don't create multiple mocks for the same dependency across tests — use a shared fixture.
3. **Verify, don't assert** — use mocks to verify interactions (the SUT called the dependency correctly), not to assert on the mock's internal state.
4. **Reset between tests** — mocks that record interactions must be reset between tests to prevent cross-test contamination.
5. **Don't mock the SUT** — never mock the system under test. Mock its dependencies, not itself.

## Fixture Design

### Setup and Teardown

Every test suite needs setup and teardown procedures that run before and after each test (or the entire suite).

| Fixture Scope | When to Use |
|---------------|-------------|
| Per-test (setUp/tearDown) | Database seeding, temp file creation — anything that must be clean for each test |
| Per-class (setUpClass) | Expensive resources shared across tests in a class (e.g., test server startup) |
| Per-session (session fixture) | Very expensive resources shared across the entire test run (e.g., database container) |

### Fixture Design Principles

1. **Independent fixtures** — each test's fixture must not depend on another test's fixture state.
2. **Idempotent setup** — running setup twice must produce the same state as running it once.
3. **Complete teardown** — teardown must clean up everything setup created, including temp files and database rows.
4. **Deterministic data** — fixtures must use fixed seed values, not random data, so test results are reproducible.
5. **Isolated environment** — fixtures must not touch production data, production databases, or shared state.

## Test Data Management

### Synthetic Data

- Always use synthetic data in tests — never real user data or production data.
- Synthetic data must be representative: cover the same partitions and boundaries as real data.
- For PII-sensitive systems, synthetic data must not accidentally match real PII patterns.

### Data Generation Tools

| Language | Tool | Purpose |
|----------|------|---------|
| Python | `faker` | Generate realistic synthetic data (names, addresses, etc.) |
| Python | `factory_boy` | Define factories for model objects with defaults |
| JavaScript | `@faker-js/faker` | Synthetic data generation |
| Any | `pytest fixtures` / `jest beforeEach` | Test-scoped data setup |

## Standards References

- ISTQB CTFL v4.0 Syllabus, §4.2.1 (Equivalence Partitioning), §4.2.2 (Boundary Value Analysis)
- ISO/IEC/IEEE 29119-3:2021 — Test documentation (test data requirements)
- ISO/IEC 25010 — Quality model (reliability, robustness characteristics)
