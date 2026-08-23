class EmptyLLMProvider:
    async def generate(self, prompt: str) -> str:
        return ""
