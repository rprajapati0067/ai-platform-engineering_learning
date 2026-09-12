from fastapi.testclient import TestClient

from app.domain.calculations import (
    calculate_cagr,
    calculate_position_size,
    calculate_valuation_status,
    calculate_weighted_score,
)
from app.domain.models import PositionSizingInput, ValuationStatusEnum
from app.main import app

client = TestClient(app)


def test_calculate_cagr():
    # 100 to 200 in 5 years is ~14.87%
    cagr = calculate_cagr(100, 200, 5)
    assert cagr == 14.87

    # Edge cases
    assert calculate_cagr(0, 100, 5) == 0.0
    assert calculate_cagr(100, 200, 0) == 0.0


def test_calculate_valuation_status():
    # Current PE 19.4 vs 10y median 19.4 -> Fairly Valued (0% discount)
    status, discount = calculate_valuation_status(19.4, 19.4)
    assert status == ValuationStatusEnum.FAIRLY_VALUED
    assert discount == 0.0

    # Current PE 14.0 vs 10y median 20.0 -> Deeply Undervalued (30% discount)
    status, discount = calculate_valuation_status(14.0, 20.0)
    assert status == ValuationStatusEnum.DEEPLY_UNDERVALUED
    assert discount == 30.0

    # Current PE 30.0 vs 10y median 20.0 -> Extremely Expensive (-50% discount)
    status, discount = calculate_valuation_status(30.0, 20.0)
    assert status == ValuationStatusEnum.EXTREMELY_EXPENSIVE
    assert discount == -50.0


def test_risk_position_sizer():
    # Portfolio: 1,000,000 INR
    # Max risk: 1% (10,000 INR)
    # Entry: 500 INR, Stop Loss: 475 INR -> Risk/share = 25 INR
    # Max shares = 10,000 / 25 = 400 shares (Value = 200,000 INR = 20% cap)
    inp = PositionSizingInput(
        portfolio_value=1000000.0,
        max_risk_percent=1.0,
        entry_price=500.0,
        stop_loss_price=475.0,
        max_position_percent=20.0,
    )
    res = calculate_position_size(inp)
    assert res.max_risk_amount == 10000.0
    assert res.risk_per_share == 25.0
    assert res.max_shares == 400
    assert res.recommended_position_value == 200000.0
    assert res.portfolio_exposure_percent == 20.0


def test_weighted_score():
    scores = {
        "fundamentals": 9.0,
        "financial_strength": 9.0,
        "growth": 9.0,
        "valuation": 9.0,
        "news": 9.0,
        "technicals": 9.0,
        "market_regime": 9.0,
        "risk_quality": 9.0,
    }
    assert calculate_weighted_score(scores) == 9.0


def test_api_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"


def test_api_stock_search():
    res = client.get("/api/stocks/search?q=rel")
    assert res.status_code == 200
    data = res.json()
    assert len(data) >= 1
    assert data[0]["ticker"] == "RELIANCE"


def test_api_stock_analysis():
    res = client.get("/api/stocks/RELIANCE/analysis")
    assert res.status_code == 200
    data = res.json()
    assert data["stock_profile"]["ticker"] == "RELIANCE"
    assert data["overall_score"] >= 7.0
    assert "trade_setup" in data
    assert "position_sizing" in data
    assert "bull_bear_case" in data
    assert len(data["bull_bear_case"]["bull_reasons"]) > 0
