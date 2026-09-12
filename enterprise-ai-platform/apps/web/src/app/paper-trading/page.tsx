'use client';

import React from 'react';
import { ShieldCheck, TrendingUp, DollarSign, Clock, PlayCircle } from 'lucide-react';

export default function PaperTradingPage() {
  const positions = [
    {
      id: 'pt-101',
      ticker: 'RELIANCE',
      action: 'BUY',
      shares: 67,
      entryPrice: 2940.0,
      currentPrice: 2945.5,
      pnl: 368.5,
      pnlPercent: '+0.19%',
      stopLoss: 2850.0,
      target: 3120.0,
      status: 'OPEN',
    },
    {
      id: 'pt-102',
      ticker: 'TCS',
      action: 'BUY',
      shares: 45,
      entryPrice: 4150.0,
      currentPrice: 4180.0,
      pnl: 1350.0,
      pnlPercent: '+0.72%',
      stopLoss: 3980.0,
      target: 4450.0,
      status: 'OPEN',
    },
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="glass-card-glow rounded-2xl p-6 sm:p-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-purple-500/10 text-purple-400 border border-purple-500/20 mb-3">
              <ShieldCheck className="w-3.5 h-3.5" />
              Risk-Free Virtual Execution
            </span>
            <h1 className="text-3xl font-extrabold text-white tracking-tight">Paper Trading Hub</h1>
            <p className="text-gray-300 text-sm mt-1">
              Simulate live AI-recommended trade setups without risking real capital.
            </p>
          </div>

          <div className="bg-card/90 p-4 rounded-xl border border-border text-right">
            <span className="text-xs text-gray-400 font-semibold block uppercase">Virtual Capital Balance</span>
            <span className="text-2xl font-black text-white">₹10,00,000.00</span>
          </div>
        </div>
      </div>

      {/* Active Positions Table */}
      <div className="glass-card rounded-2xl p-6">
        <h2 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
          <TrendingUp className="w-5 h-5 text-emerald-400" />
          Active Paper Trading Positions
        </h2>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-sm">
            <thead>
              <tr className="border-b border-border/80 text-gray-400 font-semibold text-xs uppercase tracking-wider">
                <th className="py-3 px-4">Trade ID</th>
                <th className="py-3 px-4">Stock</th>
                <th className="py-3 px-4">Action</th>
                <th className="py-3 px-4">Shares</th>
                <th className="py-3 px-4">Avg Entry</th>
                <th className="py-3 px-4">Current Price</th>
                <th className="py-3 px-4">Unrealized P&L</th>
                <th className="py-3 px-4">Stop Loss</th>
                <th className="py-3 px-4">Target 1</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border/40 font-medium">
              {positions.map((pos) => (
                <tr key={pos.id} className="hover:bg-white/[0.02] transition">
                  <td className="py-4 px-4 text-xs font-mono text-gray-400">{pos.id}</td>
                  <td className="py-4 px-4 font-bold text-white text-base">{pos.ticker}</td>
                  <td className="py-4 px-4">
                    <span className="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-400 text-xs font-bold border border-emerald-500/30">
                      {pos.action}
                    </span>
                  </td>
                  <td className="py-4 px-4 text-gray-200">{pos.shares}</td>
                  <td className="py-4 px-4 text-white">₹{pos.entryPrice.toFixed(2)}</td>
                  <td className="py-4 px-4 text-white font-semibold">₹{pos.currentPrice.toFixed(2)}</td>
                  <td className="py-4 px-4">
                    <span className="text-emerald-400 font-bold">
                      +₹{pos.pnl.toFixed(2)} ({pos.pnlPercent})
                    </span>
                  </td>
                  <td className="py-4 px-4 text-rose-400">₹{pos.stopLoss.toFixed(2)}</td>
                  <td className="py-4 px-4 text-emerald-400">₹{pos.target.toFixed(2)}</td>
                  <td className="py-4 px-4 text-right">
                    <button className="px-3 py-1.5 bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 font-semibold text-xs rounded-lg border border-rose-500/30 transition">
                      Close Position
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
