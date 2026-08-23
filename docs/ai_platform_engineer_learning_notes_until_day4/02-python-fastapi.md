# Python + FastAPI Foundations

## Project
Enterprise AI Platform — current service: `services/ai-gatway`

Python is the primary language for this journey.

## Concepts Learned
- type hints
- `async` / `await`
- Pydantic
- FastAPI
- pytest
- Ruff
- dependency management with `uv`

## Async / Await
`async def` defines a coroutine. `await` lets the coroutine suspend while waiting for asynchronous I/O so other async work can progress.

Example mental model:

```text
Authentication → wait → Redis → wait → PostgreSQL → wait → RAG → wait → LLM
```

Async is primarily useful for I/O-bound concurrency; it does not automatically make CPU-heavy work faster.

## Pydantic
`BaseModel` provides validation, parsing, serialization, and schema generation for structured application data.

## FastAPI
A route such as:

```python
@app.post("/chat")
```

creates a POST endpoint. FastAPI integrates with Pydantic for request/response validation and OpenAPI documentation.

## Testing
- pytest runs tests
- Ruff checks code quality/linting
- Ruff formats code

Project checks have been passing successfully.

## Important Rule
Keep validation at the appropriate boundary/layer rather than placing unrelated validation responsibilities inside application services.
