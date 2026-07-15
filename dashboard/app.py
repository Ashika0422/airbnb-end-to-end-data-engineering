import streamlit as st
import plotly.express as px

from pathlib import Path

from components.loader import load_data
from components.cards import metric_card
from components.footer import footer

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Airbnb Market Intelligence",

    page_icon="🏠",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# LOAD CSS
# ==========================================================

css = Path(__file__).parent / "style.css"

with open(css, encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
        /* Main page text: black */
        .stApp, .stApp p, .stApp span, .stApp li, .stApp label,
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
        .stMarkdown, .stMarkdown p, .stMarkdown li,
        div[data-testid="stDataFrame"] *,
        .stDataFrame * {
            color: #111827 !important;
        }

        /* Sidebar text: white */
        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] *,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] h4,
        section[data-testid="stSidebar"] h5,
        section[data-testid="stSidebar"] h6 {
            color: #ffffff !important;
        }

        /* Alerts readable */
        div[data-testid="stAlert"] *,
        div[data-testid="stInfo"] *,
        div[data-testid="stSuccess"] *,
        div[data-testid="stWarning"] *,
        div[data-testid="stError"] * {
            color: #111827 !important;
        }

        /* Keep hero white */
        .hero,
        .hero h1,
        .hero p {
            color: #ffffff !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data()

if df is None or df.empty:

    st.error("Dataset could not be loaded.")

    st.stop()

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="hero">

<h1>

🏠 Airbnb Market Intelligence Platform

</h1>

<p>

End-to-End Data Engineering, Analytics &
Machine Learning Dashboard

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg",
        width=80
    )

    st.markdown("# Airbnb BI Platform")

    st.caption(
        "Business Intelligence Dashboard"
    )

    st.divider()

    # -----------------------------------

    st.markdown("## 📊 Dashboard")

    st.markdown("""

🏠 **Overview**

📈 **Market Analytics**

📍 **Neighbourhood Intelligence**

👤 **Host Analytics**

🤖 **Machine Learning**

💼 **Business Insights**

""")

    st.divider()

    # -----------------------------------

    st.markdown("## 📂 Project")

    st.write("**Dataset**")

    st.write(f"Listings : **{len(df):,}**")

    if "neighbourhood_cleansed" in df.columns:

        st.write(

            f"Neighbourhoods : **{df['neighbourhood_cleansed'].nunique()}**"

        )

    st.write(

        f"Reviews : **{int(df['number_of_reviews'].sum()):,}**"

    )

    st.write("Database : **SQLite**")

    st.write("Warehouse : **Star Schema**")

    st.write("Model : **Random Forest**")

    st.divider()

    # -----------------------------------

    st.markdown("## ⚙ Filters")

    property_types = [

        "All"

    ] + sorted(

        df["property_type"]

        .dropna()

        .astype(str)

        .unique()

    )

    room_types = [

        "All"

    ] + sorted(

        df["room_type"]

        .dropna()

        .astype(str)

        .unique()

    )

    property_selected = st.selectbox(

        "🏠 Property Type",

        property_types

    )

    room_selected = st.selectbox(

        "🛏 Room Type",

        room_types

    )

    price = st.slider(

        "💰 Price Range",

        int(df["price"].min()),

        int(df["price"].max()),

        (

            int(df["price"].min()),

            int(df["price"].max())

        )

    )

    rating = st.slider(

        "⭐ Review Rating",

        float(df["review_scores_rating"].min()),

        float(df["review_scores_rating"].max()),

        (

            float(df["review_scores_rating"].min()),

            float(df["review_scores_rating"].max())

        )

    )

    st.divider()

    if st.button(

        "🔄 Reset Filters",

        use_container_width=True

    ):

        st.rerun()

    st.divider()

    st.markdown("## ⚙ Data Pipeline")

    st.success("""

📥 Raw CSV

↓

🧹 Cleaning

↓

⚙ Feature Engineering

↓

🗄 SQLite Warehouse

↓

📊 EDA

↓

📈 Statistics

↓

🤖 Machine Learning

↓

📋 Dashboard

""")

    st.divider()

    st.caption(

        "Developed by Ashika Chamodi"

    )

# ==========================================================
# FILTER DATA
# ==========================================================

filtered = df.copy()

if property_selected != "All":

    filtered = filtered[

        filtered["property_type"]

        == property_selected

    ]

if room_selected != "All":

    filtered = filtered[

        filtered["room_type"]

        == room_selected

    ]

