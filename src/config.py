import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===========================
# DATA FOLDERS
# ===========================

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")

CLEANED_DATA = os.path.join(BASE_DIR, "data", "cleaned")

TRANSFORMED_DATA = os.path.join(BASE_DIR, "data", "transformed")

PROCESSED_DATA = os.path.join(BASE_DIR, "data", "processed")

# ===========================
# DATABASE
# ===========================

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "airbnb.db"
)

# ===========================
# REPORTS
# ===========================

REPORTS = os.path.join(BASE_DIR, "reports")

FIGURES = os.path.join(REPORTS, "figures")

TABLES = os.path.join(REPORTS, "tables")

# ===========================
# MODELS
# ===========================

MODELS = os.path.join(BASE_DIR, "models")

# ===========================
# LOGS
# ===========================

LOGS = os.path.join(BASE_DIR, "logs")