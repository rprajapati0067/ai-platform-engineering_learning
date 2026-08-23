# Day 4 — Configuration, Logging, Request Correlation and Metrics

## Configuration
The project uses:
- `pyproject.toml`
- `uv`
- `uv.lock`
- Pydantic Settings
- `.env`
- `.env.example`

Treat configuration and secrets differently. Never blindly log confidential enterprise data, prompts, or responses.

## Logging
Use Python logging rather than `print()`.

Levels:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Use:

```python
logger = logging.getLogger(__name__)
```

### Important lesson
A module-level:

```python
logger.info("Processing chat request")
```

runs during import. A log inside the request-processing function runs when the request is actually processed.

## Request ID / Correlation ID
Every HTTP request receives a UUID.

```text
HTTP Request
 ↓
Middleware
 ↓
Generate UUID
 ↓
ContextVar
 ↓
Application
 ↓
Logger
```

A request ID identifies an individual HTTP request. A correlation ID is a broader identifier used to correlate related operations across services/workflows.

For the future agentic platform:

```text
API
 ↓
Agent
 ↓
RAG
 ↓
Tool
 ↓
Database
 ↓
LLM
```

## Middleware
Middleware is appropriate for cross-cutting HTTP concerns such as:
- request IDs
- authentication
- metrics
- tracing
- rate limiting
- CORS

Conceptually:

```text
Request
 ↓
Middleware before
 ↓
call_next()
 ↓
Route
 ↓
Application
 ↓
Middleware after
 ↓
Response
```

## ContextVar
`ContextVar` provides context-local state suitable for async request processing.

The request ID is set at request start and reset afterward.

Do not use a global mutable request ID.

## Automatic Request-ID Logging
A custom `logging.Filter` enriches every log record.

```text
logger.info(...)
 ↓
LogRecord
 ↓
RequestIdFilter
 ↓
get_request_id()
 ↓
record.request_id
 ↓
Formatter
```

Application code can simply write:

```python
logger.info("Calling LLM")
```

while infrastructure automatically adds the request ID.

Important rule:

> Cross-cutting concerns should be implemented in infrastructure rather than repeated in business code.

## Request Latency
Use:

```python
time.perf_counter()
```

for elapsed-duration measurement.

Start before:

```python
await call_next(request)
```

and stop after it returns.

The current service exposes:
- `X-Request-ID`
- `X-Response-Time-Ms`

and logs completed requests with method, path, status code, and latency.

Example:

```text
request_id=abc123 | HTTP request completed |
method=POST | path=/chat | status_code=200 | latency_ms=8.70
```

## Logs vs Metrics vs Traces

### Logs
Answer: **What happened?**

Example:
`LLM call failed`

### Metrics
Answer: **How much / how often?**

Example:
`P95 latency = 2.4 seconds`

### Traces
Answer: **Where did this request spend its time?**

Example:
`API → RAG → Tool → LLM`

## P50 / P95 / P99
- P50 = median
- P95 = approximately 95% of requests complete at or below that latency
- P99 = approximately 99% complete at or below that latency

P95/P99 reveal tail latency. P99 measures tail latency; it does not itself reduce latency.

## Metrics
A metric is a measurement; a log is an event.

### Counter
A counter increases over time.

Examples:
- total requests
- total errors
- total LLM calls
- total tokens

Mental model: **Counter = How many?**

### Histogram
A histogram represents a distribution of numerical observations.

Typical examples:
- HTTP latency
- LLM latency
- RAG latency
- database latency
- tool latency

A histogram can maintain bounded bucket/count information rather than storing every observation.

Mental model: **Histogram = How are values distributed?**

### Gauge
A gauge represents a current value and can go up or down.

Examples:
- active requests
- active agents
- CPU utilization
- memory usage

Mental model: **Gauge = What is the value right now?**

## Why the Toy List Is Not Production-Ready
Our educational implementation stored every duration in a Python list:

```python
durations.append(duration_seconds)
```

Memory grows with request volume and all observations disappear on process restart.

A production metrics SDK uses counters/histograms and exports metrics to a separate monitoring system.

## Histogram Memory and Storage
A histogram is not a database.

The application/metrics SDK maintains histogram state in memory, but it can use a bounded set of buckets instead of one stored value per request.

A monitoring system such as Prometheus separately collects and stores time-series metrics over time.

Conceptual architecture:

```text
FastAPI
 ↓
Metrics SDK / Histogram
 ↓
/metrics
 ↓
Prometheus
 ↓
Time-series storage
 ↓
Grafana / Monitoring
```

## Cardinality
Do not use high-cardinality identifiers as metric labels.

Bad:

```text
http_requests_total{
    request_id="unique-for-every-request"
}
```

Better:

```text
http_requests_total{
    method="POST",
    path="/chat",
    status_code="200"
}
```

High-cardinality identifiers such as request IDs generally belong in logs/traces, not metric labels.

## Production Observability Model

```text
                 Observability
                      |
          +-----------+-----------+
          |           |           |
        Logs       Metrics      Traces
          |           |           |
       Events      Numbers     Request flow
```

For the future Agentic AI platform:

```text
Agent
├── Planning    → latency histogram
├── RAG         → latency histogram
├── Tool calls  → latency histogram
├── LLM calls   → latency histogram
├── Errors      → counter
└── Active work → gauge
```

## Key Interview Rules
1. Middleware creates the request ID; the logging filter does not.
2. The filter reads request context and adds the ID to the log record.
3. Do not pass request IDs through every business method without a genuine business need.
4. Do not put request IDs in metric labels.
5. Logs = events, metrics = aggregate measurements, traces = request journeys.
6. P95/P99 expose tail latency; averages can hide slow requests.
7. Use `perf_counter()` for elapsed time.
8. A histogram is a compact distribution representation, not persistent storage.
9. Prometheus is separate from in-process metric state.
10. High-cardinality labels can create excessive metric series.

## Current Day 4 Status
Completed:
- configuration
- `.env`
- Pydantic Settings
- logging
- request ID
- ContextVar
- automatic request-ID log enrichment
- HTTP latency measurement
- metrics fundamentals
- counter/histogram/gauge concepts
- metric cardinality

Next:
- replace the toy metrics collector with a proper Prometheus/OpenTelemetry-style implementation
