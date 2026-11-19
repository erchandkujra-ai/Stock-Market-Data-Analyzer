
import pandas as pd

from src.indicators import calculate_indicators


def test_indicators():

    data = pd.DataFrame({
        "date": pd.date_range(
            "2024-01-01",
            periods=250
        ),
        "close": [
            100 + i * 0.5
            for i in range(250)
        ]
    })

    result = calculate_indicators(data)

    assert "sma20" in result.columns

    assert "sma50" in result.columns

    assert "rsi14" in result.columns

    assert "macd" in result.columns

    assert "signal" in result.columns

    assert result["sma20"].notna().any()
