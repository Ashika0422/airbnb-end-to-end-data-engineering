import streamlit as st
import plotly.express as px

from components.loader import load_data
from components.filters import sidebar_filters

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Neighbourhood Analysis",
    page_icon="📍",
    layout="wide"
)

st.title("📍 Neighbourhood Analysis")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = load_data()

if df.empty:
    st.error("Dataset not found.")
    st.stop()

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

df = sidebar_filters(df)

# ---------------------------------------------------
# CHECK REQUIRED COLUMN
# ---------------------------------------------------

if "neighbourhood_cleansed" not in df.columns:
    st.error("Column 'neighbourhood_cleansed' not found.")
    st.stop()

# ---------------------------------------------------
# KPIs
# ---------------------------------------------------

total_neighbourhoods = df["neighbourhood_cleansed"].nunique()

average_price = df.groupby(
    "neighbourhood_cleansed"
)["price"].mean().mean()

average_rating = df.groupby(
    "neighbourhood_cleansed"
)["review_scores_rating"].mean().mean()

total_listings = len(df)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Neighbourhoods",
        total_neighbourhoods
    )

with c2:
    st.metric(
        "Average Price",
        f"${average_price:.2f}"
    )

with c3:
    st.metric(
        "Average Rating",
        f"{average_rating:.2f}"
    )

with c4:
    st.metric(
        "Listings",
        f"{total_listings:,}"
    )

st.divider()

# ---------------------------------------------------
# TOP PRICE
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top 10 Most Expensive Neighbourhoods")

    top_price = (

        df.groupby("neighbourhood_cleansed")["price"]

        .mean()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )

    fig = px.bar(

        top_price,

        x="neighbourhood_cleansed",

        y="price",

        color="price",

        color_continuous_scale="Reds"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5,

        xaxis_title="Neighbourhood",

        yaxis_title="Average Price"

    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# LISTINGS
# ---------------------------------------------------

with right:

    st.subheader("🏘 Top 10 Areas by Listings")

    listing_counts = (

        df["neighbourhood_cleansed"]

        .value_counts()

        .head(10)

        .reset_index()

    )

    listing_counts.columns = [

        "Neighbourhood",

        "Listings"

    ]

    fig = px.bar(

        listing_counts,

        x="Neighbourhood",

        y="Listings",

        color="Listings",

        color_continuous_scale="Reds"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5

    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------------------------
# RATINGS
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("⭐ Best Rated Neighbourhoods")

    ratings = (

        df.groupby("neighbourhood_cleansed")[
            "review_scores_rating"
        ]

        .mean()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )

    fig = px.bar(

        ratings,

        x="neighbourhood_cleansed",

        y="review_scores_rating",

        color="review_scores_rating",

        color_continuous_scale="RdPu"

    )

    fig.update_layout(

        template="plotly_white",

        title_x=0.5,

        yaxis_title="Average Rating"

    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# ROOM TYPE
# ---------------------------------------------------

with right:

    st.subheader("🛏 Room Types")

    room = (

        df["room_type"]

        .value_counts()

        .reset_index()

    )

    room.columns = [

        "Room Type",

        "Count"

    ]

    fig = px.pie(

        room,

        names="Room Type",

        values="Count",

        hole=0.45,

        color_discrete_sequence=px.colors.sequential.Reds

    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------------------------
# MAP
# ---------------------------------------------------

if {"latitude", "longitude"}.issubset(df.columns):

    st.subheader("🗺 Airbnb Listings Map")

    map_df = df[
        [
            "latitude",
            "longitude",
            "price",
            "room_type"
        ]
    ].dropna()

    fig = px.scatter_mapbox(

        map_df,

        lat="latitude",

        lon="longitude",

        color="price",

        size="price",

        hover_data=["room_type"],

        zoom=10,

        height=600,

        color_continuous_scale="Reds"

    )

    fig.update_layout(

        mapbox_style="carto-positron",

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        )

    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------------------------
# TABLE
# ---------------------------------------------------

st.subheader("📋 Neighbourhood Summary")

summary = (

    df.groupby("neighbourhood_cleansed")

    .agg(

        Listings=("price","count"),

        Average_Price=("price","mean"),

        Average_Rating=("review_scores_rating","mean"),

        Reviews=("number_of_reviews","sum")

    )

    .reset_index()

)

st.dataframe(

    summary,

    use_container_width=True

)

st.download_button(

    "⬇ Download Summary",

    summary.to_csv(index=False),

    "neighbourhood_summary.csv",

    "text/csv"

)