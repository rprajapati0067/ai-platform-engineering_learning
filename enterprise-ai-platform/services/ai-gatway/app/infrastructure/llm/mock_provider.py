from opentelemetry import trace

tracer = trace.get_tracer(__name__)


class MockLLMProvider:
    async def generate(self, prompt: str, model: str = "mock") -> str:
        with tracer.start_as_current_span("llm.generate") as span:
            span.set_attribute("llm.model", model)
            span.set_attribute("llm.provider", "mock")

            return f"Mock response to: {prompt}"
