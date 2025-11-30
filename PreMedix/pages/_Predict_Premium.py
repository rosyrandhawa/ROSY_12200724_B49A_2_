import streamlit as st
import pandas as pd
from pickle import load


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

header("Predict Insurance Premium")

# Load model
model = load(open("model/insurancemodelf.pkl", "rb"))

# Load customers CSV
df = pd.read_csv("data/customers.csv", dtype={"phone": str})

# Enter phone number
phone = st.text_input("Enter Customer Phone Number")

customer = None

if phone != "":
    # Find customer
    mask = df['phone'] == phone
    if mask.any():
        customer = df.loc[mask].iloc[0]

        st.success("Customer Found!")

        # Display customer details
        st.subheader("📄 Customer Details")
        st.write(f"""
        **Name:** {customer['name']}  
        **Age:** {customer['age']}  
        **Gender:** {customer['gender']}  
        **Phone:** {customer['phone']}  
        **Email:** {customer['email']}  
        **Address:** {customer['address']}  
        **Region:** {customer['region']}  
        ---
        **BMI:** {customer['bmi']}  
        **Children:** {customer['children']}  
        **Smoker:** {customer['smoker']}  
        **Diabetes:** {customer['diabetes']}  
        **Blood Pressure:** {customer['blood_pressure']}  
        **Alcohol:** {customer['alcohol']}  
        **Exercise Level:** {customer['exercise_level']}  
        """)

    else:
        st.error("No customer found with this phone number.")

# If customer exists, show prediction inputs
if customer is not None:

    st.subheader("🧮 Prediction Inputs")

    age = customer['age']
    bmi = customer['bmi']
    children = customer['children']
    smoker = 1 if customer['smoker'] == "yes" else 0

    if st.button("Predict Premium"):
        input_df = pd.DataFrame([{
            "age": age,
            "bmi": bmi,
            "children": children,
            "smoker": smoker
        }])

        prediction = model.predict(input_df)[0]

        st.subheader("💰 Estimated Premium")
        st.write(f"### ₹ {prediction:,.2f}")

        # Risk level
        if prediction < 10000:
            level = "Low"
        elif prediction < 20000:
            level = "Medium"
        else:
            level = "High"

        st.write(f"**Risk Level:** {level}")

        # Save into session
        st.session_state["pred"] = prediction
        st.session_state["risk"] = level
        st.session_state["phone"] = phone

    # Save prediction button
    if "pred" in st.session_state and st.session_state["phone"] == phone:
        if st.button("Save This Prediction"):
            mask = df['phone'] == phone
            df.loc[mask, "predicted_premium"] = st.session_state["pred"]
            df.loc[mask, "risk_level"] = st.session_state["risk"]

            df.to_csv("data/customers.csv", index=False)

            st.success("Prediction saved to customer record!")
