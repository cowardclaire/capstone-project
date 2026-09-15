from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Exploratory Data Analysis", page_icon="📊")

ROOT_DIR = Path(__file__).resolve().parents[1]
EDA_DIR = ROOT_DIR / "visuals" / "eda"

st.title("📊 Exploratory Data Analysis")

st.write("### Price Distribution")
st.image(str(EDA_DIR / "price_distribution.png"))
st.caption("The price distribution plots show most products sit in the £10 - £40 price range, after which the count of products begin to decline as the prices increase.")

st.write("### Sales Volume Distribution")
st.image(str(EDA_DIR / "sales_volume_distribution.png"))
st.caption("This chart shows two peaks which indicates two different sales behaviours, which from our EDA we find out is from products that are on promotion and not on promotion.")

st.write("### Product Category Distribution")
st.image(str(EDA_DIR / "product_category_distribution.png"))
st.caption("Highlights how heavily the assortment is weighted toward jackets compared with other categories.")

st.write("### Sales Volume by Category")
st.image(str(EDA_DIR / "sales_volume_by_category.png"))
st.caption("Shows that average sales volume is broadly consistent across all product categories.")

st.write("### Sales Volume by Position")
st.image(str(EDA_DIR / "sales_volume_by_position.png"))
st.caption("Reviewing sales volume by product position shows the averages across the different positions are roughly the same.")

st.write("### Promotion Effectiveness")
st.image(str(EDA_DIR / "promotion_effectiveness.png"))
st.caption("Shows a clear uplift in average sales volume when promotions are active.")

st.write("### Promotion vs Sales Volume")
st.image(str(EDA_DIR / "promotion_vs_sales_volume.png"))
st.caption("Visualises how sales volume changes when products are promoted, helping assess promotional impact.")

st.write("### Price vs Sales Volume")
st.image(str(EDA_DIR / "price_vs_sales_volume.png"))
st.caption("This chart shows that cheaper items sell more, and we can see sales volume decline as price increases. This confirms that price is an important factor influencing demand.")

st.write("### Correlation Heatmap")
st.image(str(EDA_DIR / "correlation_heatmap.png"))
st.caption("Highlights promotion as the strongest driver of sales volume, with price showing a moderate negative correlation.")
