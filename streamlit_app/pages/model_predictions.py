import streamlit as st
import pandas as pd
import joblib

st.title("Sales Volume Prediction")

# Load trained model
model = joblib.load("../../data/model/xgboost_model.pkl")

st.write("Use the inputs below to see the predicted sales volume.")

# User inputs
price = st.slider("Price (£)", 1, 150, 30)
promotion = st.selectbox("Promotion", [0, 1])
position = st.selectbox("Product Position", ["Aisle", "End-cap", "Front of Store"])
category = st.selectbox("Product Category", ["t-shirts", "shoes", "jeans", "jackets", "sweaters"])

# Build input dataframe
input_df = pd.DataFrame({
    "price": [price],
    "promotion": [promotion],
    "store_position": [position],
    "product_category": [category]
})

# One-hot encode category
input_df = pd.get_dummies(input_df, drop_first=True)

# Ensure all expected columns exist
expected_cols = model.feature_names_in_
for col in expected_cols:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[expected_cols]

# Predict
prediction = model.predict(input_df)[0]

st.metric("Predicted Sales Volume", f"{prediction:.0f} units")
