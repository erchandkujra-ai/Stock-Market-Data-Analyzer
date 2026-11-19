
import sqlite3

from pathlib import Path
from contextlib import contextmanager


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database directory
DB_DIR = BASE_DIR / "db"

# Database file
DB_PATH = DB_DIR / "market.db"

# SQL schema
SCHEMA_PATH = DB_DIR / "schema.sql"


def initialize_database():

    # Create database directory if missing
    DB_DIR.mkdir(parents=True, exist_ok=True)

    # Check schema file
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(
            f"Database schema not found: {SCHEMA_PATH}"
        )

    # Read schema
    schema = SCHEMA_PATH.read_text(
        encoding="utf-8"
    )

    # Initialize database
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.executescript(schema)
        connection.commit()

    finally:
        connection.close()

    print("Database initialized successfully.")


@contextmanager
def get_connection():

    DB_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
