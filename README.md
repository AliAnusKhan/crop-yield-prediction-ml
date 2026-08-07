# 🌾 Global Crop Yield Prediction System

An end-to-end, production-grade Machine Learning pipeline and interactive web application built with **Streamlit** and **Scikit-Learn** to predict agricultural crop yields across different countries and environmental conditions.

---

## 📌 Project Overview

Agricultural yield forecasting is vital for food security, economic planning, and sustainable resource management. This project leverages historical data on temperature, rainfall, pesticide consumption, and crop types to predict agricultural output in **Tons per Hectare**.

---

## ✨ Key Features

* **Interactive Web Interface:** User-friendly UI built with Streamlit for real-time predictions.
* **Production-Grade Pipeline:** Preprocessing (Standard Scaling + One-Hot Encoding) bundled directly with a tuned **Random Forest Regressor**.
* **Global Scope:** Supports multiple countries, crop types (Wheat, Rice, Maize, Potatoes, etc.), and environmental factors.
* **Dual Output Units:** Displays predicted yield in both **Tons / Hectare** and **hg/ha** (hectograms per hectare).

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.11
* **Machine Learning:** Scikit-Learn (v1.6.1), XGBoost
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** Pickle / Joblib
* **Deployment:** Streamlit Cloud

---

## 📊 Input Features

The prediction pipeline requires the following input features:

| Feature Name | Description | Example Input |
| :--- | :--- | :--- |
| **Area** | Country Name | `Pakistan` |
| **Item** | Crop Type | `Potatoes` |
| **Year** | Production Year | `2024` |
| **Average Rainfall** | Annual rainfall in mm | `1149.0` |
| **Pesticides Used** | Pesticide consumption in Tonnes | `37000.0` |
| **Average Temp** | Mean temperature in °C | `20.5` |

---

## 📁 Repository Structure

```text
├── app.py                   # Streamlit web application script
├── crop_yield_pipeline.pkl  # Serialized ML Pipeline (Preprocessor + Random Forest)
├── requirements.txt         # Project dependencies & exact library versions
├── .python-version          # Python version configuration for deployment
└── README.md                # Project documentation
