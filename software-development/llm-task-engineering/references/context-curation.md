# Context Curation Reference

The methodology for selecting the minimal high-signal input context for each task. This is Task 4 of the task engineering process — the most critical step.

## Why Context Curation Matters

Anthropic's research on effective context engineering (Sep 2025) identifies **context rot**: as the number of tokens in the context window increases, the model's ability to accurately recall and reason over information from that context decreases. This is not a hard cliff but a performance gradient — models remain capable at longer contexts but show reduced precision for information retrieval and long-range reasoning.

The root cause is architectural: LLMs use self-attention where every token attends to every other token, creating n² pairwise relationships for n tokens. As context length grows, the model's ability to capture these relationships gets stretched thin. Models also have less training exposure to very long sequences, meaning fewer specialized parameters for long-range dependencies.

**The guiding principle:** find the smallest possible set of high-signal tokens that maximize the likelihood of the desired outcome. Minimal does not mean short — it means no irrelevant information.

## Context Components Checklist

For each task, determine which of these components are needed:

### Always Required
- **Module responsibility statement** — the one-sentence responsibility from the architecture's Task 3 (~100 words)
- **Relevant SRS requirements** — only the requirement IDs mapped to this task via the RTM, not the entire SRS (~200-2000 words depending on count)
- **Task constraints** — coding conventions and rules specific to this task (~200-500 words)

### Conditionally Required
- **Interface contracts — implementing side** — the contract(s) this task must implement (~500-2000 words per contract)
- **Interface contracts — consuming side** — the contract(s) this task calls as a client, trimmed to just the signatures and data models (~300-1000 words per contract)
- **Cross-cutting concern conventions** — only the conventions relevant to this task (e.g., if the task touches error handling, include the error handling convention; skip logging if the task doesn't log) (~200-500 words per relevant convention)
- **Existing code to extend** — if the task modifies existing code, include the current file contents (trimmed to relevant sections) (~variable)
- **Style guide** — if the project has a style guide, include the relevant sections (~200-500 words)

### Never Include
- Other modules' internal implementations (only their interface contracts)
- The full architecture document (include only relevant sections)
- The full RTM (include only rows for this task's requirements)
- Unrelated ADRs
- Diagrams that don't directly inform this task

## Token Estimation Heuristics

Use these rough conversions for estimating token costs:

| Content Type | Approximate Tokens |
|-------------|-------------------|
| 1 word of English prose | ~1.3 tokens |
| 1 line of code (avg) | ~10-15 tokens |
| 1 line of JSON | ~5-10 tokens |
| 1 Markdown table row | ~15-20 tokens |
| 1 Mermaid diagram (simple) | ~200-500 tokens |
| System prompt overhead | ~500-2000 tokens (model-dependent) |

### Quick estimation method

1. Count words in the assembled context (any word processor or `wc -w`).
2. Multiply by 1.3 for prose, or count code lines and multiply by 12.
3. Add 1000 tokens for formatting/markup overhead.
4. Compare against the budget (see below).

## Context Budget Rules

### The 40/60 Rule

| Budget | Percentage | Purpose |
|--------|-----------|---------|
| Input context | ≤ 40% of context window | Room for output |
| Output (code + tests + docs) | ~60% of context window | Implementation space |

For a 128K-token context window:
- Input context budget: ~51K tokens
- Output budget: ~77K tokens

For a 200K-token context window:
- Input context budget: ~80K tokens
- Output budget: ~120K tokens

### The Smart Zone

Research from Codex (2026) and Claude Code (2026) identifies a "smart zone" — the first ~100K tokens of context where attention relationships remain computationally manageable and output quality is consistently high. Beyond this zone, quality degrades predictably due to quadratic attention scaling.

**Practical guidance:** tasks with total estimated context (input + expected output) under 100K tokens will produce higher-quality output. Tasks exceeding 100K should be scrutinized — consider decomposing.

### Context Rot Thresholds

| Total Context (tokens) | Quality Impact |
|------------------------|---------------|
| < 50K | Optimal — model has full attention budget |
| 50K - 100K | Smart zone — high quality, minor degradation |
| 100K - 150K | Moderate — noticeable precision drop for retrieval |
| 150K - 200K | Degraded — increased hallucination risk, verify outputs |
| > 200K | High risk — context rot significant, decompose |

## The Curation Procedure

### Step 1: Identify Required Components

For each task, list which context components (from the checklist above) are needed. Be explicit — write down "IFC-003 (implementing), IFC-005 (consuming), error handling convention, FR-004, FR-005, FR-012."

### Step 2: Extract and Trim

For each identified component, extract the actual content and trim:

- **Interface contracts:** include only the operations the task implements or calls, not the entire contract document. If a contract has 10 operations and the task implements 3, include only those 3.
- **SRS requirements:** include only the requirement text, not surrounding context or rationale unless the rationale affects implementation.
- **Cross-cutting conventions:** include only the convention text, not the full cross-cutting concerns document.
- **Existing code:** include only the functions/classes the task will modify or call, not the entire file. Use comment markers: `// ... existing code above ...` to indicate trimmed sections.

### Step 3: Assemble

Combine all trimmed components into a single context block, organized as:

```markdown
## Task Context

### Module Responsibility
<one-sentence responsibility statement>

### Interface Contracts (Implementing)
<trimmed contract content>

### Interface Contracts (Consuming)
<trimmed contract content — signatures and data models only>

### Requirements
<relevant SRS requirement entries>

### Conventions
<relevant cross-cutting concern conventions>

### Existing Code
<trimmed code sections to extend>

### Constraints
<task-specific constraints>
```

### Step 4: Estimate and Budget-Check

Estimate the token count using the heuristics above. If it exceeds 40% of the context window:

1. Re-examine each component — can anything be further trimmed?
2. Can existing code be summarized instead of included verbatim?
3. Can consuming-side interface contracts be reduced to just signatures (no data model details)?
4. If still over budget → return to Task 2 and decompose the task into smaller units.

## Anti-Patterns

### The Document Dump
Including the entire architecture document, all interface contracts, and the full SRS in every task's context. This guarantees context rot and diluted signal.

### The Stub Context
Including only "implement the user module" with no interface contracts, no requirements, and no conventions. This guarantees hallucination — the LLM will invent interfaces and requirements.

### The Forward Reference
Including "see IFC-007 for the payment interface" instead of including the actual contract content. The LLM cannot look it up. Include the content directly.

### The Assumed Knowledge
Omitting conventions because "any developer knows how to do error handling." LLMs do not have shared project context — every convention must be explicit.
