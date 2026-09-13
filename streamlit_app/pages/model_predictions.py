import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# LOAD MODEL + DATA
# -----------------------------

model = pickle.load(open("data/model/xgboost_model.pkl", "rb"))
df = pd.read_csv("data/cleaned-data/cleaned_data.csv")

st.title("🤖 Sales Volume Prediction")

st.write(
    "Adjust the inputs below to generate a prediction and explore how price and promotion "
    "influence category and shelf position behaviour."
)

# -----------------------------
# USER INPUTS
# -----------------------------

price = st.number_input("Price (£)", min_value=1.0, max_value=150.0, value=10.0)

promotion = st.selectbox("Promotion", ["Yes", "No"])
promotion_binary = 1 if promotion == "Yes" else 0

# -----------------------------
# PREDICTION INPUT (FULL FEATURE SET)
# -----------------------------

input_df = pd.DataFrame([{
    "price": price,
    "promotion": promotion_binary
}])

# -----------------------------
# RUN PREDICTION
# -----------------------------

prediction = model.predict(input_df)[0]

st.subheader("📈 Predicted Sales Volume")
st.metric(label="Prediction", value=f"{prediction:.0f} units")

st.divider()

# -----------------------------
# FILTER DATA FOR VISUALS
# -----------------------------

filtered_df = df[df["promotion"] == promotion_binary]

# Fallback if no rows match
if filtered_df.empty:
    st.warning(
        "No historical data available for this promotion selection. "
        "Showing full dataset instead."
    )
    filtered_df = df.copy()

st.subheader("📊 How Category & Product Position Behave at This Promotion Level")

# -----------------------------
# PRICE VS SALES VOLUME
# -----------------------------

st.markdown("### Price vs Sales Volume (Promotion Filter Applied)")

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x="price", y="sales_volume", ax=ax)
ax.axvline(price, color="red", linestyle="--", label="Selected Price")
ax.set_xlabel("Price (£)")
ax.set_ylabel("Sales Volume")
ax.legend()
st.pyplot(fig)

# -----------------------------
# PRICE DISTRIBUTION BY CATEGORY
# -----------------------------

st.markdown("### Price Distribution by Category")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="terms", y="price", ax=ax)
plt.xticks(rotation=45)
ax.set_xlabel("Category")
ax.set_ylabel("Price (£)")
st.pyplot(fig)


# -----------------------------
# SALES VOLUME BY PRODUCT POSITION
# -----------------------------

st.markdown("### Sales Volume by Product Position")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=filtered_df, x="product_position", y="sales_volume", ax=ax)
ax.set_xlabel("Product Position")
ax.set_ylabel("Sales Volume")
st.pyplot(fig)

# -----------------------------
# SALES VOLUME BY DISTRIBUTION
# -----------------------------

st.markdown("### Sales Volume Distribution")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(data=filtered_df, x="sales_volume", bins=20, kde=True, ax=ax)
ax.set_xlabel("Sales Volume")
ax.set_ylabel("Frequency")
st.pyplot(fig)
