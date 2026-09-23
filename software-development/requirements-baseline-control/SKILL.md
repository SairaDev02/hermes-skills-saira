---
name: requirements-baseline-control
description: Use when producing requirements baselines.
version: 0.1.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [requirements, baseline, evidence, traceability, verification]
    related_skills: [software-requirements-engineering, software-architecture-design, qa-engineer]
---

# Requirements Baseline Control

Produce a defensible requirements baseline from repository evidence and stakeholder input. This class-level skill complements the requirements-engineering workflow by enforcing evidence provenance, draft-baseline honesty, deterministic traceability checks, and clean handoff boundaries.

## When to Use

- Establish requirements artifacts for a new project or scaffold-only repository.
- Review an SRS and RTM before handing them to architecture, task, or QA roles.
- Convert reported build, benchmark, or smoke-test results into correctly qualified evidence.
- Audit requirement counts, IDs, required fields, links, and downstream coverage.

Do not use this skill to invent architecture, implementation tasks, test cases, stakeholder approval, or legal clearance.

## Procedure

### 1. Inventory the baseline context

1. Inspect repository state with `git status --short --branch`, `git ls-files`, and targeted file searches.
2. Read existing project constitution, reference index, glossary, assumptions, change-impact map, requirements, and change history when present.
3. Classify each important fact as one of:
   - **Reported** — supplied by a stakeholder or prior operator.
   - **Repository-read** — observed directly in a file or tracked artifact.
   - **Independently rerun** — reproduced by the current session with recorded command scope.
   - **Stakeholder-validated** — confirmed in a recorded review, walkthrough, or approval.
4. If the repository is an untouched scaffold, create the minimum missing context artifacts or record their absence as explicit evidence gaps.
5. For a runtime, SDK, model, or native dependency that affects feasibility or release, inspect both the upstream source and the exact local artifact: pin the upstream revision/version, read the relevant examples/API docs, inspect the local manifest and model README, record package/archive size, and identify the exact files and checksums needed for release.
6. Separate code/runtime licensing from model/data licensing. A repository's license does not grant rights to bundled model weights, reference audio, datasets, or generated assets; record each component's source, license, attribution, prohibited-use terms, and unresolved discrepancies.

**Pitfall:** Do not treat generated build output as a requirements baseline; generated files prove an execution result only when the command and environment are known.

**Pitfall:** Do not infer model redistribution rights from the hosting repository's code license; model cards, bundled READMEs, and linked licenses can impose different or conflicting terms, so keep release clearance open until the exact artifacts are reconciled.

### 1b. Research upstream runtime and model evidence

When a requirement depends on an upstream runtime or model, use a repeatable evidence pass:

1. Fetch repository metadata from the GitHub API to capture the default branch, current revision, license, release tag, and language/platform claims.
2. Fetch raw upstream documentation and examples from `raw.githubusercontent.com`; search the repository tree for the exact runtime/model, platform examples, API types, release scripts, and license/notice files.
3. Fetch release metadata from the GitHub API and record the exact archive name, byte size, download URL, and available checksum/digest fields.
4. Read the local package manifest, integration example, model directory, and model README. Compare the local version and file set with upstream evidence rather than assuming they match.
5. Convert capabilities into requirements only at the behavior boundary: offline operation, input/output contract, reference assets, controls, failure states, measurable performance, packaging, and release obligations. Keep library names and implementation details as constraints only when explicitly approved.
6. Record a component-level license matrix and a V&V issue for every unresolved discrepancy. Do not mark commercial or production distribution approved from a successful smoke test.

**Pitfall:** Do not copy an upstream feature list into Must requirements; first verify that the exact version, model bundle, platform, language coverage, and license apply to the project artifact.

### 1a. Incorporate legacy product context without copying its implementation

When a remake or replacement is informed by an older repository, treat that repository as product evidence and change input, not as an approved design.

1. Pin the source revision before analysis. For a public GitHub repository, retrieve metadata and the default branch with the GitHub API, then retrieve the README, user/developer documentation, source files, tests, feedback data, and license from `raw.githubusercontent.com`.
2. Save large documents locally before analysis. Use a script to extract headings, feature terms, test-result summaries, and feedback statistics; do not rely on truncated terminal output or a pre-extracted URL summary.
3. Create one topical legacy-context artifact containing: product summary, preserved/revised/replaced/deferred capability matrix, historical user evidence with sample limitations, relevant test evidence, source revision, and source links.
4. Classify each legacy capability as **preserve**, **revise**, **replace**, **defer**, or **out of scope**. Preserve user-facing needs only after separating them from provider, framework, model, deployment, and module-structure choices.
5. Add legacy-derived raw needs to the stakeholder/elicitation record, create a change record, and propagate approved draft changes through the SRS, requirements table, RTM, V&V log, assumptions, change-impact map, and handoff.
6. Treat old tests, coverage, ratings, and completion responses as historical evidence. Use them to select regression areas and validation questions; never claim they verify the remake or convert small-sample averages directly into mandatory quality thresholds.

