import streamlit as st
import plotly.express as px

from pathlib import Path

from components.loader import load_data
from components.cards import metric_card
from components.footer import footer

# =======================================================
# PAGE CONFIG
# =======================================================


st.set_page_config(

    page_title="Airbnb Market Intelligence",

    page_icon="🏠",

    layout="wide",

)

# =======================================================
# LOAD CSS
# =======================================================

css = Path(__file__).parent / "style.css"

with open(css, encoding="utf-8") as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True

    )

# =======================================================
# LOAD DATA
# =======================================================

df = load_data()

# =======================================================
# HEADER
# =======================================================

st.markdown("""

<div class="hero">

<h1>

🏠 Airbnb Market Intelligence Platform

</h1>

<p>

Interactive End-to-End Data Engineering &
Analytics Dashboard

</p>

</div>

""", unsafe_allow_html=True)

# =======================================================
# DATA CHECK
# =======================================================

if df is None or df.empty:

    st.error("Dataset not found.")

    st.stop()

# =======================================================
# SIDEBAR
# =======================================================

with st.sidebar:

    st.title("⚙ Dashboard Filters")

    property_types = ["All"] + sorted(
        df["property_type"].dropna().unique()
    )

    room_types = ["All"] + sorted(
        df["room_type"].dropna().unique()
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

        "💰 Price",

        int(df["price"].min()),

        int(df["price"].max()),

        (
            int(df["price"].min()),
            int(df["price"].max())
        )

    )

# =======================================================
# FILTERING
# =======================================================

filtered = df.copy()

if property_selected != "All":

    filtered = filtered[
        filtered["property_type"] == property_selected
    ]

if room_selected != "All":

    filtered = filtered[
        filtered["room_type"] == room_selected
    ]

filtered = filtered[

    (filtered["price"] >= price[0])

    &

    (filtered["price"] <= price[1])

]

# =======================================================
# KPI
# =======================================================

st.markdown("## Executive Summary")

c1,c2,c3,c4 = st.columns(4)

with c1:

    metric_card(

        "Listings",

        f"{len(filtered):,}"

    )

with c2:

    metric_card(

        "Average Price",

        f"${filtered['price'].mean():.0f}"

    )

with c3:

    metric_card(

        "Average Rating",

        f"{filtered['review_scores_rating'].mean():.2f}",

        "#00A699"

    )

with c4:

    metric_card(

        "Reviews",

        f"{int(filtered['number_of_reviews'].sum()):,}"

    )

st.divider()

# =======================================================
# TABS
# =======================================================

overview,analytics,statistics = st.tabs(

    [

        "🏠 Overview",

        "📊 Analytics",

        "📈 Statistics"

    ]

)

# =======================================================
# OVERVIEW
# =======================================================

with overview:

    st.subheader("Project Overview")

    st.write("""

This dashboard demonstrates an end-to-end

Airbnb Data Engineering pipeline.

✔ Data Ingestion

✔ Data Cleaning

✔ Feature Engineering

✔ SQLite Data Warehouse

✔ Exploratory Data Analysis

✔ Statistical Analysis

✔ Machine Learning

✔ Interactive Dashboard

""")

# =======================================================
# ANALYTICS
# =======================================================

with analytics:

    left,right = st.columns(2)

    with left:

        fig = px.histogram(

            filtered,

            x="price",

            nbins=30,

            title="Price Distribution",

            color_discrete_sequence=["#FF5A5F"]

        )

        fig.update_layout(template="plotly_white")

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        room = filtered.groupby(

            "room_type",

            as_index=False

        )["price"].mean()

        fig = px.bar(

            room,

            x="room_type",

            y="price",

            color="price",

            color_continuous_scale="Reds"

        )

        fig.update_layout(template="plotly_white")

        st.plotly_chart(

            fig,

            use_container_width=True

        )

# =======================================================
# STATISTICS
# =======================================================

with statistics:

    st.dataframe(

        filtered.describe(),

        use_container_width=True

    )

    st.download_button(

        "⬇ Download Filtered Dataset",

        filtered.to_csv(index=False),

        "filtered_airbnb.csv"

    )

st.divider()

st.markdown("## ⚙ Data Engineering Pipeline")

st.success("""

📥 Raw CSV Files

↓

🧹 Data Cleaning

↓

⚙ Feature Engineering

↓

🗄 SQLite Data Warehouse

↓

📊 Exploratory Data Analysis

↓

📈 Statistical Analysis

↓

🤖 Machine Learning

↓

📋 Interactive Dashboard

""")

footer()