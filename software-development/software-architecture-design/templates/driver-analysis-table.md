# Driver Analysis Table

> Produced in Task 1. Every driver traces to a requirement ID from the SRS/RTM.

## Functional Drivers

| ID | Functional Requirement (SRS ID) | Description | Impact on Architecture | Priority |
|----|-------------------------------|-------------|------------------------|----------|
| FD-01 | FR-___ | <description> | <how it shapes the architecture> | Critical/Important/Minor |
| FD-02 | FR-___ | | | |

## Quality Attribute Drivers

| ID | NFR (SRS ID) | ISO/IEC 25010 Characteristic | Quality Attribute | Quantified Target | Impact on Architecture | Priority |
|----|-------------|------------------------------|-------------------|-------------------|------------------------|----------|
| QA-01 | NFR-___ | Performance Efficiency | Latency | p95 < ___ms under ___ concurrent users | <how it shapes the architecture> | Critical |
| QA-02 | NFR-___ | Reliability | Availability | ___% uptime (≤ ___ min downtime/month) | | |
| QA-03 | NFR-___ | Security | Data Protection | <encryption, auth, access control> | | |
| QA-04 | NFR-___ | Maintainability | Modifiability | <change isolation metric> | | |
| QA-05 | NFR-___ | Portability | Platform Support | <target platforms> | | |
| QA-06 | NFR-___ | Compatibility | Interoperability | <integration targets> | | |

## Constraints

| ID | Constraint (SRS ID) | Type | Description | Source | Impact on Architecture |
|----|---------------------|------|-------------|--------|------------------------|
| C-01 | C-___ | Technology | <e.g., "Must use PostgreSQL"> | <stakeholder/rationale> | <how it limits design choices> |
| C-02 | C-___ | Budget | | | |
| C-03 | C-___ | Schedule | | | |
| C-04 | C-___ | Regulatory | | | |
| C-05 | C-___ | Team | | | |
| C-06 | C-___ | Legacy | | | |

## Tradeoff Analysis

| Tradeoff ID | Sensitivity Point | Quality Attribute A (+/-) | Quality Attribute B (+/-) | Affected Drivers | Notes |
|-------------|-------------------|---------------------------|---------------------------|-----------------|-------|
| T-01 | <e.g., "Caching layer"> | Performance (+) | Consistency (−) | QA-01, QA-03 | <rationale> |
| T-02 | | | | | |

## Completeness Checklist

- [ ] Every functional requirement ID from the RTM appears in the Functional Drivers table
- [ ] Every non-functional requirement from the SRS appears in the Quality Attribute Drivers table with a quantified target
- [ ] Every constraint from the SRS appears in the Constraints table
- [ ] Every quality attribute target is measurable (can be tested)
- [ ] Tradeoff analysis identifies sensitivity points and tradeoffs
- [ ] No empty cells remain
