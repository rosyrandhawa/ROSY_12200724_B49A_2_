import streamlit as st
import pandas as pd
import os
from datetime import datetime

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


header("Add Customer Details")

csv_path = "data/customers.csv"

# Ensure CSV exists
if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
    df = pd.DataFrame(columns=[
        "name","age","gender","phone","email","address","region",
        "bmi","children","smoker","diabetes","blood_pressure",
        "alcohol","exercise_level","predicted_premium","risk_level","date"
    ])
    df.to_csv(csv_path, index=False)


# Input fields
name = st.text_input("Full Name")
age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
phone = st.text_input("Phone Number")
email = st.text_input("Email")
address = st.text_input("Address")
region = st.selectbox("Region", ["northwest","northeast","southwest","southeast"])

bmi = st.number_input("BMI", 10.0, 50.0)
children = st.number_input("Number of Children", 0, 10)
smoker = st.selectbox("Smoker?", ["yes","no"])
diabetes = st.selectbox("Diabetes?", ["yes","no"])
blood_pressure = st.selectbox("Blood Pressure", ["low","normal","high"])
alcohol = st.selectbox("Alcohol Consumption?", ["yes","no"])
exercise = st.selectbox("Exercise Level", ["low","medium","high"])

if st.button("Save Customer Details"):
    new_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "email": email,
        "address": address,
        "region": region,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "diabetes": diabetes,
        "blood_pressure": blood_pressure,
        "alcohol": alcohol,
        "exercise_level": exercise,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.read_csv(csv_path, dtype={"phone": str})
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(csv_path, index=False)

    st.success("Customer details saved successfully!")
