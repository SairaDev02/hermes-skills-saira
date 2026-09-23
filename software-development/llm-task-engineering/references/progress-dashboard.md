# Progress Dashboard Reference

The methodology for generating a self-contained HTML/CSS/JS progress dashboard
that the coding agent updates after every verification check. This is Task 9
of the task engineering process.

## Why a Progress Dashboard Matters

A task manifest with 28+ tasks dispatched across 7+ waves generates significant
coordination overhead. Without a live progress tracker:
- The user cannot see at a glance which tasks are done, in progress, or blocked.
- The coding agent has no structured place to record V&V results.
- Wave readiness is hard to assess — you need to check git logs and test
  outputs to know if a wave is complete.
- Architecture invariant checks (grep-based boundary verifications) are
  easily forgotten if not tracked in a visible place.

The dashboard solves this by being a single HTML file that both the human and
the coding agent can open in a browser to see the full state of implementation.

## Dashboard Specification

### File Location

`docs/task-engineering/dashboard/index.html`

### Architecture

The dashboard is a **single self-contained HTML file** with embedded CSS and
JavaScript. No server, no build step, no external dependencies, no framework.
Open it directly in any browser.

### Data Model

The dashboard contains two embedded JavaScript arrays that serve as the data
source — no external JSON or CSV file is needed.

#### TASKS Array

One object per manifest task. Fields split into two groups: **static** (set
at generation time, never changed) and **mutable** (updated by the coding
agent after each verification check).

```javascript
{
  // ── Static fields (do not change) ──
  id: "T-01",                    // Task ID
  title: "Schemas — ...",         // Task title
  module: "M-07",                 // Module ID
  wave: 1,                        // Wave number
  phase: "0",                     // Delivery phase
  deps: [],                       // Dependency task IDs
  blocks: ["T-02", ...],          // Blocked task IDs
  estTokens: 12000,               // Estimated total context (tokens)
  outputEst: "~6K",               // Estimated output size

  // ── Mutable fields (coding agent updates) ──
  status: "pending",              // Status lifecycle (see below)
  commit: "",                     // Git commit hash
  vvResult: "",                   // "pass" | "fail" | ""
  vvNotes: "",                    // Brief V&V findings
  vvDate: ""                      // ISO 8601 date
}
```

#### Status Lifecycle

```text
pending → dispatched → in-progress → review → passed | failed | blocked
```

| Status | Meaning | When to set |
|--------|---------|-------------|
| `pending` | Not yet started | Default at generation time |
| `dispatched` | Bundle sent to the coding agent | After dispatching the bundle |
| `in-progress` | Agent is generating code | After the agent starts producing output |
| `review` | Agent committed, awaiting V&V | After the commit is made |
| `passed` | Independent V&V confirmed pass | After the Task Engineer verifies |
| `failed` | Independent V&V found issues | After V&V fails |
| `blocked` | Cannot proceed (dependency failed) | When a blocking dependency fails |

#### INVARIANTS Array

Architecture invariant checks — grep-based or command-based verifications that
must hold after implementation. One object per invariant.

```javascript
{
  id: "inv1",                     // Invariant ID
  label: "No cactus-needle ...",  // Human-readable description
  cmd: "grep -r ...",             // Verification command
  expected: "empty",              // Expected result
  status: "pending"               // "pending" | "passed" | "failed"
}
```

### Visual Components

The dashboard should render:

1. **Summary cards** — total tasks, passed, in-progress, in review,
   failed/blocked, pending. Color-coded by status.
2. **Progress bar** — segmented bar showing proportion passed (green),
   in-progress (yellow), and remaining (dark). Includes percentage.
3. **Wave sections** — collapsible per-wave tables. Each row shows task ID,
   title, module, phase, status badge, commit hash (short), V&V result
   (✅/❌). Wave badge shows complete (green) or active (yellow).
4. **Task detail modal** — clicking a task row opens a modal showing
   dependencies, blocks, estimated context, commit hash, V&V result, V&V
   notes, and dispatch bundle path.
5. **Architecture invariant checks** — list of invariant checks with
   pass/fail icons, descriptions, and the grep commands.
6. **Last-updated timestamp** — auto-generated on render.

### Styling

Dark theme (GitHub-style): background `#0d1117`, cards `#161b22`, borders
`#30363d`, foreground `#e6edf3`. Status colors: green `#3fb950`, yellow
`#d29922`, orange `#db6d28`, red `#f85149`, blue `#58a6ff`. Use system font
stack. Monospace for code/commands. Responsive at 768px breakpoint.

## Update Protocol

### When the Coding Agent Updates

The coding agent edits the `TASKS` and `INVARIANTS` arrays directly in the
HTML file after each verification check:

1. **After a task is dispatched:** set `status` to `"dispatched"`.
2. **After a task starts generating:** set `status` to `"in-progress"`.
3. **After a task's commit is made:** set `status` to `"review"`, set
   `commit` to the commit hash.
4. **After V&V passes:** set `status` to `"passed"`, set `vvResult` to
   `"pass"`, set `vvNotes` to a brief summary, set `vvDate`.
5. **After V&V fails:** set `status` to `"failed"`, set `vvResult` to
   `"fail"`, set `vvNotes` to the failure summary, set `vvDate`.
6. **After an invariant is checked:** set its `status` to `"passed"` or
   `"failed"`.

### Dashboard Commit Discipline

- Commit dashboard updates **separately** from implementation commits.
- Commit message: `dashboard: update <T-XX> status to <status>` or
  `dashboard: update invariant checks`.
- Do NOT push — the user pushes after reviewing.

## HANDOFF Integration

The HANDOFF document must include a section documenting:
- The dashboard file path.
- The update protocol (when to update, which fields to edit).
- The status lifecycle.
- The dashboard commit discipline.
- What the dashboard shows (visual components).

This ensures the coding agent knows exactly how and when to update the
dashboard without reading the skill itself.

## Invariant Checks to Include

Derive invariant checks from the architecture's cross-cutting concerns and
security requirements. Typical invariants for a layered pipeline architecture:

1. **Model boundary:** no external model library imports outside the model
   adapter module (NFR-M01).
2. **No privileged model calls:** no `Model.run()` or equivalent in the
   execution path (FR-03, C-02).
3. **No shell interpolation:** no `shell=True` in subprocess calls (NFR-S01).
4. **Offline env vars:** required env vars set before model construction
   (NFR-O01).
5. **Type stability:** all shared dataclasses round-trip through
   serialization (NFR-M03).
6. **End-to-end vertical slice:** the Phase 1 exit command succeeds.
7. **Output purity:** JSON output mode produces valid JSON on stdout.
8. **Security checkpoint:** policy classification and sandbox resolution
   called before every tool dispatch.

The exact invariants depend on the project's architecture. Use grep commands
that are simple, deterministic, and can be run by the coding agent or the
Task Engineer during V&V.

## Anti-Patterns

### The External Data File
Putting task data in a separate JSON file and fetching it via `fetch()`. This
fails when opening the file directly in a browser (CORS restriction on
`file://` protocol). Inline the data in the HTML file as a JavaScript array.

### The Framework Dependency
Using React, Vue, or a build tool. The dashboard must be openable by anyone
on any machine with a browser — no npm install, no build step, no node server.

### The Manual Refresh
Forgetting to document the update protocol in the HANDOFF. The coding agent
needs explicit instructions on which fields to edit and when. Without the
protocol, the dashboard stays at "all pending" forever.

### The Missing Invariants
Only tracking task status but not architecture invariant checks. Invariants
are the cross-cutting boundary conditions that hold across all tasks — they
are the final verification gate and must be visible on the dashboard.
