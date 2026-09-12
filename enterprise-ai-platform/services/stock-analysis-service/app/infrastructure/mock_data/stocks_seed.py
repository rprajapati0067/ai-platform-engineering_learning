from app.domain.calculations import (
    calculate_position_size,
    calculate_valuation_status,
    calculate_weighted_score,
    generate_trade_setup,
)
from app.domain.models import (
    AIResearchReport,
    BullBearCase,
    FinancialYear,
    NewsEvent,
    PositionSizingInput,
    StockProfile,
    TechnicalMetrics,
    ValuationMetrics,
)

STOCKS_SEED_DATA: dict[str, dict] = {
    "RELIANCE": {
        "profile": StockProfile(
            ticker="RELIANCE",
            name="Reliance Industries Limited",
            exchange="NSE",
            sector="Energy & Conglomerate",
            industry="Oil & Gas, Retail, Digital Services (Jio)",
            market_cap_cr=1980000.0,
            current_price=2945.50,
            day_change_percent=1.25,
            week_52_high=3024.90,
            week_52_low=2220.30,
        ),
        "score_components": {
            "fundamentals": 9.1,
            "financial_strength": 8.7,
            "growth": 8.9,
            "valuation": 6.4,
            "news": 8.2,
            "technicals": 9.0,
            "market_regime": 7.5,
            "risk_quality": 7.8,
        },
        "valuation_raw": {
            "pe": 24.5,
            "pb": 2.4,
            "ev_ebitda": 14.2,
            "peg": 1.6,
            "fcf_yield": 3.8,
            "div_yield": 0.35,
            "pe_3y": 25.1,
            "pe_5y": 26.8,
            "pe_10y": 19.4,
        },
        "technicals": TechnicalMetrics(
            dma_20=2910.0,
            dma_50=2850.0,
            dma_100=2780.0,
            dma_200=2640.0,
            rsi_14=62.4,
            macd_signal="Bullish Crossover",
            atr_14=42.5,
            volume_surge_ratio=1.45,
            trend_status="Strong Uptrend",
        ),
        "financial_history": [
            FinancialYear(
                year=2015,
                revenue_cr=375435.0,
                ebitda_cr=37375.0,
                pat_cr=23566.0,
                eps=36.4,
                operating_cash_flow_cr=35400.0,
                free_cash_flow_cr=12400.0,
                roe_percent=10.5,
                roce_percent=11.2,
                debt_to_equity=0.45,
                interest_coverage=7.8,
            ),
            FinancialYear(
                year=2018,
                revenue_cr=408265.0,
                ebitda_cr=64141.0,
                pat_cr=36075.0,
                eps=55.8,
                operating_cash_flow_cr=62500.0,
                free_cash_flow_cr=18200.0,
                roe_percent=12.8,
                roce_percent=13.5,
                debt_to_equity=0.72,
                interest_coverage=6.2,
            ),
            FinancialYear(
                year=2021,
                revenue_cr=466924.0,
                ebitda_cr=80737.0,
                pat_cr=49128.0,
                eps=76.2,
                operating_cash_flow_cr=82400.0,
                free_cash_flow_cr=24100.0,
                roe_percent=11.1,
                roce_percent=10.8,
                debt_to_equity=0.42,
                interest_coverage=8.4,
            ),
            FinancialYear(
                year=2024,
                revenue_cr=900384.0,
                ebitda_cr=178677.0,
                pat_cr=69624.0,
                eps=102.8,
                operating_cash_flow_cr=145800.0,
                free_cash_flow_cr=48200.0,
                roe_percent=12.4,
                roce_percent=14.1,
                debt_to_equity=0.38,
                interest_coverage=9.6,
            ),
        ],
        "news_events": [
            NewsEvent(
                id="news-rel-1",
                headline="Jio Platforms Reports 12% YoY ARPU Growth Driven by 5G Upgrades",
                source="Economic Times",
                published_at="2026-09-10T10:30:00Z",
                sentiment="Positive",
                materiality="High",
                is_structural=True,
                thesis_impact="Positive",
                summary="Jio ARPU reached INR 195/month as 5G subscriber migration accelerated, strengthening telecom free cash flows.",
            ),
            NewsEvent(
                id="news-rel-2",
                headline="Reliance New Energy Solar Gigafactory Prepares for Q4 Commercial Launch",
                source="LiveMint",
                published_at="2026-09-08T14:15:00Z",
                sentiment="Positive",
                materiality="High",
                is_structural=True,
                thesis_impact="Positive",
                summary="Solar cell production line setup in Jamnagar completes trial runs, unlocking new green energy revenue streams.",
            ),
            NewsEvent(
                id="news-rel-3",
                headline="Global Refining Margins Ease Slightly Amid Crude Oil Price Stabilization",
                source="Reuters",
                published_at="2026-09-05T09:00:00Z",
                sentiment="Neutral",
                materiality="Medium",
                is_structural=False,
                thesis_impact="Neutral",
                summary="O2C segment gross refining margins (GRM) expected to remain range-bound at $10.5/bbl.",
            ),
        ],
        "bull_bear_case": BullBearCase(
            bull_reasons=[
                "Market leader in Telecom (Jio 450M+ users) and Organised Retail (18,000+ stores).",
                "Strong compounding in cash flows driven by 5G ARPU growth and retail margin expansion.",
                "Massive value-unlock potential via potential IPOs of Jio and Retail subsidiaries.",
                "Jamnagar New Energy giga-factories positioning for long-term decarbonization growth.",
            ],
            bear_reasons=[
                "Valuation trailing P/E of 24.5x sits at a premium to historical 10-year median (19.4x).",
                "High ongoing capital expenditure in green energy may suppress dividend payouts.",
                "Global refining margin cyclicality impacting Oil-to-Chemicals (O2C) earnings.",
            ],
            key_risks=[
                "Regulatory tariffs intervention in telecom.",
                "Volatility in Brent crude prices and refining crack spreads.",
                "Execution delays in green hydrogen and solar gigafactories.",
            ],
        ),
        "thesis_summary": (
            "Reliance Industries remains a quintessential core portfolio compounder. "
            "The multi-engine transition from O2C cash cow to high-growth Consumer Tech (Jio) "
            "and Retail, backed by new energy initiatives, underpins multi-year compounding. "
            "Accumulating on technical pullbacks near the 50 DMA provides attractive risk-adjusted entry."
        ),
    },
    "TCS": {
        "profile": StockProfile(
            ticker="TCS",
            name="Tata Consultancy Services Ltd",
            exchange="NSE",
            sector="Information Technology",
            industry="IT Services & Consulting",
            market_cap_cr=1520000.0,
            current_price=4180.00,
            day_change_percent=-0.45,
            week_52_high=4585.00,
            week_52_low=3400.00,
        ),
        "score_components": {
            "fundamentals": 9.4,
            "financial_strength": 9.8,
            "growth": 7.2,
            "valuation": 7.5,
            "news": 7.8,
            "technicals": 7.0,
            "market_regime": 6.8,
            "risk_quality": 9.2,
        },
        "valuation_raw": {
            "pe": 29.2,
            "pb": 12.8,
            "ev_ebitda": 21.0,
            "peg": 2.2,
            "fcf_yield": 3.4,
            "div_yield": 1.25,
            "pe_3y": 30.5,
            "pe_5y": 31.2,
            "pe_10y": 24.8,
        },
        "technicals": TechnicalMetrics(
            dma_20=4210.0,
            dma_50=4150.0,
            dma_100=4020.0,
            dma_200=3890.0,
            rsi_14=51.2,
            macd_signal="Neutral Consolidation",
            atr_14=55.0,
            volume_surge_ratio=0.95,
            trend_status="Consolidation",
        ),
        "financial_history": [
            FinancialYear(
                year=2015,
                revenue_cr=94648.0,
                ebitda_cr=26210.0,
                pat_cr=19852.0,
                eps=101.2,
                operating_cash_flow_cr=19200.0,
                free_cash_flow_cr=17100.0,
                roe_percent=38.4,
                roce_percent=46.2,
                debt_to_equity=0.0,
                interest_coverage=99.0,
            ),
            FinancialYear(
                year=2024,
                revenue_cr=240893.0,
                ebitda_cr=64120.0,
                pat_cr=46099.0,
                eps=127.4,
                operating_cash_flow_cr=44300.0,
                free_cash_flow_cr=39800.0,
                roe_percent=48.2,
                roce_percent=59.1,
                debt_to_equity=0.0,
                interest_coverage=99.0,
            ),
        ],
        "news_events": [
            NewsEvent(
                id="news-tcs-1",
                headline="TCS Signs $1.2B Multi-Year Cloud & Generative AI Transformation Deal with European Bank",
                source="CNBC TV18",
                published_at="2026-09-11T08:00:00Z",
                sentiment="Positive",
                materiality="High",
                is_structural=True,
                thesis_impact="Positive",
                summary="Generative AI pipeline total deal value (TCV) crosses $1.5 billion in Q2.",
            )
        ],
        "bull_bear_case": BullBearCase(
            bull_reasons=[
                "Zero net debt balance sheet with industry-leading ROE (>45%).",
                "Massive global delivery scale and deep relationships with Fortune 500 enterprises.",
                "High dividend payout ratio returning 80%+ of free cash flows to shareholders.",
            ],
            bear_reasons=[
                "Slowdown in discretionary IT spending in North America & Europe.",
                "Talent wage inflation and pricing competition in legacy app maintenance.",
            ],
            key_risks=[
                "US Dollar / INR currency volatility.",
                "US H-1B visa policy changes.",
            ],
        ),
        "thesis_summary": (
            "TCS is a fortress balance sheet compounder. "
            "While short-term discretionary IT demand is cautious, enterprise GenAI modernization deals "
            "provide long-term growth resilience."
        ),
    },
}