filtered = filtered[

    (filtered["price"] >= price[0])

    &

    (filtered["price"] <= price[1])

    &

    (filtered["review_scores_rating"] >= rating[0])

    &

    (filtered["review_scores_rating"] <= rating[1])

]

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

st.markdown("## 📊 Executive Summary")

total_listings = len(filtered)

average_price = filtered["price"].mean()

average_rating = filtered["review_scores_rating"].mean()

total_reviews = int(filtered["number_of_reviews"].sum())

c1, c2, c3, c4 = st.columns(4)

with c1:

    metric_card(

        "🏠 Listings",

        f"{total_listings:,}"

    )

with c2:

    metric_card(

        "💰 Average Price",

        f"${average_price:,.0f}"

    )

with c3:

    metric_card(

        "⭐ Average Rating",

        f"{average_rating:.2f}",

        "#00A699"

    )

with c4:

    metric_card(

        "📝 Reviews",

        f"{total_reviews:,}"

    )

st.divider()

# ==========================================================
# DASHBOARD TABS
# ==========================================================

overview, analytics, statistics = st.tabs(

    [

        "🏠 Overview",

        "📊 Analytics",

        "📈 Statistics"

    ]

)

# ==========================================================
# OVERVIEW TAB
# ==========================================================

with overview:

    st.subheader("Project Overview")

    left, right = st.columns([2,1])

    with left:

        st.info("""

### Airbnb Market Intelligence Platform

This project demonstrates an end-to-end
Data Engineering pipeline capable of transforming
raw Airbnb datasets into actionable business insights.

### Project Components

✅ Data Ingestion

✅ Data Cleaning

✅ Feature Engineering

✅ SQLite Data Warehouse

✅ Exploratory Data Analysis

✅ Statistical Analysis

✅ Machine Learning

✅ Interactive Dashboard

""")

    with right:

        st.success("""

### Technology Stack

🐍 Python

🐼 Pandas

🗄 SQLite

📊 Plotly

📈 Streamlit

🤖 Scikit-Learn

🏗 Data Warehouse

""")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Property Types")

        property_chart = (

            filtered["property_type"]

            .value_counts()

            .reset_index()

        )

        property_chart.columns = [

            "Property",

            "Count"

        ]

        fig = px.pie(

            property_chart,

            names="Property",

            values="Count",

            hole=.55,

            color_discrete_sequence=px.colors.sequential.Reds

        )

        fig.update_layout(

            template="plotly_white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        st.subheader("Room Types")

        room_chart = (

            filtered["room_type"]

            .value_counts()

            .reset_index()

        )

        room_chart.columns = [

            "Room",

            "Count"

        ]

        fig = px.bar(

            room_chart,

            x="Room",

            y="Count",

            color="Count",

            color_continuous_scale="Reds"

        )

        fig.update_layout(

            template="plotly_white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

# ==========================================================
# ANALYTICS TAB
# ==========================================================

with analytics:

    st.subheader("Market Analytics")

    left, right = st.columns(2)

    with left:

        fig = px.histogram(

            filtered,

            x="price",

            nbins=40,

            color_discrete_sequence=["#FF5A5F"]

        )

        fig.update_layout(

            title="Price Distribution",

            template="plotly_white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        avg_room = (

            filtered

            .groupby("room_type", as_index=False)

            ["price"]

            .mean()

        )

        fig = px.bar(

            avg_room,

            x="room_type",

            y="price",

            color="price",

            color_continuous_scale="Reds"

        )

        fig.update_layout(

            title="Average Price by Room Type",

            template="plotly_white"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    left, right = st.columns(2)

    with left:

        fig = px.scatter(

            filtered,

            x="number_of_reviews",

            y="price",

            color="room_type",

            size="review_scores_rating",

            hover_data=[

                "property_type"

            ]

        )

        fig.update_layout(

            template="plotly_white",

            title="Reviews vs Price"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        fig = px.box(

            filtered,

            x="room_type",

            y="price",

            color="room_type"

        )

        fig.update_layout(

            template="plotly_white",

            title="Price Spread by Room Type"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

# ==========================================================
# STATISTICS TAB
# ==========================================================

with statistics:

    st.subheader("📈 Descriptive Statistics")

    st.write(
        "Statistical summary of the filtered Airbnb dataset."
    )

    st.dataframe(

        filtered.describe().T,

        use_container_width=True

    )

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("Correlation Heatmap")

        numeric = filtered.select_dtypes(include="number")

        corr = numeric.corr(numeric_only=True)

        fig = px.imshow(

            corr,

            text_auto=".2f",

            aspect="auto",

            color_continuous_scale="RdBu_r"

        )

        fig.update_layout(

            template="plotly_white",

            height=600

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        st.subheader("Dataset Download")

        csv = filtered.to_csv(index=False)

        st.download_button(

            "⬇ Download Filtered Dataset",

            csv,

            "filtered_airbnb.csv",

            "text/csv",

            use_container_width=True

        )

        st.success(

            "Filtered dataset is ready for export."

        )

        st.info(

            f"""

Current Records

• Listings : {len(filtered):,}

• Average Price : ${filtered['price'].mean():.2f}

• Average Rating : {filtered['review_scores_rating'].mean():.2f}

"""
        )

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.divider()

st.markdown("## 💼 Executive Business Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""

### Market Summary

• Total Active Listings : **{len(filtered):,}**

• Average Price : **${filtered['price'].mean():.2f}**

• Average Rating : **{filtered['review_scores_rating'].mean():.2f}**

• Total Reviews : **{int(filtered['number_of_reviews'].sum()):,}**

""")

with col2:

    highest_room = (

        filtered.groupby("room_type")["price"]

        .mean()

        .idxmax()

    )

    highest_price = (

        filtered.groupby("room_type")["price"]

        .mean()

        .max()

    )

    st.info(f"""

### Key Finding

The **{highest_room}** category has the

highest average nightly price.

Average Price

**${highest_price:.2f}**

""")

st.divider()

# ==========================================================
# DATA ENGINEERING PIPELINE
# ==========================================================

st.markdown("## ⚙ Data Engineering Pipeline")

pipeline_left, pipeline_right = st.columns([2, 1])

pipeline_img = Path(__file__).parent / "assets" / "pipeline.png"

with pipeline_left:
    if pipeline_img.exists():
        st.image(str(pipeline_img), use_container_width=True)
    else:
        st.info("Pipeline image not found in dashboard/assets/pipeline.png")

with pipeline_right:
    st.success("""
### Pipeline Overview

✔ Raw CSV Data

↓

✔ Data Ingestion

↓

✔ Data Cleaning

↓

✔ Feature Engineering

↓

✔ SQLite Data Warehouse

↓

✔ Exploratory Data Analysis

↓

✔ Statistical Analysis

↓

✔ Machine Learning

↓

✔ Interactive Dashboard

""")

st.divider()

# ==========================================================
# PROJECT ARCHITECTURE
# ==========================================================

st.markdown("## 🏗 Solution Architecture")

st.code("""

Raw Airbnb CSV Files

        │

        ▼

 Data Ingestion Pipeline

        │

        ▼

 Data Cleaning & Validation

        │

        ▼

 Feature Engineering

        │

        ▼

 SQLite Data Warehouse

        │

        ▼

 Exploratory Data Analysis

        │

        ▼

 Statistical Analysis

        │

        ▼

 Machine Learning

        │

        ▼

 Interactive Dashboard

""")

st.divider()

# ==========================================================
# PROJECT FEATURES
# ==========================================================

st.markdown("## 🚀 Platform Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.success("""

### Data Engineering

✔ ETL Pipeline

✔ Data Validation

✔ Feature Engineering

✔ SQLite Warehouse

""")

with feature2:

    st.info("""

### Analytics

✔ Interactive Charts

✔ KPI Dashboard

✔ Statistical Analysis

✔ Download Reports

""")

with feature3:

    st.warning("""

### Machine Learning

✔ Price Prediction

✔ Feature Importance

✔ Model Evaluation

✔ Business Insights

""")

st.divider()

# ==========================================================
# FINAL DASHBOARD SUMMARY
# ==========================================================

st.markdown("## 📋 Dashboard Summary")

st.write("""

The Airbnb Market Intelligence Platform demonstrates a complete
end-to-end data engineering workflow.

Starting from raw Airbnb datasets, the platform performs automated
data ingestion, cleaning, feature engineering, analytical storage
using SQLite, exploratory analysis, statistical evaluation,
machine learning, and interactive business intelligence
visualization.

This dashboard enables stakeholders to explore pricing trends,
room type performance, neighbourhood characteristics,
listing distributions, and business insights through an
interactive analytical interface.

""")

st.divider()

footer()