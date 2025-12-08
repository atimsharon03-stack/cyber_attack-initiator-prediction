import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# === SAFE MODEL LOADING ===
@st.cache_resource
def load_model():
    model_path = "Rf_model.pkl"
    if not os.path.exists(model_path):
        st.error("""
        Model file 'Rf_model.pkl' is missing!
        Please make sure the file is in the same folder as app.py
        and committed to your GitHub repository.
        """)
        st.stop()
    return joblib.load(model_path)

model = load_model()

st.title("Random Forest Cyber Incident Predictor")

# Sidebar – single prediction
st.sidebar.header("Single Sample Prediction")
col1, col2 = st.sidebar.columns(2)
with col1:
    incident_type = st.sidebar.number_input("Incident Type", value=0)
    initiator_country = st.sidebar.number_input("Initiator Country", value=0)
with col2:
    receiver_country = st.sidebar.number_input("Receiver Country", value=0)
    incident_year = st.sidebar.number_input("Incident Year", min_value=1900, value=2024)

if st.sidebar.button("Predict Single Sample", type="primary"):
    input_data = np.array([[incident_type, initiator_country, receiver_country, incident_year]])
    pred = model.predict(input_data)[0]
    st.success(f"Predicted Class: **{int(pred)}**")

# Batch prediction
st.header("Batch Prediction")
uploaded_file = st.file_uploader("Upload CSV/Excel (exactly 4 columns)", type=["csv", "xlsx"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        if df.shape[1] != 4:
            st.error(f"File must have exactly 4 columns (found {df.shape[1]})")
        else:
            preds = model.predict(df.values)
            df["Prediction"] = preds.astype(int)
            st.success("Predictions ready!")
            st.dataframe(df)
            st.download_button("Download Results", df.to_csv(index=False), "predictions.csv", "text/csv")
    except Exception as e:
        st.error(f"Error: {e}")
