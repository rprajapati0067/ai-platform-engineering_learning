# Python + FastAPI

## Async/await
`async def` defines a coroutine. `await` allows the current coroutine to yield control while waiting for asynchronous I/O so other async work can progress.

Mental model:
Authentication → wait → Redis → wait → PostgreSQL → wait → RAG → wait → LLM.

## FastAPI
`@app.post("/chat")` creates a POST `/chat` endpoint.

## Pydantic
Pydantic models provide structured validation/parsing/serialization. `BaseModel` is the base class used to define these models.

## Tooling
- pytest runs tests.
- pytest-asyncio supports async tests.
- Ruff checks/lints and formats.
- `uv` manages dependencies and execution.

Project checks:
```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

The early project checkpoint had all tests passing and Ruff checks passing.
