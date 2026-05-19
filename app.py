import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("Customer Churn Prediction System")

# Numerical Features
tenure = st.number_input("Tenure")

monthly = st.number_input("Monthly Charges")

total = st.number_input("Total Charges")

# Categorical Features
contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

# Encoding

# Contract Encoding
if contract == "Month-to-month":
    contract = 0
elif contract == "One year":
    contract = 1
else:
    contract = 2

# Internet Service Encoding
if internet_service == "DSL":
    internet_service = 0
elif internet_service == "Fiber optic":
    internet_service = 1
else:
    internet_service = 2

# Tech Support Encoding
if tech_support == "Yes":
    tech_support = 1
else:
    tech_support = 0

# Prediction
if st.button("Predict"):

    data = np.array([[
        tenure,
        monthly,
        total,
        contract,
        internet_service,
        tech_support
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
     st.error("⚠️ Customer Will Churn")
    else:
     st.success("✅ Customer Will Stay")