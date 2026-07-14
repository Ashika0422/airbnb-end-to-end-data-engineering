import os

import pandas as pd

from config import *
from logger import logger

os.makedirs(REPORTS, exist_ok=True)

file_path = os.path.join(CLEANED_DATA, "listings_clean.csv")
df = pd.read_csv(file_path)

report_lines = []


def add_section(title, value):
    report_lines.append(title)
    report_lines.append("-" * len(title))
    report_lines.append(str(value))
    report_lines.append("")


duplicate_ids = 0
if "id" in df.columns:
    duplicate_ids = int(df["id"].duplicated().sum())
elif "listing_id" in df.columns:
    duplicate_ids = int(df["listing_id"].duplicated().sum())

missing_values = df.isnull().sum().sort_values(ascending=False)
negative_prices = int(pd.to_numeric(df["price"], errors="coerce").lt(0).sum()) if "price" in df.columns else 0
invalid_latitude = int(
    pd.to_numeric(df["latitude"], errors="coerce").dropna().pipe(lambda series: ((series < -90) | (series > 90)).sum())
) if "latitude" in df.columns else 0
invalid_longitude = int(
    pd.to_numeric(df["longitude"], errors="coerce").dropna().pipe(lambda series: ((series < -180) | (series > 180)).sum())
) if "longitude" in df.columns else 0
empty_listing_names = int(
    df["name"].astype(str).str.strip().eq("").sum()
) if "name" in df.columns else 0

add_section("Duplicate IDs", duplicate_ids)
add_section("Missing Values", missing_values.to_string())
add_section("Negative Prices", negative_prices)
add_section("Invalid Latitude", invalid_latitude)
add_section("Invalid Longitude", invalid_longitude)
add_section("Empty Listing Names", empty_listing_names)

report_path = os.path.join(REPORTS, "validation_report.txt")

with open(report_path, "w", encoding="utf-8") as file:
    file.write("\n".join(report_lines))

logger.info("Validation report saved to %s", report_path)
logger.info("Duplicate IDs: %s", duplicate_ids)
logger.info("Negative Prices: %s", negative_prices)
logger.info("Invalid Latitude: %s", invalid_latitude)
logger.info("Invalid Longitude: %s", invalid_longitude)
logger.info("Empty Listing Names: %s", empty_listing_names)
