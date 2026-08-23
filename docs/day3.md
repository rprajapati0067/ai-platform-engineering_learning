# Day 3 — Clean Architecture, Dependency Injection & Testing

## Objective

Move the AI Gateway from a simple FastAPI application toward a maintainable production architecture.

Core principle:

> Business/application logic should not be tightly coupled to infrastructure.

## 1. Why Architecture Matters

A small application can start with:

```text
app/
├── main.py
└── models.py
```

But an AI Gateway can eventually interact with:

```text
OpenAI
Claude
Gemini
PostgreSQL
Redis
Qdrant
Neo4j
Kafka
MCP tools
Kubernetes
Observability systems
```

If everything lives inside FastAPI route handlers, the code becomes difficult to change and test.

## 2. Clean Architecture

Our conceptual layers:

```text
Presentation
     ↓
Application
     ↓
Domain
     ↓
Infrastructure
```

### Presentation
HTTP/API concerns:
- FastAPI routes
- Request handling
- Response formatting
- HTTP-specific behavior

### Application
Use cases and application orchestration:
- ChatService
- AgentService
- ExecuteTool
- RetrieveContext
- CreateAgent

### Domain
Core concepts and contracts:
- ChatRequest
- ChatResponse
- Agent
- Tool
- LLMProvider

The domain should not directly depend on FastAPI, PostgreSQL, OpenAI, Kafka, or Kubernetes.

### Infrastructure
External integrations:
- OpenAI
- Claude
- Gemini
- PostgreSQL
- Redis
- Kafka
- Qdrant
- Neo4j
- Kubernetes

## 3. AI Gateway Architecture

```text
                    HTTP Request
                         │
                         ▼
                ┌─────────────────┐
                │   Presentation  │
                │     FastAPI     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Application   │
                │   ChatService   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Domain      │
                │   LLMProvider   │
                └────────┬────────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          OpenAI       Claude      Gemini
```

## 4. Dependency Inversion

Core principle:

> High-level application logic should not depend directly on low-level infrastructure.

Bad:

```text
ChatService
    ↓
OpenAIProvider
```

Better:

```text
ChatService
    ↓
LLMProvider
    ↑
OpenAIProvider
```

`LLMProvider` is the abstraction/contract.

## 5. Go Mental Model

Go interfaces provide a familiar comparison:

```go
type LLMProvider interface {
    Generate(ctx context.Context, prompt string) (string, error)
}
```

Concrete implementations can be OpenAI, Claude, etc.

## 6. Python Protocol

```python
from typing import Protocol

class LLMProvider(Protocol):

    async def generate(self, prompt: str) -> str:
        ...
```

Python uses structural typing here: a compatible implementation can satisfy the contract without explicitly inheriting from `LLMProvider`.

Example:

```python
class FakeLLMProvider:

    async def generate(self, prompt: str) -> str:
        return "Fake AI response"
```

## 7. Application Service

```python
class ChatService:

    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    async def execute(self, request: ChatRequest) -> ChatResponse:
        response = await self.llm_provider.generate(
            request.message
        )

        return ChatResponse(
            response=response,
            model=request.model,
        )
```

`ChatService` does not know about FastAPI, OpenAI, Claude, HTTP, PostgreSQL, or Redis.

## 8. Dependency Injection

Dependency Injection means:

> Give an object the dependencies it needs from outside rather than having the object construct them itself.

Bad:

```python
class ChatService:

    def __init__(self):
        self.provider = OpenAIProvider()
```

Better:

```python
class ChatService:

    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider
```

Then:

```python
provider = OpenAIProvider()
service = ChatService(provider)
```

## 9. Dependency Inversion vs Dependency Injection

**Dependency Inversion** is the architectural principle:

```text
ChatService
     ↓
LLMProvider
     ↑
OpenAIProvider
```

**Dependency Injection** is the technique used to supply the dependency:

```python
service = ChatService(provider)
```

They are related but not identical.

## 10. Why DI Helps Testing

Without DI:

```text
Test
 ↓
ChatService
 ↓
OpenAI API
 ↓
Internet
```

With DI:

```text
Test
 ↓
ChatService
 ↓
FakeLLMProvider
```

Benefits:
- Fast tests
- Deterministic tests
- No external API
- No API cost
- Easy failure simulation

## 11. Fake Providers

We created multiple implementations:

```python
class FakeLLMProvider:

    async def generate(self, prompt: str) -> str:
        return "Fake AI response: Hello"
```

and:

```python
class AnotherFakeLLMProvider:

    async def generate(self, prompt: str) -> str:
        return "Another response"
```

The same `ChatService` can use either implementation without changing its code.

## 12. Unit Testing

Our unit-test architecture:

```text
Test
 ↓
ChatService
 ↓
FakeLLMProvider
```

We use Arrange → Act → Assert.

