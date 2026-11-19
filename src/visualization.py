
import matplotlib.pyplot as plt
import seaborn as sns

from src.config import CHART_DIR


sns.set_theme(style="darkgrid")


def create_charts(data, ticker="AAPL"):

    df = data.copy()

    # Chart 1: Closing price
    plt.figure(figsize=(12, 6))

    plt.plot(
        df["date"],
        df["close"],
        label="Closing Price"
    )

    plt.title(f"{ticker} Stock Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "stock_price.png",
        dpi=150
    )

    plt.close()

    # Chart 2: Moving averages
    plt.figure(figsize=(12, 6))

    plt.plot(
        df["date"],
        df["close"],
        label="Close"
    )

    plt.plot(
        df["date"],
        df["sma20"],
        label="SMA 20"
    )

    plt.plot(
        df["date"],
        df["sma50"],
        label="SMA 50"
    )

    plt.title(f"{ticker} Moving Average Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "moving_average.png",
        dpi=150
    )

    plt.close()

    # Chart 3: Daily returns distribution
    plt.figure(figsize=(10, 5))

    sns.histplot(
        df["daily_return"].dropna(),
        bins=40,
        kde=True
    )

    plt.title(f"{ticker} Daily Returns Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "daily_returns.png",
        dpi=150
    )

    plt.close()

    print("All charts generated successfully.")
