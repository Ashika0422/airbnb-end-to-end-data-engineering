import streamlit as st

from components.loader import load_data

from components.filters import sidebar_filters

from components.charts import *

st.set_page_config(

    page_title="Price Analytics",

    page_icon="📊",

    layout="wide"

)

st.title("📊 Price Analytics")

df = load_data()

if df.empty:

    st.error("Dataset not found.")

    st.stop()

# --------------------------------

# Filters

# --------------------------------

df = sidebar_filters(df)

# --------------------------------

# KPIs

# --------------------------------

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(

        "Average Price",

        f"${df['price'].mean():.2f}"

    )

with c2:

    st.metric(

        "Maximum Price",

        f"${df['price'].max():.2f}"

    )

with c3:

    st.metric(

        "Minimum Price",

        f"${df['price'].min():.2f}"

    )

st.divider()

# --------------------------------

# Charts

# --------------------------------

left, right = st.columns(2)

with left:

    st.plotly_chart(

        price_distribution(df),

        use_container_width=True

    )

with right:

    st.plotly_chart(

        pie_room_type(df),

        use_container_width=True

    )

left, right = st.columns(2)

with left:

    st.plotly_chart(

        room_type_chart(df),

        use_container_width=True

    )

with right:

    st.plotly_chart(

        property_chart(df),

        use_container_width=True

    )

st.plotly_chart(

    scatter_reviews(df),

    use_container_width=True

)

st.divider()

st.subheader("Dataset Preview")

st.dataframe(

    df.head(20),

    use_container_width=True

)

csv = df.to_csv(index=False)

st.download_button(

    "⬇ Download Filtered Dataset",

    csv,

    "filtered_airbnb.csv",

    "text/csv"

)