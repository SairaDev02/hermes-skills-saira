# Architectural Drivers Reference

Architectural drivers are the requirements and constraints that shape architecture. They come in three categories, all extracted from the SRS and RTM.

## Three Categories of Drivers

### 1. Functional Drivers

What the system must **do** — the behaviors, inputs, outputs, and data processing. Functional drivers rarely determine the architecture directly, but they constrain it: a real-time analytics system has different architectural needs than a batch ETL pipeline, even if both "process data."

**Source:** Functional requirements in the SRS.

### 2. Quality Attribute Drivers (Non-Functional)

How **well** the system must do it. These are the primary architecture drivers. Map each to an ISO/IEC 25010 quality characteristic and quantify:

| ISO/IEC 25010 Characteristic | Example Driver | Quantified Form |
|-----|-----|-----|
| Performance efficiency | "The system shall respond quickly" | "p95 latency < 200ms for read operations under 1000 concurrent users" |
| Reliability | "The system shall be highly available" | "99.95% availability (≤ 4.38 min downtime/month), RTO < 5 min" |
| Security | "The system shall be secure" | "All data in transit encrypted with TLS 1.3; auth via OAuth 2.0 + PKCE; secrets in vault" |
| Maintainability | "The system shall be easy to modify" | "Adding a new data source requires changes to ≤ 2 modules; no changes to core processing" |
| Portability | "The system shall run on multiple platforms" | "Deployable on Linux, macOS, and Windows without code changes" |
| Usability | "The system shall be user-friendly" | "New users complete primary task in ≤ 3 min without training (SUS score ≥ 80)" |
| Compatibility | "The system shall integrate with existing systems" | "Interoperates with system X via REST API; data exchange via JSON per schema Y" |
| Functional suitability | (Covered by functional drivers) | — |

**Source:** Non-functional requirements in the SRS. Every quality attribute must be **measurable** — if you can't write a test for it, it's not a valid driver.

### 3. Constraints

Limitations on the solution space — things the architect cannot change:

- **Technology constraints:** "Must use PostgreSQL" (legacy infrastructure), "Must run on Kubernetes"
- **Budget constraints:** "Total infrastructure cost ≤ $5000/month"
- **Schedule constraints:** "MVP in 8 weeks"
- **Regulatory constraints:** "GDPR compliance required", "Data must stay in EU"
- **Team constraints:** "Team knows Python and Go, not Rust"
- **Legacy constraints:** "Must integrate with existing SOAP service X"

**Source:** Constraint requirements and project context in the SRS.

## Driver Analysis Heuristics

### Identifying Architecturally Significant Requirements (ASRs)

Not every requirement affects architecture. A requirement is an ASR if it:

- Affects the structure of the system (modules, layers, interfaces)
- Affects a quality attribute with measurable impact
- Has broad impact (many modules affected)
- Is a constraint that limits design choices

**SEI Attribute-Driven Design (ADD) guidance:** Start with ASRs only — don't wait for all requirements to be finalized. Architecture can begin once a set of ASRs is available.

### Priority-Weighted Driver Analysis

Assign each driver a weight based on its impact on the architecture:

- **Critical** — shapes the fundamental pattern (e.g., "must handle 1M concurrent users" → microservices/event-driven)
- **Important** — influences module boundaries or technology (e.g., "must support horizontal scaling" → stateless modules)
- **Minor** — affects individual module design but not the overall architecture (e.g., "must use specific date format")

### Tradeoff Identification (ATAM-Inspired)

When multiple quality attributes compete, document the tradeoff:

| Tradeoff Type | Example |
|-----|-----|
| **Sensitivity point** — a property that affects more than one quality attribute | "Caching layer" affects both performance (positive) and consistency (negative) |
| **Tradeoff** — improving one quality attribute degrades another | "Synchronous validation" improves security but degrades performance |
| **Risk** — an architectural decision that may not meet its quality attribute target | "Chosen message broker may not handle peak throughput — needs load testing" |

Reference these tradeoffs in your ADRs and decomposability validation.

## Sources

- ISO/IEC 25010:2011 — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality model
- SEI Attribute-Driven Design (ADD) method — Bass, Clements, Kazman, *Software Architecture in Practice* (3rd ed.), Ch. 17
- SEI Architecture Tradeoff Analysis Method (ATAM) — Clements, Kazman, Klein, *Evaluating Software Architectures* (2001)