### Arrange

```python
provider = FakeLLMProvider()
service = ChatService(provider)

request = ChatRequest(
    message="Hello",
    model="fake-model",
)
```

### Act

```python
response = await service.execute(request)
```

### Assert

```python
assert response.response == "Fake AI response: Hello"
assert response.model == "fake-model"
```

## 13. Async Unit Tests

Because `ChatService.execute()` is asynchronous:

```python
async def execute(...):
```

the test is asynchronous:

```python
@pytest.mark.asyncio
async def test_chat_service_returns_llm_response():
    ...
```

Then:

```python
response = await service.execute(request)
```

## 14. Error Handling

An empty LLM response is not considered a successful result.

```text
LLM
 ↓
""
 ↓
Validation
 ↓
LLMResponseError
```

Custom exception:

```python
class LLMResponseError(Exception):
    pass
```

Validation:

```python
response = await self.llm_provider.generate(
    request.message
)

if not response.strip():
    raise LLMResponseError(
        "LLM returned an empty response"
    )
```

`strip()` handles empty/whitespace-only responses such as `""`, `" "`, `"
"`, and `"	"`.

## 15. Testing Exceptions

Use `pytest.raises()`:

```python
@pytest.mark.asyncio
async def test_chat_service_raises_error_for_empty_llm_response():
    provider = EmptyLLMProvider()
    service = ChatService(provider)

    request = ChatRequest(
        message="Hello",
        model="fake-model",
    )

    with pytest.raises(LLMResponseError):
        await service.execute(request)
```

## 16. Error Categories

### Invalid Input

Example:

```text
message = ""
```

Typically 400/422 depending on the API contract.

### LLM Provider Failure

Example:

```text
OpenAI timeout
```

Potentially 502/503 depending on semantics.

### Internal Application Failure

Unexpected application error:

```text
500
```

Never expose internal stack traces or secrets to API consumers.

## 17. Future AI Platform Error Flow

```text
ChatService
     │
     ▼
LLMProvider
     │
 ┌───┴──────────────┐
 │                  │
Success           Failure
 │                  │
 ▼                  ▼
Response       Retry/Fallback
                   │
             ┌─────┴─────┐
             ▼           ▼
          Claude       Gemini
```

This will become part of our future model-routing/fallback design.

## 18. Important Architectural Lesson

Do not create abstractions just because they are possible.

Create abstractions when they solve a real problem.

For example, a dedicated response-validation component may become useful later when validation includes:
- Schema validation
- Safety checks
- Policy checks
- Hallucination checks
- Quality checks

But we should not create unnecessary abstractions prematurely.

## 19. Presentation vs Application Testing

### API/integration-style test

```text
HTTP
 ↓
FastAPI
 ↓
ChatService
 ↓
Provider
```

### Unit test

```text
ChatService
 ↓
Fake Provider
```

The unit test is faster and isolates application behavior.

Later we will use:
- Unit tests
- Integration tests
- API tests
- End-to-end tests

## 20. Final Day 3 Architecture

```text
                         FastAPI
                            │
                            ▼
                     API / Routes
                            │
                            ▼
                      ChatService
                            │
                            ▼
                      LLMProvider
                            ▲
                ┌───────────┼───────────┐
                │           │           │
              Mock         Fake       Empty
                │           │           │
                └───────────┼───────────┘
                            │
                            ▼
                       Validation
                            │
                 ┌──────────┴──────────┐
                 │                     │
               Valid                 Empty
                 │                     │
                 ▼                     ▼
           ChatResponse        LLMResponseError
```

## 21. Day 3 Interview Questions

**Why should `ChatService` not directly instantiate `OpenAIProvider`?**  
Because that tightly couples application logic to a concrete infrastructure implementation and makes provider replacement and testing harder.

**What is Dependency Injection?**  
Supplying dependencies to a component from outside rather than having the component construct them itself.

**What is Dependency Inversion?**  
High-level application logic should depend on abstractions rather than concrete low-level infrastructure.

**Why use `Protocol`?**  
To define an expected interface/contract while allowing compatible implementations to satisfy it through structural typing.

**Why use fake providers in unit tests?**  
To isolate application logic from external systems and make tests fast, deterministic, and inexpensive.

**Why shouldn't FastAPI routes contain business logic?**  
It couples business behavior to the transport layer and makes the logic harder to test, reuse, and evolve.

## 22. Completion

- [x] Clean Architecture
- [x] Presentation/Application/Domain/Infrastructure
- [x] `LLMProvider` abstraction
- [x] Python `Protocol`
- [x] Dependency Inversion
- [x] Dependency Injection
- [x] Fake provider testing
- [x] Async unit testing
- [x] Empty response validation
- [x] Custom application exception
- [x] Exception test
- [x] Ruff checks
- [x] pytest passed

**Status: COMPLETE**
