import streamlit as st

pg = st.navigation([
    st.Page("main_page.py", title="Home", icon="🏠"),
    st.Page("eda.py", title="Exploratory Data Analysis", icon="🔍"),
    st.Page("insights_and_recommendations.py", title="Insights & Recommendations", icon="💡"),
    st.Page("model_predictions.py", title="Model Predictions", icon="📈")
])

pg.run()