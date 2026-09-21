# Output Contracts Reference

The methodology for defining output contracts for each task. This is Task 5 of the task engineering process.

## Why Output Contracts Matter

The output contract is what the Tester uses to write tests *before* implementation exists (TDD RED phase). It's also what the Code Reviewer checks against. If the output contract is vague, the tests will be vague, and the review will be subjective.

An output contract must be precise enough that:
1. A tester can write tests against it without seeing the implementation.
2. A reviewer can verify the implementation matches it.
3. The LLM implementing the task knows exactly what to produce.

## Output Contract Structure

Each task's output contract field has four sections:

### 1. Public API

List every public function, method, class, and type the task must produce:

```markdown
### Output Contract: Public API

#### Function: processPayment

```typescript
function processPayment(
  order: Order,
  paymentMethod: PaymentMethod
): Promise<PaymentResult>
```

**Parameters:**
- `order: Order` — the order to process (see data model below)
- `paymentMethod: PaymentMethod` — the payment method to use

**Returns:** `Promise<PaymentResult>` — resolves with the payment result, rejects on error

#### Type: PaymentResult

```typescript
interface PaymentResult {
  transactionId: string;
  status: 'success' | 'failed' | 'pending';
  processedAt: string; // ISO 8601
  amount: number;
  currency: string;
  error?: PaymentError;
}
```

#### Type: PaymentError

```typescript
interface PaymentError {
  code: string;        // e.g., 'CARD_DECLINED', 'INSUFFICIENT_FUNDS'
  message: string;     // human-readable
  retryable: boolean;
}
```
```

### 2. Behavior Description

For each function, describe the expected behavior — normal path, error paths, side effects:

```markdown
### Output Contract: Behavior

#### processPayment behavior:

**Normal path:**
1. Validate the order has items and a total > 0.
2. Validate the payment method has valid details.
3. Call the payment gateway (via PaymentGateway interface, IFC-009).
4. On success: return PaymentResult with status 'success' and transaction ID.
5. On failure: return PaymentResult with status 'failed' and error details.

**Error paths:**
- Invalid order (no items, total ≤ 0): throw ValidationError with code 'INVALID_ORDER'.
- Invalid payment method: throw ValidationError with code 'INVALID_PAYMENT_METHOD'.
- Payment gateway timeout: return PaymentResult with status 'pending' and error.code 'GATEWAY_TIMEOUT', retryable: true.
- Payment gateway rejects: return PaymentResult with status 'failed' with the gateway's error code.

**Side effects:**
- Writes a transaction record to the database (via TransactionRepository, IFC-010).
- Emits a 'payment.processed' event (via EventBus, IFC-011).
- Does NOT send notifications (that's the NotificationService's job, triggered by the event).
```

### 3. File Structure

List every file the task must create or modify, with expected content:

```markdown
### Output Contract: File Structure

**Files to create:**
- `src/modules/payment/processor.ts` — processPayment function, PaymentResult/PaymentError types
- `src/modules/payment/validator.ts` — validateOrder, validatePaymentMethod functions (private)
- `src/modules/payment/types.ts` — shared type definitions (Order, PaymentMethod, PaymentResult, PaymentError)
- `src/modules/payment/index.ts` — public exports (processPayment, types)

**Files to modify:**
- `src/routes/api.ts` — add POST /api/v1/payments endpoint that calls processPayment
```

### 4. Integration Points

Describe how this task's output connects to other modules:

```markdown
### Output Contract: Integration Points

- **Implements:** IFC-009 (Payment Processing Interface) — provides processPayment
- **Consumes:** IFC-010 (Transaction Repository) — persists transaction records
- **Consumes:** IFC-011 (Event Bus) — emits 'payment.processed' event
- **Called by:** Order Service (TASK-004) — when order status transitions to 'pending_payment'
- **Tested by:** Test suite for IFC-009 (written by Tester role)
```

## Output Contract Quality Checks

### Type Completeness
Every function parameter and return type must have a concrete type definition — no `any`, no `object`, no `unknown`. If a type is complex, define it as an interface/type and include it in the contract.

### Behavior Coverage
For each function, the behavior description must cover:
- Normal path (happy path)
- Every error path (validation errors, runtime errors, timeout)
- Side effects (database writes, event emissions, state changes)
- Explicit non-effects ("does NOT do X" for common misconceptions)

### File Completeness
Every file in the output contract's file structure must map to a file in the task's inclusion scope (Task 3). No surprise files.

### Interface Alignment
Every integration point must reference an existing interface contract from the architecture document. If the contract doesn't exist, the task cannot be completed — flag this for the Architect.

## Common Pitfalls

### The Untyped Return
"Returns the result" — what type? what shape? The tester can't write assertions without a concrete type. Always specify the return type structure.

### The Missing Error Path
Describes only the happy path. The LLM will implement only the happy path and either crash or return undefined on errors. Enumerate every error case.

### The Implicit Side Effect
"Processes the payment" — does it write to the database? Emit an event? Send an email? If side effects aren't documented, the LLM will skip them or add unintended ones.

### The Interface Forward Reference
"Uses the payment gateway" — which interface? IFC-009? A different one? Always reference the specific interface contract ID.
