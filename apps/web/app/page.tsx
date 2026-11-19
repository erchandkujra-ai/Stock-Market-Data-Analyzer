
"use client";

import { useState } from "react";

const watchlist = [
  ["AAPL", "Apple Inc.", "213.45", "+2.45%"],
  ["MSFT", "Microsoft", "425.30", "+1.32%"],
  ["NVDA", "NVIDIA", "145.20", "+3.85%"],
  ["GOOGL", "Alphabet", "182.65", "-0.42%"],
  ["AMZN", "Amazon", "198.75", "+1.64%"],
  ["TSLA", "Tesla", "342.80", "-1.25%"],
  ["META", "Meta", "625.40", "+2.10%"],
  ["NFLX", "Netflix", "1025.60", "+0.86%"],
];

const candleData = [
  [65, 115, 85, 100], [100, 90, 65, 75],
  [75, 105, 55, 95], [95, 80, 40, 55],
  [55, 65, 30, 45], [45, 85, 35, 75],
  [75, 110, 60, 100], [100, 90, 50, 65],
  [65, 75, 35, 45], [45, 100, 40, 90],
  [90, 125, 80, 115], [115, 105, 70, 85],
  [85, 100, 60, 95], [95, 120, 75, 110],
  [110, 90, 55, 65], [65, 85, 40, 75],
  [75, 105, 55, 95], [95, 115, 65, 80],
  [80, 95, 45, 55], [55, 80, 35, 70],
  [70, 100, 50, 90], [90, 110, 65, 75],
  [75, 95, 45, 60], [60, 85, 35, 50],
];

function ChartGrid() {
  return (
    <>
      {[35, 75, 115, 155, 195].map((y) => (
        <line key={y} x1="0" y1={y} x2="600" y2={y}
          stroke="#26344a" strokeDasharray="4 5" />
      ))}
    </>
  );
}

function CandlestickChart() {
  return (
    <svg viewBox="0 0 600 220" className="chart">
      <ChartGrid />
      {candleData.map(([open, high, low, close], i) => {
        const x = 12 + i * 24;
        const rising = close < open;
        const color = rising ? "#19d58b" : "#fa526b";
        return (
          <g key={i}>
            <line x1={x + 7} x2={x + 7} y1={high} y2={low}
              stroke={color} strokeWidth="2" />
            <rect x={x} y={Math.min(open, close)}
              width="14" height={Math.max(5, Math.abs(close - open))}
              fill={color} rx="1" />
          </g>
        );
      })}
      <path d="M0 140 Q90 95 160 125 T310 110 T460 125 T600 95"
        fill="none" stroke="#f4a64e" strokeWidth="2" />
      <path d="M0 165 Q120 155 200 170 T390 150 T600 165"
        fill="none" stroke="#df5476" strokeWidth="2" />
    </svg>
  );
}

function VolumeChart({ red = false }: { red?: boolean }) {
  return (
    <svg viewBox="0 0 600 180" className="chart">
      <ChartGrid />
      {Array.from({ length: 45 }, (_, i) => {
        const h = 20 + ((i * 37 + i * i * 13) % 115);
        return (
          <rect key={i} x={5 + i * 13} y={155 - h}
            width="8" height={h}
            fill={red ? "#ef4565" : "#18c879"} rx="1" />
        );
      })}
    </svg>
  );
}

function IndicatorChart() {
  return (
    <svg viewBox="0 0 600 180" className="chart">
      <ChartGrid />
      <path
        d="M0 65 Q40 25 80 70 T160 65 T240 100 T320 55 T400 75 T480 115 T600 85"
        fill="none" stroke="#20d68c" strokeWidth="3"
      />
      <path
        d="M0 90 Q70 75 130 85 T250 80 T380 95 T500 75 T600 100"
        fill="none" stroke="#ef647a" strokeWidth="2"
      />
      <line x1="0" y1="90" x2="600" y2="90"
        stroke="#64748b" strokeDasharray="5 5" />
    </svg>
  );
}

function MacdChart() {
  return (
    <svg viewBox="0 0 600 200" className="chart">
      <ChartGrid />
      <line x1="0" y1="100" x2="600" y2="100"
        stroke="#64748b" strokeDasharray="5 5" />
      {Array.from({ length: 35 }, (_, i) => {
        const h = 15 + ((i * 19 + i * i * 7) % 65);
        const positive = i % 5 < 2;
        return (
          <rect key={i} x={8 + i * 17} y={positive ? 100 - h : 100}
            width="10" height={h}
            fill={positive ? "#18d58b" : "#ee526b"} />
        );
      })}
      <path
        d="M0 65 Q100 45 170 85 T310 90 T450 130 T600 155"
        fill="none" stroke="#e7a0bc" strokeWidth="3"
      />
      <path
        d="M0 115 Q100 100 180 105 T350 80 T480 70 T600 45"
        fill="none" stroke="#c6d5ef" strokeWidth="2"
      />
    </svg>
  );
}

