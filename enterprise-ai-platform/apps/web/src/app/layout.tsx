import './globals.css';
import Link from 'next/link';
import { TrendingUp, ShieldCheck, LineChart, Bookmark, Cpu } from 'lucide-react';

export const metadata = {
  title: 'AI Stock Investment & Trading Platform (NSE/BSE)',
  description: 'Evidence-based AI investment research, historical valuation bands, and risk-based position sizing for Indian equities.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-background text-gray-100 min-h-screen flex flex-col">
        {/* Top Navbar */}
        <header className="border-b border-border/60 bg-card/80 backdrop-blur-md sticky top-0 z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <Link href="/" className="flex items-center space-x-3 group">
              <div className="p-2 rounded-xl bg-gradient-to-tr from-primary-600 to-accent text-white shadow-lg shadow-primary-500/20 group-hover:scale-105 transition-transform">
                <Cpu className="w-5 h-5" />
              </div>
              <div>
                <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-white via-gray-200 to-primary-500 bg-clip-text text-transparent">
                  AlphaResearch AI
                </span>
                <span className="text-[10px] font-semibold tracking-wider block text-indigo-400 -mt-1 uppercase">
                  NSE / BSE Equities
                </span>
              </div>
            </Link>

            <nav className="flex items-center space-x-1 sm:space-x-4 text-sm font-medium">
              <Link
                href="/"
                className="px-3 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition flex items-center gap-1.5"
              >
                <TrendingUp className="w-4 h-4 text-emerald-400" />
                Dashboard
              </Link>
              <Link
                href="/stock/RELIANCE"
                className="px-3 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition flex items-center gap-1.5"
              >
                <LineChart className="w-4 h-4 text-indigo-400" />
                Research Workspace
              </Link>
              <Link
                href="/paper-trading"
                className="px-3 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/5 transition flex items-center gap-1.5"
              >
                <ShieldCheck className="w-4 h-4 text-purple-400" />
                Paper Trading
              </Link>
            </nav>

            <div className="flex items-center space-x-3">
              <span className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                6-Agent AI Active
              </span>
            </div>
          </div>
        </header>

        {/* Main Body */}
        <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
          {children}
        </main>

        {/* Footer */}
        <footer className="border-t border-border/40 py-6 text-center text-xs text-gray-500">
          <p>AlphaResearch AI Platform &copy; 2026. For educational and investment research purposes only.</p>
          <p className="mt-1 text-gray-600">Zero-guarantee profit policy | Risk-controlled position sizing engine</p>
        </footer>
      </body>
    </html>
  );
}
