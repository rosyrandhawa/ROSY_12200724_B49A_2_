import streamlit as st

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


st.set_page_config(page_title="PreMedix", page_icon="🩺")

# Custom Header
st.markdown("""
    <h1 style='text-align:center; color:#4e8cff; font-size:45px;'>
        🩺 PreMedix Insurance System
    </h1>
    <p style='text-align:center; font-size:18px; color:gray;'>
        Smart Medical Insurance Analysis & Premium Prediction
    </p>
    <hr style='border:1px solid #4e8cff;'>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown("""
<style>
.feature-card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-align: center;
    border-left: 5px solid #4e8cff;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='feature-card'>
            <h3>➕ Add Customer</h3>
            <p>Store detailed customer information securely.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='feature-card'>
            <h3>📊 Predict Premium</h3>
            <p>AI-powered medical insurance cost prediction.</p>
        </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
        <div class='feature-card'>
            <h3>📁 View Customers</h3>
            <p>View, filter & analyze all registered customers.</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class='feature-card'>
            <h3>💡 Smart Risk Analysis</h3>
            <p>Automatically calculates risk level from predictions.</p>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.info("Use the sidebar on the left to navigate between features.")
