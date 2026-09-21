# Test Case Template

> One entry per test case. Each test case must trace to a requirement ID
> via the RTM and have a designated ISTQB test design technique.
> This template defines the structure; fill in all fields.

---

## TC-<ID>: <Test Case Title>

### Metadata

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-<ID> |
| **Requirement ID** | <FR-XXX or NFR-XXX from SRS> |
| **Output Contract** | <Task ID / contract ID being tested> |
| **Test Level** | Unit / Integration / System |
| **Test Type** | Functional / Non-functional / Regression |
| **Design Technique** | EP / BVA / Decision Table / State Transition / Error Guessing / Exploratory |
| **Polarity** | Positive / Negative / Boundary |
| **Priority** | P1 / P2 / P3 |

### Preconditions

<Conditions that must be true before the test runs — e.g., "database is seeded with test user", "mock API is configured to return 200 OK", "test environment is clean".>

### Test Steps

1. <Step 1 — specific action, e.g., "Call `processPayment(order)` with order.total = 100.00">
2. <Step 2 — e.g., "Verify the return value">
3. <Step 3 — if needed>

### Test Data

| Parameter | Value | Partition |
|-----------|-------|-----------|
| <param name> | <test value> | <valid/invalid partition name> |

### Expected Result

<Precise expected output — return value, side effect, state change, or exception. Cite the requirement ID.>

### Expected Error (for negative tests)

<For negative tests: the error type, error message, or failure mode expected.>

### Postconditions

<State the system should be in after the test — e.g., "database transaction rolled back", "no side effects persisted".>
