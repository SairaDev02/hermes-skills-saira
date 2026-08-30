# Software Requirements Specification (SRS) Template

Based on IEEE 830 structure with ISO/IEC/IEEE 29148:2018 guidance.
Adapt sections as needed — not every section applies to every project.

---

# Software Requirements Specification: [Project Name]

**Version:** [X.Y.Z]
**Status:** [ ] Draft  [ ] Reviewed  [ ] Validated  [ ] Approved
**Date:** [YYYY-MM-DD]
**Author(s):** [Names]

## Revision History

| Version | Date | Author | Description of Changes |
|---------|------|--------|----------------------|
| 0.1.0 | | | Initial draft |
| | | | |

## Table of Contents

[Auto-generated or manual]

---

## 1. Introduction

### 1.1 Purpose

State the purpose of this SRS and its intended audience (developers, testers,
project managers, stakeholders).

### 1.2 Scope

Describe the software being specified:
- **Name:** [system name]
- **What it does:** [1-2 sentence summary]
- **Benefits:** [value to stakeholders]
- **What it does NOT do:** [explicitly out of scope]

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|-----------|
| SRS | Software Requirements Specification |
| RTM | Requirements Traceability Matrix |
| | |

### 1.4 References

List all documents referenced in this SRS:
- [1] ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Requirements engineering
- [2] [Other standards, regulations, or internal documents]
- [3]

### 1.5 Overview

Briefly describe how the rest of the document is organized.

---

## 2. Overall Description

### 2.1 Product Perspective

Describe the system's context:
- Is it a standalone product or a component of a larger system?
- What external systems does it interface with?
- Include a context diagram (text description or diagram reference)

**System Interfaces:**
| External System | Interface Type | Data Exchanged |
|----------------|---------------|----------------|
| | | |

**User Interfaces:**
- [ ] CLI
- [ ] Web UI
- [ ] Mobile app
- [ ] Desktop GUI
- [ ] API
- Describe key UI principles and standards to follow

**Hardware Interfaces:**
| Hardware | Purpose | Interface |
|----------|---------|-----------|
| | | |

**Software Interfaces:**
| Software/Platform | Version | Purpose |
|-------------------|---------|---------|
| | | |

**Communication Interfaces:**
| Protocol | Purpose |
|----------|---------|
| | | |

### 2.2 Product Functions

Summary of the major functions the system will perform (not detailed requirements —
those are in Section 3). Number them for reference:

1. [Function 1]
2. [Function 2]
3. [Function 3]

### 2.3 User Characteristics

Describe each user class that will interact with the system:

| User Class | Education/Experience | Technical Proficiency | Frequency of Use |
|-----------|---------------------|----------------------|-----------------|
| | | | |

### 2.4 Constraints

List all design and implementation constraints:
- C-01: [Constraint description]
- C-02: [Constraint description]

### 2.5 Assumptions and Dependencies

**Assumptions:**
- A-01: [Assumption — what we assume to be true]
- A-02: [Assumption]

**Dependencies:**
- D-01: [Dependency on external system, library, or condition]
- D-02: [Dependency]

---

## 3. Specific Requirements

This section contains the detailed, testable requirements. Each requirement
follows the format in `templates/requirements-table.md`.

### 3.1 Functional Requirements

#### FR-01: [Requirement Name]

| Field | Value |
|-------|-------|
| **ID** | FR-01 |
| **Description** | [EARS-formatted requirement statement] |
| **Source** | [Stakeholder/Document] |
| **Priority** | [Must/Should/Could/Won't] |
| **Status** | [Draft/Reviewed/Validated] |
| **Verification** | [Test/Demo/Inspection/Analysis] |
| **Rationale** | [Why this requirement exists] |

[Continue for each functional requirement]

#### FR-02: [Requirement Name]
...

### 3.2 Non-Functional Requirements

Group by ISO/IEC 25010 quality categories:

#### Performance

| ID | Description | Metric | Threshold | Source |
|----|------------|--------|-----------|--------|
| NFR-P01 | The system shall respond to API requests within 200ms at the 95th percentile | Response time | ≤200ms (P95) | |
| NFR-P02 | | | | |

#### Reliability

| ID | Description | Metric | Threshold | Source |
|----|------------|--------|-----------|--------|
| NFR-R01 | The system shall maintain 99.9% uptime per calendar month | Availability | ≥99.9% | |

#### Security

| ID | Description | Source |
|----|------------|--------|
| NFR-S01 | | |

#### Usability

| ID | Description | Source |
|----|------------|--------|
| NFR-U01 | | |

#### Maintainability

| ID | Description | Source |
|----|------------|--------|
| NFR-M01 | | |

#### Portability

| ID | Description | Source |
|----|------------|--------|
| NFR-PT01 | | |

### 3.3 Interface Requirements

[API specifications, data format contracts, protocol requirements — or reference to
external interface control documents]

### 3.4 Data Requirements

[Data model summary — ER description, data dictionary entries, data volume estimates]

---

## 4. Verification and Validation

### 4.1 Verification Methods

| Requirement ID | Method | Description |
|----------------|--------|-------------|
| FR-01 | Test | |
| NFR-P01 | Test | |
| NFR-R01 | Analysis | |

### 4.2 Validation Plan

[How requirements will be validated with stakeholders: reviews, prototyping, demos]

---

## 5. Requirements Traceability Matrix

See `templates/rtm-template.md` for the full RTM. Include a summary here:

| Requirement ID | Source | Priority | Status | Verified By |
|----------------|--------|----------|--------|-------------|
| FR-01 | | | | |
| FR-02 | | | | |

---

## 6. Appendices

### Appendix A: Analysis Models

[ER diagram descriptions, DFD descriptions, FDD descriptions, data dictionaries]

### Appendix B: Issues List

| Issue ID | Description | Affected Requirements | Status | Resolution |
|----------|-------------|----------------------|--------|------------|
| ISS-01 | | | | |

### Appendix C: Glossary

[Extended definitions of domain-specific terms]
