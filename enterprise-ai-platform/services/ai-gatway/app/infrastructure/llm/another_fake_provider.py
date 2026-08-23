class AnotherFakeLLMProvider:
    async def generate(self, prompt: str) -> str:
        return "Another response"
