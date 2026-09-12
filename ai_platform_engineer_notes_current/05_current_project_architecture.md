# Current Enterprise AI Platform Architecture

## Current service
Python/FastAPI `ai-gatway`.

## Layers

```text
app/
├── api/
│   ├── routes/
│   └── middleware/
├── application/
│   ├── chat_service.py
│   └── exceptions.py
├── core/
│   ├── config.py
│   ├── logging.py
│   ├── metrics.py
│   └── request_context.py
├── domain/
│   ├── llm.py
│   └── models.py
└── infrastructure/
    └── llm/
        └── mock_provider.py
```

## Request flow

```text
HTTP request
 ↓
Request ID middleware
 ↓
ContextVar request ID
 ↓
Timer
 ↓
FastAPI route
 ↓
ChatService
 ↓
LLMProvider abstraction
 ↓
Mock/Fake provider
 ↓
ChatResponse
 ↓
Metrics + logging
 ↓
HTTP response
```

## Observability flow

```text
HTTP request
 ├── request_id → logs
 ├── latency → histogram
 └── count → counter
          ↓
       /metrics
          ↓
      Prometheus
          ↓
       PromQL
```

## Current environment
- Python 3.13 locally
- project requires Python >=3.12
- `uv`
- Docker working
- Prometheus running in Docker
- FastAPI running on host
- Prometheus target confirmed UP

## Future AI platform

```text
User
 ↓
API Gateway
 ↓
Agent Orchestrator
 ├── RAG
 ├── Tools
 ├── Databases
 └── LLM Providers
 ↓
Response

Cross-cutting:
Auth
Security
Correlation
Metrics
Logs
Traces
SLOs
Cost/token tracking
Governance
```
