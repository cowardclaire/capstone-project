import streamlit as st

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Retail Sales Analytics Dashboard")
st.write("""
Welcome to the Retail Sales Dashboard.  
Using this app, you can explore product performance, pricing behaviour, as well as promotional impact. It also predicts sales volume using an XGBoost model.
""")

# 1. Define your pages with custom titles and icons
main_page = st.Page("main_page.py", title="Home Dashboard", icon="🏠", default=True)
eda_page = st.Page("Pages/eda.py", title="Exploratory Data Analysis", icon="📊")
insights_page = st.Page("Pages/insights_and_recommendations.py", title="Insights & Recs", icon="💡")
predictions_page = st.Page("Pages/model_predictions.py", title="Model Predictions", icon="🤖")

# 2. Pass them as a list to st.navigation
pg = st.navigation([main_page, eda_page, insights_page, predictions_page])

# 3. Run the configuration
st.set_page_config(page_title="Data App", page_icon="📈")
pg.run()

