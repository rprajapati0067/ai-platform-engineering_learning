# Clean Architecture, Dependency Inversion and Testing

## Current Flow

```text
HTTP Route
 ↓
ChatService
 ↓
LLMProvider
 ↓
Concrete Provider
```

## Provider Abstraction

```text
LLMProvider
   ↑
   ├── MockLLMProvider
   ├── FakeLLMProvider
   └── Future real providers
```

`ChatService` depends on the abstraction rather than a concrete provider.

This is dependency inversion and makes providers replaceable without changing application logic.

## Error Handling
We created:

```python
class LLMResponseError(Exception):
    pass
```

and reject blank provider output:

```python
if not response.strip():
    raise LLMResponseError("LLM returned an empty response")
```

## Tests
Tests cover:
- normal provider response
- alternative provider implementation
- empty provider response

Pattern:

```python
with pytest.raises(LLMResponseError):
    await service.execute(request)
```

## Architecture Principles
- Keep routes thin.
- Keep application services independent of infrastructure details.
- Depend on abstractions, not concrete LLM implementations.
- Test behavior rather than implementation details.
- Use Arrange → Act → Assert.
