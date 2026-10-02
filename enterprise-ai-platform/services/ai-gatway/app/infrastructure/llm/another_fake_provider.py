class AnotherFakeLLMProvider:
    async def generate(self, prompt: str, model: str = "fake") -> str:
        return "Another response"
