---
name: code-reviewer
description: Review code against requirements, architecture, security.
version: 0.2.0
author: FerdinandM, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [code-review, security, compliance, complexity, edge-cases, verdict]
    related_skills: [software-architecture-design, software-requirements-engineering, qa-engineer, llm-task-engineering]
---

# Code Reviewer Skill

Produce an evidence-backed review package for completed code. This role checks requirements, architecture, security, conventions, maintainability, and edge cases, then records comments and a verdict; it does not modify code, write tests, or merge changes.

## When to Use

- Review completed code against its task spec, SRS, RTM, architecture, or contracts.
- Assess security, scope, complexity, maintainability, and uncovered edge cases.
- Produce structured comments and an approve, request-changes, or reject verdict.
- Don't use for: implementing fixes, writing tests, GitHub posting, or simplifying approved code.

## Prerequisites

- Diff, PR, or file set and the task spec that generated it.
- Applicable SRS, RTM, architecture, interface contracts, and test results.
- Available scanners/linters and their actual output; mark unavailable tools honestly.
- Use `read_file`, `search_files`, `terminal`, `write_file`, and `patch` for review artifacts. Use `github-code-review` only when the user asks to publish comments.

## Procedure

### 1. Establish review basis

Catalog changed files, task scope and exclusions, source artifact versions, and available test/security results. **Done when:** the review queue identifies exactly what is being reviewed and which evidence is missing.

### 2. Check requirements and architecture

Map every acceptance criterion and RTM requirement to code locations and pass/fail evidence. Check module ownership, scope boundaries, interface signatures/schemas/errors, cross-cutting conventions, and undocumented dependencies. **Done when:** every mapped criterion, changed file, and touched interface has a disposition.

### 3. Check security and conventions

Run available SAST, dependency, and secret scans through `terminal`; record tool, version, scope, result, and limitations. Review added code for injection, authorization, sensitive-data exposure, unsafe deserialization, path traversal, dangerous evaluation, and insecure defaults. Check lint/type/style constraints and debug artifacts. **Done when:** every applicable category is passed, findings are recorded, or unavailability is explicit.

### 4. Assess maintainability and edge cases

Assess changed functions for complexity, length, nesting, naming, duplication, error handling, resource cleanup, state transitions, concurrency, boundaries, and unhandled inputs. Cross-reference each gap with QA coverage. **Done when:** every changed function and relevant edge category has evidence or a documented limitation.

### 5. Write findings and verdict

Consolidate findings with stable IDs, severity, type, precise location, evidence, requirement/contract link, and fix direction. Use the decision matrix: approve only with no blocking findings; request changes for fixable critical/warning issues; reject when the approach requires re-architecture. **Done when:** the verdict counts findings exactly, states residual risk, and names the next owner and feedback path.

## Required artifact shapes

- **Finding:** ID, severity, type, location, evidence, violated criterion, direction, owner.
- **Review basis:** task ID, changed files, artifact versions, checks run/unavailable.
- **Verdict:** decision, counts, rationale, residual risk, required actions, feedback destination.

## Quick Reference

| Check | Artifact |
|---|---|
| Scope/spec | Compliance checklist |
| Architecture | Boundary and contract report |
| Security | Scan results |
| Quality | Complexity and style findings |
| Robustness | Edge-case findings |
| Gate | Review comments and verdict |

## Pitfalls

- Reviewing style before establishing requirements and scope.
- Treating a clean scanner result as proof of security.
- Claiming a scan ran when the tool was unavailable.
- Reporting vague findings without a location, evidence, or violated criterion.
- Calling a fix “approved” while warnings remain under the stated matrix.
- Posting external comments without reading back the exact target.

## Verification

- [ ] Changed files and review evidence are complete or gaps are explicit.
- [ ] Every acceptance criterion and RTM requirement has a code disposition.
- [ ] Scope, module boundaries, interfaces, and cross-cutting rules are checked.
- [ ] Security, dependency, and secret checks are run or marked unavailable.
- [ ] Every changed function has maintainability and edge-case assessment.
- [ ] Findings have stable IDs, severity, location, evidence, and direction.
- [ ] Verdict counts match the enumerated findings and residual risk is recorded.
- [ ] No code, test, or configuration was modified by the review role.
