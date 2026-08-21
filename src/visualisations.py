# --------------------------------------------------------
# VISUALISATIONS MODULE (MODULAR VERSION)
# --------------------------------------------------------

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="whitegrid")

# --------------------------------------------------------
# SAVE FUNCTION
# --------------------------------------------------------

def save_plot(fig, filename):
    visuals_path = os.path.join(os.path.dirname(__file__), "..", "visuals", "eda")
    os.makedirs(visuals_path, exist_ok=True)

    full_path = os.path.join(visuals_path, filename)
    fig.savefig(full_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {os.path.normpath(full_path)}")

# --------------------------------------------------------
# REBUILD PRODUCT POSITION (for visuals)
# --------------------------------------------------------

def rebuild_product_position(df):
    position_cols = [col for col in df.columns if col.startswith("product_position_")]

    if len(position_cols) == 0:
        print("No encoded product_position columns found.")
        return df

    df['product_position'] = (
        df[position_cols]
        .idxmax(axis=1)
        .str.replace("product_position_", "")
    )

    return df

# --------------------------------------------------------
# 1. SALES VOLUME DISTRIBUTION
# --------------------------------------------------------

def plot_sales_volume_distribution(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(df['sales_volume'], kde=True, bins=30, color='steelblue', ax=ax)
    ax.set_title("Sales Volume Distribution")
    ax.set_xlabel("Sales Volume")
    ax.set_ylabel("Frequency")

    save_plot(fig, "sales_volume_distribution.png")

# --------------------------------------------------------
# 2. PRICE DISTRIBUTION + BOXPLOT
# --------------------------------------------------------

def plot_price_distribution(df):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    sns.histplot(df['price'], kde=True, bins=30, ax=ax[0], color='teal')
    ax[0].set_title("Price Distribution")

    sns.boxplot(x=df['price'], ax=ax[1], color='salmon')
    ax[1].set_title("Price Boxplot")

    save_plot(fig, "price_distribution.png")

# --------------------------------------------------------
# 3. PRODUCT CATEGORY DISTRIBUTION
# --------------------------------------------------------

def plot_product_category(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.countplot(data=df, x='terms', hue='terms', palette='magma', legend=False, ax=ax)
    plt.title("Product Category Distribution")
    plt.xticks(rotation=45)

    save_plot(fig, "product_category_distribution.png")

# --------------------------------------------------------
# 4. PROMOTION VS SALES VOLUME
# --------------------------------------------------------

def plot_promotion_vs_sales(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(data=df, x='promotion', y='sales_volume', hue='promotion',
                palette='coolwarm', legend=False, ax=ax)
    plt.title("Sales Volume by Promotion")
    plt.xlabel("Promotion (0 = No, 1 = Yes)")
    plt.ylabel("Sales Volume")

    save_plot(fig, "promotion_vs_sales_volume.png")

# --------------------------------------------------------
# 5. CORRELATION HEATMAP
# --------------------------------------------------------

def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    corr = numeric_df.corr().round(2)

    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(corr, annot=True, cmap='Blues', ax=ax, fmt=".2f")
    ax.set_title("Correlation Heatmap")

    save_plot(fig, "correlation_heatmap.png")

# --------------------------------------------------------
# 6. SALES VOLUME BY CATEGORY
# --------------------------------------------------------

def plot_sales_volume_by_category(df):
    fig, ax = plt.subplots(figsize=(12,6))
    category_means = df.groupby('terms')['sales_volume'].mean().sort_values()
    sns.barplot(x=category_means.index, y=category_means.values,
                palette='viridis', ax=ax)
    ax.set_title("Average Sales Volume by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Average Sales Volume")
    plt.xticks(rotation=45)

    save_plot(fig, "sales_volume_by_category.png")

# --------------------------------------------------------
# 7. SALES VOLUME BY PRODUCT POSITION
# --------------------------------------------------------

def plot_sales_volume_by_position(df):
    fig, ax = plt.subplots(figsize=(12,6))
    sns.boxplot(data=df, x='product_position', y='sales_volume',
                palette='coolwarm', ax=ax)
    ax.set_title("Sales Volume by Product Position")
    ax.set_xlabel("Product Position")
    ax.set_ylabel("Sales Volume")
    plt.xticks(rotation=45)

    save_plot(fig, "sales_volume_by_position.png")

# --------------------------------------------------------
# 8. PROMOTION EFFECTIVENESS
# --------------------------------------------------------

def plot_promotion_effectiveness(df):
    fig, ax = plt.subplots(figsize=(8,6))
    promo_means = df.groupby('promotion')['sales_volume'].mean()
    sns.barplot(x=promo_means.index, y=promo_means.values,
                palette='coolwarm', ax=ax)
    ax.set_title("Promotion Effectiveness (Mean Sales Volume)")
    ax.set_xlabel("Promotion (0 = No, 1 = Yes)")
    ax.set_ylabel("Average Sales Volume")

    save_plot(fig, "promotion_effectiveness.png")

# --------------------------------------------------------
# 9. PRICE VS SALES VOLUME
# --------------------------------------------------------

def plot_price_vs_sales(df):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=df, x='price', y='sales_volume', color='purple', ax=ax)
    sns.regplot(data=df, x='price', y='sales_volume',
                scatter=False, color='black', ax=ax)
    ax.set_title("Price vs Sales Volume")
    ax.set_xlabel("Price")
    ax.set_ylabel("Sales Volume")

    save_plot(fig, "price_vs_sales_volume.png")

# --------------------------------------------------------
# 10. OUTLIER BOXPLOTS
# --------------------------------------------------------

def plot_outlier_boxplots(df):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))

    sns.boxplot(y=df['price'], ax=ax[0], color='teal')
    ax[0].set_title("Price Outliers")

    sns.boxplot(y=df['sales_volume'], ax=ax[1], color='salmon')
    ax[1].set_title("Sales Volume Outliers")

    save_plot(fig, "outlier_boxplots.png")

# --------------------------------------------------------
# 11. PAIRPLOT
# --------------------------------------------------------

def plot_pairplot(df):
    cols = ['price', 'sales_volume', 'promotion']
    fig = sns.pairplot(df[cols], diag_kind='kde', corner=True)
    fig.fig.suptitle("Pairplot of Key Variables", y=1.02)

    save_plot(fig.fig, "pairplot.png")

# --------------------------------------------------------
# 12. PRICE BY CATEGORY
# --------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_by_category(df):
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df, x='terms', y='price', palette='viridis')
    plt.title("Price by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Price")
    plt.xticks(rotation=45)

    save_plot(plt.gcf(), "price_by_category.png")


# --------------------------------------------------------
# 13. GENERATE ALL VISUALS (MAIN FUNCTION)
# --------------------------------------------------------

def generate_all_visuals(df):

    df = rebuild_product_position(df)

    plot_price_distribution(df)
    plot_product_category(df)
    plot_promotion_vs_sales(df)
    plot_sales_volume_distribution(df)
    plot_correlation_heatmap(df)
    plot_sales_volume_by_category(df)
    plot_sales_volume_by_position(df)
    plot_promotion_effectiveness(df)
    plot_price_vs_sales(df)
    plot_outlier_boxplots(df)
    plot_pairplot(df)
    plot_price_by_category(df)  
    print("\n--- ALL EDA VISUALS SAVED TO /visuals/eda ---")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        base_dir, "..", "data", "cleaned-data", "cleaned_data.csv"
    )
    data = pd.read_csv(data_path)
    generate_all_visuals(data)
