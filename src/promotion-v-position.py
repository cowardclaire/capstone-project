#after analysing the sales volume by product position and promotion, we can see that the sales volume is higher for products in the top position and when there is a promotion. This suggests that both product position and promotion have a significant impact on sales volume.
#wanting to delve into further and compare promo uplift across different product positions, we can create a new visualization that shows the average sales volume for each combination of product position and promotion status. This will help us understand how the effectiveness of promotions varies depending on where the product is positioned.
#used AI to help me calculate the below

import pandas as pd

# Loading cleaned dataset
df = pd.read_csv("data/cleaned-data/cleaned_data.csv")  

#---------------------------------------------------------
#1. Compute medians for each Position × Promotion group
#---------------------------------------------------------

median_table = (
    df.groupby(['product_position', 'promotion'])['sales_volume']
      .median()
      .unstack()  # columns: 0 = no promo, 1 = promo
)

median_table.columns = ['median_no_promo', 'median_promo']

#---------------------------------------------------------
# 2. Compute uplift
#---------------------------------------------------------

median_table['absolute_uplift'] = (
    median_table['median_promo'] - median_table['median_no_promo']
)

median_table['percentage_uplift'] = (
    median_table['absolute_uplift'] / median_table['median_no_promo'] * 100
)

median_table = median_table.round(0)
print(median_table.to_string())
