# AI Platform Engineer Journey — Revision Notes

## Goal
Become a Senior AI Platform Engineer with Python primary, Golang secondary, Java third, plus Agentic AI, distributed systems, cloud, Kubernetes, and production engineering.

## Notes
- `00_learning_journey_rules.md` — permanent learning/documentation rules
- `01_foundations.md` — AI Platform fundamentals
- `02_python_fastapi.md` — Python/FastAPI foundations
- `03_architecture_testing.md` — architecture and testing
- `04_observability.md` — logging, metrics, Prometheus, P95/P99
- `05_current_project_architecture.md` — current project snapshot

## Completed
- AI Platform fundamentals
- Agent mental model
- Python/FastAPI
- async/await
- Pydantic
- pytest/Ruff
- provider abstraction
- dependency inversion
- testing and error handling
- configuration/logging
- Request ID and ContextVar
- latency
- Counter/Histogram/cardinality
- Prometheus client
- `/metrics`
- Prometheus server
- PromQL
- `rate()`
- histogram buckets
- P95/P99

## Current position
**Next: SLI/SLO/SLA and error budgets.**

Start with:
> What is an SLI vs SLO, and how should we define SLOs for our AI Gateway?

## Last verified practical state
Prometheus target: `ai-gateway` = `UP`

Observed `/chat`:
- P95 ≈ 4.75ms
- P99 ≈ 4.95ms

These are local/fake-provider measurements and should not be treated as real LLM performance.