function Panel({
  title,
  children,
  tag,
}: {
  title: string;
  children: React.ReactNode;
  tag?: string;
}) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h3>{title}</h3>
        <span>{tag || "1D  ·  1W  ·  1M"}</span>
      </div>
      {children}
    </section>
  );
}

export default function Home() {
  const [selected, setSelected] = useState("AAPL");
  const [search, setSearch] = useState("");

  const filtered = watchlist.filter((item) =>
    item[0].toLowerCase().includes(search.toLowerCase())
  );

  const current = watchlist.find((item) => item[0] === selected);

  return (
    <main className="dashboard">
      <header className="topbar">
        <div className="brand">
          <div className="brand-icon">S</div>
          <div>
            <h2>MARKET<span>PRO</span></h2>
            <small>STOCK ANALYTICS TERMINAL</small>
          </div>
        </div>

        <div className="market-status">
          <span className="live-dot" /> DEMO MARKET DATA
        </div>

        <div className="top-actions">
          <button>⌕</button>
          <button>⚙</button>
          <div className="profile">ER</div>
        </div>
      </header>

      <div className="workspace">
        <aside className="sidebar">
          <div className="side-title">
            <h3>WATCHLIST</h3>
            <span>＋</span>
          </div>

          <input
            className="search"
            placeholder="Search symbol..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />

          <div className="watch-items">
            {filtered.map((item) => (
              <button
                key={item[0]}
                onClick={() => setSelected(item[0])}
                className={`watch-item ${selected === item[0] ? "active" : ""}`}
              >
                <div>
                  <strong>{item[0]}</strong>
                  <small>{item[1]}</small>
                </div>
                <div className="watch-price">
                  <strong>${item[2]}</strong>
                  <small className={item[3].startsWith("+") ? "green" : "red"}>
                    {item[3]}
                  </small>
                </div>
              </button>
            ))}
          </div>

          <div className="sidebar-bottom">
            <span className="live-dot" /> Market data preview
          </div>
        </aside>

        <section className="main-content">
          <div className="page-heading">
            <div>
              <p className="eyebrow">MARKET OVERVIEW / US EQUITIES</p>
              <h1>{selected} <span>·</span> {current?.[1]}</h1>
              <p className="subheading">Stock market technical analysis dashboard</p>
            </div>
            <div className="time-filters">
              <button>1H</button>
              <button className="selected-filter">1D</button>
              <button>1W</button>
              <button>1M</button>
              <button>1Y</button>
            </div>
          </div>

          <div className="stats-row">
            <div className="stat-card">
              <small>LAST PRICE</small>
              <h2>${current?.[2]}</h2>
              <span className="green">▲ {current?.[3]}</span>
            </div>
            <div className="stat-card">
              <small>RSI (14)</small>
              <h2>62.48</h2>
              <span className="green">Neutral zone</span>
            </div>
            <div className="stat-card">
              <small>MACD</small>
              <h2>3.284</h2>
              <span className="green">Bullish signal</span>
            </div>
            <div className="stat-card">
              <small>VOLUME</small>
              <h2>42.8M</h2>
              <span className="muted">Sample volume</span>
            </div>
          </div>

          <div className="chart-grid">
            <Panel title="PRICE ACTION" tag="CANDLESTICK · SMA">
              <CandlestickChart />
              <div className="legend">
                <span><i className="green-bg" /> Bullish</span>
                <span><i className="red-bg" /> Bearish</span>
                <span><i className="orange-bg" /> SMA</span>
              </div>
            </Panel>

            <Panel title="TRADING VOLUME" tag="VOLUME · DAILY">
              <VolumeChart />
              <div className="chart-footer">Volume distribution · Sample data</div>
            </Panel>

            <Panel title="VOLUME PROFILE" tag="BUY / SELL ACTIVITY">
              <VolumeChart red />
              <div className="chart-footer">Trading activity · Sample data</div>
            </Panel>

            <Panel title="RSI INDICATOR" tag="RELATIVE STRENGTH INDEX">
              <IndicatorChart />
              <div className="chart-footer">RSI 14: 62.48 · Neutral zone</div>
            </Panel>

            <Panel title="MACD ANALYSIS" tag="MACD · SIGNAL · HISTOGRAM">
              <MacdChart />
              <div className="chart-footer">MACD 3.284 · Signal 2.810</div>
            </Panel>

            <Panel title="MARKET TREND" tag="MOVING AVERAGES">
              <IndicatorChart />
              <div className="chart-footer">SMA 20 · SMA 50 · Trend analysis</div>
            </Panel>
          </div>

          <footer className="footer">
            STOCK MARKET DATA ANALYZER
            <span>Educational dashboard · Illustrative data, not investment advice</span>
          </footer>
        </section>
      </div>
    </main>
  );
}
