'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import {
  Search,
  TrendingUp,
  ArrowUpRight,
  ShieldAlert,
  BarChart3,
  Award,
  Zap,
  CheckCircle2,
  AlertTriangle,
} from 'lucide-react';

export default function DashboardPage() {
  const [searchQuery, setSearchQuery] = useState('');

  const opportunities = [
    {
      ticker: 'RELIANCE',
      name: 'Reliance Industries Ltd',
      sector: 'Energy & Retail',
      price: '₹2,945.50',
      change: '+1.25%',
      isPositive: true,
      recommendation: 'ACCUMULATE',
      score: 8.2,
      confidence: 84,
      entryZone: '₹2,910 - ₹2,940',
      target1: '₹3,120',
      stopLoss: '₹2,840',
      rrRatio: '2.25',
    },
    {
      ticker: 'TCS',
      name: 'Tata Consultancy Services',
      sector: 'IT Services',
      price: '₹4,180.00',
      change: '-0.45%',
      isPositive: false,
      recommendation: 'BUY',
      score: 8.4,
      confidence: 87,
      entryZone: '₹4,120 - ₹4,170',
      target1: '₹4,450',
      stopLoss: '₹3,980',
      rrRatio: '2.40',
    },
    {
      ticker: 'HDFCBANK',
      name: 'HDFC Bank Ltd',
      sector: 'Banking & Financials',
      price: '₹1,645.20',
      change: '+0.85%',
      isPositive: true,
      recommendation: 'STRONG BUY',
      score: 8.9,
      confidence: 91,
      entryZone: '₹1,620 - ₹1,640',
      target1: '₹1,820',
      stopLoss: '₹1,560',
      rrRatio: '2.80',
    },
  ];

  return (
    <div className="space-y-8">
      {/* Top Banner / Hero Header */}
      <div className="glass-card-glow rounded-2xl p-6 sm:p-8 relative overflow-hidden">
        <div className="absolute -right-10 -bottom-10 w-72 h-72 bg-primary-600/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="relative z-10 max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mb-4">
            <Zap className="w-3.5 h-3.5" />
            AI Opportunity Engine & Risk Sizer
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white mb-3">
            Evidence-Based AI Investment Research for Indian Equities
          </h1>
          <p className="text-gray-300 text-sm sm:text-base leading-relaxed mb-6">
            Combining 10+ years of financials, historical valuation bands, 6-agent AI reasoning, 
            and zero-hallucination risk-based position sizing for NSE & BSE stocks.
          </p>

          {/* Stock Search Bar */}
          <div className="relative max-w-xl">
            <Search className="absolute left-4 top-3.5 w-5 h-5 text-gray-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search NSE stock by symbol or company name (e.g. RELIANCE, TCS)..."
              className="w-full pl-11 pr-32 py-3.5 bg-card/90 border border-border/80 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary-500/50 text-sm shadow-inner"
            />
            <Link
              href={searchQuery ? `/stock/${searchQuery.toUpperCase()}` : '/stock/RELIANCE'}
              className="absolute right-2 top-2 px-4 py-2 bg-gradient-to-r from-primary-600 to-indigo-600 hover:from-primary-500 hover:to-indigo-500 text-white font-medium text-xs rounded-lg shadow-md transition flex items-center gap-1"
            >
              Analyze Stock
              <ArrowUpRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>
      </div>

      {/* Portfolio & Performance Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="glass-card rounded-xl p-5 border-l-4 border-indigo-500">
          <span className="text-xs font-semibold text-gray-400 block uppercase tracking-wider">
            Total Portfolio Value
          </span>
          <div className="text-2xl font-bold text-white mt-1">₹10,00,000</div>
          <div className="text-xs text-emerald-400 mt-1 font-medium flex items-center gap-1">
            <TrendingUp className="w-3.5 h-3.5" /> +₹45,200 (+4.52% unrealized)
          </div>
        </div>

        <div className="glass-card rounded-xl p-5 border-l-4 border-emerald-500">
          <span className="text-xs font-semibold text-gray-400 block uppercase tracking-wider">
            Win Rate / Profit Factor
          </span>
          <div className="text-2xl font-bold text-white mt-1">78.5%</div>
          <div className="text-xs text-gray-300 mt-1 font-medium">
            Profit Factor: <span className="text-emerald-400 font-bold">2.42</span> (Paper Trades)
          </div>
        </div>

        <div className="glass-card rounded-xl p-5 border-l-4 border-purple-500">
          <span className="text-xs font-semibold text-gray-400 block uppercase tracking-wider">
            Market Regime
          </span>
          <div className="text-2xl font-bold text-emerald-400 mt-1 flex items-center gap-2">
            Bullish Trend
          </div>
          <div className="text-xs text-gray-400 mt-1 font-medium">
            NIFTY &gt; 200 DMA (Volatility: Normal)
          </div>
        </div>

        <div className="glass-card rounded-xl p-5 border-l-4 border-amber-500">
          <span className="text-xs font-semibold text-gray-400 block uppercase tracking-wider">
            Current Risk Exposure
          </span>
          <div className="text-2xl font-bold text-white mt-1">1.0% Max/Trade</div>
          <div className="text-xs text-amber-400 mt-1 font-medium flex items-center gap-1">
            <ShieldAlert className="w-3.5 h-3.5" /> Max Position Cap: 20.0%
          </div>
        </div>
      </div>

      {/* High Quality AI Opportunities Feed Table */}
      <div className="glass-card rounded-2xl p-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
          <div>
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <Award className="w-5 h-5 text-indigo-400" />
              High-Quality AI Investment Feed
            </h2>
            <p className="text-xs text-gray-400 mt-0.5">
              Ranked by 6-Agent AI Score, fundamental safety, and risk/reward ratio.
            </p>
          </div>
          <div className="text-xs text-gray-400 bg-white/5 px-3 py-1.5 rounded-lg border border-border/50">
            Strategy Rule: <span className="text-indigo-300 font-medium">NO TRADE</span> if Risk/Reward &lt; 1.8
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-sm">
            <thead>
              <tr className="border-b border-border/80 text-gray-400 font-semibold text-xs uppercase tracking-wider">
                <th className="py-3 px-4">Stock Ticker</th>
                <th className="py-3 px-4">AI Recommendation</th>
                <th className="py-3 px-4">Current Price</th>
                <th className="py-3 px-4">Accumulation Zone</th>
                <th className="py-3 px-4">Target 1</th>
                <th className="py-3 px-4">Stop Loss</th>
                <th className="py-3 px-4">Risk / Reward</th>
                <th className="py-3 px-4 text-center">AI Score</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/40 font-medium">
              {opportunities.map((stock) => (
                <tr key={stock.ticker} className="hover:bg-white/[0.02] transition">
                  <td className="py-4 px-4">
                    <div className="font-bold text-white text-base">{stock.ticker}</div>
                    <div className="text-xs text-gray-400">{stock.name}</div>
                  </td>
                  <td className="py-4 px-4">
                    <span
                      className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold ${
                        stock.recommendation === 'STRONG BUY'
                          ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                          : stock.recommendation === 'BUY'
                          ? 'bg-indigo-500/20 text-indigo-400 border border-indigo-500/30'
                          : 'bg-purple-500/20 text-purple-300 border border-purple-500/30'
                      }`}
                    >
                      <CheckCircle2 className="w-3 h-3" />
                      {stock.recommendation}
                    </span>
                  </td>
                  <td className="py-4 px-4 font-semibold text-white">
                    {stock.price}
                    <span
                      className={`block text-xs ${
                        stock.isPositive ? 'text-emerald-400' : 'text-rose-400'
                      }`}
                    >
                      {stock.change}
                    </span>
                  </td>
                  <td className="py-4 px-4 text-indigo-200">{stock.entryZone}</td>
                  <td className="py-4 px-4 text-emerald-400 font-semibold">{stock.target1}</td>
                  <td className="py-4 px-4 text-rose-400">{stock.stopLoss}</td>
                  <td className="py-4 px-4">
                    <span className="px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-300 text-xs font-semibold">
                      {stock.rrRatio} : 1
                    </span>
                  </td>
                  <td className="py-4 px-4 text-center">
                    <div className="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-tr from-primary-600 to-indigo-600 text-white font-extrabold text-sm shadow-md">
                      {stock.score}
                    </div>
                  </td>
                  <td className="py-4 px-4 text-right">
                    <Link
                      href={`/stock/${stock.ticker}`}
                      className="inline-flex items-center gap-1 px-3 py-1.5 bg-card hover:bg-white/10 text-gray-200 font-semibold text-xs rounded-lg border border-border transition shadow-sm"
                    >
                      View Report
                      <ArrowUpRight className="w-3.5 h-3.5 text-primary-400" />
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Disclaimers & Rules */}
      <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs flex items-start gap-3">
        <AlertTriangle className="w-5 h-5 shrink-0 text-amber-400 mt-0.5" />
        <div>
          <span className="font-bold block text-amber-200">Strict Capital Preservation Philosophy</span>
          AlphaResearch AI explicitly enforces risk-based position sizing and never guarantees trading profits. 
          All BUY recommendations are rigorously challenged by an Adversarial (Devil's Advocate) agent before rendering a final score.
        </div>
      </div>
    </div>
  );
}
