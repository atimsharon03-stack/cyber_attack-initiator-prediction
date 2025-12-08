import streamlit as st

# Load model
model = joblib.load('/content/Rf_model.pkl')

st.title("🔍 Random Forest Predictor")

st.sidebar.header("Manual Input")
feature1 = st.sidebar.number_input("incident_type", value=0.0)
feature2 = st.sidebar.number_input("initiator_country", value=0.0)
feature3 = st.sidebar.number_input("reciever_country", value=0.0)
feature4 = st.sidebar.number_input("incident_year", value=0.0)

if st.sidebar.button("Predict Single Sample"):
    input_data = np.array([[feature1, feature2, feature3, feature4]])
    prediction = model.predict(input_data)[0]
    st.write(f"📌 Prediction: **Class {prediction}**")

st.header("📁 Upload File for Batch Prediction")
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    if df.shape[1] != 4:
        st.error("Uploaded file must have exactly 4 columns.")
    else:
        predictions = model.predict(df.values)
        df["Prediction"] = predictions
        st.write("✅ Predictions:")
        st.dataframe(df)
        st.download_button("Download Results", df.to_csv(index=False), "predictions.csv", "text/csv")