**Pitfall:** Do not copy a legacy feature list directly into Must requirements; preserve/revise/reject each capability explicitly because a replacement endpoint, local model, privacy boundary, or platform can change feasibility and behavior.

### 2. Record feasibility and stakeholder gaps

1. Assess technical, operational, economic, legal, and schedule feasibility separately.
2. Give each dimension a verdict, rationale, evidence source, risk level, owner, and exit evidence.
3. Register end users, product owners, technical owners, operators, QA/release owners, legal/licensing owners, and external dependencies.
4. Record raw needs, conflicts, assumptions, open questions, elicitation technique, feedback path, and validation status.
5. Use **conditional-go** when enough evidence supports continued discovery but release-critical decisions remain open.

**Pitfall:** Do not infer economic, legal, or stakeholder approval from a successful technical smoke test; those dimensions require their own evidence and decision owners.

### 3. Specify atomic draft requirements

1. Classify each entry as functional, quality/non-functional, interface, constraint/domain rule, or acceptance criterion.
2. Assign stable IDs and write one observable obligation per entry using `shall`, `should`, or `may`.
3. Include, at minimum: statement, type, source, priority, rationale, status, version, verification method, verification criteria, dependencies, conflicts, author, and update date.
4. Quantify performance and quality proposals, but label them draft until the target device, workload, provider, or stakeholder reference is approved.
5. Keep unresolved choices explicit with `Draft`, `Pending`, an owner, and an evidence gap; do not hide them behind vague prose.
6. Keep constraints separate from implementation choices. A current library, runtime, or model is a constraint only when the project explicitly commits to it.

**Pitfall:** Do not promote a setup fact into a product requirement without a source and rationale; a verified toolchain can support feasibility without defining user-visible behavior.

### 4. Build the SRS and RTM together

1. Assemble the SRS from the requirement entries, including scope, out-of-scope behavior, users, constraints, assumptions, dependencies, verification, validation, and open issues.
2. Add one RTM row for every requirement, linking source, priority, status, downstream design/task/test artifacts, verification method, and result.
3. When architecture, tasks, or tests do not exist yet, write `Pending` and log the coverage gap; never fabricate artifact IDs to make the table appear complete.
4. Add a change record covering scope, architecture, interfaces, quality, security/privacy, verification, schedule, cost, release, decision, approver, and propagation status.
5. Write a handoff with baseline version, feasibility decision, changed IDs, unresolved assumptions, verification methods, stakeholder validation status, and receiving-role actions.

### 4a. Stakeholder Q&A and change-record propagation

When the stakeholder is the user in a Hermes chat session, use the `clarify` tool. Batch up to five genuinely independent questions in one call; for a full requirement-by-requirement review, each question must identify the requirement ID and show its exact current statement before soliciting a response. Ask about the individual requirement, not a family-wide or batch-wide blanket acceptance. Capture stakeholder disposition separately from the quality-attribute assessment. For each requirement, review necessity, appropriateness, unambiguity, completeness, atomicity, feasibility, verifiability, and correctness; let the stakeholder flag concerns or request changes rather than forcing acceptance. Map every answer to its ID, stakeholder, and review evidence.

Before asking questions, reconcile the review list against the current SRS and any authoritative decision log. Treat prior recorded answers as answered, preload their exact disposition and provenance, and do not ask the stakeholder to repeat them. Maintain explicit reviewed and outstanding ID sets, and continue in manageable batches until every in-scope entry has a disposition. If earlier answers are summarized by range, verify the included IDs against the source records rather than assuming the range is complete. Stakeholder acceptance is not executable verification or baseline approval: keep entries Draft until the agreed full-baseline review and approval gates are complete.

Record decisions and resulting requirement changes in the formal change record (CR-NNN), RTM, V&V log, and HANDOFF as applicable, with rationale and approver. Bump the SRS revision history and version number for each decision batch. If the user changes a product name after artifacts are written, do a full audit (regex search for the old name across all files) after the replacement pass — `patch` and `execute_code` replacements can silently miss occurrences due to whitespace, encoding, or context-sensitive patterns (e.g., CLI commands vs product names vs config paths). Replace historical references only in change-record rows describing the rename itself; mark superseded CRs with strikethrough.

**Pitfall:** Do not infer individual quality-attribute approval from a stakeholder's general statement that a group of requirements is acceptable; each requirement needs its own mapped disposition and review evidence, because group-level agreement can conceal requirement-specific defects.

**Pitfall:** Do not call a draft RTM complete merely because every requirement has a row; downstream coverage is complete only when each required design/task/test link exists or the gap is explicitly carried forward.

### 5. Run deterministic quality checks

