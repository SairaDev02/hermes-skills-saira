# Test Implementation Specification Template

> One entry per test implementation. Each entry specifies what the
> coding harness (Pi) should implement as executable test code.
> Use pseudocode for test logic — do not write executable code.
> Cite the test case ID from Task 2 and the test specification from Task 3.

---

## TI-<ID>: <Test Implementation Title>

### Metadata

| Field | Value |
|-------|-------|
| **Implementation ID** | TI-<ID> |
| **Test Case ID** | TC-<ID from Task 2> |
| **Test Level** | Unit / Integration |
| **Test Framework** | pytest / jest / go test / JUnit / <other> |
| **Target File** | <path/to/test_file.ext> |
| **Target Function** | <test_function_name> |

### Test Function Signature

```
<function_name>(<parameters>) -> <return_type>
```

### Arrange Block

```
# Pseudocode — setup for this test
<describe preconditions, fixture setup, mock/stub configuration, test data initialization>
<reference fixture IDs from Task 4 if applicable>
```

### Act Block

```
# Pseudocode — the action under test
<describe the function call or operation being tested>
<include exact input values from Task 4 test data>
```

### Assert Block

```
# Pseudocode — assertions to verify
<list each assertion: what to assert, expected value, comparison method>
<example: assert result.status == "success">
<example: assert mock_api.called_with(expected_payload)>
<example: assert raises(ExpectedError) when input is None>
```

### RED Phase Expectation

- **Expected result without implementation:** Test fails or errors with <specific error type/message>
- **Reason:** <why this test should fail when no implementation exists — e.g., "function does not exist", "assertion fails on default return value">

### Test Quality Checks

- [ ] Independent — does not depend on another test's execution order
- [ ] Single assertion focus — tests one behavior
- [ ] Descriptive name — name describes the behavior being tested
