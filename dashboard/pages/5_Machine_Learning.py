import os
import joblib
import pandas as pd
import streamlit as st

from components.loader import load_data

# ---------------------------------------------
# PAGE CONFIG
# ---------------------------------------------

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Airbnb Price Prediction")

# ---------------------------------------------
# PATHS
# ---------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "airbnb_price_prediction.pkl"
)

RESULT_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "model_results.txt"
)

FEATURE_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "figures",
    "feature_importance.png"
)

# ---------------------------------------------
# LOAD MODEL
# ---------------------------------------------

try:
    model = joblib.load(MODEL_PATH)
except Exception:
    st.error("Model not found.")
    st.stop()

df = load_data()

st.success("Model Loaded Successfully")

# ---------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------

st.sidebar.header("Prediction Inputs")

accommodates = st.sidebar.slider(
    "Guests",
    1,
    16,
    2
)

bedrooms = st.sidebar.slider(
    "Bedrooms",
    0,
    10,
    1
)

beds = st.sidebar.slider(
    "Beds",
    1,
    15,
    1
)

availability = st.sidebar.slider(
    "Availability (Days)",
    0,
    365,
    180
)

rating = st.sidebar.slider(
    "Review Rating",
    0.0,
    5.0,
    4.7,
    0.1
)

reviews = st.sidebar.slider(
    "Number of Reviews",
    0,
    500,
    50
)

experience = st.sidebar.slider(
    "Host Experience",
    0,
    20,
    5
)

# ---------------------------------------------
# PREDICT
# ---------------------------------------------

input_df = pd.DataFrame({

    "accommodates":[accommodates],

    "bedrooms":[bedrooms],

    "beds":[beds],

    "availability_365":[availability],

    "review_scores_rating":[rating],

    "number_of_reviews":[reviews],

    "host_experience":[experience]

})

prediction = model.predict(input_df)[0]

# ---------------------------------------------
# RESULT
# ---------------------------------------------

st.markdown("---")

st.subheader("💰 Estimated Airbnb Price")

st.metric(
    "Predicted Nightly Price",
    f"${prediction:.2f}"
)

# ---------------------------------------------
# MODEL INFORMATION
# ---------------------------------------------

st.markdown("---")

left,right = st.columns(2)

with left:

    st.subheader("Model Details")

    st.info("""

Algorithm

Random Forest Regressor

Prediction Type

Regression

Target Variable

Nightly Airbnb Price

""")

with right:

    st.subheader("Training Dataset")

    st.metric(
        "Listings",
        len(df)
    )

    st.metric(
        "Features",
        7
    )

# ---------------------------------------------
# METRICS
# ---------------------------------------------

st.markdown("---")

st.subheader("Model Performance")

if os.path.exists(RESULT_PATH):

    with open(RESULT_PATH) as f:

        st.code(f.read())

# ---------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------

st.markdown("---")

st.subheader("Feature Importance")

if os.path.exists(FEATURE_PATH):

    st.image(
        FEATURE_PATH,
        use_container_width=True
    )

# ---------------------------------------------
# FEATURE DESCRIPTION
# ---------------------------------------------

st.markdown("---")

st.subheader("Features Used")

feature_table = pd.DataFrame({

    "Feature":[

        "Guests",

        "Bedrooms",

        "Beds",

        "Availability",

        "Review Rating",

        "Reviews",

        "Host Experience"

    ],

    "Description":[

        "Maximum guests",

        "Number of bedrooms",

        "Number of beds",

        "Available days",

        "Average rating",

        "Total reviews",

        "Years hosting"

    ]

})

st.dataframe(
    feature_table,
    use_container_width=True
)

# ---------------------------------------------
# BUSINESS INTERPRETATION
# ---------------------------------------------

st.markdown("---")

st.subheader("Business Interpretation")

st.success("""

Higher prices are generally associated with:

• More bedrooms

• Higher guest capacity

• Better review ratings

• Experienced hosts

• High availability

These insights can help Airbnb hosts optimise pricing strategies.

""")