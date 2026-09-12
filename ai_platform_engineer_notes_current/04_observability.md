# Observability

## Logs vs metrics vs traces
Logs answer: **What happened?**
Metrics answer: **How much/how often/how fast?**
Traces answer: **What happened to this request across components?**

## Request ID / Correlation ID
Request IDs correlate logs belonging to one request.

```text
HTTP request
 ↓
Request ID middleware
 ↓
request.state.request_id
 ↓
ContextVar
 ↓
logs include request_id
```

Middleware is appropriate because request correlation is a cross-cutting concern. `ContextVar` avoids passing the ID through every method.

Do not use request IDs, user IDs, session IDs, or trace IDs as metric labels because they have high cardinality.

## Logging
A logging filter can modify a log record before formatting/output. Automatic request-ID ingestion avoids repeating `get_request_id()` everywhere.

Structured JSON logging is useful for log collectors and observability systems.

## Latency
Measure total request latency around:

```python
start = time.perf_counter()
response = await call_next(request)
latency = time.perf_counter() - start
```

The API exposes `X-Request-ID` and `X-Response-Time-Ms`.

## Metrics
Counter → how many? (`inc()`)
Histogram → distribution (`observe(value)`)
Gauge → current value.

The initial educational implementation used dictionaries/lists and a lock. That was useful for learning but storing every duration indefinitely in application memory does not scale.

## Prometheus
The project now uses `prometheus-client`.

Metrics:
- `http_requests_total`
- `http_request_duration_seconds`

The Python client also exposes runtime metrics such as GC and `python_info`.

The application exposes `GET /metrics`.

Prometheus scrapes the endpoint every 15 seconds.

Configuration:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "ai-gateway"
    static_configs:
      - targets: ["host.docker.internal:8000"]
```

FastAPI runs on the Mac and Prometheus runs in Docker. `host.docker.internal` lets the container reach the host.

Target was successfully verified as `UP`.

## Histogram
Histogram buckets are cumulative.

`le` means less than or equal to.

Examples:
- `le="0.005"` → observations ≤ 5ms
- `le="0.01"` → observations ≤ 10ms

Histogram also exposes:
- `_bucket`
- `_count`
- `_sum`

`_count` = number of observations.
`_sum` = total duration in seconds.

## PromQL
Raw counter:
```promql
http_requests_total
```

Filter:
```promql
http_requests_total{path="/chat"}
```

Aggregate:
```promql
sum(http_requests_total{path="/chat"})
```

Rate:
```promql
rate(http_requests_total[1m])
```

`rate()` estimates how quickly a counter is increasing.

## Endpoint instrumentation
Initially `/metrics` was being counted as application traffic. `/docs` and `/openapi.json` are also documentation/observability endpoints.

They are excluded from business/API Counter and Histogram metrics.

A duplicate instrumentation block once caused `/chat` to be incremented twice. The fix was to record metrics exactly once inside the non-excluded path condition.

## P95/P99
P95 query:

```promql
histogram_quantile(
    0.95,
    sum by (le) (
        rate(http_request_duration_seconds_bucket{path="/chat"}[5m])
    )
)
```

Observed P95: `0.00475` seconds ≈ **4.75ms**.

P99 query:

```promql
histogram_quantile(
    0.99,
    sum by (le) (
        rate(http_request_duration_seconds_bucket{path="/chat"}[5m])
    )
)
```

Observed P99: `0.00495` seconds ≈ **4.95ms**.

These are local/fake-provider measurements, not real LLM performance.

Mental model:

```text
_bucket
 ↓
rate()
 ↓
sum by (le)
 ↓
histogram_quantile()
 ↓
P95/P99
```

## Current next topic
SRE reliability concepts:
- SLI
- SLO
- SLA
- Error budget
- Availability SLO
- Latency SLO
- Error-rate SLO
- Prometheus SLO queries
- Alerting
