# PreMedix-Medical-Insurance-Prediction-System-
.

🩺 Project Description – PreMedix (Medical Insurance Prediction System)
🩺 PreMedix – AI Medical Insurance Prediction System

👉 Live App: https://bbcgntfhpyzap8znrtn6nc.streamlit.app/

Objective of the PreMedix Medical Insurance Prediction System

The main objective of the PreMedix project is to build an end-to-end medical insurance prediction system that can:

Collect customer details

Store their information in a CSV database

Predict insurance premium using a trained machine learning model

Classify the customer’s risk level

View and manage all customer data

This system allows users to not only estimate insurance costs but also maintain a complete customer record system for real-world usage.

🎯 Core Prediction Inputs

The machine learning model predicts insurance charges based on:

Age

BMI (Body Mass Index)

Number of dependent children

Smoking status

These factors strongly influence medical insurance premiums according to real-world datasets.

📝 Modules in the PreMedix System
1️⃣ Add Customer Module

This module collects full customer details including:

Name

Age

Gender

Phone Number

Email

Address

BMI

Smoker / Diabetes / Blood Pressure

Alcohol consumption

Exercise level

Region

All information is saved into customers.csv, which acts as a lightweight database.

2️⃣ Predict Premium Module

User enters the customer phone number

System automatically fetches the saved details from CSV

ML model predicts the insurance premium

The system generates a Risk Level:

Low

Medium

High

Option to save predicted premium back into CSV

3️⃣ View Customer Records

Displays all customer entries saved in customers.csv

Shows predicted premium & risk level

Works like a simple internal dashboard

💡 Use Cases / Applications
1. Insurance Companies

PreMedix can help insurance agents generate instant premium estimates based on customer data.

2. Healthcare Financial Planning

Individuals can understand how their lifestyle (BMI, smoking, exercise) affects insurance costs.

3. Hospitals / Clinics

Useful for giving estimated treatment cost plans or coverage amounts to patients.

4. FinTech & Insurance Apps

Can be integrated into existing applications for premium estimation or customer onboarding.

🧰 Technologies Used
Programming & Framework

Python – Main language

Streamlit – Web application UI

Pandas – Data handling & CSV operations

Machine Learning

Scikit-Learn – Model training

Pickle – Saving and loading ML model (insurancemodelf.pkl)

Optional Tools

NumPy – Numerical computations

Jupyter Notebook – For model development & testing

🗂️ Data Storage

The project uses a CSV file:

data/customers.csv


This stores:

Customer information

Predicted premium

Risk category

Phone number is used as a unique identifier.

🖥️ Requirements to Run the Project
Software Requirements

Python installed

Required libraries:

pip install streamlit pandas scikit-learn numpy

Model Requirement

A trained model file must be present:

model/insurancemodelf.pkl

🚀 Steps to Run the Application
1. Install Dependencies
pip install -r requirements.txt

2. Run the Streamlit App
streamlit run app.py

3. Open in Browser

Visit:
http://localhost:8501

4. Enter Customer Data

Go to “Add Customer” page

Enter full details

Save customer

5. Predict Premium

Go to “Predict Premium” page

Enter customer’s phone number

View prediction + risk level

6. View Records

All customers appear in the “View Customers” page.

🏁 Final Output

Accurate medical insurance premium prediction

Customer record management system

Risk classification

Modern UI with sidebar customization

Fully functional end-to-end insurance prediction app
