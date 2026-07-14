import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import *
from logger import logger

sns.set_style("whitegrid")

os.makedirs(FIGURES, exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(os.path.join(CLEANED_DATA, "listings_clean.csv"))

plt.figure(figsize=(10,6))

plt.hist(df["price"], bins=40)

plt.title("Distribution of Airbnb Prices")
plt.xlabel("Price")
plt.ylabel("Number of Listings")

plt.savefig(os.path.join(FIGURES, "price_distribution.png"))

plt.show()

plt.figure(figsize=(8,6))

df["room_type"].value_counts().plot(kind="bar")

plt.title("Distribution of Room Types")
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"room_type_distribution.png"))
plt.show()

plt.figure(figsize=(8,6))

df.groupby("room_type")["price"].mean().sort_values().plot(kind="bar")

plt.title("Average Price by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"average_price_room_type.png"))
plt.show()

plt.figure(figsize=(10,6))

df["neighbourhood_cleansed"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Neighbourhoods by Number of Listings")
plt.xlabel("Neighbourhood")
plt.ylabel("Listings")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"top10_neighbourhoods.png"))
plt.show()

plt.figure(figsize=(12,6))

df.groupby("neighbourhood_cleansed")["price"]\
.mean()\
.sort_values(ascending=False)\
.head(10)\
.plot(kind="bar")

plt.title("Top 10 Most Expensive Neighbourhoods")
plt.xlabel("Neighbourhood")
plt.ylabel("Average Price")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"expensive_neighbourhoods.png"))
plt.show()

plt.figure(figsize=(8,6))

plt.hist(df["review_scores_rating"].dropna(), bins=25)

plt.title("Distribution of Review Scores")
plt.xlabel("Review Rating")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"review_score_distribution.png"))
plt.show()

plt.figure(figsize=(6,6))

df["host_is_superhost"].value_counts().plot(kind="bar")

plt.title("Superhost vs Non-Superhost")
plt.xlabel("Superhost")
plt.ylabel("Number of Hosts")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"superhost_distribution.png"))
plt.show()

plt.figure(figsize=(8,6))

plt.hist(df["availability_365"], bins=30)

plt.title("Availability Throughout the Year")
plt.xlabel("Available Days")
plt.ylabel("Listings")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"availability_distribution.png"))
plt.show()

plt.figure(figsize=(12,8))

columns = [
    "price",
    "accommodates",
    "bedrooms",
    "beds",
    "availability_365",
    "number_of_reviews",
    "review_scores_rating"
]

corr = df[columns].corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"correlation_heatmap.png"))
plt.show()

plt.figure(figsize=(8,6))

plt.scatter(
    df["review_scores_rating"],
    df["price"],
    alpha=0.3
)

plt.title("Price vs Review Score")
plt.xlabel("Review Score")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"price_vs_review.png"))
plt.show()

plt.figure(figsize=(8,6))

plt.hist(
    df["estimated_revenue_l365d"].dropna(),
    bins=30
)

plt.title("Estimated Annual Revenue Distribution")
plt.xlabel("Estimated Revenue")
plt.ylabel("Listings")

plt.tight_layout()

plt.savefig(os.path.join(FIGURES,"estimated_revenue.png"))
plt.show()

logger.info("Analysis figures saved to %s", FIGURES)