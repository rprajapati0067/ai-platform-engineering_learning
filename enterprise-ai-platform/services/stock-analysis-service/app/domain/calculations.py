import math

from app.domain.models import (
    PositionSizeRecommendation,
    PositionSizingInput,
    RecommendationEnum,
    TradeSetup,
    ValuationStatusEnum,
)


def calculate_cagr(start_val: float, end_val: float, years: int) -> float:
    """Calculate Compound Annual Growth Rate (%) with safety checks."""
    if start_val <= 0 or end_val <= 0 or years <= 0:
        return 0.0
    return round((math.pow(end_val / start_val, 1 / years) - 1) * 100, 2)


def calculate_valuation_status(
    current_pe: float, pe_10y_median: float
) -> tuple[ValuationStatusEnum, float]:
    """Calculate valuation discount/premium relative to 10y median and classify status."""
    if pe_10y_median <= 0:
        return ValuationStatusEnum.FAIRLY_VALUED, 0.0

    discount_percent = round(((pe_10y_median - current_pe) / pe_10y_median) * 100, 2)

    if discount_percent >= 25.0:
        status = ValuationStatusEnum.DEEPLY_UNDERVALUED
    elif discount_percent >= 10.0:
        status = ValuationStatusEnum.UNDERVALUED
    elif discount_percent >= -10.0:
        status = ValuationStatusEnum.FAIRLY_VALUED
    elif discount_percent >= -25.0:
        status = ValuationStatusEnum.EXPENSIVE
    else:
        status = ValuationStatusEnum.EXTREMELY_EXPENSIVE

    return status, discount_percent


def calculate_position_size(
    inp: PositionSizingInput,
) -> PositionSizeRecommendation:
    """Risk-based position sizing formula (Deterministic, 0 risk of math error)."""
    max_risk_amount = inp.portfolio_value * (inp.max_risk_percent / 100.0)
    risk_per_share = max(0.01, inp.entry_price - inp.stop_loss_price)

    raw_shares = math.floor(max_risk_amount / risk_per_share)
    max_position_cap = inp.portfolio_value * (inp.max_position_percent / 100.0)
    max_cap_shares = math.floor(max_position_cap / inp.entry_price)

    final_shares = max(0, min(raw_shares, max_cap_shares))
    recommended_value = round(final_shares * inp.entry_price, 2)
    exposure_percent = round((recommended_value / inp.portfolio_value) * 100, 2)

    return PositionSizeRecommendation(
        portfolio_value=inp.portfolio_value,
        max_risk_amount=round(max_risk_amount, 2),
        risk_per_share=round(risk_per_share, 2),
        max_shares=final_shares,
        recommended_position_value=recommended_value,
        portfolio_exposure_percent=exposure_percent,
    )


def calculate_weighted_score(components: dict[str, float]) -> float:
    """Calculate overall weighted score (0.0 to 10.0) based on specification weights."""
    weights = {
        "fundamentals": 0.25,
        "financial_strength": 0.15,
        "growth": 0.15,
        "valuation": 0.15,
        "news": 0.10,
        "technicals": 0.10,
        "market_regime": 0.05,
        "risk_quality": 0.05,
    }

    total_score = 0.0
    for key, weight in weights.items():
        score = components.get(key, 7.0)
        # Clamp score between 0.0 and 10.0
        clamped_score = max(0.0, min(10.0, score))
        total_score += clamped_score * weight

    return round(total_score, 1)


def generate_trade_setup(
    current_price: float,
    overall_score: float,
    valuation_status: ValuationStatusEnum,
    atr_14: float,
) -> TradeSetup:
    """Generate trade parameters, entry zones, targets, and stop-loss deterministically."""
    # Determine base recommendation from overall score
    if overall_score >= 8.5:
        recommendation = RecommendationEnum.STRONG_BUY
    elif overall_score >= 7.8:
        recommendation = RecommendationEnum.BUY
    elif overall_score >= 7.0:
        recommendation = RecommendationEnum.ACCUMULATE
    elif overall_score >= 5.5:
        recommendation = RecommendationEnum.HOLD
    elif overall_score >= 4.5:
        recommendation = RecommendationEnum.WATCH
    elif overall_score >= 3.5:
        recommendation = RecommendationEnum.REDUCE
    else:
        recommendation = RecommendationEnum.SELL

    # Determine zones based on current price & volatility (ATR)
    atr = max(atr_14, current_price * 0.02)

    accumulation_min = round(current_price - (1.5 * atr), 2)
    accumulation_max = round(current_price - (0.3 * atr), 2)

    fair_val_min = round(current_price * 0.98, 2)
    fair_val_max = round(current_price * 1.12, 2)
    overval_threshold = round(current_price * 1.25, 2)

    entry_min = round(current_price * 0.96, 2)
    entry_max = round(current_price * 0.99, 2)

    stop_loss = round(current_price - (2.0 * atr), 2)
    target_1 = round(current_price + (2.5 * atr), 2)
    target_2 = round(current_price + (4.5 * atr), 2)

    risk = max(0.01, current_price - stop_loss)
    rr_t1 = round((target_1 - current_price) / risk, 2)
    rr_t2 = round((target_2 - current_price) / risk, 2)

    confidence = min(95, max(50, int(overall_score * 10 + 2)))

    return TradeSetup(
        recommendation=recommendation,
        accumulation_zone_min=accumulation_min,
        accumulation_zone_max=accumulation_max,
        fair_value_min=fair_val_min,
        fair_value_max=fair_val_max,
        overvaluation_threshold=overval_threshold,
        suggested_entry_min=entry_min,
        suggested_entry_max=entry_max,
        target_1=target_1,
        target_2=target_2,
        stop_loss=stop_loss,
        risk_reward_ratio_t1=rr_t1,
        risk_reward_ratio_t2=rr_t2,
        expected_holding_period="4 to 12 weeks",
        confidence_score=confidence,
    )
