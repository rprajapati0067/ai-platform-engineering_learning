# Enterprise AI Platform — Current Architecture

## Current Service
`enterprise-ai-platform/services/ai-gatway`

## Architecture

```text
                         FastAPI
                            |
                            v
                  Request ID Middleware
                            |
                 +----------+----------+
                 |                     |
             UUID ID               Timer
                 |                     |
                 v                     |
             ContextVar                |
                 |                     |
                 v                     |
              Router                  |
                 |                     |
                 v                     |
            ChatService               |
                 |                     |
                 v                     |
             LLMProvider              |
                 ^                     |
                 |                     |
        MockLLMProvider                |
        FakeLLMProvider                |
        Other Fake Provider            |
```

## Observability Flow

```text
HTTP Request
 ↓
Request ID
 ↓
ContextVar
 ↓
Application logs
 ↓
RequestIdFilter
 ↓
Correlated logs

HTTP Request
 ↓
Start timer
 ↓
Application
 ↓
Stop timer
 ↓
latency_ms
```

## Example

```text
request_id=b3db71ac-0b7a-4523-be90-696f8e2afd9f
Processing chat request

request_id=b3db71ac-0b7a-4523-be90-696f8e2afd9f
HTTP request completed
method=POST
path=/chat
status_code=200
latency_ms=8.70
```

## Principles
- Keep routes thin.
- Keep application services independent of HTTP concerns.
- Depend on abstractions rather than concrete LLM implementations.
- Keep cross-cutting concerns in infrastructure.
- Use request-scoped context for correlation.
- Keep high-cardinality identifiers out of metric labels.
- Build observability into the platform.

## Current Milestone
Implemented:
- FastAPI foundation
- Pydantic models
- async service
- provider abstraction
- dependency inversion
- unit testing
- error handling
- configuration
- logging
- request IDs
- ContextVar
- automatic request-ID logging
- HTTP latency measurement
- metrics fundamentals

Next:
- proper Prometheus/OpenTelemetry-style metrics
- Counter
- Histogram
- Gauge
- metrics endpoint
- distributed tracing/OpenTelemetry later
