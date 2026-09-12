from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/paper-trade", tags=["Paper Trading"])


class PaperTradeRequest(BaseModel):
    ticker: str
    action: str = Field(..., example="BUY")
    shares: int = Field(..., gt=0)
    entry_price: float
    stop_loss: float
    target_1: float
    target_2: float


class PaperTradeResponse(BaseModel):
    trade_id: str
    status: str
    message: str
    ticker: str
    shares: int
    total_invested: float


MOCK_PAPER_TRADES = [
    {
        "trade_id": "pt-101",
        "ticker": "RELIANCE",
        "action": "BUY",
        "shares": 67,
        "entry_price": 2940.0,
        "current_price": 2945.50,
        "stop_loss": 2850.0,
        "target_1": 3100.0,
        "target_2": 3250.0,
        "unrealized_pnl": 368.5,
        "unrealized_pnl_percent": 0.19,
        "status": "OPEN",
    }
]


@router.get("/positions")
async def get_paper_positions() -> list[dict]:
    """Get active paper trading positions."""
    return MOCK_PAPER_TRADES


@router.post("/execute", response_model=PaperTradeResponse)
async def execute_paper_trade(req: PaperTradeRequest) -> PaperTradeResponse:
    """Simulate paper execution of an AI-recommended trade."""
    total_val = round(req.shares * req.entry_price, 2)
    return PaperTradeResponse(
        trade_id=f"pt-{len(MOCK_PAPER_TRADES) + 101}",
        status="EXECUTED",
        message=f"Paper trade executed for {req.shares} shares of {req.ticker} @ ₹{req.entry_price}",
        ticker=req.ticker,
        shares=req.shares,
        total_invested=total_val,
    )
