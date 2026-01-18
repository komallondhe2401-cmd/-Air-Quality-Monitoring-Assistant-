import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("aqi_model.pkl")

# Page title
st.set_page_config(page_title="AQI Assistant", layout="centered")
st.title("🌍 Air Quality Monitoring Assistant")
st.write("Enter pollutant values to predict Air Quality Category")

# User inputs
pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0)
no2  = st.number_input("NO₂ (µg/m³)", min_value=0.0)
so2  = st.number_input("SO₂ (µg/m³)", min_value=0.0)
co   = st.number_input("CO (mg/m³)", min_value=0.0)
o3   = st.number_input("O₃ (µg/m³)", min_value=0.0)

# AQI label mapping
aqi_labels = {
    0: "Good",
    1: "Satisfactory",
    2: "Moderate",
    3: "Poor",
    4: "Very Poor",
    5: "Severe"
}

# Prediction button
if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(input_data)[0]

    st.subheader("🌡️ Predicted Air Quality")
    st.success(aqi_labels[prediction])

    # Health advice
    st.subheader("🩺 Health Advisory")
    if prediction >= 4:
        st.error("Avoid outdoor activities. Wear a mask and stay indoors.")
    elif prediction == 3:
        st.warning("Sensitive groups should limit outdoor exertion.")
    else:
        st.info("Air quality is acceptable. Enjoy your day responsibly.")

    # Sustainability tip
    st.subheader("🌱 Sustainability Tip")
    st.write("Use public transport, avoid burning waste, and conserve energy.")
