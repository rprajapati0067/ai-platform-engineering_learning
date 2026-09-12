import logging

import httpx

logger = logging.getLogger(__name__)


class BaseAIAgent:
    """Base class for specialized financial AI agents."""

    def __init__(self, agent_name: str, ai_gateway_url: str = "http://localhost:8000"):
        self.agent_name = agent_name
        self.ai_gateway_url = ai_gateway_url

    async def call_llm(self, prompt: str) -> str | None:
        """Calls the AI Gateway endpoint with fallback handling."""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(
                    f"{self.ai_gateway_url}/chat",
                    json={"message": prompt, "model": "gemini-3.6-flash"},
                )
                if resp.status_code == 200:
                    data = resp.json()
                    return data.get("response")
        except httpx.HTTPError as err:
            logger.warning(
                f"[{self.agent_name}] AI Gateway call failed: {err}. Using deterministic agent fallback."
            )
        return None
