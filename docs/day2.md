# Day 2 — Python for AI Platform Engineering

## Objective

Build the Python foundation needed for our Enterprise AI Platform.

The goal is not to learn all of Python. We focus on the Python concepts we will repeatedly use in AI services, Agentic AI, FastAPI, testing, and platform engineering.

## 1. Python as Our Primary Language

Our language priority is:

1. **Python — Primary**
   - AI/LLM engineering
   - FastAPI
   - LangGraph
   - MCP
   - RAG
   - AI evaluation
   - AI services

2. **Golang — Secondary**
   - High-performance services
   - Concurrent workers
   - Gateways
   - Event processing
   - Distributed systems

3. **Java — Tertiary**
   - Enterprise integration
   - Spring Boot
   - Existing-system understanding
   - Interview preparation

## 2. Type Hints

Python is dynamically typed, but our production code will use type hints extensively.

```python
def get_user(user_id: int) -> User:
    ...
```

Benefits:
- Better IDE support
- Easier code review
- Static analysis
- Better documentation
- Fewer accidental type errors
- Clearer contracts

## 3. Dataclasses

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```

Conceptually similar to a Go struct.

For API/validation models, we will often use Pydantic.

## 4. Pydantic

Pydantic provides data validation, parsing, serialization, structured models, and JSON schema generation.

```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    model: str
```

`BaseModel` is the foundation that tells Pydantic to treat the class as a Pydantic model and provides validation, parsing, serialization, and schema behavior.

Pydantic will be important for:
- API requests/responses
- Agent inputs
- Tool definitions
- LLM structured outputs
- Configuration

## 5. FastAPI

FastAPI is our Python web framework.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}
```

This creates `GET /health`.

FastAPI also generates OpenAPI/Swagger documentation at `/docs`.

## 6. Request and Response Models

```python
class ChatRequest(BaseModel):
    message: str
    model: str

class ChatResponse(BaseModel):
    response: str
    model: str
```

These define explicit API contracts.

```text
Client
  │ ChatRequest
  ▼
FastAPI
  │ ChatResponse
  ▼
Client
```

## 7. async and await

`async def` defines a coroutine that can suspend while waiting for asynchronous operations.

```python
async def get_data():
    ...
```

`await` suspends the current coroutine until an asynchronous operation produces a result, while allowing the event loop to run other available work.

```python
result = await fetch_data()
```

Important: `await` does not mean the operation runs in another thread, and sequential awaits are still sequential within that coroutine.

## 8. AI Platform Async Example

For an AI Gateway:

```text
Authentication → 10 ms
Redis          → 5 ms
PostgreSQL     → 50 ms
RAG Service    → 200 ms
LLM            → 2 seconds
```

While one asynchronous I/O operation is waiting, other requests/tasks can make progress.

The key mental model:

> `await` suspends the current coroutine so the event loop can run other available work.

Go and Python are different internally:

| Go | Python |
|---|---|
| Goroutine | Coroutine / asyncio task |
| Go runtime scheduler | asyncio event loop |
| Channel | asyncio.Queue / related primitives |
| `go func()` | `asyncio.create_task()` |
| `go test` | `pytest` |

Do not treat goroutines and coroutines as identical.

## 9. pytest

pytest is our test framework.

```python
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
```

Automated tests provide a safety net as the platform grows.

```text
Code Change
    ↓
Tests
    ↓
 ┌──┴──┐
Pass  Fail
 ↓      ↓
Deploy  Fix
```

## 10. Ruff

Ruff handles Python linting/code-quality checks and formatting.

```bash
uv run ruff check .
uv run ruff format .
```

Mental model:

```text
Ruff   → Is the code clean and consistently written?
pytest → Does the code behave correctly?
```

## 11. Day 2 Project Work

We created an initial FastAPI service:

```text
services/ai-gateway/
├── app/
│   ├── main.py
│   └── models.py
├── tests/
├── pyproject.toml
└── README.md
```

Initial APIs:
- `GET /health`
- `GET /version`
- `POST /chat`

The architecture was then evolved on Day 3.

## 12. Key Lessons

1. Python will be our primary engineering language.
2. We will write typed, production-quality Python.
3. Pydantic gives us structured data contracts.
4. FastAPI owns the HTTP/API layer.
5. Async I/O is important for AI applications.
6. pytest protects behavior.
7. Ruff protects code quality and consistency.

## 13. Interview Takeaways

**What is `async def`?**  
A declaration of a coroutine that can suspend during asynchronous operations.

**What does `await` do?**  
Suspends the current coroutine while allowing the event loop to run other available work.

**Why use Pydantic?**  
For validated, structured data models used by APIs, tools, configuration, and AI outputs.

**Why use FastAPI?**  
For modern Python APIs with async support, type-driven validation, and automatic OpenAPI documentation.

**Why automated tests?**  
To provide repeatable protection against regressions as the codebase grows.

## 14. Completion

- [x] Python environment
- [x] FastAPI application
- [x] `/health`
- [x] `/version`
- [x] `/chat`
- [x] Pydantic models
- [x] Async/await understanding
- [x] pytest
- [x] Ruff

**Status: COMPLETE**
