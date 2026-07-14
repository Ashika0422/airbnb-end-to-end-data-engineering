import streamlit as st
import plotly.express as px
import pandas as pd

from components.loader import load_data
from components.filters import sidebar_filters

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Business Insights",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Business Insights & Recommendations")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data()

if df.empty:
    st.error("Dataset not found.")
    st.stop()

df = sidebar_filters(df)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

avg_price = df["price"].mean()

avg_rating = df["review_scores_rating"].mean()

total_reviews = df["number_of_reviews"].sum()

total_listings = len(df)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Average Price",
        f"${avg_price:.2f}"
    )

with c2:
    st.metric(
        "Average Rating",
        f"{avg_rating:.2f}"
    )

with c3:
    st.metric(
        "Total Listings",
        f"{total_listings:,}"
    )

with c4:
    st.metric(
        "Total Reviews",
        f"{int(total_reviews):,}"
    )

st.divider()

# --------------------------------------------------
# PRICE BY ROOM TYPE
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🏠 Average Price by Room Type")

    room = (

        df.groupby("room_type")["price"]

        .mean()

        .reset_index()

        .sort_values("price", ascending=False)

    )

    fig = px.bar(

        room,

        x="room_type",

        y="price",

        color="price",

        color_continuous_scale="Reds"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# --------------------------------------------------
# REVIEWS
# --------------------------------------------------

with right:

    st.subheader("⭐ Reviews by Room Type")

    reviews = (

        df.groupby("room_type")["number_of_reviews"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        reviews,

        x="room_type",

        y="number_of_reviews",

        color="number_of_reviews",

        color_continuous_scale="RdPu"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()

# --------------------------------------------------
# TOP NEIGHBOURHOODS
# --------------------------------------------------

st.subheader("📍 Top 10 Highest Revenue Neighbourhoods")

if "neighbourhood_cleansed" in df.columns:

    revenue = df.copy()

    revenue["estimated_revenue"] = (

        revenue["price"]

        *

        revenue["availability_365"]

    )

    revenue = (

        revenue.groupby("neighbourhood_cleansed")

        ["estimated_revenue"]

        .sum()

        .reset_index()

        .sort_values(

            "estimated_revenue",

            ascending=False

        )

        .head(10)

    )

    fig = px.bar(

        revenue,

        x="neighbourhood_cleansed",

        y="estimated_revenue",

        color="estimated_revenue",

        color_continuous_scale="Reds"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_tickangle=-35

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.subheader("📈 Key Business Insights")

insights = [

"Entire homes command the highest nightly prices compared with private or shared rooms.",

"Neighbourhoods with higher average ratings generally receive more guest reviews.",

"Experienced hosts tend to maintain better review scores and pricing consistency.",

"Highly available listings have greater potential revenue opportunities.",

"Properties with more bedrooms and larger guest capacity usually achieve higher prices."

]

for item in insights:

    st.success(item)

st.divider()

# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

st.subheader("💡 Business Recommendations")

recommendations = [

"Increase investment in high-demand neighbourhoods where prices and occupancy remain consistently high.",

"Encourage hosts to improve guest experience and review ratings through better amenities and communication.",

"Promote Superhosts and experienced hosts as trusted accommodation providers.",

"Use machine learning price predictions to recommend competitive nightly prices for new listings.",

"Monitor low-performing listings and adjust pricing dynamically based on market demand."

]

for rec in recommendations:

    st.info(rec)

st.divider()

# --------------------------------------------------
# SWOT ANALYSIS
# --------------------------------------------------

st.subheader("📊 SWOT Analysis")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### ✅ Strengths")

    st.write("""

- Large number of listings

- Strong review ecosystem

- Diverse property types

- Rich historical data

""")

    st.markdown("### ⚠ Weaknesses")

    st.write("""

- Price variation across neighbourhoods

- Missing values in some host attributes

- Revenue estimation is approximate

""")

with col2:

    st.markdown("### 🚀 Opportunities")

    st.write("""

- Dynamic pricing

- Personalized recommendations

- AI-powered host analytics

- Occupancy prediction

""")

    st.markdown("### ⚡ Threats")

    st.write("""

- Seasonal demand fluctuations

- Market competition

- Regulatory changes

- Economic uncertainty

""")

st.divider()

# --------------------------------------------------
# PROJECT ACHIEVEMENTS
# --------------------------------------------------

st.subheader("🏆 Project Achievements")

achievements = pd.DataFrame({

    "Component":[

        "Data Ingestion",

        "Data Cleaning",

        "Feature Engineering",

        "SQLite Warehouse",

        "Exploratory Analysis",

        "Statistical Analysis",

        "Machine Learning",

        "Interactive Dashboard"

    ],

    "Status":[

        "✅ Completed",

        "✅ Completed",

        "✅ Completed",

        "✅ Completed",

        "✅ Completed",

        "✅ Completed",

        "✅ Completed",

        "✅ Completed"

    ]

})

st.dataframe(

    achievements,

    use_container_width=True

)

st.divider()

# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------

st.success("""

### Executive Summary

This project successfully developed an end-to-end Airbnb Market Intelligence Platform
covering data engineering, exploratory data analysis, statistical analysis,
machine learning, and interactive visualization.

The dashboard enables users to explore pricing trends, neighbourhood performance,
host analytics, and predictive insights while demonstrating a complete modern
data engineering workflow.

""")