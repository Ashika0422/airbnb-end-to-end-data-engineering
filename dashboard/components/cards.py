import streamlit as st


def metric_card(title, value, color="#FF5A5F", icon=""):
    st.markdown(
        f"""
        <div style="
            background: #ffffff;
            padding: 22px 18px;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 8px 22px rgba(0,0,0,0.08);
            border: 1px solid #eef1f5;
            min-height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 28px; line-height: 1; margin-bottom: 8px;">{icon}</div>
            <div style="
                color: {color};
                font-size: 40px;
                font-weight: 800;
                line-height: 1.1;
                margin-bottom: 8px;
            ">
                {value}
            </div>
            <div style="
                color: #4b5563;
                font-size: 16px;
                font-weight: 600;
            ">
                {title}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )