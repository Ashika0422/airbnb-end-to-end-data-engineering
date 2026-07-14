import os
import sys

import joblib

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from config import *

MODEL_PATH = os.path.join(MODELS, "airbnb_price_prediction.pkl")


def get_number(prompt, default_value):
    raw_value = input(f"{prompt} [{default_value}]: ").strip()
    if not raw_value:
        return float(default_value)
    try:
        return float(raw_value)
    except ValueError:
        print(f"Invalid value. Using default {default_value}.")
        return float(default_value)


def main():
    if not os.path.exists(MODEL_PATH):
        print(f"Model not found at {MODEL_PATH}")
        return

    model = joblib.load(MODEL_PATH)

    print("AIRBNB PRICE PREDICTION")
    print("Enter values or press Enter to use defaults.")

    features = {
        "accommodates": get_number("Accommodates", 4),
        "bedrooms": get_number("Bedrooms", 2),
        "beds": get_number("Beds", 3),
        "availability_365": get_number("Availability", 220),
        "review_scores_rating": get_number("Rating", 4.8),
        "number_of_reviews": get_number("Reviews", 50),
        "host_experience": get_number("Host Experience", 8),
    }

    prediction = model.predict([list(features.values())])[0]

    predicted_price_per_person = prediction / features["accommodates"] if features["accommodates"] else prediction

    print()
    print("Predicted Price")
    print(f"${prediction:.2f}")
    print(f"Predicted Price Per Person: ${predicted_price_per_person:.2f}")


if __name__ == "__main__":
    main()
