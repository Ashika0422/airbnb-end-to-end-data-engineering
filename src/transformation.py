import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEANED_DATA = os.path.join(BASE_DIR, "data", "cleaned")
TRANSFORMED_DATA = os.path.join(BASE_DIR, "data", "transformed")

os.makedirs(TRANSFORMED_DATA, exist_ok=True)

df = pd.read_csv(
    os.path.join(CLEANED_DATA, "listings_clean.csv")
)

print("Dataset Loaded Successfully")
print(df.shape)

date_columns = [
    "host_since",
    "first_review",
    "last_review"
]

for column in date_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )
# Feature Engineering: 

df["price_per_person"] = (
    df["price"] /
    df["accommodates"]
)

current_year = pd.Timestamp.now().year

df["host_experience"] = (
    current_year - df["host_since"].dt.year
)

# Replace missing values with the median
df["host_experience"] = df["host_experience"].fillna(
    df["host_experience"].median()
)

df["review_year"] = (
    df["last_review"].dt.year
)

df["review_month"] = (
    df["last_review"].dt.month
)

df["review_scores_rating"] = (
    df["review_scores_rating"]
    .fillna(df["review_scores_rating"].mean())
)

df["bedrooms"] = (
    df["bedrooms"]
    .fillna(df["bedrooms"].median())
)

df["beds"] = (
    df["beds"]
    .fillna(df["beds"].median())
)

columns_to_remove = [

    "listing_url",

    "picture_url",

    "host_url",

    "host_thumbnail_url",

    "host_picture_url",

    "calendar_updated"

]

df.drop(
    columns=[
        col
        for col in columns_to_remove
        if col in df.columns
    ],
    inplace=True
)

print()

print("Final Dataset Shape")

print(df.shape)

print()

print(df.head())

output_path = os.path.join(
    TRANSFORMED_DATA,
    "listings_transformed.csv"
)

df.to_csv(
    output_path,
    index=False
)

print()

print("Transformation Completed Successfully!")

print(f"Saved to:\n{output_path}")

