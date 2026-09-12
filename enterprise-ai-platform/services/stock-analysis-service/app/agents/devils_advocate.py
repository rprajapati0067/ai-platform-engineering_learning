from typing import Any

from app.agents.base import BaseAIAgent
from app.domain.models import BullBearCase, StockProfile


class DevilsAdvocateAgent(BaseAIAgent):
    """Adversarial AI Agent specifically tasked with disproving the BUY thesis."""

    def __init__(self):
        super().__init__(agent_name="DevilsAdvocateAgent")

    async def challenge_thesis(
        self, profile: StockProfile, bull_bear: BullBearCase
    ) -> dict[str, Any]:
        """Critically evaluates stock risks and challenges optimism."""
        prompt = (
            f"You are a skeptic short-seller and risk auditor analyzing {profile.name} ({profile.ticker}).\n"
            f"Current Bull Case: {', '.join(bull_bear.bull_reasons)}\n"
            "Identify 3 subtle risks or reasons this investment could underperform over the next 12-24 months."
        )

        llm_response = await self.call_llm(prompt)

        adversarial_flags = [
            "Valuation risks if growth slows below market expectations.",
            f"Regulatory or sector headwinds in {profile.sector}.",
            "Operating margin pressure from input cost inflation.",
        ]

        if llm_response:
            # Parse or format LLM response if available
            pass

        return {
            "adversarial_score_penalty": 0.5,
            "adversarial_flags": adversarial_flags,
            "llm_insight": llm_response,
        }
