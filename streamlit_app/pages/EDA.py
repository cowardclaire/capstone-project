from pathlib import Path

import streamlit as st

st.set_page_config(page_title="EDA - Retail Sales Analytics", layout="wide")


ROOT_DIR = Path(__file__).resolve().parents[2]
EDA_DIR = ROOT_DIR / "visuals" / "eda"

st.title("📊 Exploratory Data Analysis")

st.write("### Price Distribution")
st.image(str(EDA_DIR / "price_distribution.png"))

st.write("### Sales Volume Distribution")
st.image(str(EDA_DIR / "sales_volume_distribution.png"))

st.write("### Product Category Distribution")
st.image(str(EDA_DIR / "product_category_distribution.png"))

st.write("### Sales Volume by Category")
st.image(str(EDA_DIR / "sales_volume_by_category.png"))

st.write("### Sales Volume by Position")
st.image(str(EDA_DIR / "sales_volume_by_position.png"))

st.write("### Promotion Effectiveness")
st.image(str(EDA_DIR / "promotion_effectiveness.png"))

st.write("### Promotion vs Sales Volume")
st.image(str(EDA_DIR / "promotion_vs_sales_volume.png"))

st.write("### Price vs Sales Volume")
st.image(str(EDA_DIR / "price_vs_sales_volume.png"))

st.write("### Correlation Heatmap")
st.image(str(EDA_DIR / "correlation_heatmap.png"))
