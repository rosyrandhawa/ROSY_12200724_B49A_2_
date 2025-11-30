import streamlit as st
import pandas as pd

# Custom Sidebar Title
st.markdown("""
    <style>
        [data-testid="stSidebar"] .css-1d391kg { 
            visibility: hidden;
        }
        [data-testid="stSidebar"]::before {
            content: "🩺 PreMedix System";
            font-size: 24px;
            font-weight: bold;
            color: #4e8cff;
            padding-left: 20px;
            padding-top: 20px;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)


def header(title):
    st.markdown(f"""
        <h1 style='text-align:center; color:#4e8cff;'>
            {title}
        </h1>
        <hr style='height:2px; border:none; background:#4e8cff;'>
    """, unsafe_allow_html=True)

header("View All Customers")

csv_path = "data/customers.csv"

try:
    df = pd.read_csv(csv_path)
    st.dataframe(df)
except:
    st.error("No customer data found.")
