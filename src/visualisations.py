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

def plot_sales_volume_distribution(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(df['sales_volume'], kde=True, bins=30, color='steelblue', ax=ax)
    ax.set_title("Sales Volume Distribution")
    ax.set_xlabel("Sales Volume")
    ax.set_ylabel("Frequency")

    save_plot(fig, "sales_volume_distribution.png")


def plot_price_distribution(df):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    sns.histplot(df['price'], kde=True, bins=30, ax=ax[0], color='teal')
    ax[0].set_title("Price Distribution")

    sns.boxplot(x=df['price'], ax=ax[1], color='salmon')
    ax[1].set_title("Price Boxplot")

    save_plot(fig, "price_distribution.png")


def plot_product_category(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(data=df, x='terms', hue='terms', palette='magma', legend=False, ax=ax)
    plt.title("Product Category Distribution")
    plt.xticks(rotation=45)

    save_plot(fig, "product_category_distribution.png")


def plot_promotion_vs_sales(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(data=df, x='promotion', y='sales_volume', hue='promotion', palette='coolwarm', legend=False, ax=ax)
    plt.title("Sales Volume by Promotion")
    plt.xlabel("Promotion (0 = No, 1 = Yes)")
    plt.ylabel("Sales Volume")

    save_plot(fig, "promotion_vs_sales_volume.png")

# ---------------------------------------------------------
# GENERATE ALL VISUALS
# ---------------------------------------------------------

def generate_all_visuals(df):
    plot_sales_volume_distribution(df)
    plot_price_distribution(df)
    plot_product_category(df)
    plot_promotion_vs_sales(df)

# ---------------------------------------------------------
# RUN WHEN EXECUTED DIRECTLY
# ---------------------------------------------------------

if __name__ == "__main__":
    cleaned_path = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned-data", "cleaned_data.csv")
    df = pd.read_csv(cleaned_path)

    generate_all_visuals(df)
    print("All visuals saved to /visuals folder.")
