from enum import Enum

from pydantic import BaseModel, Field


class RecommendationEnum(str, Enum):
    STRONG_BUY = "STRONG BUY"
    BUY = "BUY"
    ACCUMULATE = "ACCUMULATE"
    HOLD = "HOLD"
    WATCH = "WATCH"
    REDUCE = "REDUCE"
    SELL = "SELL"
    NO_TRADE = "NO TRADE"


class ValuationStatusEnum(str, Enum):
    DEEPLY_UNDERVALUED = "Deeply Undervalued"
    UNDERVALUED = "Undervalued"
    FAIRLY_VALUED = "Fairly Valued"
    EXPENSIVE = "Expensive"
    EXTREMELY_EXPENSIVE = "Extremely Expensive"


class StockProfile(BaseModel):
    ticker: str = Field(..., example="RELIANCE")
    name: str = Field(..., example="Reliance Industries Ltd")
    exchange: str = Field(default="NSE")
    sector: str = Field(..., example="Oil & Gas / Conglomerate")
    industry: str = Field(..., example="Refineries & Retail & Telecom")
    market_cap_cr: float = Field(..., description="Market Cap in INR Crores")
    current_price: float
    day_change_percent: float
    week_52_high: float
    week_52_low: float


class FinancialYear(BaseModel):
    year: int
    revenue_cr: float
    ebitda_cr: float
    pat_cr: float
    eps: float
    operating_cash_flow_cr: float
    free_cash_flow_cr: float
    roe_percent: float
    roce_percent: float
    debt_to_equity: float
    interest_coverage: float


class ValuationMetrics(BaseModel):
    pe_ratio: float
    pb_ratio: float
    ev_ebitda: float
    peg_ratio: float
    fcf_yield_percent: float
    dividend_yield_percent: float
    pe_3y_median: float
    pe_5y_median: float
    pe_10y_median: float
    valuation_status: ValuationStatusEnum
    pe_discount_to_10y_percent: float


class TechnicalMetrics(BaseModel):
    dma_20: float
    dma_50: float
    dma_100: float
    dma_200: float
    rsi_14: float
    macd_signal: str
    atr_14: float
    volume_surge_ratio: float
    trend_status: str


class NewsEvent(BaseModel):
    id: str
    headline: str
    source: str
    published_at: str
    sentiment: str  # Positive, Neutral, Negative
    materiality: str  # High, Medium, Low
    is_structural: bool
    thesis_impact: str  # Positive, Neutral, Negative
    summary: str


class BullBearCase(BaseModel):
    bull_reasons: list[str]
    bear_reasons: list[str]
    key_risks: list[str]


class TradeSetup(BaseModel):
    recommendation: RecommendationEnum
    accumulation_zone_min: float
    accumulation_zone_max: float
    fair_value_min: float
    fair_value_max: float
    overvaluation_threshold: float
    suggested_entry_min: float
    suggested_entry_max: float
    target_1: float
    target_2: float
    stop_loss: float
    risk_reward_ratio_t1: float
    risk_reward_ratio_t2: float
    expected_holding_period: str
    confidence_score: int = Field(..., ge=0, le=100)


class PositionSizingInput(BaseModel):
    portfolio_value: float = Field(
        default=1000000.0, description="Total Portfolio Value in INR"
    )
    max_risk_percent: float = Field(
        default=1.0, description="Max acceptable risk % per trade"
    )
    entry_price: float
    stop_loss_price: float
    max_position_percent: float = Field(
        default=20.0, description="Cap on single stock allocation"
    )


class PositionSizeRecommendation(BaseModel):
    portfolio_value: float
    max_risk_amount: float
    risk_per_share: float
    max_shares: int
    recommended_position_value: float
    portfolio_exposure_percent: float


class AIResearchReport(BaseModel):
    stock_profile: StockProfile
    overall_score: float = Field(..., ge=0.0, le=10.0)
    confidence_score: int = Field(..., ge=0, le=100)
    score_breakdown: dict[str, float]
    recommendation: RecommendationEnum
    trade_setup: TradeSetup
    position_sizing: PositionSizeRecommendation
    bull_bear_case: BullBearCase
    financial_history: list[FinancialYear]
    valuation: ValuationMetrics
    technicals: TechnicalMetrics
    recent_news: list[NewsEvent]
    thesis_summary: str
    disclaimer: str = Field(
        default="This AI research report is for informational and educational purposes only. "
        "It does not guarantee profits or constitute financial advice."
    )
