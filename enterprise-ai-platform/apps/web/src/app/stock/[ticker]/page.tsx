'use client';

import React, { useState } from 'react';
import {
  TrendingUp,
  ShieldCheck,
  Award,
  AlertOctagon,
  CheckCircle2,
  XCircle,
  Calculator,
  ArrowUpRight,
  Newspaper,
  Layers,
  Sparkles,
} from 'lucide-react';

export default function StockResearchPage({ params }: { params: { ticker: string } }) {
  const tickerSymbol = params.ticker ? params.ticker.toUpperCase() : 'RELIANCE';

  // State for Position Sizing Calculator
  const [portfolioValue, setPortfolioValue] = useState(1000000);
  const [riskPercent, setRiskPercent] = useState(1.0);
  const [maxPositionCap, setMaxPositionCap] = useState(20.0);

  // Stock Mock Data
  const stock = {
    ticker: tickerSymbol,
    name: tickerSymbol === 'TCS' ? 'Tata Consultancy Services Ltd' : 'Reliance Industries Limited',
    sector: tickerSymbol === 'TCS' ? 'Information Technology' : 'Energy & Conglomerate',
    industry: tickerSymbol === 'TCS' ? 'IT Services & Consulting' : 'Oil & Gas, Retail, Telecom (Jio)',
    marketCap: tickerSymbol === 'TCS' ? '₹15,20,000 Cr' : '₹19,80,000 Cr',
    currentPrice: tickerSymbol === 'TCS' ? 4180.0 : 2945.5,
    dayChange: tickerSymbol === 'TCS' ? '-0.45%' : '+1.25%',
    week52High: tickerSymbol === 'TCS' ? 4585.0 : 3024.9,
    week52Low: tickerSymbol === 'TCS' ? 3400.0 : 2220.3,
    overallScore: tickerSymbol === 'TCS' ? 8.4 : 8.2,
    confidenceScore: tickerSymbol === 'TCS' ? 87 : 84,
    recommendation: tickerSymbol === 'TCS' ? 'BUY' : 'ACCUMULATE',
    valuationStatus: 'Moderately Expensive (24.5x P/E vs 19.4x 10Y Median)',
    scoreBreakdown: {
      fundamentals: 9.1,
      financialStrength: 8.7,
      growth: 8.9,
      valuation: 6.4,
      news: 8.2,
      technicals: 9.0,
      marketRegime: 7.5,
      riskQuality: 7.8,
    },
    tradeSetup: {
      accumulationZone: tickerSymbol === 'TCS' ? '₹4,120 - ₹4,170' : '₹2,910 - ₹2,940',
      fairValue: tickerSymbol === 'TCS' ? '₹4,180 - ₹4,400' : '₹2,945 - ₹3,150',
      target1: tickerSymbol === 'TCS' ? 4450.0 : 3120.0,
      target2: tickerSymbol === 'TCS' ? 4650.0 : 3250.0,
      stopLoss: tickerSymbol === 'TCS' ? 3980.0 : 2840.0,
      rrRatio: tickerSymbol === 'TCS' ? '2.40' : '2.25',
      expectedHolding: '4 to 12 weeks',
    },
    bullReasons: [
      'Market leader in core business with robust free cash flow compounding.',
      'Jio 5G ARPU expansion & Retail margin improvement driving operating leverage.',
      'Value unlock potential via strategic subsidiary IPOs.',
      'Strong green energy gigafactory execution positioning for decarbonization.',
    ],
    bearReasons: [
      'Current P/E sits at a premium to historical 10-year median.',
      'High ongoing green energy capex may temporarily limit dividend payouts.',
      'O2C segment gross refining margins exposed to global crude volatility.',
    ],
    keyRisks: [
      'Regulatory tariff intervention in telecom.',
      'Volatility in crude crack spreads.',
      'Execution delays in green hydrogen projects.',
    ],
    financialHistory: [
      { year: 2015, revenue: '3,75,435', pat: '23,566', eps: 36.4, roe: '10.5%', debtToEquity: '0.45' },
      { year: 2018, revenue: '4,08,265', pat: '36,075', eps: 55.8, roe: '12.8%', debtToEquity: '0.72' },
      { year: 2021, revenue: '4,66,924', pat: '49,128', eps: 76.2, roe: '11.1%', debtToEquity: '0.42' },
      { year: 2024, revenue: '9,00,384', pat: '69,624', eps: 102.8, roe: '12.4%', debtToEquity: '0.38' },
    ],
    recentNews: [
      {
        headline: 'Jio Platforms Reports 12% YoY ARPU Growth Driven by 5G Upgrades',
        source: 'Economic Times',
        sentiment: 'Positive',
        materiality: 'High',
        isStructural: true,
        summary: 'ARPU reached INR 195/month as 5G migration accelerated telecom cash flows.',
      },
      {
        headline: 'Jamnagar Solar Gigafactory Prepares for Commercial Trials',
        source: 'LiveMint',
        sentiment: 'Positive',
        materiality: 'High',
        isStructural: true,
        summary: 'Solar cell production line setup completes trial runs in Jamnagar.',
      },
    ],
  };

  // Deterministic Position Sizing Calculations
  const maxRiskAmount = portfolioValue * (riskPercent / 100.0);
  const riskPerShare = Math.max(0.01, stock.currentPrice - stock.tradeSetup.stopLoss);
  const rawShares = Math.floor(maxRiskAmount / riskPerShare);
  const maxCapAmount = portfolioValue * (maxPositionCap / 100.0);
  const maxCapShares = Math.floor(maxCapAmount / stock.currentPrice);
  const finalRecommendedShares = Math.max(0, Math.min(rawShares, maxCapShares));
  const recommendedCapitalNum = finalRecommendedShares * stock.currentPrice;
  const recommendedCapital = recommendedCapitalNum.toFixed(2);
  const portfolioExposure = ((recommendedCapitalNum / portfolioValue) * 100).toFixed(1);

  return (
    <div className="space-y-8">
      {/* Top Header & AI Rating Bar */}
      <div className="glass-card-glow rounded-2xl p-6 sm:p-8">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div>
            <div className="flex items-center gap-3">
              <h1 className="text-3xl font-extrabold text-white tracking-tight">{stock.ticker}</h1>
              <span className="text-sm font-semibold px-3 py-1 rounded-full bg-white/10 text-gray-300">
                {stock.sector}
              </span>
            </div>
            <p className="text-gray-300 text-sm mt-1">{stock.name} • {stock.industry}</p>
            <div className="flex items-center gap-6 mt-4 text-xs text-gray-400 font-medium">
              <div>Market Cap: <span className="text-white font-semibold">{stock.marketCap}</span></div>
              <div>52W Range: <span className="text-white font-semibold">₹{stock.week52Low} - ₹{stock.week52High}</span></div>
            </div>
          </div>

          {/* AI Score & Recommendation Badge */}
          <div className="flex items-center gap-4 bg-card/90 p-4 rounded-xl border border-border">
            <div className="text-center">
              <span className="text-[10px] uppercase tracking-wider text-gray-400 font-bold block">
                AI Recommendation
              </span>
              <span className="text-lg font-black text-emerald-400 tracking-wide block mt-0.5">
                {stock.recommendation}
              </span>
            </div>
            <div className="w-px h-10 bg-border"></div>
            <div className="text-center">
              <span className="text-[10px] uppercase tracking-wider text-gray-400 font-bold block">
                Overall Score
              </span>
              <span className="text-2xl font-black text-white block mt-0.5">
                {stock.overallScore}<span className="text-xs text-gray-400 font-normal">/10</span>
              </span>
            </div>
            <div className="w-px h-10 bg-border"></div>
            <div className="text-center">
              <span className="text-[10px] uppercase tracking-wider text-gray-400 font-bold block">
                Confidence
              </span>
              <span className="text-lg font-black text-indigo-400 block mt-0.5">
                {stock.confidenceScore}%
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* 8-Component Scorecard Breakdown Grid */}
      <div className="glass-card rounded-2xl p-6">
        <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-indigo-400" />
          6-Agent Scorecard Breakdown
        </h2>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          {Object.entries(stock.scoreBreakdown).map(([key, val]) => (
            <div key={key} className="bg-card/70 p-3.5 rounded-xl border border-border/60">
              <span className="text-xs text-gray-400 font-semibold uppercase tracking-wider block">
                {key.replace(/([AZ])/g, ' $1').trim()}
              </span>
              <div className="flex items-center justify-between mt-2">
                <span className="text-xl font-extrabold text-white">{val}</span>
                <div className="w-12 bg-gray-800 rounded-full h-2 overflow-hidden">
                  <div
                    className="bg-gradient-to-r from-primary-500 to-indigo-500 h-full rounded-full"
                    style={{ width: `${val * 10}%` }}
                  ></div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Bull Case vs Bear Case (Devil's Advocate Adversarial Agent) */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Bull Case Card */}
        <div className="glass-card rounded-2xl p-6 border-t-4 border-emerald-500">
          <h3 className="text-base font-bold text-emerald-400 flex items-center gap-2 mb-4">
            <CheckCircle2 className="w-5 h-5" />
            Bull Thesis (What Could Go Right?)
          </h3>
          <ul className="space-y-3 text-sm text-gray-300">
            {stock.bullReasons.map((reason, idx) => (
              <li key={idx} className="flex items-start gap-2.5">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0"></span>
                <span>{reason}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Bear Case (Devil's Advocate) Card */}
        <div className="glass-card rounded-2xl p-6 border-t-4 border-rose-500">
          <h3 className="text-base font-bold text-rose-400 flex items-center gap-2 mb-4">
            <XCircle className="w-5 h-5" />
            Adversarial Bear Thesis (Devil's Advocate)
          </h3>
          <ul className="space-y-3 text-sm text-gray-300">
            {stock.bearReasons.map((reason, idx) => (
              <li key={idx} className="flex items-start gap-2.5">
                <span className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2 shrink-0"></span>
                <span>{reason}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Interactive Risk-Based Position Sizer Widget */}
      <div className="glass-card rounded-2xl p-6 border border-primary-500/30">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <Calculator className="w-5 h-5 text-indigo-400" />
              Deterministic Risk Position Sizing Calculator
            </h2>
            <p className="text-xs text-gray-400 mt-0.5">
              Calculates exact share quantity based on capital risk limits (Zero hallucination formula).
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Input Controls */}
          <div className="space-y-4 bg-card/60 p-4 rounded-xl border border-border">
            <div>
              <label className="text-xs font-semibold text-gray-300 block mb-1.5">
                Total Portfolio Capital (₹)
              </label>
              <input
                type="number"
                value={portfolioValue}
                onChange={(e) => setPortfolioValue(Number(e.target.value))}
                className="w-full px-3 py-2 bg-gray-900 border border-border rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
            </div>

            <div>
              <label className="text-xs font-semibold text-gray-300 block mb-1.5">
                Max Acceptable Risk Per Trade (%)
              </label>
              <input
                type="number"
                step="0.1"
                value={riskPercent}
                onChange={(e) => setRiskPercent(Number(e.target.value))}
                className="w-full px-3 py-2 bg-gray-900 border border-border rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
            </div>

            <div>
              <label className="text-xs font-semibold text-gray-300 block mb-1.5">
                Single Stock Max Position Cap (%)
              </label>
              <input
                type="number"
                value={maxPositionCap}
                onChange={(e) => setMaxPositionCap(Number(e.target.value))}
                className="w-full px-3 py-2 bg-gray-900 border border-border rounded-lg text-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
              />
            </div>
          </div>

          {/* Calculated Output Card */}
          <div className="lg:col-span-2 bg-gradient-to-br from-card to-indigo-950/40 p-6 rounded-xl border border-indigo-500/30 flex flex-col justify-between">
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <div>
                <span className="text-xs text-gray-400 font-semibold block uppercase">Max Risk Amount</span>
                <span className="text-lg font-bold text-rose-400">₹{maxRiskAmount.toLocaleString()}</span>
              </div>
              <div>
                <span className="text-xs text-gray-400 font-semibold block uppercase">Risk Per Share</span>
                <span className="text-lg font-bold text-amber-400">₹{riskPerShare.toFixed(2)}</span>
              </div>
              <div>
                <span className="text-xs text-gray-400 font-semibold block uppercase">Max Shares</span>
                <span className="text-2xl font-black text-emerald-400">{finalRecommendedShares}</span>
              </div>
              <div>
                <span className="text-xs text-gray-400 font-semibold block uppercase">Portfolio Exposure</span>
                <span className="text-lg font-bold text-indigo-300">{portfolioExposure}%</span>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-indigo-500/20 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <span className="text-xs text-gray-400 block">Recommended Position Allocation</span>
                <span className="text-xl font-extrabold text-white">₹{Number(recommendedCapital).toLocaleString()}</span>
              </div>
              <button className="px-5 py-2.5 bg-gradient-to-r from-primary-600 to-indigo-600 hover:from-primary-500 hover:to-indigo-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-primary-500/25 transition">
                Simulate Paper Execution
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Trade Setup Parameters & Zones */}
      <div className="glass-card rounded-2xl p-6">
        <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
          <Layers className="w-5 h-5 text-indigo-400" />
          Trade Setup & Buy Zone Parameters
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-sm">
          <div className="bg-card/70 p-4 rounded-xl border border-border">
            <span className="text-xs text-gray-400 font-semibold uppercase block">Accumulation Zone</span>
            <span className="text-base font-bold text-indigo-300 mt-1 block">{stock.tradeSetup.accumulationZone}</span>
          </div>

          <div className="bg-card/70 p-4 rounded-xl border border-border">
            <span className="text-xs text-gray-400 font-semibold uppercase block">Target 1 & Target 2</span>
            <span className="text-base font-bold text-emerald-400 mt-1 block">₹{stock.tradeSetup.target1} / ₹{stock.tradeSetup.target2}</span>
          </div>

          <div className="bg-card/70 p-4 rounded-xl border border-border">
            <span className="text-xs text-gray-400 font-semibold uppercase block">Stop Loss Level</span>
            <span className="text-base font-bold text-rose-400 mt-1 block">₹{stock.tradeSetup.stopLoss}</span>
          </div>

          <div className="bg-card/70 p-4 rounded-xl border border-border">
            <span className="text-xs text-gray-400 font-semibold uppercase block">Risk / Reward Ratio</span>
            <span className="text-base font-bold text-white mt-1 block">{stock.tradeSetup.rrRatio} : 1</span>
          </div>
        </div>
      </div>
    </div>
  );
}
