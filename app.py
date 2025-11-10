import pandas as pd
import joblib
import streamlit as st

# Load the saved model
saved = joblib.load("iris_classifier.pkl")
model = saved["model"]

st.title("Iris Classifier")

# Input features
sepal_length = st.number_input("Sepal Length", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width", 0.0, 10.0, 0.2)

# Make prediction
if st.button("Predict"):
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(sample)
    st.success(f"Prediction: {prediction[0]}")
