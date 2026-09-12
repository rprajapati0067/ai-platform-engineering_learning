# Architecture, Dependency Inversion & Testing

## Provider abstraction
`ChatService` depends on an `LLMProvider` abstraction rather than a concrete provider.

```text
ChatService
    ↓
LLMProvider
    ├── MockLLMProvider
    ├── FakeLLMProvider
    └── Real provider later
```

This makes provider implementations replaceable and testable.

## Validation boundary
Request validation belongs at the API/domain boundary rather than coupling application services to HTTP validation concerns.

## Empty response handling
The service rejects empty/whitespace-only provider responses:

```python
if not response.strip():
    raise LLMResponseError("LLM returned an empty response")
```

## Tests
Tests cover:
- successful provider response
- alternate provider implementation
- empty provider response raising `LLMResponseError`

Production lesson: provider/model choices change frequently, so the application service should depend on an abstraction.
