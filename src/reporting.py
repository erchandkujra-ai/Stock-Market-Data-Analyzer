
import json

from src.config import REPORT_DIR


def generate_report(ticker, summary):

    report = {
        "project": "Stock Market Data Analyzer",
        "ticker": ticker,
        "analysis": summary,
        "disclaimer": (
            "Educational analysis only. "
            "Not financial advice."
        )
    }

    output_path = (
        REPORT_DIR /
        f"{ticker.upper()}_report.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    # Human-readable report
    text_path = (
        REPORT_DIR /
        f"{ticker.upper()}_report.txt"
    )

    with open(
        text_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "STOCK MARKET DATA ANALYZER\n"
        )

        file.write("=" * 40 + "\n\n")

        file.write(f"Ticker: {ticker}\n\n")

        for key, value in summary.items():

            file.write(
                f"{key}: {value}\n"
            )

        file.write(
            "\nEducational purposes only. "
            "Not financial advice.\n"
        )

    print(f"Report saved: {text_path}")

    return output_path
