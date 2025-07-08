import streamlit as st
import pandas as pd
from predictor import load_model_and_predict

st.set_page_config(page_title="Used Bike Price Predictor", layout="centered")

st.title("🏍️ Used Bike Price Prediction App")
st.markdown("Enter the bike details below to predict its selling price.")

def user_input():
    model_name = st.text_input("Model Name", "Bajaj Pulsar 150cc 2018")
    model_year = st.number_input("Model Year", min_value=1990, max_value=2025, value=2018)
    kms_driven = st.number_input("KMs Driven", min_value=0, value=20000)
    owner = st.selectbox("Owner", ["first owner", "second owner", "third owner", "fourth owner", "Unknown"])
    location = st.text_input("Location", "delhi")
    mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=50.0)
    power = st.number_input("Power (bhp)", min_value=0.0, value=15.0)
    return {
        "model_name": model_name,
        "model_year": model_year,
        "kms_driven": kms_driven,
        "owner": owner,
        "location": location,
        "mileage": mileage,
        "power": power,
    }

input_dict = user_input()

if st.button("Predict Price"):
    try:
        pred = load_model_and_predict(input_dict, "models/bike_price_model.joblib", "models/encoder.joblib")
        st.success(f"💰 Predicted Selling Price: ₹{pred:,.0f}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
