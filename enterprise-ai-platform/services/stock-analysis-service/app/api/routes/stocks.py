from fastapi import APIRouter, HTTPException, Query

from app.agents.synthesizer import MultiAgentSynthesizer
from app.domain.calculations import calculate_position_size
from app.domain.models import (
    AIResearchReport,
    PositionSizeRecommendation,
    PositionSizingInput,
    StockProfile,
)
from app.infrastructure.mock_data.stocks_seed import STOCKS_SEED_DATA

router = APIRouter(prefix="/api/stocks", tags=["Stock Research"])
synthesizer = MultiAgentSynthesizer()


@router.get("/search", response_model=list[StockProfile])
async def search_stocks(q: str = Query("", min_length=0)) -> list[StockProfile]:
    """Search stocks by ticker or company name."""
    query = q.upper().strip()
    results = []

    for data in STOCKS_SEED_DATA.values():
        profile: StockProfile = data["profile"]
        if not query or query in profile.ticker or query in profile.name.upper():
            results.append(profile)

    return results


@router.get("/{ticker}/analysis", response_model=AIResearchReport)
async def get_stock_analysis(ticker: str) -> AIResearchReport:
    """Generate or retrieve a full 6-agent AI Research Report for a stock."""
    report = await synthesizer.analyze_stock(ticker)
    if not report:
        raise HTTPException(
            status_code=404,
            detail=f"Stock ticker '{ticker}' not found. Try searching for 'RELIANCE' or 'TCS'.",
        )
    return report


@router.post("/position-size/calculate", response_model=PositionSizeRecommendation)
async def calculate_risk_position_size(
    inp: PositionSizingInput,
) -> PositionSizeRecommendation:
    """Calculate exact risk-based position sizing (Zero hallucination risk)."""
    return calculate_position_size(inp)
