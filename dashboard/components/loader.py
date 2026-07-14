from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    base_dir = Path(__file__).resolve().parents[2]

    data_path = (
        base_dir
        / "data"
        / "transformed"
        / "listings_transformed.csv"
    )

    if not data_path.exists():
        return pd.DataFrame()

    df = pd.read_csv(data_path)

    return df