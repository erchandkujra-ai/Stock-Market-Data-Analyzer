
import pandas as pd
import yfinance as yf

from src.config import RAW_DATA_DIR


def fetch_stock_data(
    ticker="AAPL",
    start="2021-01-01",
    end=None
):
    """
    Download historical stock market data.
    """

    print(f"Downloading data for {ticker}...")

    try:
        data = yf.download(
            ticker,
            start=start,
            end=end,
            auto_adjust=False,
            progress=False
        )

        if data.empty:
            raise ValueError("No stock data returned.")

        # Handle different Yahoo Finance column formats
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data.columns = [
            str(column).lower().replace(" ", "_")
            for column in data.columns
        ]

        data.index.name = "date"
        data = data.reset_index()

        if "adj_close" not in data.columns:
            data["adj_close"] = data["close"]

        required = [
            "date",
            "open",
            "high",
            "low",
            "close",
            "adj_close",
            "volume"
        ]

        data = data[required]

        filename = f"{ticker.upper()}_raw.csv"

        data.to_csv(
            RAW_DATA_DIR / filename,
            index=False
        )

        print(f"Data downloaded: {len(data)} records")

        return data

    except Exception as error:
        print(f"Online download failed: {error}")

        return load_csv_data(ticker)


def load_csv_data(ticker="AAPL"):
    """
    Load locally saved CSV data if online data is unavailable.
    """

    path = RAW_DATA_DIR / f"{ticker.upper()}_raw.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"CSV not found: {path}"
        )

    print("Loading data from CSV...")

    return pd.read_csv(path, parse_dates=["date"])
