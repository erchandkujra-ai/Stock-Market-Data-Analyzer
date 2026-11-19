
import pandas as pd

from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands


def calculate_indicators(data):

    df = data.copy()

    close = df["close"]

    # Moving averages
    df["sma20"] = SMAIndicator(
        close,
        window=20
    ).sma_indicator()

    df["sma50"] = SMAIndicator(
        close,
        window=50
    ).sma_indicator()

    df["sma200"] = SMAIndicator(
        close,
        window=200
    ).sma_indicator()

    # RSI
    df["rsi14"] = RSIIndicator(
        close,
        window=14
    ).rsi()

    # MACD
    macd_indicator = MACD(close)

    df["macd"] = macd_indicator.macd()

    df["macd_signal"] = (
        macd_indicator.macd_signal()
    )

    df["macd_hist"] = (
        macd_indicator.macd_diff()
    )

    # Bollinger Bands
    bb = BollingerBands(
        close,
        window=20,
        window_dev=2
    )

    df["bb_upper"] = bb.bollinger_hband()
    df["bb_mid"] = bb.bollinger_mavg()
    df["bb_lower"] = bb.bollinger_lband()

    # Daily returns
    df["daily_return"] = close.pct_change()

    # Annualized rolling volatility
    df["volatility"] = (
        df["daily_return"]
        .rolling(window=20)
        .std() * (252 ** 0.5)
    )

    # Research signal
    df["signal"] = "HOLD"

    df.loc[
        (df["sma20"] > df["sma50"]) &
        (df["rsi14"] < 70),
        "signal"
    ] = "BUY"

    df.loc[
        (df["sma20"] < df["sma50"]) |
        (df["rsi14"] >= 70),
        "signal"
    ] = "SELL"

    return df
