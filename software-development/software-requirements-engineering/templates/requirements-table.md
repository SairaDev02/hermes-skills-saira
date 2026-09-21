# Individual Requirement Entry Template

Use this format for each requirement in the SRS. Copy and fill for every requirement.

---

## [REQ-ID]: [Requirement Name]

| Field | Value |
|-------|-------|
| **ID** | [FR-XX / NFR-XX / C-XX] |
| **Type** | [Functional / Non-Functional / Constraint / Acceptance Criterion] |
| **Description** | [Requirement statement in EARS syntax or structured prose] |
| **Rationale** | [Why this requirement exists — what stakeholder need it addresses] |
| **Source** | [Stakeholder name/role, document, or regulation that originated this] |
| **Priority** | [Must / Should / Could / Won't (this time)] |
| **Status** | [Draft / Reviewed / Validated / Approved / Implemented / Verified] |
| **Version** | [X.Y.Z] |
| **Verification Method** | [Test / Analysis / Demonstration / Inspection] |
| **Verification Criteria** | [Specific, measurable pass/fail conditions] |
| **Dependencies** | [IDs of requirements this one depends on] |
| **Conflicts** | [IDs of requirements this one conflicts with, if any] |
| **Estimated Effort** | [Story points / hours / days] |
| **Author** | [Name] |
| **Last Updated** | [YYYY-MM-DD] |

---

## Example Filled Entries

### FR-01: User Authentication

| Field | Value |
|-------|-------|
| **ID** | FR-01 |
| **Type** | Functional |
| **Description** | When the user submits valid credentials, the system shall authenticate the user and create a session. |
| **Rationale** | Users need secure access to their accounts (Stakeholder: Product Owner) |
| **Source** | Product Owner, Interview 2026-08-15 |
| **Priority** | Must |
| **Status** | Validated |
| **Version** | 1.0.0 |
| **Verification Method** | Test |
| **Verification Criteria** | Given valid credentials, the system returns HTTP 200 with a session token. Given invalid credentials, the system returns HTTP 401. |
| **Dependencies** | None |
| **Conflicts** | None |
| **Estimated Effort** | 5 story points |
| **Author** | Jane Doe |
| **Last Updated** | 2026-08-29 |

### NFR-P01: API Response Time

| Field | Value |
|-------|-------|
| **ID** | NFR-P01 |
| **Type** | Non-Functional (Performance) |
| **Description** | The system shall respond to API requests within 200 milliseconds at the 95th percentile under normal load (≤1000 concurrent requests). |
| **Rationale** | User experience degrades significantly above 200ms (Stakeholder: UX Team) |
| **Source** | UX Research Report, 2026-07-20 |
| **Priority** | Must |
| **Status** | Reviewed |
| **Version** | 1.0.0 |
| **Verification Method** | Test |
| **Verification Criteria** | Load test with 1000 concurrent requests; 95th percentile response time ≤200ms. Measured over 10-minute sustained load. |
| **Dependencies** | FR-01 (authentication must work for test setup) |
| **Conflicts** | None |
| **Estimated Effort** | 3 story points |
| **Author** | Jane Doe |
| **Last Updated** | 2026-08-29 |

### C-01: Technology Stack Constraint

| Field | Value |
|-------|-------|
| **ID** | C-01 |
| **Type** | Constraint |
| **Description** | The system shall be deployable on Kubernetes 1.28+ clusters. |
| **Rationale** | Organizational infrastructure standard (Stakeholder: DevOps Lead) |
| **Source** | DevOps Lead, Architecture Review 2026-08-10 |
| **Priority** | Must |
| **Status** | Approved |
| **Version** | 1.0.0 |
| **Verification Method** | Demonstration |
| **Verification Criteria** | System deploys and runs on a standard Kubernetes 1.28 cluster without modifications. |
| **Dependencies** | None |
| **Conflicts** | None |
| **Estimated Effort** | N/A (constraint, not feature) |
| **Author** | John Smith |
| **Last Updated** | 2026-08-29 |
