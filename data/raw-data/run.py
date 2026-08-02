#--------------------------------------------------------
#1. IMPORTING LIBRARIES FOR CLEANING AND VISUALIZING DATA
#--------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#--------------------------------------------------------
#2. CREATING A FUNCTION TO LOAD DATA, CHECK DATATYPES AND NULL VALUES
#--------------------------------------------------------   

def inspect_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, sep=";")

    # Basic shape
    print("\n--- SHAPE ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Show first few rows
    print("\n--- HEAD ---")
    print(df.head())

    # Show datatypes
    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    # Missing values
    print("\n--- MISSING VALUES ---")
    print(df.isna().sum())

    # Count unique values (helps spot categorical fields)
    print("\n--- UNIQUE VALUES PER COLUMN ---")
    print(df.nunique())

    return df

df = inspect_data("data/raw-data/Zara_sales_EDA.csv")

#--------------------------------------------------------
#3. STANDARDISING COLUMN NAMES
#--------------------------------------------------------   

def standardise_column_names(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("[^A-Za-z0-9_]+", "", regex=True)
    )
    return df

df = standardise_column_names(df)
print("\n--- AFTER STANDARDIZING COLUMN NAMES ---")
print(df.columns)

#--------------------------------------------------------
#4. REMOVE MISSING VALUES
#--------------------------------------------------------
#choosing to remove missing values as there are only 3 rows with missing values in the dataset

df = df.dropna()

print("\n--- AFTER DROPPING MISSING VALUES ---")
print(df.isna().sum())
print(df.shape)

#---------------------------------------------------------
#5. HANDLING DUPLICATE VALUES
#---------------------------------------------------------

def duplicate_summary_table(df):
    rows = []

    for col in df.columns:
        counts = df[col].value_counts()

        duplicated_values = counts[counts > 1]              # values that appear more than once
        num_unique_dups = len(duplicated_values)            # how many distinct duplicated values
        total_dup_entries = duplicated_values.sum()         # total number of duplicate entries

        top_dup_value = (
            duplicated_values.idxmax() if num_unique_dups > 0 else None
        )
        top_dup_count = (
            duplicated_values.max() if num_unique_dups > 0 else None
        )

        rows.append({
            "column": col,
            "unique_duplicated_values": num_unique_dups,
            "total_duplicate_entries": total_dup_entries,
            "top_duplicated_value": top_dup_value,
            "top_duplicated_count": top_dup_count
        })

    return pd.DataFrame(rows)

summary_df = duplicate_summary_table(df)
print("\n--- DUPLICATE SUMMARY TABLE ---")
print(summary_df)   

#After checking summary table, duplicates are not a concern as there are no duplicates in product id which would need to be unique. Therefore, we will not drop any duplicates.

#---------------------------------------------------------
#6. CHECKING FOR OUTLIERS
#---------------------------------------------------------

def detect_outliers_iqr(df):
    """
    Detects outliers in all numerical columns using the IQR method.
    Returns a dictionary where each key is a column name and the value 
    is a DataFrame containing the outlier rows for that column.
    """
    
    outlier_results = {}
    
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Identify outliers
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        # Store results
        outlier_results[col] = outliers
        
    return outlier_results

outliers = detect_outliers_iqr(df)

for col, rows in outliers.items():
    print(f"Outliers in {col}: {len(rows)} rows")
    print(rows.head())

#checking outliers in price

print(df['price'].describe().round(2)) #IQR method flagged outliers in price but after reviewing the price situation, I have decided to keep the outliers as they are valid data points and removing them would result in loss of valuable information.

# ---------------------------------------------------------
# 7. ENCODE CATEGORICAL VARIABLES
# ---------------------------------------------------------
def encode_categorical_features(df):

    # 1. Binary encode yes/no columns
    binary_map = {"Yes": 1, "No": 0}

    if "seasonal" in df.columns:
        df["seasonal"] = df["seasonal"].map(binary_map)

    if "promotion" in df.columns:
        df["promotion"] = df["promotion"].map(binary_map)

    # 2. One-hot encode product_position
    if "product_position" in df.columns:
        df = pd.get_dummies(df, columns=["product_position"], drop_first=True)

    return df

print("\n--- BEFORE ENCODING CATEGORICAL VARIABLES ---")
print(df.head())

df = encode_categorical_features(df)

print("\n--- AFTER ENCODING CATEGORICAL VARIABLES ---")
print(df.head())

# ---------------------------------------------------------
# 9. FINAL VALIDATION CHECKS
# ---------------------------------------------------------
def final_checks(df):
    print("\n--- FINAL INFO ---")
    print(df.info())

    print("\n--- FINAL MISSING VALUES ---")
    print(df.isna().sum())

    print("\n--- FINAL SHAPE ---")
    print(df.shape)

final_checks(df)