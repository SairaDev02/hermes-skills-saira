# Requirement Quality Attributes

Quality characteristics for individual requirements and requirement sets, synthesized
from ISO/IEC/IEEE 29148:2018, INCOSE Guide for Writing Requirements V3.1, and IREB CPRE.

## Individual Requirement Characteristics

### C1 — Necessary

**Definition:** The requirement defines an essential capability. Removing it creates a
deficiency that cannot be fulfilled by other requirements.

**Check:**
- [ ] Can trace the requirement to a stakeholder need or parent requirement
- [ ] The author can explain *why* this requirement exists (rationale)
- [ ] Removing it would leave a gap in system capability

### C2 — Appropriate

**Definition:** The requirement is relevant to the system's purpose and scope.

**Check:**
- [ ] Falls within the identified system boundary
- [ ] Addresses a legitimate stakeholder concern, not gold-plating

### C3 — Unambiguous

**Definition:** The requirement can be interpreted in only one way and is easy to understand.

**Check:**
- [ ] No vague terms (\"fast\", \"user-friendly\", \"robust\", \"efficient\")
- [ ] Quantified where possible (specific numbers, thresholds, units)
- [ ] Consistent terminology — same word means the same thing throughout
- [ ] No acronyms without definition on first use

### C4 — Complete

**Definition:** The requirement needs no further amplification to be understood and implemented.

**Check:**
- [ ] All conditions, inputs, outputs, and error states are described
- [ ] No \"TBD\", \"TBA\", or placeholder text
- [ ] Includes measurable thresholds where performance is expected

### C5 — Singular (Atomic)

**Definition:** The requirement contains exactly one obligation.

**Check:**
- [ ] No \"and\" / \"or\" connecting separate obligations (split into multiple requirements)
- [ ] No compound requirements that would need partial verification
- [ ] Each requirement can be individually tested and individually traced

### C6 — Feasible

**Definition:** The requirement can be satisfied within technical, schedule, and budget
constraints.

**Check:**
- [ ] Achievable with current or planned technology
- [ ] No requirement for impossible or contradictory conditions
- [ ] The set of all requirements is collectively feasible (not just each individually)

### C7 — Verifiable

**Definition:** It is possible to prove that the system satisfies the requirement through
inspection, analysis, demonstration, or test.

**Check:**
- [ ] A test case or verification method can be defined from the requirement text
- [ ] Pass/fail criteria are derivable from the requirement
- [ ] No subjective success criteria (\"the system should look good\")
- [ ] If using EARS, the response clause is observable

### C8 — Correct

**Definition:** The requirement accurately describes what the stakeholder actually needs.

**Check:**
- [ ] Validated with the source stakeholder
- [ ] No errors in technical assumptions
- [ ] Consistent with domain knowledge and business rules

### C9 — Implementation-Free

**Definition:** The requirement describes *what* the system must do, not *how* it must do it.

**Check:**
- [ ] No specific technology, product, or vendor named (unless that IS the requirement)
- [ ] No architectural decisions embedded (\"use Redis\", \"implement as microservice\")
- [ ] Describes the capability, not the solution
- [ ] Does not prescribe a design pattern or algorithm

### C10 — Traceable

**Definition:** The requirement can be traced upward to its source and downward to derived
requirements, design elements, and test cases.

**Check:**
- [ ] Links to at least one source (stakeholder need, parent requirement, or regulation)
- [ ] Links to at least one verification artifact (test case, review, demonstration)
- [ ] Bidirectional traceability maintained in the RTM

## Requirement Set Characteristics

### S1 — Consistent (Set)

- No two requirements conflict with each other
- No duplicate requirements covering the same capability
- Same term used for the same concept throughout the entire set

### S2 — Complete (Set)

- The set needs no further amplification — it contains everything pertinent to defining
  the system
- No TBDs or placeholders in the set
- All stakeholder needs are addressed by at least one requirement
- Implicit requirements (error handling, session management, compatibility) are
  explicitly documented

### S3 — Feasible (Set)

- The complete set can be satisfied within lifecycle constraints (schedule, budget,
  technical capability)
- No requirement in the set makes another infeasible

### S4 — Bounded

- The set stays within the identified scope
- No requirements for capabilities outside the system boundary

### S5 — Modifiable and Extensible

- The set has a clear structure that allows changes without destabilizing the whole
- Requirements are organized by category and theme
- Change impact is assessable via traceability links

## Verification Methods (per ISO/IEC/IEEE 29148)

| Method | When to use |
|--------|-------------|
| **Inspection** | Visual or document review (e.g., UI layout, data format) |
| **Analysis** | Mathematical or logical proof (e.g., throughput calculation, security model) |
| **Demonstration** | Observable functional behavior (e.g., user can complete checkout flow) |
| **Test** | Instrumented measurement against thresholds (e.g., response time < 200ms) |

Each requirement should declare its intended verification method. If you cannot assign a
method, the requirement is likely not verifiable — revise it.
