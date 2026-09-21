# Complexity Metrics Reference

The methodology for assessing code complexity and maintainability using McCabe's cyclomatic complexity (1976), Sonar's cognitive complexity (2018), and the SEI maintainability risk categories. Supports Task 6 of the Code Reviewer process.

## Cyclomatic Complexity (McCabe, 1976)

Thomas J. McCabe introduced cyclomatic complexity in his 1976 paper "A Complexity Measure." It quantifies the number of linearly independent paths through a program's control flow graph.

### Formula

For a single function with one entry and one exit:

```
M = E - N + 2P
```

Where:
- E = number of edges in the control flow graph
- N = number of nodes
- P = number of connected components (1 for a single function)

In practice, the formula simplifies to:

```
M = 1 + (number of decision points)
```

Decision points: `if`, `else if`, `for`, `while`, `do while`, `case` (excluding `default`), `catch`, ternary operator (`?:`), and short-circuit operators (`&&`, `||`).

### SEI Risk Categories

The Software Engineering Institute established risk categories based on cyclomatic complexity, widely adopted by tools (e.g., Klocwork, radon):

| Cyclomatic Complexity | Risk Level | Action |
|-----------------------|------------|--------|
| 1–10 | Simple module, low risk | No action required |
| 11–20 | More complex, moderate risk | Review for simplification |
| 21–50 | Complex, high risk | Strongly consider refactoring |
| 51+ | Untestable, very high risk | Must refactor — reject in review |

McCabe's original recommendation was to limit cyclomatic complexity to 10. NIST's Structured Testing methodology confirmed this threshold with "substantial corroborating evidence," while noting that some circumstances justify going as high as 15 with a written explanation.

### Tools

| Language | Tool | Command |
|----------|------|---------|
| Python | radon | `radon cc <file> -a` |
| JavaScript | complexity-report | `complexity-report <file>` |
| Java | PMD | `pmd <file> -R rulesets/java/cyclomatic_complexity.xml` |
| Go | gocyclo | `gocyclo <file>` |
| C/C++ | lizard | `lizard <file>` |

### Manual Counting (When No Tool Is Available)

Count decision points per function:
1. Start with 1 (the base path).
2. Add 1 for each `if`, `else if`, `for`, `while`, `do while`, `case` (not `default`), `catch`, ternary `?:`.
3. Add 1 for each `&&` and `||` (short-circuit operators).
4. The total is the cyclomatic complexity.

## Cognitive Complexity (Sonar, 2018)

Sonar introduced cognitive complexity in 2018 to address cyclomatic complexity's shortcomings as a maintainability signal. While cyclomatic complexity excels at measuring testability (minimum test cases needed), it is unsatisfactory at measuring understandability because methods with equal cyclomatic complexity do not necessarily present equal difficulty to the maintainer.

### Three Rules

1. **Ignore** structures that allow multiple statements to be readably shorthanded into one (e.g., a switch with many cases is one increment, not twelve).
2. **Increment** by one for each break in the linear flow of the code (if, for, while, catch, ternary, sequences of binary logical operators, recursion, goto/label jumps).
3. **Increment again** when flow-breaking control structures are nested (nesting penalty).

### What Makes Cognitive Complexity Different

The key difference from cyclomatic complexity is the **nesting penalty**. Cyclomatic complexity treats one `if` statement the same whether it's at the top level or buried three levels deep. Cognitive complexity penalizes the deeper one because high complexity in nested code taxes working memory and increases mental effort.

```
// Cyclomatic complexity: 3  |  Cognitive complexity: 3
function top_level(a, b, c) {
    if (a) {           // +1
        if (b) {       // +2 (nesting +1, structural +1)
            if (c) {   // +3 (nesting +2, structural +1)
                // ...
            }
        }
    }
}
```

### Cognitive Complexity Increment Rules

| Structure | Increment | Nesting? |
|-----------|-----------|----------|
| `if`, `else if`, `else` | +1 structural | Yes (increments nesting level) |
| Ternary `?:` | +1 structural | Yes |
| `switch` (all cases combined) | +1 structural | Yes |
| `for`, `foreach` | +1 structural | Yes |
| `while`, `do while` | +1 structural | Yes |
| `catch` | +1 structural | Yes |
| Binary logical operator sequences (`&&`, `\|\|`) | +1 fundamental per sequence | No |
| Recursion (direct or indirect) | +1 fundamental | No |
| `goto LABEL`, `break LABEL`, `continue LABEL` | +1 fundamental | No |
| `try`, `finally` | ignored | No |
| `break` (unlabeled), `continue` (unlabeled), early `return` | ignored | No |

### Assessment Heuristic for Review

When no cognitive complexity tool is available, use these manual heuristics:

- **Nesting depth > 3 levels** — flag for flattening. Deep nesting taxes working memory.
- **Mixed boolean operators without parentheses** — flag for readability. `a && b \|\| c && d` is harder to parse than `(a && b) \|\| (c && d)`.
- **Switch with > 10 cases** — consider whether a lookup table or polymorphism would be clearer.
- **Recursive calls** — flag for complexity; recursion represents a "meta-loop" that many developers find difficult to understand.
- **Long method chains** — flag for readability; chain depth > 3 can be hard to follow.

## Function Length

| Length (excl. comments/blank lines) | Assessment | Action |
|-------------------------------------|------------|--------|
| ≤ 20 lines | Good | No action |
| 21–50 lines | Acceptable | Review for extraction opportunities |
| 51–100 lines | Long | Flag for extraction; likely mixing responsibilities |
| > 100 lines | Very long | Flag as critical; must be broken into smaller functions |

## Naming Clarity Assessment

Check every public identifier (function, class, variable) in the changed code:

| Issue | Examples | Action |
|-------|----------|--------|
| Vague names | `data`, `process`, `handle`, `tmp`, `val`, `x` | Flag — name should describe what, not that |
| Misleading names | `getUser` that also creates a user | Flag — name must match behavior |
| Inconsistent casing | `getUserData` and `get_user_data` in same module | Flag — follow project convention |
| Abbreviations | `calcAvg` instead of `calculateAverage` | Flag unless abbreviation is domain-standard |
| Boolean naming | `flag` instead of `isValid` | Flag — booleans should read as questions |

## DRY (Don't Repeat Yourself) Assessment

Identify duplicated logic:

1. **Exact duplication** — identical code blocks in multiple locations. Flag both locations.
2. **Near-identical** — code blocks that differ only in variable names or constants. Flag for extraction into a parameterized function.
3. **Structural duplication** — different code that follows the same pattern (e.g., same try/catch/finally structure with different operations). Flag for pattern extraction.
4. **Copy-paste with modification** — code that was clearly copied and slightly modified. Flag for extraction and parameterization.

### DRY Threshold

- **3 or more instances** of duplicated logic (exact or near-identical) = must extract.
- **2 instances** = review for extraction; extract if the duplication is > 5 lines.
