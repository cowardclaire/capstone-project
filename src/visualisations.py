#Purpose : This file contains reusable Plotly, Matplotlib, or Seaborn chart functions, such as: time-series charts, bar charts,
#scatter plots, box plots, customer segmentation visuals

import matplotlib.pyplot as plt
import seaborn as sns   
import pandas as pd
import numpy as np
import os

# Build path to cleaned data
cleaned_path = os.path.join(
    os.path.dirname(__file__),   # folder where visualisations.py lives (src)
    "..",                        # go up to CAPSTONE-PROJECT
    "data",                      # enter data folder
    "cleaned-data",              # enter cleaned-data folder
    "cleaned_data.csv"           # your cleaned file
)

# Load cleaned dataset
df = pd.read_csv(cleaned_path)

print("Loaded cleaned data successfully")
print(df.head())


