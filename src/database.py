import os
import sqlite3

import pandas as pd

from config import *
from logger import logger

os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

listings = pd.read_csv(os.path.join(CLEANED_DATA, "listings_clean.csv"))
calendar = pd.read_csv(os.path.join(CLEANED_DATA, "calendar_clean.csv"))
reviews = pd.read_csv(os.path.join(CLEANED_DATA, "reviews_clean.csv"))
neighbourhoods = pd.read_csv(os.path.join(CLEANED_DATA, "neighbourhoods_clean.csv"))

conn = sqlite3.connect(DATABASE)

listings.to_sql("listings", conn, if_exists="replace", index=False)
calendar.to_sql("calendar", conn, if_exists="replace", index=False)
reviews.to_sql("reviews", conn, if_exists="replace", index=False)
neighbourhoods.to_sql("neighbourhoods", conn, if_exists="replace", index=False)

logger.info("Database created successfully!")

conn.close()