def get_stock_analysis_report(ticker: str) -> AIResearchReport | None:
    """Retrieve or compute a full AI Research Report for a given ticker."""
    stock_key = ticker.upper().strip()
    if stock_key not in STOCKS_SEED_DATA:
        return None

    data = STOCKS_SEED_DATA[stock_key]
    profile: StockProfile = data["profile"]
    scores: dict[str, float] = data["score_components"]
    val_raw = data["valuation_raw"]
    technicals: TechnicalMetrics = data["technicals"]
    fin_history: list[FinancialYear] = data["financial_history"]
    news: list[NewsEvent] = data["news_events"]
    bull_bear: BullBearCase = data["bull_bear_case"]

    val_status, pe_discount = calculate_valuation_status(
        val_raw["pe"], val_raw["pe_10y"]
    )

    valuation = ValuationMetrics(
        pe_ratio=val_raw["pe"],
        pb_ratio=val_raw["pb"],
        ev_ebitda=val_raw["ev_ebitda"],
        peg_ratio=val_raw["peg"],
        fcf_yield_percent=val_raw["fcf_yield"],
        dividend_yield_percent=val_raw["div_yield"],
        pe_3y_median=val_raw["pe_3y"],
        pe_5y_median=val_raw["pe_5y"],
        pe_10y_median=val_raw["pe_10y"],
        valuation_status=val_status,
        pe_discount_to_10y_percent=pe_discount,
    )

    overall_score = calculate_weighted_score(scores)

    trade_setup = generate_trade_setup(
        current_price=profile.current_price,
        overall_score=overall_score,
        valuation_status=val_status,
        atr_14=technicals.atr_14,
    )

    pos_input = PositionSizingInput(
        portfolio_value=1000000.0,
        max_risk_percent=1.0,
        entry_price=profile.current_price,
        stop_loss_price=trade_setup.stop_loss,
        max_position_percent=20.0,
    )
    pos_recommendation = calculate_position_size(pos_input)

    return AIResearchReport(
        stock_profile=profile,
        overall_score=overall_score,
        confidence_score=trade_setup.confidence_score,
        score_breakdown=scores,
        recommendation=trade_setup.recommendation,
        trade_setup=trade_setup,
        position_sizing=pos_recommendation,
        bull_bear_case=bull_bear,
        financial_history=fin_history,
        valuation=valuation,
        technicals=technicals,
        recent_news=news,
        thesis_summary=data["thesis_summary"],
    )
