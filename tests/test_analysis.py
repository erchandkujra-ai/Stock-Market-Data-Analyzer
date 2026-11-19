
import pandas as pd

from src.analysis import analyze_stock


def test_analysis_returns():

    data = pd.DataFrame({
        "date": pd.date_range(
            "2025-01-01",
            periods=3
        ),
        "open": [100, 105, 110],
        "high": [110, 115, 120],
        "low": [95, 100, 105],
        "close": [100, 110, 120],
        "volume": [1000, 1200, 1500],
        "daily_return": [None, 0.10, 0.090909],
        "rsi14": [50, 55, 60]
    })

    result = analyze_stock(data)

    assert result["latest_close"] == 120

    assert result["highest_price"] == 120

    assert result["lowest_price"] == 95

    assert result["total_return"] == 0.20
