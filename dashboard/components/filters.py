import streamlit as st


def sidebar_filters(df):

    st.sidebar.title("⚙ Dashboard Filters")

    filtered_df = df.copy()

    # -----------------------------
    # Property Type
    # -----------------------------

    if "property_type" in df.columns:

        property_types = ["All"] + sorted(
            df["property_type"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        property_selected = st.sidebar.selectbox(
            "🏠 Property Type",
            property_types
        )

        if property_selected != "All":
            filtered_df = filtered_df[
                filtered_df["property_type"] == property_selected
            ]

    # -----------------------------
    # Room Type
    # -----------------------------

    if "room_type" in df.columns:

        room_types = ["All"] + sorted(
            df["room_type"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        room_selected = st.sidebar.selectbox(
            "🛏 Room Type",
            room_types
        )

        if room_selected != "All":
            filtered_df = filtered_df[
                filtered_df["room_type"] == room_selected
            ]

    # -----------------------------
    # Price
    # -----------------------------

    if "price" in df.columns:

        minimum = int(df["price"].min())
        maximum = int(df["price"].max())

        price_range = st.sidebar.slider(

            "💰 Price Range",

            minimum,

            maximum,

            (minimum, maximum)

        )

        filtered_df = filtered_df[
            (filtered_df["price"] >= price_range[0])
            &
            (filtered_df["price"] <= price_range[1])
        ]

    return filtered_df