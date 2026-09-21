# EARS: Easy Approach to Requirements Syntax

Reference guide for writing structured natural-language requirements using EARS patterns.
Developed by Alistair Mavin et al. at Rolls-Royce (IEEE RE'09). EARS gently constrains
natural language to reduce ambiguity, vagueness, and incompleteness.

## General Structure

```
WHILE <optional precondition(s)>, WHEN <optional trigger>, the <system name> SHALL <system response>
```

### EARS Ruleset

- Zero or many preconditions
- Zero or one trigger
- Exactly one system name
- One or many system responses
- Clauses always appear in the same temporal order
- Use "shall" for mandatory, "should" for recommended, "may" for optional

## The Five Basic EARS Patterns

### 1. Ubiquitous

No preconditions or trigger. Always active.

```
The <system name> shall <system response>.
```

**Example:**
> The payment gateway shall encrypt all transaction data using AES-256.

### 2. Event-Driven (When)

Triggered by an event.

```
When <trigger>, the <system name> shall <system response>.
```

**Example:**
> When the user submits the registration form, the system shall validate the email address format.

### 3. State-Driven (While)

Active during a state.

```
While <precondition>, the <system name> shall <system response>.
```

**Example:**
> While the database is in maintenance mode, the system shall display a maintenance notification to all users.

### 4. Optional (Where)

Conditional on a feature or mode being present.

```
Where <feature is included>, the <system name> shall <system response>.
```

**Example:**
> Where multi-factor authentication is enabled, the system shall require a time-based one-time password at login.

### 5. Unwanted Behavior (If...Then...Else)

Handles error or exception conditions.

```
If <trigger>, then the <system name> shall <system response>.
```

**Example:**
> If the payment processing service returns an error, then the system shall log the error and display a retry option to the user.

## Combined Patterns

EARS patterns can be combined when a requirement has both preconditions and triggers:

```
While <precondition>, when <trigger>, the <system name> shall <system response>.
```

**Example:**
> While the user is authenticated, when the session timeout threshold is reached, the system shall prompt the user to extend their session.

With optional feature:

```
Where <feature>, while <precondition>, when <trigger>, the <system name> shall <system response>.
```

**Example:**
> Where offline mode is enabled, while the device has no network connectivity, when the user creates a new record, the system shall store the record locally and queue it for synchronization.

With unwanted behavior + precondition:

```
While <precondition>, if <trigger>, then the <system name> shall <system response>.
```

**Example:**
> While the user is in a checkout flow, if the payment authorization fails, then the system shall preserve the cart contents and display the payment error.

## EARS Cardinality (Clause limits)

| Clause | Cardinality |
|--------|-------------|
| Preconditions (While/Where) | Zero or many |
| Trigger (When/If) | Zero or one |
| System name | Exactly one |
| System response (shall...) | One or many |

## When NOT to Use EARS

- **More than three preconditions** — the sentence becomes too long and hard to parse. Use a table, decision tree, or structured prose instead.
- **Non-textual requirements** — some requirements are better expressed as diagrams, formulas, or tables. Don't force everything into text.
- **Non-functional requirements with complex metrics** — e.g., "The system shall achieve 99.95% availability measured as..." may be better as a structured table with columns for metric, threshold, measurement method, and context.
- **Interface specifications** — API contracts, data formats, and protocol specs are better as schema definitions (OpenAPI, Protobuf, JSON Schema).

## Quality Checks After Writing EARS

1. **Active voice** — the system name is the subject performing the action, not the object.
2. **Single obligation** — no "and" or "or" chaining multiple responses into one statement (split into separate requirements).
3. **Verifiable** — the response is observable and can be tested.
4. **No passive voice** — avoid "shall be" constructions that hide who performs the action.
5. **Consistent terminology** — use the same term for the same concept across all requirements.
