# C4 Diagramming Reference

Text-based architecture diagrams using Mermaid's C4 model support. The C4 model (by Simon Brown) describes software at four zoom levels — each diagram answers one question at one altitude.

## Why Text-Based

LLMs consume and reason about text, not images. Mermaid C4 diagrams are:
- **Version-controllable** — diffs show what changed
- **Readable as text** — LLMs can parse the structure
- **Renderable in Markdown** — any Markdown viewer shows the diagram

## C4 Levels

| Level | Question | Mermaid Keyword | When to Use |
|-----|-----|-----|-----|
| 1. Context | What is the system and who uses it? | `C4Context` | Stakeholder overview, system boundaries |
| 2. Container | What are the deployable pieces? | `C4Container` | Developer overview, technology stack |
| 3. Component | What's inside each container? | `C4Component` | Internal module structure |
| 4. Code | Class-level detail | (use class diagrams) | Rarely needed; use UML class diagrams |

## Context Diagram (Level 1)

```mermaid
C4Context
    title System Context Diagram for Order Management System

    Person(customer, "Customer", "Places orders online")
    Person(admin, "Admin", "Manages products and orders")

    System(oms, "Order Management System", "Processes customer orders")

    System_Ext(payment, "Payment Gateway", "Processes payments")
    System_Ext(email, "Email Service", "Sends order confirmations")
    System_Ext(inv, "Inventory System", "Tracks stock levels")

    Rel(customer, oms, "Places orders via")
    Rel(admin, oms, "Manages")
    Rel(oms, payment, "Processes payment via")
    Rel(oms, email, "Sends emails via")
    Rel(oms, inv, "Checks stock via")
```

**Key elements:**
- `Person(id, "Label", "Description")` — human actor
- `Person_Ext` — external human
- `System(id, "Label", "Description")` — your system
- `System_Ext(id, "Label", "Description")` — external system
- `Rel(from, to, "Label")` — relationship
- `Rel(from, to, "Label", "Technology")` — with technology annotation

## Container Diagram (Level 2)

```mermaid
C4Container
    title Container Diagram for Order Management System

    Person(customer, "Customer", "Places orders online")

    System_Boundary(oms, "Order Management System") {
        Container(webapp, "Web App", "React", "Customer-facing UI")
        Container(api, "API Gateway", "Node.js", "REST API, auth, routing")
        Container(order_svc, "Order Service", "Python/FastAPI", "Order processing")
        Container(inv_svc, "Inventory Service", "Go", "Stock management")
        Container(db, "Database", "PostgreSQL", "Order and product data")
        Container(queue, "Message Queue", "Kafka", "Async event bus")
    }

    System_Ext(payment, "Payment Gateway", "Processes payments")

    Rel(customer, webapp, "Uses", "HTTPS")
    Rel(webapp, api, "Calls", "REST/HTTPS")
    Rel(api, order_svc, "Routes to", "gRPC")
    Rel(api, inv_svc, "Routes to", "gRPC")
    Rel(order_svc, db, "Reads/Writes", "SQL")
    Rel(inv_svc, db, "Reads/Writes", "SQL")
    Rel(order_svc, queue, "Publishes events")
    Rel(order_svc, payment, "Processes payment via")
```

**Key elements:**
- `Container(id, "Label", "Tech", "Description")` — deployable piece
- `Container_Ext` — external deployable
- `Container_Boundary` — groups containers in a system
- The **Tech** parameter (3rd) shows the technology from Task 5

## Component Diagram (Level 3)

```mermaid
C4Component
    title Component Diagram for Order Service

    Container_Boundary(order_svc, "Order Service") {
        Component(controller, "Order Controller", "FastAPI", "Handles HTTP requests")
        Component(service, "Order Service", "Python", "Business logic")
        Component(repo, "Order Repository", "SQLAlchemy", "Database access")
        Component(events, "Event Publisher", "aiokafka", "Publishes domain events")
    }

    Rel(controller, service, "Calls")
    Rel(service, repo, "Uses")
    Rel(service, events, "Publishes via")
```

**Key elements:**
- `Component(id, "Label", "Tech", "Description")` — module within a container

## Deployment Diagram

```mermaid
C4Deployment
    title Deployment Diagram for Order Management System

    Deployment_Node(prod, "Production", "AWS") {
        Deployment_Node(region, "us-east-1") {
            Deployment_Node(cluster, "EKS Cluster") {
                Container(api, "API Gateway", "Node.js", "REST API")
                Container(order_svc, "Order Service", "Python", "Order processing")
                Container(inv_svc, "Inventory Service", "Go", "Stock management")
            }
        }
        Deployment_Node(rds, "RDS") {
            ContainerDb(db, "Database", "PostgreSQL", "Order data")
        }
    }

    Rel(api, order_svc, "Routes to")
    Rel(api, inv_svc, "Routes to")
    Rel(order_svc, db, "Reads/Writes")
```

**Key elements:**
- `Deployment_Node(id, "Label", "Environment")` — infrastructure node
- `ContainerDb` — database container
- `ContainerQueue` — message queue container

## Data Flow Diagram

Use a standard Mermaid flowchart for data flow (C4 doesn't have a dedicated DFD type):

```mermaid
flowchart LR
    Customer -->|Places order| API_Gateway
    API_Gateway -->|Validates & routes| Order_Controller
    Order_Controller -->|Creates order| Order_Service
    Order_Service -->|Checks stock| Inventory_Service
    Inventory_Service -->|Returns availability| Order_Service
    Order_Service -->|Processes payment| Payment_Gateway
    Payment_Gateway -->|Returns status| Order_Service
    Order_Service -->|Publishes OrderCreated| Message_Queue
    Message_Queue -->|Notifies| Fulfillment_Service
    Order_Service -->|Sends confirmation| Email_Service
    Order_Service -->|Persists| Database
```

## C4 Best Practices

1. **Stay at one level per diagram.** A context diagram with containers crammed in is unreadable. One altitude per diagram.
2. **Order matters for layout.** Mermaid C4 doesn't have smart auto-layout. If the diagram looks wrong, reorder element declarations.
3. **Keep it simple.** Don't cram a 50-microservice system into one diagram. Break into multiple focused diagrams per subsystem.
4. **Annotate with technology.** The `Tech` parameter in `Container` and `Component` is where Task 5's technology decisions show up.
5. **Use `System_Ext` for external dependencies.** This makes system boundaries explicit — critical for the interface contracts in Task 4.
6. **Every module from Task 3 must appear.** The container/component diagrams are the visual proof that the decomposition is complete.

## Rendering

Mermaid diagrams render natively in:
- GitHub Markdown (push to a repo)
- VS Code with Mermaid extension
- Mermaid Live Editor (https://mermaid.live)
- Hermes desktop preview pane (open the `.md` file)

For PlantUML as an alternative, see the PlantUML component diagram syntax — it supports a similar level-based approach but requires a PlantUML server or local binary to render.
