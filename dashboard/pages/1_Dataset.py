import streamlit as st
import pandas as pd
import plotly.express as px

from components.loader import load_data

st.set_page_config(
    page_title="Dataset Overview",
    page_icon="📂",
    layout="wide"
)

df = load_data()

st.title("📂 Dataset Overview")

if df.empty:
    st.error("Dataset not found.")
    st.stop()

#####################################################
# Dataset Summary
#####################################################

st.subheader("Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Rows",
        f"{len(df):,}"
    )

with c2:
    st.metric(
        "Columns",
        len(df.columns)
    )

with c3:
    st.metric(
        "Missing Values",
        int(df.isna().sum().sum())
    )

with c4:
    memory = (
        df.memory_usage(deep=True).sum()
        / 1024**2
    )

    st.metric(
        "Memory",
        f"{memory:.2f} MB"
    )

st.divider()

#####################################################
# Dataset Preview
#####################################################

st.subheader("Dataset Preview")

rows = st.slider(
    "Rows to Display",
    5,
    100,
    10
)

st.dataframe(
    df.head(rows),
    use_container_width=True
)

#####################################################
# Column Explorer
#####################################################

st.divider()

st.subheader("Column Explorer")

column = st.selectbox(
    "Choose a Column",
    df.columns
)

st.write(df[column].describe())

#####################################################
# Missing Values
#####################################################

st.divider()

st.subheader("Missing Values")

missing = (
    df.isna()
      .sum()
      .reset_index()
)

missing.columns = [
    "Column",
    "Missing Values"
]

missing = missing.sort_values(
    "Missing Values",
    ascending=False
)

fig = px.bar(

    missing.head(20),

    x="Column",

    y="Missing Values",

    color="Missing Values",

    color_continuous_scale="Reds"

)

fig.update_layout(

    template="plotly_white",

    xaxis_tickangle=-45

)

st.plotly_chart(
    fig,
    use_container_width=True
)

#####################################################
# Data Types
#####################################################

st.divider()

st.subheader("Column Data Types")

dtype_df = pd.DataFrame({

    "Column": df.columns,

    "Data Type": df.dtypes.astype(str)

})

st.dataframe(
    dtype_df,
    use_container_width=True
)

#####################################################
# Numeric Summary
#####################################################

st.divider()

st.subheader("Numerical Summary")

st.dataframe(

    df.describe(),

    use_container_width=True

)

#####################################################
# Download
#####################################################

st.divider()

csv = df.to_csv(index=False)

st.download_button(

    "⬇ Download Dataset",

    csv,

    "listings_transformed.csv",

    "text/csv"

)