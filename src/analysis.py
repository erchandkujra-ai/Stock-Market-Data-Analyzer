
import numpy as np
import pandas as pd


def analyze_stock(data):

    df = data.copy()

    returns = df["daily_return"].dropna()

    if len(df) < 2 or returns.empty:
        raise ValueError(
            "Not enough valid data for analysis."
        )

    highest = df.loc[df["high"].idxmax()]
    lowest = df.loc[df["low"].idxmin()]

    total_return = (
        df["close"].iloc[-1] /
        df["close"].iloc[0] - 1
    )

    average_return = returns.mean()

    daily_volatility = returns.std()

    annual_volatility = (
        daily_volatility * np.sqrt(252)
    )

    cumulative_returns = (
        (1 + returns).cumprod()
    )

    peak = cumulative_returns.cummax()

    drawdown = (
        cumulative_returns / peak - 1
    )

    max_drawdown = drawdown.min()

    result = {
        "start_date": str(df["date"].iloc[0]),
        "end_date": str(df["date"].iloc[-1]),
        "first_close": float(df["close"].iloc[0]),
        "latest_close": float(df["close"].iloc[-1]),
        "highest_price": float(highest["high"]),
        "highest_date": str(highest["date"]),
        "lowest_price": float(lowest["low"]),
        "lowest_date": str(lowest["date"]),
        "total_return": float(total_return),
        "average_daily_return": float(average_return),
        "annualized_volatility": float(annual_volatility),
        "max_drawdown": float(max_drawdown),
        "average_volume": float(df["volume"].mean()),
        "latest_rsi": float(df["rsi14"].iloc[-1])
        if pd.notna(df["rsi14"].iloc[-1])
        else None
    }

    return result
