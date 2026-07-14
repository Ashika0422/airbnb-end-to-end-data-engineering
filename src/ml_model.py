import os

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from config import *
from logger import logger

os.makedirs(REPORTS, exist_ok=True)
os.makedirs(MODELS, exist_ok=True)
os.makedirs(FIGURES, exist_ok=True)

file_path = os.path.join(TRANSFORMED_DATA, "listings_transformed.csv")

df = pd.read_csv(file_path)

logger.info("===================================")
logger.info("Dataset Loaded Successfully")
logger.info("Shape: %s", df.shape)
logger.info("===================================")

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")

features = [
    "accommodates",
    "bedrooms",
    "beds",
    "availability_365",
    "review_scores_rating",
    "number_of_reviews",
    "host_experience"
]

target = "price"

df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
df["beds"] = df["beds"].fillna(df["beds"].median())
df["review_scores_rating"] = df["review_scores_rating"].fillna(
    df["review_scores_rating"].mean()
)
df["host_experience"] = df["host_experience"].fillna(
    df["host_experience"].median()
)

df = df.dropna(subset=["price"])

logger.info("Missing Values After Cleaning")
logger.info("%s", df[features + [target]].isnull().sum().to_string())
logger.info("Dataset Shape After Cleaning: %s", df.shape)

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

logger.info("========== MODEL RESULTS ==========")
logger.info("MAE        : %.2f", mae)
logger.info("RMSE       : %.2f", rmse)
logger.info("R² Score   : %.4f", r2)

results = f"""
Random Forest Regressor

Dataset Size : {len(df)}

Features Used :
{features}

MAE : {mae:.2f}

RMSE : {rmse:.2f}

R² Score : {r2:.4f}
"""

with open(
    os.path.join(REPORTS, "model_results.txt"),
    "w"
) as file:
    file.write(results)

importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values()

plt.figure(figsize=(8, 6))
importance.plot(kind="barh")
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, "feature_importance.png"))
plt.show()

joblib.dump(
    model,
    os.path.join(
        MODELS,
        "airbnb_price_prediction.pkl"
    )
)

logger.info("===================================")
logger.info("MODEL TRAINED SUCCESSFULLY")
logger.info("===================================")
logger.info("Model Saved Successfully")
logger.info("Results Saved Successfully")
logger.info("Feature Importance Saved Successfully")