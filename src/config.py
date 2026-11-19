
from pathlib import Path

# Main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Output folders
CHART_DIR = BASE_DIR / "outputs" / "charts"
REPORT_DIR = BASE_DIR / "outputs" / "reports"

# Create folders automatically
for folder in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    CHART_DIR,
    REPORT_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)

# Default stock configuration
DEFAULT_TICKER = "AAPL"
DEFAULT_START_DATE = "2021-01-01"

TRADING_DAYS = 252
