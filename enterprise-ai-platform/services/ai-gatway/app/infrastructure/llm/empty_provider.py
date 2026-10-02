class EmptyLLMProvider:
    async def generate(self, prompt: str, model: str = "fake") -> str:
        return ""
