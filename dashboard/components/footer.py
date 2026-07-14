import streamlit as st


def footer():

    st.markdown("---")

    st.markdown(
        """

<div style="text-align:center;
padding:20px;
color:gray;">

<h4>🏠 Airbnb Market Intelligence Platform</h4>

Developed by <b>Ashika Chamodi</b>

<br>

University of Kelaniya

<br><br>

Python • Pandas • SQLite • Plotly • Streamlit • Scikit-learn

<br><br>

© 2026

</div>

""",
        unsafe_allow_html=True,
    )