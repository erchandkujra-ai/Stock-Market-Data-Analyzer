
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd

from src.ingest import fetch_stock_data
from src.cleaning import clean_stock_data
from src.indicators import calculate_indicators
from src.analysis import analyze_stock
from src.backtest import run_sma_backtest
from src.database import (
    initialize_database,
    save_market_data,
    save_indicators,
    get_connection
)

app = FastAPI(
    title="Stock Market Data Analyzer API",
    description="Financial market analytics API",
    version="1.0.0"
)


class BacktestRequest(BaseModel):

    ticker: str = Field(
        min_length=1,
        max_length=15
    )

    fee_bps: float = Field(
        default=5,
        ge=0,
        le=1000
    )

    start: str | None = None
    end: str | None = None


@app.get("/")
def home():

    return {
        "message": "Stock Market Data Analyzer API",
        "status": "running"
    }


@app.get("/health")
def health():

    return {"status": "healthy"}


@app.post("/refresh/{ticker}")
def refresh(ticker: str):

    ticker = ticker.upper()

    try:

        initialize_database()

        raw = fetch_stock_data(ticker)

        clean = clean_stock_data(
            raw,
            ticker
        )

        analyzed = calculate_indicators(
            clean
        )

        save_market_data(
            clean,
            ticker
        )

        save_indicators(
            analyzed,
            ticker
        )

        return {
            "success": True,
            "ticker": ticker,
            "records": len(analyzed)
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/chart/{ticker}")
def chart(ticker: str, days: int = 252):

    if days < 1 or days > 5000:
        raise HTTPException(
            status_code=400,
            detail="days must be between 1 and 5000"
        )

    try:

        with get_connection() as connection:

            df = pd.read_sql_query(
                """
                SELECT
                    c.date,
                    c.close,
                    c.volume,
                    i.sma20,
                    i.sma50,
                    i.rsi14,
                    i.macd
                FROM candles_daily c
                LEFT JOIN indicators_daily i
                    ON c.ticker = i.ticker
                    AND c.date = i.date
                WHERE c.ticker = ?
                ORDER BY c.date DESC
                LIMIT ?
                """,
                connection,
                params=(ticker.upper(), days)
            )

        df = df.iloc[::-1]

        if df.empty:
            raise HTTPException(
                status_code=404,
                detail="Ticker not found. Refresh data first."
            )

        return df.astype(object).where(
            pd.notna(df),
            None
        ).to_dict(orient="records")

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/summary/{ticker}")
def summary(ticker: str):

    try:

        with get_connection() as connection:

            df = pd.read_sql_query(
                """
                SELECT
                    c.date,
                    c.open,
                    c.high,
                    c.low,
                    c.close,
                    c.volume,
                    i.sma20,
                    i.sma50,
                    i.rsi14,
                    i.macd,
                    i.macd_signal,
                    i.macd_hist,
                    i.bb_upper,
                    i.bb_mid,
                    i.bb_lower
                FROM candles_daily c
                LEFT JOIN indicators_daily i
                    ON c.ticker = i.ticker
                    AND c.date = i.date
                WHERE c.ticker = ?
                ORDER BY c.date
                """,
                connection,
                params=(ticker.upper(),)
            )

        if df.empty:
            raise HTTPException(
                status_code=404,
                detail="No stock data found."
            )

        # Recalculate derived features for a complete summary
        df["daily_return"] = df["close"].pct_change()

        df["volatility"] = (
            df["daily_return"].rolling(20).std()
            * (252 ** 0.5)
        )

        return analyze_stock(df)

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/backtest/sma")
def backtest(request: BacktestRequest):

    try:

        with get_connection() as connection:

            df = pd.read_sql_query(
                """
                SELECT
                    c.date,
                    c.close,
                    i.sma20,
                    i.sma50
                FROM candles_daily c
                JOIN indicators_daily i
                    ON c.ticker = i.ticker
                    AND c.date = i.date
                WHERE c.ticker = ?
                ORDER BY c.date
                """,
                connection,
                params=(request.ticker.upper(),)
            )

        if df.empty:
            raise HTTPException(
                status_code=404,
                detail="Refresh stock data before backtesting."
            )

        df["date"] = pd.to_datetime(df["date"])

        if request.start:
            df = df[
                df["date"] >= pd.to_datetime(request.start)
            ]

        if request.end:
            df = df[
                df["date"] <= pd.to_datetime(request.end)
            ]

        stats, curve = run_sma_backtest(
            df,
            fee_bps=request.fee_bps
        )

        return {
            "ticker": request.ticker.upper(),
            "stats": stats,
            "equity_curve": curve.to_dict(
                orient="records"
            )
        }

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/alerts")
def alerts():

    with get_connection() as connection:

        connection.row_factory = None

        rows = connection.execute(
            """
            SELECT id, ticker, rule, threshold,
                   active, last_fired
            FROM alerts
            WHERE active = 1
            """
        ).fetchall()

    return [
        {
            "id": row[0],
            "ticker": row[1],
            "rule": row[2],
            "threshold": row[3],
            "active": row[4],
            "last_fired": row[5]
        }
        for row in rows
    ]