1. Inspect the actual SRS and RTM structure and representative IDs before writing a scanner. Requirements may be Markdown table rows rather than headings, and families can have different separators (for example, `NFR-DET-01`). Smoke-test each pattern on known IDs and report unmatched candidate rows before trusting totals.
2. Use a script or one-off Python command to derive, not manually count:
   - total requirement IDs and uniqueness;
   - exact set equality between SRS and RTM IDs (compare sets and separately report order differences when order is meant to match);
   - family counts and any declared/dashboard totals;
   - required-field counts per entry;
   - missing local Markdown links;
   - stale coverage totals;
   - `git diff --check` output.
3. Cross-check related artifact statements, not only ID structure: baseline/version and change dispositions across SRS, RTM, change log, feasibility report, V&V log, assumptions, and handoff. Resolve stale contradictions where supported by recorded decisions; otherwise log the unresolved conflict with an owner instead of silently choosing a value.
4. Run a wording screen for potential compound obligations, vague terms, absolutes, and missing measurable criteria where useful. Treat automated flags as review prompts, not confirmed defects; inspect the actual requirement and record confirmed findings separately.
5. Record the validation pass in the V&V log and handoff with date/scope, commands or checks actually run, results, corrections made, and explicit exclusions. Keep stakeholder validation, requirement correctness, full atomicity review, executable test results, and release/legal decisions separate unless independently evidenced.

For a Markdown-table SRS, a suitable starting point is to capture IDs from table rows in both files, adapting the family alternatives to the observed syntax (for example, `FR-\\d+`, `NFR-[A-Z]+-\\d+`, `C-\\d+`, `AC-\\d+`, `DEFR-\\d+`). Assert uniqueness and exact set equality, then derive family counts. Do not copy a regex without testing it against representative entries.

Report the exact scope of verification. If a command cannot be rerun, preserve the supplied result as **reported** and record the independent verification gap.

**Pitfall:** Never hand-maintain totals in a requirements artifact; stale counts make otherwise correct traceability look unreliable and conceal orphan rows.

**Pitfall:** Do not interpret an empty scanner result as proof that a family is absent until the parser is checked against the file's actual heading/table format and representative IDs; a syntactically valid but mismatched regex can undercount silently.

**Pitfall:** Do not label an issue fully resolved when only its measurable sub-obligation is specified but a release decision, target, or evidence gate remains pending; distinguish partial resolution from closure in the issue log and handoff.

**Pitfall:** Do not trust `patch` success reports after a bulk find-and-replace across many files — `patch` can match and report success without actually changing content when `old_string` has subtle whitespace or encoding differences. Always run a regex search for the old term after bulk replacements and inspect any file that should have changed but did not. Use `write_file` for full rewrites of complex files (HTML, large structured docs) where `patch` matching is unreliable. The `write_file` stale-write guard requires reading the full file first (every page if offset/limit was used) before overwriting.

### 6. Handoff without overclaiming

1. Mark the baseline Draft, Reviewed, Validated, or Approved only when the evidence supports that state.
2. Summarize what changed, what was verified, what remains pending, and who owns each gate.
3. Distinguish implementation-ready requirements from requirements that still depend on endpoint, legal, privacy, hardware, or stakeholder decisions.
4. Do not claim production readiness, commercial clearance, stakeholder agreement, or downstream test coverage unless the corresponding evidence is linked.

## Required artifact set

For a new baseline, prefer this compact set:

- `docs/PROJECT-CONSTITUTION.md`
- `docs/REFERENCE-INDEX.md`
- `docs/GLOSSARY.md`
- `docs/ASSUMPTIONS.md`
- `docs/requirements/FEASIBILITY.md`
- `docs/requirements/STAKEHOLDERS.md`
- `docs/requirements/SRS.md`
- `docs/requirements/REQUIREMENTS.md`
- `docs/requirements/RTM.md`
- `docs/requirements/V_AND_V.md`
- `docs/requirements/CHANGE-LOG.md`
- `templates/HANDOFF.md`

Use the existing project templates when available; do not create a per-session reference file for ordinary baseline content.

## Verification checklist

- [ ] Repository and prior requirements context were inventoried.
- [ ] Evidence provenance is labeled as reported, repository-read, independently rerun, or stakeholder-validated.
- [ ] All five feasibility dimensions have verdicts, rationale, evidence, and owners.
- [ ] Critical stakeholders, feedback paths, raw needs, conflicts, and gaps are recorded.
- [ ] Every requirement is atomic, uniquely identified, sourced, prioritized, and verifiable.
- [ ] SRS and RTM contain the same requirement IDs in the same baseline.
- [ ] Pending downstream links are explicit; no artifact IDs were invented.
- [ ] Change impact covers scope, architecture, interfaces, quality, verification, schedule, cost, and release.
- [ ] Totals and coverage were derived programmatically.
- [ ] Local links and `git diff --check` pass.
- [ ] Handoff states validation gaps and receiving-role actions without overclaiming.
