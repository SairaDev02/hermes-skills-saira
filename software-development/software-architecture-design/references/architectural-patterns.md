# Architectural Patterns Reference

Common architectural patterns with their quality attribute strengths, weaknesses, and LLM-decomposition suitability. Use this to evaluate pattern candidates in Task 2.

## Pattern Catalog

### Layered (N-Tier)

**Structure:** Presentation → Business Logic → Data Access → Database. Each layer only depends on the layer directly below.

| Quality Attribute | Impact |
|-----|-----|
| Maintainability | Good — changes isolated to one layer |
| Scalability | Poor — entire tier must scale together |
| Performance | Moderate — each layer adds latency |
| Testability | Good — layers can be mocked independently |
| Deployability | Poor — entire application redeployed for changes |

**LLM decomposition:** Good — each layer can be a module. But layers tend to be coarse-grained; further decomposition within each layer is usually needed.

### Microservices

**Structure:** Independently deployable services, each owning its data, communicating via APIs or events.

| Quality Attribute | Impact |
|-----|-----|
| Scalability | Excellent — each service scales independently |
| Maintainability | Good — small, focused codebases |
| Performance | Variable — network overhead between services |
| Deployability | Excellent — independent deployment |
| Consistency | Poor — distributed transactions are hard |
| Complexity | High — service discovery, API gateway, distributed tracing |

**LLM decomposition:** Excellent — each microservice is naturally a single-context-window unit with a clear boundary.

### Event-Driven

**Structure:** Producers emit events; consumers react asynchronously. Often combined with microservices.

| Quality Attribute | Impact |
|-----|-----|
| Scalability | Excellent — consumers scale independently |
| Performance | Good for async flows; poor for synchronous request-response |
| Decoupling | Excellent — producers and consumers are independent |
| Debuggability | Poor — hard to trace event chains |
| Consistency | Eventual — requires careful design for consistency |

**LLM decomposition:** Excellent — each consumer is a module triggered by a well-defined event contract.

### Hexagonal (Ports and Adapters)

**Structure:** Core domain logic surrounded by ports (interfaces) and adapters (implementations). The core has no knowledge of external systems.

| Quality Attribute | Impact |
|-----|-----|
| Testability | Excellent — core tested without external dependencies |
| Maintainability | Good — adapters are swappable |
| Portability | Good — new adapters for new platforms |
| Complexity | Moderate — requires discipline to keep core pure |

**LLM decomposition:** Excellent — the core domain is a module; each adapter is a module. The port IS the interface contract.

### Model-View-Controller (MVC)

**Structure:** Model (data + logic), View (presentation), Controller (input handling).

| Quality Attribute | Impact |
|-----|-----|
| Maintainability | Good — separation of concerns |
| Testability | Good — model and controller testable independently |
| Scalability | Poor — typically a monolithic deployment |

**LLM decomposition:** Moderate — M, V, and C are natural modules but the pattern is coarse-grained; typically combined with other patterns.

### Client-Server

**Structure:** Client sends requests to a server that processes and responds.

| Quality Attribute | Impact |
|-----|-----|
| Performance | Moderate — request-response latency |
| Scalability | Moderate — server is a bottleneck |
| Security | Good — centralized server controls access |

**LLM decomposition:** Naturally splits into client module and server module(s).

### Pipe and Filter

**Structure:** Data flows through a series of filters (processing stages), each transforming input to output.

| Quality Attribute | Impact |
|-----|-----|
| Performance | Good for batch/streaming — parallelizable |
| Maintainability | Good — each filter is independent |
| Reusability | Excellent — filters are composable |

**LLM decomposition:** Excellent — each filter is a module with a clear input contract and output contract.

### Space-Based

**Structure:** No central database; data and processing distributed across nodes in a tuple space or grid.

| Quality Attribute | Impact |
|-----|-----|
| Scalability | Excellent — linear scaling |
| Performance | Good — data is local to processing |
| Consistency | Complex — eventual consistency by design |

**LLM decomposition:** Moderate — the space/grid infrastructure is complex; individual processing units decompose well.

## Pattern Selection Heuristics

1. **Start with quality attributes, not features.** "We need to handle 10K requests/sec" points to microservices or event-driven. "We need to change the UI without touching business logic" points to layered or hexagonal.
2. **Combine patterns.** Real systems use multiple patterns: microservices where independent scaling is needed, hexagonal within each service, event-driven between services.
3. **Prefer fewer patterns.** Each pattern adds conceptual overhead. Start with one primary pattern and add others only when a driver demands it.
4. **Check LLM familiarity.** Well-represented patterns (layered, MVC, microservices) have more training data coverage; exotic patterns may produce lower-quality LLM output.
5. **Document the tradeoff.** Every pattern choice rejects alternatives — document why in the ADR.

## Sources

- Bass, Clements, Kazman — *Software Architecture in Practice* (3rd ed.)
- Richards, Ford — *Fundamentals of Software Architecture* (O'Reilly, 2020)
- SEI Attribute-Driven Design (ADD) method — design concept catalogs
