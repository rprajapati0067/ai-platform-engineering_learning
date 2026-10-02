class FakeLLMProvider:
    async def generate(self, prompt: str, model: str = "fake") -> str:
        return f"Fake AI response: {prompt}"
