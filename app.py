import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model and feature names
with open('Model/rainfall_model.pkl', 'rb') as file:
    model_data = pickle.load(file)

model = model_data['model']
feature_names = model_data['feature_names']

# Streamlit App Setup
st.set_page_config(page_title="Rainfall Prediction App", page_icon="🌧️", layout="centered")

st.title("🌦️ Rainfall Prediction Using Machine Learning")
st.markdown("This app predicts whether it will rain based on weather parameters.")

# Sidebar Inputs
st.sidebar.header("Input Weather Parameters")

def get_user_input():
    pressure = st.sidebar.number_input('Pressure (hPa)', min_value=950.0, max_value=1050.0, value=1013.0)
    dewpoint = st.sidebar.number_input('Dew Point (°C)', min_value=-10.0, max_value=40.0, value=15.0)
    humidity = st.sidebar.slider('Humidity (%)', 0, 100, 70)
    cloud = st.sidebar.slider('Cloud Cover (%)', 0, 100, 50)
    sunshine = st.sidebar.number_input('Sunshine (hours)', min_value=0.0, max_value=15.0, value=5.0)
    winddirection = st.sidebar.number_input('Wind Direction (°)', min_value=0, max_value=360, value=180)
    windspeed = st.sidebar.number_input('Wind Speed (km/h)', min_value=0.0, max_value=100.0, value=10.0)

    features = pd.DataFrame({
        'pressure': [pressure],
        'dewpoint': [dewpoint],
        'humidity': [humidity],
        'cloud': [cloud],
        'sunshine': [sunshine],
        'winddirection': [winddirection],
        'windspeed': [windspeed]
    })

    return features

input_df = get_user_input()

# Display User Input
st.subheader("Input Parameters")
st.write(input_df)

# Make Prediction
if st.button('Predict'):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    result = '🌧️ Rainfall Expected' if prediction[0] == 1 else '☀️ No Rainfall'
    probability = prediction_proba[0][1] * 100

    st.subheader("Prediction Result")
    st.success(f"{result}")

    st.subheader("Prediction Probability")
    st.info(f"Chance of Rainfall: {probability:.2f}%")

