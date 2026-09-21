# Test Design Techniques Reference

The methodology for deriving test cases from specifications using ISTQB CTFL v4.0 test design techniques. This reference supports Tasks 2 and 3 of the QA Engineer process.

## Overview

ISTQB classifies test techniques into three categories (ISTQB CTFL v4.0, §4):

| Category | Techniques | Basis |
|----------|-----------|-------|
| Black-box (specification-based) | Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, State Transition Testing | Requirements, specifications — no knowledge of internal structure |
| White-box (structure-based) | Statement Testing, Branch Testing | Code structure, control flow, data flow |
| Experience-based | Error Guessing, Exploratory Testing, Checklist-Based Testing | Tester experience, knowledge of common defect types |

## Black-Box Test Techniques

### Equivalence Partitioning (EP)

Divides input data into partitions where all values within a partition should be treated identically by the system. If one value from a partition works correctly, all should; if one fails, all should.

**Procedure:**

1. Identify all input parameters and their domains.
2. Partition each domain into valid and invalid equivalence classes.
3. Partitions must not overlap and must be non-empty.
4. Select one representative value from each partition.
5. Write one test case per partition (including invalid partitions).

**Coverage:** 100% = every identified partition (valid and invalid) is exercised by at least one test case.

**Example:** Input accepts ages 18–65.

| Partition | Representative Value | Valid? |
|-----------|---------------------|--------|
| Age < 18 | 17 | Invalid |
| 18 ≤ Age ≤ 65 | 30 | Valid |
| Age > 65 | 70 | Invalid |

### Boundary Value Analysis (BVA)

Focuses on the boundaries of equivalence partitions because developers are more likely to make errors at boundaries. Typical defects: boundaries misplaced above/below their intended position, or omitted altogether. BVA can only be used for ordered partitions.

**Two-value BVA (standard):** For each boundary, test the boundary value and its closest neighbor in the adjacent partition.

**Three-value BVA (rigorous):** For each boundary, test the boundary value and both its neighbors (inner and outer). Catches off-by-one errors that 2-value BVA misses (e.g., `if (x = 10)` implemented instead of `if (x ≤ 10)` — 2-value BVA tests x=10 and x=11, both pass; 3-value BVA tests x=9, which fails).

**Example:** Input accepts ages 18–65.

| BVA Type | Values to Test |
|----------|---------------|
| 2-value | 17, 18, 65, 66 |
| 3-value | 16, 17, 18, 19, 64, 65, 66, 67 |

### Decision Table Testing

Tests complex business rules where different combinations of conditions result in different outcomes. Each column in the decision table represents a unique combination of conditions (a rule) and the associated actions.

**Procedure:**

1. List all conditions (Boolean or multi-valued).
2. Enumerate all feasible combinations of conditions — each combination is a rule (column).
3. For each rule, specify the actions the system should take.
4. Mark infeasible combinations as N/A.
5. Write one test case per feasible rule.

**Coverage:** 100% = every feasible column (rule) is exercised by at least one test case.

**Notation:**

- `T` = condition is true
- `F` = condition is false
- `–` = condition is irrelevant for this rule
- `N/A` = infeasible combination
- `X` = action should occur
- blank = action should not occur

**Example:** Discount rules for an online store.

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-----------|--------|--------|--------|--------|
| Premium member | T | T | F | F |
| Order > $100 | T | F | T | F |
| **Actions** | | | | |
| 20% discount | X | | | |
| 10% discount | | X | X | |
| No discount | | | | X |

**Note:** With n conditions, rules grow as 2^n. For large tables, use a minimized decision table or risk-based approach to reduce test count.

### State Transition Testing

Models system behavior as states and transitions between them. A transition is initiated by an event, optionally qualified by a guard condition, and may result in an action. Transition syntax: `event [guard condition] / action`.

**Procedure:**

1. Identify all states the system can be in.
2. Identify all events that can trigger transitions.
3. Identify guard conditions that must be true for a transition to occur.
4. Identify actions that occur during transitions.
5. Build a state transition diagram or state table.
6. Write test cases as sequences of events that result in sequences of state changes.

**Coverage criteria (in increasing rigor):**

1. **All states covered** — every state is reached by at least one test.
2. **All valid transitions covered** — every valid transition is exercised by at least one test.
3. **All invalid transitions covered** (negative testing) — every invalid transition (empty cells in the state table) is tested to confirm the system rejects it.

**Example:** ATM session states.

| Current State | Event | Guard | Action | Next State |
|---------------|-------|-------|--------|------------|
| Idle | Insert card | | Display PIN prompt | Card inserted |
| Card inserted | Valid PIN | | Show menu | PIN verified |
| Card inserted | Invalid PIN | Attempts < 3 | Display retry | Card inserted |
| Card inserted | Invalid PIN | Attempts = 3 | Retain card | Card retained |

## White-Box Test Techniques

### Statement Testing and Coverage

Every executable statement in the code should be exercised by at least one test case.

**Coverage:** (statements exercised / total executable statements) × 100%.

**Minimum bar:** 100% statement coverage does NOT guarantee all defects are found — a statement can be executed without its branch being tested.

### Branch Testing and Coverage

Every branch (decision outcome) in the code should be exercised by at least one test case. For each `if`, `while`, `for`, `switch`, both the true and false paths must be tested.

**Coverage:** (branches exercised / total branches) × 100%.

**Key:** Branch coverage is stronger than statement coverage. 100% branch coverage guarantees 100% statement coverage, but not vice versa.

## Experience-Based Test Techniques

### Error Guessing

The tester uses experience to anticipate likely defects and writes tests targeting those areas. Based on knowledge of: common programming errors, typical LLM hallucination patterns, and domain-specific failure modes.

### Exploratory Testing

Time-boxed sessions where the tester simultaneously learns the system, designs tests, and executes them. Guided by a test charter that defines the scope and objectives of the session. See the `dogfood` skill for web application exploratory methodology.

### Checklist-Based Testing

The tester uses a high-level checklist of test conditions to guide testing. The checklist is derived from experience, standards, and known risk areas. Each item on the checklist generates one or more test cases.

## Choosing the Right Technique

| Technique | Best For |
|-----------|---------|
| Equivalence Partitioning | Input validation, data processing |
| Boundary Value Analysis | Numeric ranges, date ranges, string lengths |
| Decision Table Testing | Complex business rules, multi-condition logic |
| State Transition Testing | Workflows, session management, protocol states |
| Statement Coverage | Basic code coverage baseline |
| Branch Coverage | Decision logic coverage |
| Error Guessing | Known problem areas, LLM hallucination patterns |
| Exploratory Testing | New features, limited documentation, integration gaps |
| Checklist-Based Testing | Regression testing, compliance, standard risk areas |

## Combining Techniques

Effective testing combines multiple techniques:

1. Start with equivalence partitioning to identify value domains.
2. Add boundary value analysis for edges of ordered partitions.
3. Use decision table testing for complex business rules.
4. Apply state transition testing for stateful behavior.
5. Measure white-box coverage (statement, branch) to find structural gaps.
6. Supplement with error guessing for known problem areas.
7. Add exploratory testing sessions for integration and state management gaps.

## Standards References

- ISTQB CTFL v4.0 Syllabus, §4.2 (Black-Box), §4.3 (White-Box), §4.4 (Experience-Based)
- ISO/IEC/IEEE 29119-3:2021 — Test documentation
- ISO/IEC 25010 — Quality model (for non-functional test derivation)
