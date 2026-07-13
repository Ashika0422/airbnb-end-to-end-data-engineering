import os
import sqlite3
import pandas as pd

# -------------------------
# Project Paths
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEAN_DATA = os.path.join(BASE_DIR, "data", "cleaned")
DATABASE = os.path.join(BASE_DIR, "data", "airbnb.db")

# -------------------------
# Load Cleaned Data
# -------------------------
listings = pd.read_csv(os.path.join(CLEAN_DATA, "listings_clean.csv"))
calendar = pd.read_csv(os.path.join(CLEAN_DATA, "calendar_clean.csv"))
reviews = pd.read_csv(os.path.join(CLEAN_DATA, "reviews_clean.csv"))
neighbourhoods = pd.read_csv(os.path.join(CLEAN_DATA, "neighbourhoods_clean.csv"))

# -------------------------
# Create Database
# -------------------------
conn = sqlite3.connect(DATABASE)

listings.to_sql("listings", conn, if_exists="replace", index=False)
calendar.to_sql("calendar", conn, if_exists="replace", index=False)
reviews.to_sql("reviews", conn, if_exists="replace", index=False)
neighbourhoods.to_sql("neighbourhoods", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()