# 📈 Stock Market Data Analyzer

**A Python-based financial analytics platform for historical stock data analysis, technical indicators, strategy backtesting, portfolio tracking, and interactive visualization.**

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Project-Educational-success)

## 📌 Project Overview

Stock Market Data Analyzer is an industry-oriented Python and FinTech project designed to analyze historical stock market data and generate meaningful financial insights.

The application collects market data using Yahoo Finance or CSV files, cleans and processes OHLCV data, calculates technical indicators, evaluates historical trading strategies, and visualizes results through a web dashboard.

## 🎯 Problem Statement

Financial market data contains large volumes of historical price and trading information. Manually analyzing this data can be time-consuming and difficult.

This project automates important analytical tasks, including:

- Historical stock data collection
- Data cleaning and preprocessing
- Moving average calculations
- Technical indicator analysis
- Daily return calculations
- Volatility and drawdown analysis
- Historical strategy backtesting
- Financial reporting and visualization

## 🏭 Industry Relevance

Similar analytical workflows are useful in:

- FinTech applications
- Stock brokerage research tools
- Financial analytics
- Investment research
- Quantitative finance education
- Portfolio monitoring
- Financial data engineering

## ✨ Features

- Historical stock market data ingestion
- Yahoo Finance integration
- CSV fallback support
- OHLCV data cleaning
- SMA 20, SMA 50 and SMA 200
- RSI 14
- MACD
- Bollinger Bands
- Daily returns
- Annualized volatility
- Maximum drawdown
- SMA crossover backtesting
- Transaction cost simulation
- SQLite data storage
- FastAPI REST endpoints
- Simulated portfolio accounting
- Rule-based market alerts
- Stock price visualizations
- JSON and TXT reports
- Next.js dashboard

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical calculations |
| yfinance | Market data collection |
| Matplotlib | Charts |
| Seaborn | Statistical visualization |
| ta | Technical indicators |
| SQLite | Database |
| FastAPI | REST API |
| Pydantic | Data validation |
| Next.js | Frontend |
| TypeScript | Frontend development |
| Tailwind CSS | UI styling |
| Recharts | Interactive charts |
| Pytest | Automated testing |
| Docker | Containerization |

## 📂 Project Structure

```text
Stock-Market-Data-Analyzer/
├── api/
├── apps/
│   └── web/
├── data/
│   ├── raw/
│   └── processed/
├── db/
├── docs/
├── images/
├── jobs/
├── notebooks/
├── outputs/
│   ├── charts/
│   └── reports/
├── reports/
├── src/
├── tests/
├── main.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/erchandkujra-ai/Stock-Market-Data-Analyzer.git
cd Stock-Market-Data-Analyzer
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run Python Analysis

```bash
python main.py --ticker AAPL --start 2021-01-01
```

Other supported examples:

```bash
python main.py --ticker MSFT
python main.py --ticker NVDA
python main.py --ticker TSLA
```

## 🌐 Run FastAPI Backend

```bash
uvicorn api.app:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## 💻 Run Next.js Dashboard

```bash
cd apps/web
npm install
npm run dev
```

Dashboard:

http://localhost:3000

## 📊 Technical Indicators

| Indicator | Description |
|---|---|
| SMA 20 | 20-day average price |
| SMA 50 | 50-day average price |
| SMA 200 | Long-term average price |
| RSI 14 | Momentum indicator |
| MACD | Trend and momentum indicator |
| Bollinger Bands | Volatility indicator |

## 📈 Project Outputs

The application generates:

- Stock closing price charts
- Moving average comparison charts
- Daily returns distribution
- Cleaned stock datasets
- Technical indicator datasets
- Strategy backtesting results
- Financial summary reports
- SQLite database

## 📸 Screenshots

Add your actual screenshots to the `images/` directory.

Suggested screenshots:

1. `images/dashboard.png`
2. `images/stock_price.png`
3. `images/moving_average.png`
4. `images/daily_returns.png`
5. `images/api_docs.png`
6. `images/backtest.png`

## 🧪 Testing

Run:

```bash
pytest -v
```

## 🚀 Future Enhancements

- Real-time market data integration
- Advanced strategy backtesting
- Portfolio performance analytics
- Automated email and Telegram alerts
- Multi-timeframe technical analysis
- PostgreSQL database integration
- Interactive watchlists
- Cloud deployment
- Walk-forward strategy validation
- Risk-based position sizing

## 📚 Learning Outcomes

Through this project, I developed practical knowledge of:

- Python programming
- Financial time-series analysis
- Data engineering fundamentals
- Data preprocessing
- Technical analysis
- Statistical risk measurement
- Historical backtesting
- REST API development
- Full-stack application integration
- Git and GitHub

## ⚠️ Disclaimer

This project is developed strictly for educational, academic, and research purposes.

The stock analysis, indicators, simulated signals, and historical backtesting results are not financial advice or investment recommendations. Historical performance does not guarantee future returns. No real trades are executed.

## 👨‍💻 Author

**ER. CHAND KUJRA**

GitHub: https://github.com/erchandkujra-ai

Project: Stock Market Data Analyzer

---

**Built with Python, Data Analytics, and Financial Technology.**