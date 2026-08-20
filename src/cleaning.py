#Purpose : This file contains all your data cleaning and preparation functions, such as: loading raw data, handling missing values
#,removing duplicates, normalising columns, feature engineering, saving cleaned data into /data/cleaned/

# --------------------------------------------------------
# CLEANING MODULE (MODULAR VERSION)
# --------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --------------------------------------------------------
# 1. INSPECT RAW DATA
# --------------------------------------------------------

def inspect_data(file_path):
    df = pd.read_csv(file_path, sep=";")

    print("\n--- SHAPE ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n--- HEAD ---")
    print(df.head())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isna().sum())

    print("\n--- UNIQUE VALUES PER COLUMN ---")
    print(df.nunique())

    return df

# --------------------------------------------------------
# 2. STANDARDISE COLUMN NAMES
# --------------------------------------------------------

def standardise_column_names(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("[^A-Za-z0-9_]+", "", regex=True)
    )
    return df

# --------------------------------------------------------
# 3. DUPLICATE SUMMARY
# --------------------------------------------------------

def duplicate_summary_table(df):
    rows = []
    for col in df.columns:
        counts = df[col].value_counts()
        duplicated_values = counts[counts > 1]
        num_unique_dups = len(duplicated_values)
        total_dup_entries = duplicated_values.sum()
        top_dup_value = duplicated_values.idxmax() if num_unique_dups > 0 else None
        top_dup_count = duplicated_values.max() if num_unique_dups > 0 else None

        rows.append({
            "column": col,
            "unique_duplicated_values": num_unique_dups,
            "total_duplicate_entries": total_dup_entries,
            "top_duplicated_value": top_dup_value,
            "top_duplicated_count": top_dup_count
        })
    return pd.DataFrame(rows)

# --------------------------------------------------------
# 4. OUTLIER DETECTION (IQR)
# --------------------------------------------------------

def detect_outliers_iqr(df):
    outlier_results = {}
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        outlier_results[col] = outliers

    return outlier_results

# --------------------------------------------------------
# 5. FEATURE ENGINEERING
# --------------------------------------------------------

def engineer_features(df):
    if "sales_volume" in df.columns:
        q1 = df["sales_volume"].quantile(0.33)
        q2 = df["sales_volume"].quantile(0.66)

        def bucket(x):
            if x <= q1:
                return "low"
            elif x <= q2:
                return "average"
            else:
                return "high"

        df["sales_performance_bucket"] = df["sales_volume"].apply(bucket)

# --------------------------------------------------------
# 6. ENCODE CATEGORICAL FEATURES
# --------------------------------------------------------

def encode_categorical_features(df):
    binary_map = {"Yes": 1, "No": 0}

    if "seasonal" in df.columns:
        df["seasonal"] = df["seasonal"].map(binary_map)

    if "promotion" in df.columns:
        df["promotion"] = df["promotion"].map(binary_map)

    if "product_position" in df.columns:
        df = pd.get_dummies(df, columns=["product_position"], drop_first=False)

    return df

# --------------------------------------------------------
# 7. FINAL CHECKS
# --------------------------------------------------------

def final_checks(df):
    print("\n--- FINAL INFO ---")
    print(df.info())

    print("\n--- FINAL MISSING VALUES ---")
    print(df.isna().sum())

    print("\n--- FINAL SHAPE ---")
    print(df.shape)

# --------------------------------------------------------
# 8. WRAP EVERYTHING INTO ONE FUNCTION
# --------------------------------------------------------

def clean_data():
    # Load raw data
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw-data", "raw_data.csv")
    df = inspect_data(file_path)

    # Standardise column names
    df = standardise_column_names(df)

    # Drop missing values
    df = df.dropna()

    # Duplicate summary (no dropping)
    duplicate_summary_table(df)

    # Outlier detection (kept)
    detect_outliers_iqr(df)

    # Feature engineering
    engineer_features(df)

    # Encode categorical variables
    df = encode_categorical_features(df)

    # Rebuild product_position
    position_cols = [col for col in df.columns if col.startswith("product_position_")]
    df["product_position"] = (
        df[position_cols]
        .idxmax(axis=1)
        .str.replace("product_position_", "")
    )

    # Final checks
    final_checks(df)

    # Save cleaned data
    output_path = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned-data", "cleaned_data.csv")
    df.to_csv(output_path, index=False)

    print("\n--- CLEANED DATASET EXPORTED ---")
    print("Saved to:", output_path)

    return df
