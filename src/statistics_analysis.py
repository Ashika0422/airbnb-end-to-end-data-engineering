import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANSFORMED_DATA = os.path.join(BASE_DIR, "data", "transformed")
REPORTS = os.path.join(BASE_DIR, "reports")
FIGURES = os.path.join(REPORTS, "figures")

os.makedirs(REPORTS, exist_ok=True)
os.makedirs(FIGURES, exist_ok=True)

df = pd.read_csv(
    os.path.join(
        TRANSFORMED_DATA,
        "listings_transformed.csv"
    )
)

print("Dataset Loaded Successfully")
print(df.shape)

print("\n========== DATASET SUMMARY ==========\n")

print(df.describe())

summary = df.describe()

summary.to_csv(
    os.path.join(
        REPORTS,
        "statistics_summary.csv"
    )
)

mean_price = df["price"].mean()
print("Average Price:", round(mean_price,2))

median_price = df["price"].median()
print("Median Price:", median_price)

std_price = df["price"].std()
print("Standard Deviation:", round(std_price,2))

print("Minimum Price:", df["price"].min())

print("Maximum Price:", df["price"].max())

print(
    "Average Rating:",
    round(
        df["review_scores_rating"].mean(),
        2
    )
)

print(
    "Average Reviews:",
    round(
        df["number_of_reviews"].mean(),
        2
    )
)

print(
    "Average Bedrooms:",
    round(
        df["bedrooms"].mean(),
        2
    )
)

print(
    "Average Availability:",
    round(
        df["availability_365"].mean(),
        2
    )
)

stats = pd.DataFrame({

"Metric":[
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

"Value":[
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

plt.figure(figsize=(10,8))

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
df.groupby(
"neighbourhood_cleansed"
)["price"]
.mean()
.sort_values(ascending=False)
.head(10)
)

print(top_price)

top_price.to_csv(

os.path.join(
REPORTS,
"top_neighbourhood_prices.csv"
)

)

room_stats = (

df.groupby(
"room_type"
)["price"]

.agg(
["mean","median","min","max"]
)

)

print(room_stats)

room_stats.to_csv(

os.path.join(
REPORTS,
"room_type_statistics.csv"
)

)

print("\n==========================")

print("STATISTICAL ANALYSIS COMPLETED")

print("==========================")

print("Files Saved Successfully!")
