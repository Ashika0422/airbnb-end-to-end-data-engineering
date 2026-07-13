import os
import pandas as pd

# ----------------------------
# Project Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")
CLEAN_DATA = os.path.join(BASE_DIR, "data", "cleaned")

os.makedirs(CLEAN_DATA, exist_ok=True)

# ----------------------------
# Load Datasets
# ----------------------------
listings = pd.read_csv(os.path.join(RAW_DATA, "listings.csv"))
calendar = pd.read_csv(os.path.join(RAW_DATA, "calendar.csv"))
reviews = pd.read_csv(os.path.join(RAW_DATA, "reviews.csv"))
neighbourhoods = pd.read_csv(os.path.join(RAW_DATA, "neighbourhoods.csv"))

listings["last_scraped"] = pd.to_datetime(listings["last_scraped"])

listings = listings.drop_duplicates()

print(listings.columns.tolist())

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
    os.path.join(CLEAN_DATA, "listings_clean.csv"),
    index=False
)

calendar.to_csv(
    os.path.join(CLEAN_DATA, "calendar_clean.csv"),
    index=False
)

reviews.to_csv(
    os.path.join(CLEAN_DATA, "reviews_clean.csv"),
    index=False
)

neighbourhoods.to_csv(
    os.path.join(CLEAN_DATA, "neighbourhoods_clean.csv"),
    index=False
)

print("Cleaning Completed Successfully!")

print("Clean files saved in:")
print(CLEAN_DATA)

