# Task Sizing Reference

The methodology for estimating task complexity and ensuring each task fits within a single LLM context window. This is Task 9 of the task engineering process.

## The Sizing Problem

An LLM coding agent has a fixed context window. Everything it needs — instructions, context, code it reads, code it writes, tool outputs — competes for that window. If the total exceeds the window, the model either truncates (losing information silently) or the harness triggers compaction (summarizing prior context, which loses detail).

Research confirms that output quality degrades as context fills. The principle: "Results will tend to be better when the context window is 'less full'" (OpenAI, 2026). Anthropic's context rot research (2025) shows measurable attention degradation as token count grows.

## The Sizing Formula

For each task, estimate:

```
Total Context = Input Context + Output Contract + Constraints + Expected Output
```

| Component | Source | Estimation Method |
|-----------|--------|------------------|
| Input Context | Task 4 (context curation) | Token estimation from `references/context-curation.md` |
| Output Contract | Task 5 | Count signatures + behavior descriptions; ~1.3 tokens/word |
| Constraints | Task 8 | Count constraint text; ~1.3 tokens/word |
| Expected Output | Estimated from output contract | Count expected files × estimated lines × ~12 tokens/line |

### Expected Output Estimation

Estimate the code the task will produce:

| Task Type | Estimated Output Lines | Notes |
|-----------|-----------------------|-------|
| Simple CRUD endpoint | 50-150 lines | Handler + validation + model |
| Module with 3-5 functions | 200-500 lines | Implementation + types |
| Integration/adapter | 100-300 lines | Glue code + mapping |
| Complex algorithm | 300-800 lines | Logic + edge cases |
| Test suite | 100-400 lines | Tests + fixtures |
| Full module (moderate) | 500-1500 lines | All functions + types |
| Full module (complex) | 1500-3000 lines | Decompose if estimated here |

Multiply estimated lines by ~12 tokens/line for the token estimate.

## Sizing Thresholds

### Pass Criteria

| Check | Threshold | Action if Exceeded |
|-------|-----------|-------------------|
| Input context ≤ 40% of window | 51K (128K window) / 80K (200K window) | Trim context (Task 4) or decompose (Task 2) |
| Total context ≤ 60% of window | 77K (128K window) / 120K (200K window) | Decompose into sub-tasks (return to Task 2) |
| Total context in smart zone | < 100K tokens | Flag for extra scrutiny if exceeded |

### Context Window Reference (2026)

| Model | Context Window | 40% Budget | 60% Budget | Smart Zone |
|-------|---------------|-------------|-------------|------------|
| Claude Sonnet 4.5 | 200K | 80K | 120K | < 100K |
| GPT-5.4 | 272K | 109K | 163K | < 100K |
| GPT-5.4 long-context | 1.05M | 420K | 630K | < 100K |
| Codex (o3-based) | 192K | 77K | 115K | < 100K |
| o4-mini | 200K | 80K | 120K | < 100K |

Note: The smart zone (~100K) is consistent across models because it derives from the attention mechanism, not the window size. Larger windows allow more total work but don't eliminate context rot.

## Decomposition Axes

When a task fails the sizing check, decompose along one of four axes (Codex, 2026):

### 1. By Layer

Split a full-stack task into frontend, API, and database sub-tasks. Each layer has distinct tooling, test suites, and file patterns.

**Example:** "Implement user registration" →
- Sub-task A: Database schema + migration for users table
- Sub-task B: API endpoint + validation logic
- Sub-task C: Frontend form + API integration

### 2. By Feature Slice (Vertical)

Split by user-facing behavior. Each slice cuts across layers but implements one complete feature.

**Example:** "Implement the search feature" →
- Sub-task A: Text search with basic filtering
- Sub-task B: Faceted search with advanced filtering
- Sub-task C: Search results pagination and sorting

### 3. By Phase

Split by implementation phase: explore, implement, test, document. Each phase can run as a separate task or milestone.

**Example:** "Implement the payment module" →
- Sub-task A: Explore existing payment patterns and define approach
- Sub-task B: Implement core payment logic
- Sub-task C: Write test suite against output contract
- Sub-task D: Write integration documentation

### 4. By Service

In microservice architectures, split by service boundary. Each service is a natural decomposition point.

**Example:** "Implement order processing" →
- Sub-task A: Order service — create order, validate inventory
- Sub-task B: Payment service — process payment, handle refunds
- Sub-task C: Notification service — send order confirmation

## Task-Sizing Heuristic

Not every unit of work should be a separate task. Decomposing too aggressively introduces coordination overhead. Use this heuristic (Codex, 2026):

| Factor | Keep Together | Split Apart |
|--------|-------------|-------------|
| File scope | Changes touch 1-3 tightly coupled files | Changes span 5+ loosely related files |
| Verification | Single test suite validates the change | Multiple independent test suites needed |
| Context dependency | Each step depends on the previous step's output | Steps are independent and parallelizable |
| Token budget | Estimated context stays under ~100K tokens | Context likely exceeds 150K tokens |

**Rule of thumb:** If you would review the change as a single pull request, it is probably a single task. If it would naturally split into multiple PRs, split the agent work too.

## The "Done When" Test

Every task must have a concrete, programmatically verifiable acceptance criterion — a "done when" clause. If you cannot write one, the task is too vague to dispatch (Codex, 2026):

```markdown
## Task: Add rate-limiting middleware to /api/v2/*

**Goal:** Implement sliding-window rate limiting (100 req/min per API key).
**Context:** Express 5.x, Redis for state, existing auth middleware in src/middleware/auth.ts.
**Constraints:** No new npm dependencies beyond ioredis (already installed).
**Done when:** `npm test` passes, new tests cover 429 responses, `npm run lint` clean.
```

If "done when" cannot be specified concretely, use plan mode to interview the user first — the task is not ready for dispatch.

## Post-Deccomposition Re-validation

When a task is decomposed, the new sub-tasks must re-run Tasks 3–8:

1. **Scope (Task 3):** Each sub-task needs its own inclusion/exclusion scope.
2. **Context (Task 4):** Each sub-task gets a trimmed context — the parent's context split along the decomposition axis.
3. **Output contract (Task 5):** Each sub-task gets its own output contract — the parent's contract split by responsibility.
4. **Acceptance criteria (Task 6):** Each sub-task gets criteria derived from the parent's requirements.
5. **Dependencies (Task 7):** Sub-tasks from the same parent may depend on each other — record these edges.
6. **Constraints (Task 8):** Each sub-task inherits the parent's constraints plus any sub-task-specific additions.
7. **Sizing (Task 9):** Re-run the sizing check on each sub-task — if still too large, decompose again.
