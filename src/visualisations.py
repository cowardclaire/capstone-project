#Purpose : This file contains reusable Plotly, Matplotlib, or Seaborn chart functions, such as: time-series charts, bar charts,
#scatter plots, box plots, customer segmentation visuals

#--------------------------------------------------------
#IMPORTING LIBRARIES FOR CLEANING AND VISUALIZING DATA
#--------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns   
import pandas as pd
import numpy as np
import os

#--------------------------------------------------------
# BUILD PATH TO CLEANED DATA FILE
#--------------------------------------------------------

cleaned_path = os.path.join(
    os.path.dirname(__file__),   # folder where visualisations.py lives (src)
    "..",                        # go up to CAPSTONE-PROJECT
    "data",                      # enter data folder
    "cleaned-data",              # enter cleaned-data folder
    "cleaned_data.csv"           # your cleaned file
)

#--------------------------------------------------------
# LOAD CLEANED DATA
#--------------------------------------------------------
df = pd.read_csv(cleaned_path)

print("Loaded cleaned data successfully")
print(df.head())

#--------------------------------------------------------
# SALES VOLUME DISTRIBUTION PLOT
#--------------------------------------------------------

plt.figure(figsize=(10,6))
sns.histplot(df['sales_volume'], kde=True)
plt.title("Sales Volume Distribution")
plt.show()


#--------------------------------------------------------
# PRICE DISTRIBUTION PLOT
#--------------------------------------------------------

fig, ax = plt.subplots(1, 2, figsize=(14,6))

sns.histplot(df['price'], kde=True, bins=30, ax=ax[0], color='teal')
ax[0].set_title("Price Distribution")

sns.boxplot(x=df['price'], ax=ax[1], color='salmon')
ax[1].set_title("Price Boxplot")

plt.show()

#--------------------------------------------------------
# PRODUCT CATEGORY DISTRIBUTION PLOT    
#--------------------------------------------------------

plt.figure(figsize=(12,6))
sns.countplot(data=df, x='terms', hue='terms', palette='magma', legend=False)
plt.title("Product Category Distribution")
plt.xticks(rotation=45)
plt.show()

#--------------------------------------------------------
# PROMOTION VS SALES VOLUME PLOT
#--------------------------------------------------------

plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='promotion', y='sales_volume', hue='promotion', palette='coolwarm', legend=False)
plt.title("Sales Volume by Promotion")
plt.xlabel("Promotion (0 = No, 1 = Yes)")
plt.ylabel("Sales Volume")
plt.show()
