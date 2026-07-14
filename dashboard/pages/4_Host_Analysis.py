import streamlit as st
import plotly.express as px
import pandas as pd

from components.loader import load_data
from components.filters import sidebar_filters

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Host Analysis",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Host Analysis")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data()

if df.empty:
    st.error("Dataset not found.")
    st.stop()

df = sidebar_filters(df)

# --------------------------------------------------
# CREATE OPTIONAL COLUMNS
# --------------------------------------------------

if "host_name" not in df.columns:
    df["host_name"] = "Unknown Host"

if "host_is_superhost" not in df.columns:
    df["host_is_superhost"] = "Unknown"

if "host_response_rate" in df.columns:
    df["host_response_rate"] = (
        df["host_response_rate"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["host_response_rate"] = pd.to_numeric(
        df["host_response_rate"],
        errors="coerce"
    )

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

total_hosts = df["host_id"].nunique()

superhosts = (
    df["host_is_superhost"]
    .astype(str)
    .str.lower()
    .eq("t")
    .sum()
)

avg_exp = (
    df["host_experience"].mean()
    if "host_experience" in df.columns
    else 0
)

avg_response = (
    df["host_response_rate"].mean()
    if "host_response_rate" in df.columns
    else 0
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Hosts",
        f"{total_hosts:,}"
    )

with c2:
    st.metric(
        "Superhosts",
        f"{superhosts:,}"
    )

with c3:
    st.metric(
        "Avg Host Experience",
        f"{avg_exp:.1f} Years"
    )

with c4:
    st.metric(
        "Avg Response Rate",
        f"{avg_response:.1f}%"
    )

st.divider()

# --------------------------------------------------
# TOP HOSTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top Hosts by Listings")

    top_hosts = (
        df.groupby("host_name")
        .size()
        .reset_index(name="Listings")
        .sort_values("Listings", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_hosts,
        x="host_name",
        y="Listings",
        color="Listings",
        color_continuous_scale="Reds"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Host",
        yaxis_title="Listings"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# SUPERHOSTS
# --------------------------------------------------

with right:

    st.subheader("⭐ Superhost Distribution")

    superhost_df = (
        df["host_is_superhost"]
        .astype(str)
        .replace({
            "t": "Superhost",
            "f": "Regular Host",
            "Unknown": "Unknown"
        })
        .value_counts()
        .reset_index()
    )

    superhost_df.columns = [
        "Host Type",
        "Count"
    ]

    fig = px.pie(
        superhost_df,
        names="Host Type",
        values="Count",
        hole=0.45,
        color_discrete_sequence=px.colors.sequential.Reds
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

left, right = st.columns(2)

if "host_experience" in df.columns:

    with left:

        st.subheader("📈 Host Experience")

        fig = px.histogram(
            df,
            x="host_experience",
            nbins=20,
            color_discrete_sequence=["#FF5A5F"]
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.subheader("💰 Price vs Experience")

        exp_price = (
            df.groupby("host_experience")["price"]
            .mean()
            .reset_index()
        )

        fig = px.line(
            exp_price,
            x="host_experience",
            y="price",
            markers=True
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# RESPONSE RATE
# --------------------------------------------------

if "host_response_rate" in df.columns:

    st.subheader("📨 Host Response Rate")

    fig = px.histogram(
        df,
        x="host_response_rate",
        nbins=20,
        color_discrete_sequence=["#FF5A5F"]
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --------------------------------------------------
# HOST SUMMARY TABLE
# --------------------------------------------------

st.subheader("📋 Host Summary")

summary = (
    df.groupby(["host_id", "host_name"])
    .agg(
        Listings=("price", "count"),
        Average_Price=("price", "mean"),
        Reviews=("number_of_reviews", "sum"),
        Average_Rating=("review_scores_rating", "mean")
    )
    .reset_index()
)

st.dataframe(
    summary,
    use_container_width=True
)

# --------------------------------------------------
# DOWNLOAD
# --------------------------------------------------

csv = summary.to_csv(index=False)

st.download_button(
    "⬇ Download Host Summary",
    csv,
    "host_summary.csv",
    "text/csv"
)

st.success("✅ Host analysis completed successfully.")