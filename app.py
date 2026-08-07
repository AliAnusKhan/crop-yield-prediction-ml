import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page Configuration
st.set_page_config(
    page_title="Global Crop Yield Predictor",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Global Crop Yield Prediction System")
st.write("Production-Grade Machine Learning Pipeline (Random Forest Regressor)")

# Load Pipeline
@st.cache_resource
def load_pipeline():
    return joblib.load('crop_yield_pipeline.pkl')

try:
    pipeline = load_pipeline()
    st.sidebar.success("Model Loaded Successfully! ✅")
except Exception as e:
    st.sidebar.error(f"Model File Not Found: {e}")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    area = st.text_input("Country (Area):", value="Pakistan")
    item = st.selectbox("Crop Type (Item):", ['Potatoes', 'Maize', 'Wheat', 'Rice, paddy', 'Soybeans', 'Cassava', 'Sweet potatoes', 'Yams', 'Sorghum', 'Plantains and others'])
    year = st.slider("Year:", 1990, 2030, 2024)

with col2:
    rainfall = st.number_input("Average Rainfall (mm/year):", value=1149.0)
    pesticides = st.number_input("Pesticides Used (Tonnes):", value=37000.0)
    temp = st.number_input("Average Temp (°C):", value=20.5)

if st.button("🚀 Estimate Crop Yield"):
    input_data = pd.DataFrame({
        'Area': [area],
        'Item': [item],
        'Year': [year],
        'average_rain_fall_mm_per_year': [rainfall],
        'pesticides_tonnes': [pesticides],
        'avg_temp': [temp]
    })
    
    try:
        pred_tons = pipeline.predict(input_data)[0]
        st.success(f"Predicted Yield: **{pred_tons:.3f} Tons / Hectare** ({pred_tons * 10000:,.0f} hg/ha)")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
