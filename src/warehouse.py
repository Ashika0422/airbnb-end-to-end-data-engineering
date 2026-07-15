import os
import sqlite3
import pandas as pd

# =====================================================
# PATH CONFIGURATION
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANSFORMED_DATA = os.path.join(
    BASE_DIR,
    "data",
    "transformed",
    "listings_transformed.csv"
)

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "airbnb.db"
)

# =====================================================
# LOAD TRANSFORMED DATA
# =====================================================

print("=" * 50)
print("      AIRBNB DATA WAREHOUSE CREATION")
print("=" * 50)

print("\nLoading transformed dataset...")

df = pd.read_csv(TRANSFORMED_DATA)

print(f"Dataset Shape : {df.shape}")

# =====================================================
# CONNECT TO SQLITE DATABASE
# =====================================================

conn = sqlite3.connect(DB_PATH)

print("\nConnected to SQLite Database Successfully.")

# =====================================================
# FACT TABLE
# =====================================================

print("\nCreating Fact Table...")

fact_columns = [
    "id",
    "host_id",
    "neighbourhood_cleansed",
    "property_type",
    "room_type",
    "price",
    "accommodates",
    "bedrooms",
    "beds",
    "availability_365",
    "number_of_reviews",
    "review_scores_rating",
    "price_per_person",
    "host_experience"
]

fact_columns = [col for col in fact_columns if col in df.columns]

fact = df[fact_columns]

fact.to_sql(
    "fact_listings",
    conn,
    if_exists="replace",
    index=False
)

print("✓ fact_listings created")

# =====================================================
# HOST DIMENSION
# =====================================================

print("Creating Host Dimension...")

host_columns = [
    "host_id",
    "host_name",
    "host_since",
    "host_experience"
]

host_columns = [col for col in host_columns if col in df.columns]

dim_host = (
    df[host_columns]
    .drop_duplicates()
    .reset_index(drop=True)
)

dim_host.to_sql(
    "dim_host",
    conn,
    if_exists="replace",
    index=False
)

print("✓ dim_host created")

# =====================================================
# LISTING DIMENSION
# =====================================================

print("Creating Listing Dimension...")

listing_columns = [
    "id",
    "property_type",
    "room_type",
    "accommodates",
    "bedrooms",
    "beds"
]

listing_columns = [
    col for col in listing_columns
    if col in df.columns
]

dim_listing = (
    df[listing_columns]
    .drop_duplicates()
    .reset_index(drop=True)
)

dim_listing.to_sql(
    "dim_listing",
    conn,
    if_exists="replace",
    index=False
)

print("✓ dim_listing created")

# =====================================================
# NEIGHBOURHOOD DIMENSION
# =====================================================

print("Creating Neighbourhood Dimension...")

neighbourhood_columns = [
    "neighbourhood_cleansed"
]

neighbourhood_columns = [
    col for col in neighbourhood_columns
    if col in df.columns
]

dim_neighbourhood = (
    df[neighbourhood_columns]
    .drop_duplicates()
    .reset_index(drop=True)
)

dim_neighbourhood.to_sql(
    "dim_neighbourhood",
    conn,
    if_exists="replace",
    index=False
)

print("✓ dim_neighbourhood created")

# =====================================================
# DATE DIMENSION
# =====================================================

print("Creating Date Dimension...")

date_columns = [
    "review_year",
    "review_month"
]

date_columns = [
    col for col in date_columns
    if col in df.columns
]

if len(date_columns) > 0:

    dim_date = (
        df[date_columns]
        .drop_duplicates()
        .sort_values(date_columns)
        .reset_index(drop=True)
    )

    dim_date.to_sql(
        "dim_date",
        conn,
        if_exists="replace",
        index=False
    )

    print("✓ dim_date created")

else:

    print("Date columns not found. Skipping...")

# =====================================================
# VERIFY TABLES
# =====================================================

print("\nDatabase Tables:")

cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

tables = cursor.fetchall()

for table in tables:
    print(f"• {table[0]}")

# =====================================================
# CLOSE CONNECTION
# =====================================================

conn.close()

print("\n" + "=" * 50)
print(" DATA WAREHOUSE CREATED SUCCESSFULLY ")
print("=" * 50)

print(f"\nDatabase Location:\n{DB_PATH}")

print("\nWarehouse Tables Added:")

print("✓ fact_listings")
print("✓ dim_host")
print("✓ dim_listing")
print("✓ dim_neighbourhood")
print("✓ dim_date")

print("\nRaw Tables Preserved:")

print("✓ listings")
print("✓ calendar")
print("✓ reviews")
print("✓ neighbourhoods")