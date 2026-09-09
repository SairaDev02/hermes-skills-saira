# Hermes Skills — Software Development Roles

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built for Hermes Agent](https://img.shields.io/badge/Hermes-Agent-blue)](https://hermes-agent.nousresearch.com/docs)
[![Skills: 7](https://img.shields.io/badge/Skills-7-green)](#skills)
[![Docs-only: 6 of 7](https://img.shields.io/badge/Docs--only-6_of_7-lightgrey)](#documentation-only-principle)

A collection of [Hermes Agent](https://hermes-agent.nousresearch.com/docs) skills covering the software-development lifecycle, from requirements through release. Each skill guides a specialist role's thinking and writing; the roles hand work to each other through versioned document packages, never through hallway conversation.

**Role index:** [Roles.md](Roles.md) is the authoritative lifecycle map — inputs, outputs, next owner, handoff readiness, feedback routing, and closure. This README is the front door; `Roles.md` is the contract.

## Documentation-Only Principle

Six of the seven skills are strictly documentation-only: they produce specifications, plans, reports, and evidence records. They may contain pseudocode and Mermaid/PlantUML diagrams, but they do not write or execute application code, tests, CI/CD configuration, deployment scripts, or operational commands — and they never claim execution without harness evidence. From `docs/PROJECT-CONSTITUTION.md`: an unverified claim is a finding, not a result.

The sole exception is [Rapid Application Development](software-development/rapid-application-development/SKILL.md), a cross-cutting iterative-delivery role whose own skill defines its separate operating boundary. It is intentionally **not** a numbered row in `Roles.md`.

## Installation

Three ways to get these roles into Hermes Agent, easiest first. For CLI installs from a private fork, set `GITHUB_TOKEN` in `~/.hermes/.env` (already required for hub rate limits; private repos won't resolve without it).

### Option A — by prompting (in-chat, easiest)

Ask Hermes directly — it loads skills via `skill_view` and installs via the `/skills` slash commands, no terminal needed:

```
Install the qa-engineer role from SairaDev02/hermes-skills-saira
```

or explicitly:

```
/skills tap add SairaDev02/hermes-skills-saira
/skills install SairaDev02/hermes-skills-saira/software-development/qa-engineer
```

Installed skills take effect in new sessions — run `/reset` or start a fresh session if the role doesn't respond immediately. Verify with `/skills search qa-engineer` or by invoking the role: `/qa-engineer describe your task`.

### Option B — via CLI (manual, persistent)

**Single role, direct from GitHub** (no tap needed — direct path installs work on any repo your `GITHUB_TOKEN` can read):

```bash
hermes skills install SairaDev02/hermes-skills-saira/software-development/qa-engineer --category software-development
```

Replace `qa-engineer` with any role directory: `software-requirements-engineering`, `software-architecture-design`, `llm-task-engineering`, `code-reviewer`, `devops-release-engineer`, `rapid-application-development`.

**All roles via tap** (subscribe once, then install/search by name). Note: this repo keeps roles under `software-development/`, not the default `skills/` tap path — after adding the tap, point it at the right subtree in `~/.hermes/skills/.hub/taps.json`:

```bash
hermes skills tap add SairaDev02/hermes-skills-saira
hermes skills search qa-engineer
hermes skills install SairaDev02/hermes-skills-saira/software-development/qa-engineer --category software-development
```

```json
{ "taps": [{ "repo": "SairaDev02/hermes-skills-saira", "path": "software-development/" }] }
```

(`hermes skills tap add` defaults new taps to `path: "skills/"`; edit the file directly when skills live elsewhere. `hermes skills tap list` shows the effective path per tap.)

### Option C — local copy (contributors, offline, editing)

Clone and drop the role directories straight into the skills dir — no registration needed, a skill appears automatically once its folder lands here:

```bash
git clone https://github.com/SairaDev02/hermes-skills-saira.git
mkdir -p ~/.hermes/skills/software-development
cp -r hermes-skills-saira/software-development/qa-engineer ~/.hermes/skills/software-development/qa-engineer/
```

Repeat the `cp` per role, or copy the whole `software-development/` tree for all seven. Two variants:

- **Live off your checkout** instead of copying: add it under `skills:` in `~/.hermes/config.yaml` via `hermes config set`, so edits are picked up without re-copying:
  ```yaml
  skills:
    external_dirs:
      - ~/projects/hermes-skills
  ```
- **Repo-local only** (roles active just inside this checkout): place them under `<project-root>/.hermes/skills/` (or `.agents/skills/` for cross-tool sharing) and run `hermes skills trust` once from inside the repo. Project skills outrank profile skills and are tagged `[project]` in the index.

### Verify

```bash
hermes skills list | grep qa-engineer
```

Then in chat: `/qa-engineer <your task>` — every installed role is automatically a slash command. Hub-installed roles can be refreshed with `hermes skills check` / `hermes skills update`; locally edited copies are skipped by `update` so your changes are never silently overwritten.

## Skills

| # | Skill | Role | Stage | Produces (documents only) |
|---|---|---|---|---|
| 1 | [software-requirements-engineering](software-development/software-requirements-engineering/SKILL.md) | Requirements Engineer | Start | SRS, RTM, feasibility decision, validation and change records |
| 2 | [software-architecture-design](software-development/software-architecture-design/SKILL.md) | Architect | Design | Architecture baseline, ADRs, module boundaries, interface contracts, diagrams |
| 3 | [llm-task-engineering](software-development/llm-task-engineering/SKILL.md) | Task Engineer | Dispatch | Normalized task manifest plus self-contained dispatch bundles |
| 4 | [qa-engineer](software-development/qa-engineer/SKILL.md) | Tester / QA Engineer | Verification | Test plans, cases, fixture and execution specs, bug and coverage reports |
| 5 | [code-reviewer](software-development/code-reviewer/SKILL.md) | Code Reviewer | Gate | Review evidence, findings, comments, and gate verdict |
| 6 | [devops-release-engineer](software-development/devops-release-engineer/SKILL.md) | DevOps / Release Engineer | Release | CI/CD, environment, release, monitoring, and rollback specifications |
| — | [rapid-application-development](software-development/rapid-application-development/SKILL.md) | RAD Engineer | Cross-cutting | Iterative-delivery plans and feedback governance; governed separately, not a lifecycle gate |

## Lifecycle Flow

```
Requirements → Architecture → Task Engineering → [implementation harness]
                                      ↓
                              QA + Code Review
                                      ↓
                              DevOps / Release

RAD Engineer ── coordinates evidence and decisions across the lifecycle when selected
```

Each arrow carries a versioned package using the shared [handoff template](templates/HANDOFF.md). Findings travel as [feedback records](templates/feedback-record.yaml), never as informal "talk to the other role" notes. See [Roles.md](Roles.md) for the full input → output → next-owner chain and the feedback-routing table.

## How to Use

**For agents (start sequence, from `docs/COLLABORATION-PROTOCOL.md`):**

1. Read the applicable handoff package.
2. Read `docs/PROJECT-CONSTITUTION.md`, `docs/GLOSSARY.md`, and the referenced contracts.
3. Resolve referenced `REF-` IDs (`docs/REFERENCE-INDEX.md`) and `ASM-` IDs (`docs/ASSUMPTIONS.md`).
4. Confirm scope, exclusions, output contract, and evidence requirements before writing.
5. Ask only when ambiguity changes implementation or acceptance; otherwise record a bounded assumption — never silently expand scope or rewrite an upstream baseline.

**For humans:**

1. Start at [Roles.md](Roles.md) to find the owning role for the work at hand.
2. Open that role's `SKILL.md` — it defines its tasks, completion criteria, and verification.
3. Use the role's `templates/` for output shape and `references/` for technique guidance.
4. Hand off with [templates/HANDOFF.md](templates/HANDOFF.md); route dissent with [templates/feedback-record.yaml](templates/feedback-record.yaml).

## Shared Contract

| Artifact | Purpose |
|---|---|
| [templates/HANDOFF.md](templates/HANDOFF.md) | Every role transition. Carries status (`READY` / `CONDITIONAL` / `BLOCKED`), artifact versions, binding decisions, claim states (`PLANNED` → `IMPLEMENTED` → `VERIFIED`, plus `BLOCKED` / `DISPUTED` / `STALE`), open findings, and receiver acceptance criteria. A handoff is complete only when the receiver can work without an undocumented conversation. |
| [templates/feedback-record.yaml](templates/feedback-record.yaml) | Every cross-role finding. Records source/target role, severity (`blocking` / `major` / `minor` / `informational`), affected IDs, evidence, and required action. The receiving role closes it or supersedes it — upstream baselines are never silently edited. |
| [templates/CLOSURE.md](templates/CLOSURE.md) | End of project. Closure is a checklist, not a role: all feedback closed or superseded, assumptions resolved or archived, packages final and versioned, change-impact map clear of follow-ups, lessons forwarded as next-project inputs. Coordinated by the DevOps / Release Engineer, accepted by the service owner. |

## Shared Context (`docs/`)

| Document | What it settles |
|---|---|
| [PROJECT-CONSTITUTION.md](docs/PROJECT-CONSTITUTION.md) | Binding rules for humans, role agents, and harnesses; source-of-truth table (SRS/RTM, ADRs, contracts, task manifest, test matrix, feedback records) |
| [COLLABORATION-PROTOCOL.md](docs/COLLABORATION-PROTOCOL.md) | Agent start sequence and working rules |
| [REFERENCE-INDEX.md](docs/REFERENCE-INDEX.md) | Registry of external technical sources (`REF-` IDs, versioned, status-marked). Internal templates are intentionally not indexed here. |
| [GLOSSARY.md](docs/GLOSSARY.md) | Canonical term definitions; field names and units defer to interface contracts |
| [ASSUMPTIONS.md](docs/ASSUMPTIONS.md) | Open uncertainty (`ASM-` IDs). Tasks depending on an open assumption are `CONDITIONAL`, never `READY`. |
| [CHANGE-IMPACT-MAP.md](docs/CHANGE-IMPACT-MAP.md) | What a change in one artifact obliges downstream — consult before accepting any change |

## Structure

```
software-development/<role>/
  SKILL.md          # role contract: tasks, completion criteria, verification
  references/       # technique guidance (checklists, methods, design notes)
  templates/        # output shapes (present in all roles except RAD)
templates/
  HANDOFF.md
  feedback-record.yaml
  CLOSURE.md
docs/
  PROJECT-CONSTITUTION.md
  COLLABORATION-PROTOCOL.md
  REFERENCE-INDEX.md
  GLOSSARY.md
  ASSUMPTIONS.md
  CHANGE-IMPACT-MAP.md
tests/skills/       # pytest contract tests per skill; green before any push
README.md
Roles.md
LICENSE
```

## Change Rules

- Preserve public API compatibility unless an approved change record permits a break.
- Never modify files outside task scope without recording a finding.
- No new dependencies without an architecture decision or dependency record.
- Tests must not depend on execution order or shared mutable state.
- Never commit secrets, credentials, or production data.
- Consult the change-impact map before accepting a change; version what moves.

## License

MIT — see [LICENSE](LICENSE).
