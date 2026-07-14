import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import *
from logger import logger

sns.set_style("whitegrid")

os.makedirs(REPORTS, exist_ok=True)
os.makedirs(FIGURES, exist_ok=True)

df = pd.read_csv(
    os.path.join(
        TRANSFORMED_DATA,
        "listings_transformed.csv"
    )
)

logger.info("Dataset Loaded Successfully")
logger.info("%s", df.shape)
logger.info("========== DATASET SUMMARY ==========")
logger.info("%s", df.describe().to_string())

summary = df.describe()

summary.to_csv(
    os.path.join(
        REPORTS,
        "statistics_summary.csv"
    )
)

mean_price = df["price"].mean()
median_price = df["price"].median()
std_price = df["price"].std()

logger.info("Average Price: %s", round(mean_price, 2))
logger.info("Median Price: %s", median_price)
logger.info("Standard Deviation: %s", round(std_price, 2))
logger.info("Minimum Price: %s", df["price"].min())
logger.info("Maximum Price: %s", df["price"].max())
logger.info("Average Rating: %s", round(df["review_scores_rating"].mean(), 2))
logger.info("Average Reviews: %s", round(df["number_of_reviews"].mean(), 2))
logger.info("Average Bedrooms: %s", round(df["bedrooms"].mean(), 2))
logger.info("Average Availability: %s", round(df["availability_365"].mean(), 2))

stats = pd.DataFrame({
    "Metric": [
        "Average Price",
        "Median Price",
        "Standard Deviation",
        "Minimum Price",
        "Maximum Price",
        "Average Rating",
        "Average Reviews",
        "Average Bedrooms",
        "Average Availability"
    ],
    "Value": [
        mean_price,
        median_price,
        std_price,
        df["price"].min(),
        df["price"].max(),
        df["review_scores_rating"].mean(),
        df["number_of_reviews"].mean(),
        df["bedrooms"].mean(),
        df["availability_365"].mean()
    ]
})

stats.to_csv(
    os.path.join(
        REPORTS,
        "key_statistics.csv"
    ),
    index=False
)

columns = [
    "price",
    "accommodates",
    "bedrooms",
    "beds",
    "availability_365",
    "review_scores_rating",
    "number_of_reviews",
    "price_per_person",
    "host_experience"
]

corr = df[columns].corr(numeric_only=True)

corr.to_csv(
    os.path.join(
        REPORTS,
        "correlation_matrix.csv"
    )
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURES,
        "correlation_heatmap_statistics.png"
    )
)

plt.show()

top_price = (
    df.groupby("neighbourhood_cleansed")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

logger.info("%s", top_price.to_string())

top_price.to_csv(
    os.path.join(
        REPORTS,
        "top_neighbourhood_prices.csv"
    )
)

room_stats = (
    df.groupby("room_type")["price"]
    .agg(["mean", "median", "min", "max"])
)

logger.info("%s", room_stats.to_string())

room_stats.to_csv(
    os.path.join(
        REPORTS,
        "room_type_statistics.csv"
    )
)

logger.info("==========================")
logger.info("STATISTICAL ANALYSIS COMPLETED")
logger.info("==========================")
logger.info("Files Saved Successfully!")
