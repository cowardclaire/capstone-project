#importing libraries for cleaning and visualizing data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#creating a path to the data file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "Zara_sales_EDA.csv")

#function to load the data file and checking the data types of columns and null values

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

# Load the data using your function
df = inspect_data(file_path)

#dropping the columns with missing values as minimal

df = inspect_data(file_path)

# Drop rows with any missing values
df = df.dropna()

print("\n--- AFTER DROPPING MISSING VALUES ---")
print(df.isna().sum())
print(df.shape)

#creating a function that standardizes the column names to lower case and replacing spaces with underscores

def standardise_column_names(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('[^A-Za-z0-9_]+', '', regex=True)
    )
    return df


df = standardise_column_names(df)
print("\n--- AFTER STANDARDIZING COLUMN NAMES ---")
print(df.columns)

#creating a function to check for outliers in the numerical columns using the IQR method

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

print(df['price'].describe().round(2)) #IQR method flagged outliers in price but after reviewing the price sitruation, I have decided to keep the outliers as they are valid data points and removing them would result in loss of valuable information.

