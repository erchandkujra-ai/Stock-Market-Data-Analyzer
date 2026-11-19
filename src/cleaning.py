
import pandas as pd

from src.config import PROCESSED_DATA_DIR


REQUIRED_COLUMNS = [
    "date",
    "open",
    "high",
    "low",
    "close",
    "adj_close",
    "volume"
]


def clean_stock_data(data, ticker="AAPL"):

    df = data.copy()

    # Normalize column names
    df.columns = [
        str(col).lower().replace(" ", "_")
        for col in df.columns
    ]

    # Validate columns
    missing = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    # Convert date
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "adj_close",
        "volume"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove invalid dates and prices
    df = df.dropna(
        subset=["date", "open", "high", "low", "close"]
    )

    # Remove invalid price records
    df = df[
        (df["open"] > 0) &
        (df["high"] > 0) &
        (df["low"] > 0) &
        (df["close"] > 0)
    ]

    # Validate OHLC relationships
    df = df[
        (df["high"] >= df["low"]) &
        (df["high"] >= df["open"]) &
        (df["high"] >= df["close"]) &
        (df["low"] <= df["open"]) &
        (df["low"] <= df["close"])
    ]

    # Sort by date
    df = df.sort_values("date")

    # Remove duplicate dates
    df = df.drop_duplicates(
        subset=["date"],
        keep="last"
    )

    df = df.reset_index(drop=True)

    output_path = (
        PROCESSED_DATA_DIR /
        f"{ticker.upper()}_clean.csv"
    )

    df.to_csv(output_path, index=False)

    print(f"Clean dataset saved: {output_path}")
    print(f"Clean records: {len(df)}")

    return df
