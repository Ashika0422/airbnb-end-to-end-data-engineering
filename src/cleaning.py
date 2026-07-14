import os

import pandas as pd

from config import *
from logger import logger

os.makedirs(CLEANED_DATA, exist_ok=True)

listings = pd.read_csv(os.path.join(RAW_DATA, "listings.csv"))
calendar = pd.read_csv(os.path.join(RAW_DATA, "calendar.csv"))
reviews = pd.read_csv(os.path.join(RAW_DATA, "reviews.csv"))
neighbourhoods = pd.read_csv(os.path.join(RAW_DATA, "neighbourhoods.csv"))

listings["last_scraped"] = pd.to_datetime(listings["last_scraped"])
listings = listings.drop_duplicates()

logger.info("%s", listings.columns.tolist())

listings["price"] = (
    listings["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

listings["price"] = pd.to_numeric(
    listings["price"],
    errors="coerce"
)

listings["reviews_per_month"] = listings["reviews_per_month"].fillna(0)
calendar["date"] = pd.to_datetime(calendar["date"])
calendar["available"] = calendar["available"].replace({
    "t": True,
    "f": False
})

reviews["date"] = pd.to_datetime(reviews["date"])
reviews["comments"] = reviews["comments"].fillna("No Comment")
reviews["reviewer_name"] = reviews["reviewer_name"].fillna("Unknown")

listings.to_csv(
    os.path.join(CLEANED_DATA, "listings_clean.csv"),
    index=False
)

calendar.to_csv(
    os.path.join(CLEANED_DATA, "calendar_clean.csv"),
    index=False
)

reviews.to_csv(
    os.path.join(CLEANED_DATA, "reviews_clean.csv"),
    index=False
)

neighbourhoods.to_csv(
    os.path.join(CLEANED_DATA, "neighbourhoods_clean.csv"),
    index=False
)

logger.info("Cleaning Completed Successfully!")
logger.info("Clean files saved in:")
logger.info("%s", CLEANED_DATA)

