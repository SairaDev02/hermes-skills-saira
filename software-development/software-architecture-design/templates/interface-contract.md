# Interface Contract Template

> One contract per inter-module interaction. Produced in Task 4.
> A developer (or LLM) must be able to implement either side of the interface from this document alone.

---

## Interface: <Interface Name>

**Interface ID:** IFC-NNN
**Owner module:** <module that provides this interface>
**Consumer module(s):** <module(s) that consume this interface>
**Version:** 0.1.0
**Status:** <draft | approved | deprecated>

### 1. Communication Pattern

<Asynchronous (message queue/event bus) | Synchronous (REST/gRPC) | In-process (function call)>

| Property | Value |
|----------|-------|
| Protocol | <REST / gRPC / Kafka topic / in-process> |
| Transport | <HTTPS / TCP / IPC> |
| Direction | <Module A → Module B | bidirectional> |
| Sync/Async | <synchronous | asynchronous (fire-and-forget) | asynchronous (request-reply)> |

### 2. Operations

#### Operation: <operationName>

**Description:** <what this operation does>

**Request:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| param1 | string | Yes | <description> |
| param2 | integer | No | <description> |

**Response (Success — 200/0):**

| Field | Type | Description |
|-------|------|-------------|
| field1 | string | <description> |
| field2 | object | <description> |

**Example request:**

```json
{
  "param1": "example_value",
  "param2": 42
}
```

**Example success response:**

```json
{
  "field1": "result",
  "field2": { "nested": "data" }
}
```

#### Operation: <operationName2>

<repeat structure above for each operation>

### 3. Data Models

#### Model: <ModelName>

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| id | UUID | Yes | UUIDv4 | Unique identifier |
| name | string | Yes | max 255 chars | Display name |
| status | enum | Yes | one of: active, inactive, pending | Current state |
| createdAt | datetime | Yes | ISO 8601 UTC | Creation timestamp |

**Example:**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Example entity",
  "status": "active",
  "createdAt": "2025-01-15T10:30:00Z"
}
```

#### Model: <ModelName2>

<repeat for each data model>

### 4. Error Contracts

#### Error Response Format

```json
{
  "error": {
    "code": "MODULE_ERROR_CODE",
    "message": "Human-readable message",
    "details": { "field": "validation_error" },
    "correlationId": "uuid"
  }
}
```

#### Error Catalog

| Error Code | HTTP Status (if applicable) | Description | Retryable? |
|------------|------------------------------|-------------|------------|
| MODULE_NOT_FOUND | 404 | Resource does not exist | No |
| MODULE_VALIDATION | 400 | Input failed validation | No |
| MODULE_CONFLICT | 409 | State conflict (e.g., duplicate) | No |
| MODULE_TIMEOUT | 504 | Operation timed out | Yes (with backoff) |
| MODULE_INTERNAL | 500 | Unexpected internal error | Yes (with backoff) |

#### Retry Policy

| Error Code | Max Retries | Backoff Strategy | Notes |
|------------|-------------|------------------|-------|
| MODULE_TIMEOUT | 3 | Exponential: 1s, 2s, 4s | Jitter ±20% |
| MODULE_INTERNAL | 2 | Exponential: 1s, 2s | Circuit breaker after 5 consecutive failures |

### 5. Protocol-Specific Details

#### If REST:

- Base URL: `<base_path>` (e.g., `/api/v1/orders`)
- Authentication: <OAuth 2.0 bearer token | API key in header | none>
- Rate limit: <requests per minute>
- Idempotency: <supported via Idempotency-Key header? | not supported>

#### If Event/Message:

- Topic/Queue: `<topic_name>`
- Message format: <JSON schema reference>
- Ordering: <ordered | unordered>
- Delivery guarantee: <at-least-once | exactly-once>
- Dead letter queue: <yes | no> — <DLQ name>

#### If gRPC:

- Service definition: `<path to .proto file>`
- Streaming: <unary | server streaming | client streaming | bidirectional>

### 6. Versioning

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | <date> | Initial draft |

### 7. Contract Completeness Checklist

- [ ] Every operation has a typed signature (name, parameters, return type)
- [ ] Every data model referenced in a signature has a defined schema
- [ ] Every operation has documented error behavior
- [ ] Communication pattern is specified for each interaction
- [ ] Protocol-specific details are documented
- [ ] Error catalog includes all possible error codes
- [ ] Retry policy covers retryable errors
- [ ] Versioning scheme is defined
