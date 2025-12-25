import streamlit as st
import numpy as np
import joblib

academic_model = joblib.load("academic_model.pkl")
academic_scaler = joblib.load("academic_scaler.pkl")

placement_model = joblib.load("placement_model.pkl")
placement_scaler = joblib.load("placement_scaler.pkl")

st.title("🎓 Smart Student Performance & Placement Predictor")

st.header("📘 Academic Performance Prediction")

studytime = st.number_input("Study Time (1–4)", min_value=1, max_value=4)
absences = st.number_input("Number of Absences", min_value=0)
failures = st.number_input("Past Failures", min_value=0)
g1 = st.number_input("First Period Grade (G1)", min_value=0, max_value=20)
g2 = st.number_input("Second Period Grade (G2)", min_value=0, max_value=20)

if st.button("Predict Academic Result"):
    academic_input = np.array([[studytime, absences, failures, g1, g2]])
    academic_input = academic_scaler.transform(academic_input)
    result = academic_model.predict(academic_input)

    if result[0] == 1:
        st.success("✅ Student is likely to PASS")
    else:
        st.error("❌ Student is likely to FAIL")

st.header("💼 Placement Package Prediction")

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Predict Placement Package"):
    placement_input = np.array([[cgpa]])
    placement_input = placement_scaler.transform(placement_input)
    package = placement_model.predict(placement_input)

    st.info(f"💰 Expected Placement Package: {package[0]:.2f} LPA")