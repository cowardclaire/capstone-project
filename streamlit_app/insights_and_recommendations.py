import streamlit as st

st.set_page_config(page_title="Insights & Recommendations")

st.title("📈 Insights & Recommendations")

st.write("""
### Key Insights

- **Promotion is the strongest driver of sales.**  
  Promoted items consistently sell significantly more than any other attribute.

- **Higher prices reduce sales volume.**  
  The price vs sales scatterplot shows a decline in sales volume as price increases.

- **Product category has minimal impact.**  
  The average sales across each product category varies very little, suggesting that category is not a strong predictor of sales.

- **Product position only matters when combined with promotion.**  
  Without promotion, we see minimal variance in performance when comparing aisle, end-cap, and front-of-store store positions. However, when combined with promotion, end-cap and front-of-store positions outperform aisle positions.

---

### Recommendations

- Increase promotional activity for high-margin items.
- Use promotional activity to manage stock levels and reduce overstocking in stores.
- Review pricing strategy for premium products.
- Focus less on store position and more on promotional timing.
- Use the prediction model to support stock planning and forecasting demand.

---

### Model Performance Summary

The XGBoost model achieved:

- **RMSE:** ~108  
- **MAE:** ~83  
- **R²:** ~0.86  

This means the model explains over **86%** of sales behaviour — strong performance for real retail data.
""")
