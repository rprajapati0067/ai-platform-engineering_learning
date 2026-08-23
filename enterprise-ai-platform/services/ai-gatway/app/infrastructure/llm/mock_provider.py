class MockLLMProvider:
    async def generate(self, prompt: str) -> str:
        return f"Mock response to: {prompt}"
