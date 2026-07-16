import sqlite3
import pandas as pd
from pathlib import Path

# ==========================================
# PROJECT ROOT
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "database" / "airbnb.db"

# ==========================================
# LOAD DATA
# ==========================================

def load_data():

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found:\n{DB_PATH}"
        )

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        "SELECT * FROM fact_listings",
        conn
    )

    conn.close()

    return df