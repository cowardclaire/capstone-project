#Purpose : This file contains reusable Plotly, Matplotlib, or Seaborn chart functions, such as: time-series charts, bar charts,
#scatter plots, box plots, customer segmentation visuals

#--------------------------------------------------------
#IMPORTING LIBRARIES FOR CLEANING AND VISUALIZING DATA
#--------------------------------------------------------

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# SAVE FUNCTION
# ---------------------------------------------------------

def save_plot(fig, filename):
    visuals_path = os.path.join(os.path.dirname(__file__), "..", "visuals")
    os.makedirs(visuals_path, exist_ok=True)

    full_path = os.path.join(visuals_path, filename)
    fig.savefig(full_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

# ---------------------------------------------------------
# INDIVIDUAL PLOT FUNCTIONS
# ---------------------------------------------------------

#---------------------------------------------------------
#1. PLOT SALES VOLUME DISTRIBUTION  
#---------------------------------------------------------

def plot_sales_volume_distribution(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(df['sales_volume'], kde=True, bins=30, color='steelblue', ax=ax)
    ax.set_title("Sales Volume Distribution")
    ax.set_xlabel("Sales Volume")
    ax.set_ylabel("Frequency")

    save_plot(fig, "sales_volume_distribution.png")

#---------------------------------------------------------
#2. PLOT PRICE DISTRIBUTION
#---------------------------------------------------------

def plot_price_distribution(df):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    sns.histplot(df['price'], kde=True, bins=30, ax=ax[0], color='teal')
    ax[0].set_title("Price Distribution")

    sns.boxplot(x=df['price'], ax=ax[1], color='salmon')
    ax[1].set_title("Price Boxplot")

    save_plot(fig, "price_distribution.png")

#---------------------------------------------------------
#3. PLOT PRODUCT CATEGORY DISTRIBUTION
#---------------------------------------------------------

def plot_product_category(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(data=df, x='terms', hue='terms', palette='magma', legend=False, ax=ax)
    plt.title("Product Category Distribution")
    plt.xticks(rotation=45)

    save_plot(fig, "product_category_distribution.png")

#---------------------------------------------------------
#4. PLOT PROMOTION VS SALES VOLUME
#---------------------------------------------------------

def plot_promotion_vs_sales(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(data=df, x='promotion', y='sales_volume', hue='promotion', palette='coolwarm', legend=False, ax=ax)
    plt.title("Sales Volume by Promotion")
    plt.xlabel("Promotion (0 = No, 1 = Yes)")
    plt.ylabel("Sales Volume")

    save_plot(fig, "promotion_vs_sales_volume.png")

#---------------------------------------------------------
#5.CORRELATION HEATMAP  
#---------------------------------------------------------

def plot_correlation_heatmap(df):
    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(df.corr(), annot=True, cmap='Blues', ax=ax)
    ax.set_title("Correlation Heatmap")

    save_plot(fig, "correlation_heatmap.png")

#---------------------------------------------------------
#6. SALES VOLUME BY CATEGORY
#---------------------------------------------------------

def plot_sales_volume_by_category(df):
    fig, ax = plt.subplots(figsize=(12,6))
    category_means = df.groupby('terms')['sales_volume'].mean().sort_values()
    sns.barplot(x=category_means.index, y=category_means.values, palette='viridis', ax=ax)
    ax.set_title("Average Sales Volume by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Average Sales Volume")
    plt.xticks(rotation=45)

    save_plot(fig, "sales_volume_by_category.png")

#---------------------------------------------------------
#7. SALES VOLUME BY PRODUCT POSITION
#---------------------------------------------------------

def plot_sales_volume_by_position(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.boxplot(data=df, x='product_position', y='sales_volume', palette='coolwarm', ax=ax)
    ax.set_title("Sales Volume by Product Position")
    ax.set_xlabel("Product Position")
    ax.set_ylabel("Sales Volume")
    plt.xticks(rotation=45)

    save_plot(fig, "sales_volume_by_position.png")

#---------------------------------------------------------
#8. PROMOTION EFFECTIVENESS (AVERAGE SALES)
#---------------------------------------------------------

def plot_promotion_effectiveness(df):
    fig, ax = plt.subplots(figsize=(8,6))
    promo_means = df.groupby('promotion')['sales_volume'].mean()
    sns.barplot(x=promo_means.index, y=promo_means.values, palette='coolwarm', ax=ax)
    ax.set_title("Promotion Effectiveness (Mean Sales Volume)")
    ax.set_xlabel("Promotion (0 = No, 1 = Yes)")
    ax.set_ylabel("Average Sales Volume")

    save_plot(fig, "promotion_effectiveness.png")

#---------------------------------------------------------
#9. PRICE vs. SALES VOLUME
#---------------------------------------------------------

def plot_price_vs_sales(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=df, x='price', y='sales_volume', color='purple', ax=ax)
    sns.regplot(data=df, x='price', y='sales_volume', scatter=False, color='black', ax=ax)
    ax.set_title("Price vs Sales Volume")
    ax.set_xlabel("Price")
    ax.set_ylabel("Sales Volume")

    save_plot(fig, "price_vs_sales_volume.png")

#---------------------------------------------------------
#10. OUTLIER BOXPLOTS
#---------------------------------------------------------

def plot_outlier_boxplots(df):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))

    sns.boxplot(y=df['price'], ax=ax[0], color='teal')
    ax[0].set_title("Price Outliers")

    sns.boxplot(y=df['sales_volume'], ax=ax[1], color='salmon')
    ax[1].set_title("Sales Volume Outliers")

    save_plot(fig, "outlier_boxplots.png")

#---------------------------------------------------------
#11. PAIRPLOT OF KEY VARIABLES
#---------------------------------------------------------

def plot_pairplot(df):
    cols = ['price', 'sales_volume', 'promotion']
    fig = sns.pairplot(df[cols], diag_kind='kde', corner=True)
    fig.fig.suptitle("Pairplot of Key Variables", y=1.02)

    # pairplot saving trick
    fig.savefig(os.path.join(os.path.dirname(__file__), "..", "visuals", "pairplot.png"), dpi=300, bbox_inches='tight')
    plt.close()


# ---------------------------------------------------------
# GENERATE ALL VISUALS
# ---------------------------------------------------------

def generate_all_visuals(df):
    plot_sales_volume_distribution(df)
    plot_price_distribution(df)
    plot_product_category(df)
    plot_promotion_vs_sales(df)
    plot_correlation_heatmap(df)
    plot_sales_volume_by_category(df)
    plot_sales_volume_by_position(df)
    plot_promotion_effectiveness(df)
    plot_price_vs_sales(df)
    plot_outlier_boxplots(df)
    plot_pairplot(df)

# ---------------------------------------------------------
# RUN WHEN EXECUTED DIRECTLY
# ---------------------------------------------------------

if __name__ == "__main__":
    cleaned_path = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned-data", "cleaned_data.csv")
    df = pd.read_csv(cleaned_path)

    generate_all_visuals(df)
    print("All visuals saved to /visuals folder.")
