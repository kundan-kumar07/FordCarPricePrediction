import streamlit as st
import pandas as pd
import joblib
import pickle

# Load model, scaler, and encoders
model = joblib.load("car_price_model.pkl")
scaler = joblib.load("scaler.pkl")
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

st.title("🚗 Ford Car Price Predictor")

# Arrange inputs in rows of 2-3
col1, col2, col3 = st.columns(3)
with col1:
    year = st.number_input("Year", min_value=2005, max_value=2025, step=1)
with col2:
    mileage = st.number_input("Mileage", min_value=0, max_value=200000, step=1000)
with col3:
    tax = st.number_input("Tax", min_value=0, max_value=600, step=10)

col4, col5, col6 = st.columns(3)
with col4:
    mpg = st.number_input("MPG", min_value=0.0, max_value=200.0, step=0.1)
with col5:
    engineSize = st.number_input("Engine Size (L)", min_value=0.5, max_value=6.0, step=0.1)
with col6:
    model_name = st.selectbox("Model", label_encoders['model'].classes_)

col7, col8 = st.columns(2)
with col7:
    transmission = st.selectbox("Transmission", label_encoders['transmission'].classes_)
with col8:
    fuelType = st.selectbox("Fuel Type", label_encoders['fuelType'].classes_)

# Convert categorical inputs to numeric (label encoding)
model_val = label_encoders['model'].transform([model_name])[0]
trans_val = label_encoders['transmission'].transform([transmission])[0]
fuel_val = label_encoders['fuelType'].transform([fuelType])[0]

# Create dataframe for prediction
input_df = pd.DataFrame([[model_val, year, trans_val, mileage, fuel_val, tax, mpg, engineSize]],
                        columns=['model','year','transmission','mileage','fuelType','tax','mpg','engineSize'])

# Scale numerical features
input_df[input_df.columns] = scaler.transform(input_df)

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Car Price: £{prediction:,.2f}")
