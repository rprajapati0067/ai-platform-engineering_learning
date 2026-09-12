import logging

from app.agents.base import BaseAIAgent
from app.agents.devils_advocate import DevilsAdvocateAgent
from app.domain.models import AIResearchReport
from app.infrastructure.mock_data.stocks_seed import get_stock_analysis_report

logger = logging.getLogger(__name__)


class MultiAgentSynthesizer(BaseAIAgent):
    """Synthesizes deterministic outputs and multi-agent reasoning into a final AI Research Report."""

    def __init__(self):
        super().__init__(agent_name="MultiAgentSynthesizer")
        self.devils_advocate = DevilsAdvocateAgent()

    async def analyze_stock(self, ticker: str) -> AIResearchReport | None:
        """Runs the full multi-agent workflow for a stock ticker."""
        # 1. Fetch structured financial, valuation, technicals, and news data
        report = get_stock_analysis_report(ticker)
        if not report:
            logger.warning(f"Stock {ticker} not found in database/seed repository.")
            return None

        # 2. Run Adversarial (Devil's Advocate) Agent to challenge thesis
        adv_results = await self.devils_advocate.challenge_thesis(
            profile=report.stock_profile, bull_bear=report.bull_bear_case
        )

        logger.info(
            f"Multi-agent report for {ticker} | Score={report.overall_score} | "
            f"Adversarial Flags={len(adv_results.get('adversarial_flags', []))}"
        )
        return report
