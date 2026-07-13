import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRANSFORMED_DATA = os.path.join(BASE_DIR, "data", "transformed")
REPORTS = os.path.join(BASE_DIR, "reports")
MODELS = os.path.join(BASE_DIR, "models")
FIGURES = os.path.join(REPORTS, "figures")

os.makedirs(REPORTS, exist_ok=True)
os.makedirs(MODELS, exist_ok=True)
os.makedirs(FIGURES, exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

file_path = os.path.join(TRANSFORMED_DATA, "listings_transformed.csv")

df = pd.read_csv(file_path)

print("===================================")
print("Dataset Loaded Successfully")
print("Shape:", df.shape)
print("===================================")

# =====================================================
# Convert Price to Numeric
# =====================================================

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")

# =====================================================
# Feature Selection
# =====================================================

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

# =====================================================
# Handle Missing Values
# =====================================================

df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
df["beds"] = df["beds"].fillna(df["beds"].median())

df["review_scores_rating"] = df["review_scores_rating"].fillna(
    df["review_scores_rating"].mean()
)

df["host_experience"] = df["host_experience"].fillna(
    df["host_experience"].median()
)

df = df.dropna(subset=["price"])

print("\nMissing Values After Cleaning")
print(df[features + [target]].isnull().sum())

print("\nDataset Shape After Cleaning:", df.shape)

# =====================================================
# Features and Target
# =====================================================

X = df[features]
y = df[target]

# =====================================================
# Train-Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =====================================================
# Train Model
# =====================================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================================
# Prediction
# =====================================================

predictions = model.predict(X_test)

# =====================================================
# Evaluation
# =====================================================

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

print("\n========== MODEL RESULTS ==========")

print(f"MAE        : {mae:.2f}")
print(f"RMSE       : {rmse:.2f}")
print(f"R² Score   : {r2:.4f}")

# =====================================================
# Save Results
# =====================================================

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

# =====================================================
# Feature Importance
# =====================================================

importance = pd.Series(
    model.feature_importances_,
    index=features
)

importance = importance.sort_values()

plt.figure(figsize=(8, 6))

importance.plot(kind="barh")

plt.title("Feature Importance")

plt.xlabel("Importance Score")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURES,
        "feature_importance.png"
    )
)

plt.show()

# =====================================================
# Save Model
# =====================================================

joblib.dump(
    model,
    os.path.join(
        MODELS,
        "airbnb_price_prediction.pkl"
    )
)

print("\n===================================")
print("MODEL TRAINED SUCCESSFULLY")
print("===================================")

print("Model Saved Successfully")
print("Results Saved Successfully")
print("Feature Importance Saved Successfully")