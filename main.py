
import argparse

from src.ingest import fetch_stock_data
from src.cleaning import clean_stock_data
from src.indicators import calculate_indicators
from src.analysis import analyze_stock
from src.visualization import create_charts
from src.reporting import generate_report

from src.config import PROCESSED_DATA_DIR


def run_project(ticker, start, csv_mode=False):

    ticker = ticker.upper()

    print("\n" + "=" * 55)
    print("       STOCK MARKET DATA ANALYZER")
    print("=" * 55)

    # Phase 1: Fetch data
    if csv_mode:
        import pandas as pd

        data = pd.read_csv(
            PROCESSED_DATA_DIR /
            f"{ticker}_clean.csv",
            parse_dates=["date"]
        )
    else:
        data = fetch_stock_data(
            ticker=ticker,
            start=start
        )

    # Phase 2: Clean data
    clean_data = clean_stock_data(
        data,
        ticker
    )

    # Phase 3: Calculate indicators
    analyzed_data = calculate_indicators(
        clean_data
    )

    # Save processed indicators
    analyzed_data.to_csv(
        PROCESSED_DATA_DIR /
        f"{ticker}_analysis.csv",
        index=False
    )

    # Phase 4: Analyze
    summary = analyze_stock(
        analyzed_data
    )

    # Phase 5: Visualizations
    create_charts(
        analyzed_data,
        ticker
    )

    # Phase 6: Report
    generate_report(
        ticker,
        summary
    )

    print("\nSTOCK ANALYSIS SUMMARY")
    print("-" * 40)

    for key, value in summary.items():

        print(f"{key}: {value}")

    print("\nPROJECT COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Stock Market Data Analyzer"
    )

    parser.add_argument(
        "--ticker",
        default="AAPL"
    )

    parser.add_argument(
        "--start",
        default="2021-01-01"
    )

    parser.add_argument(
        "--csv",
        action="store_true",
        help="Load existing cleaned CSV data"
    )

    args = parser.parse_args()

    run_project(
        ticker=args.ticker,
        start=args.start,
        csv_mode=args.csv
    )
