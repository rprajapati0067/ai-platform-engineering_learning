class FakeLLMProvider:
    async def generate(self, prompt: str) -> str:
        return f"Fake AI response: {prompt}"
