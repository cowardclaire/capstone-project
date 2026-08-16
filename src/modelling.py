#Purpose :This file contains all your machine learning or statistical modelling code, such as: linear regression, clustering (KMeans),
#forecasting models, evaluation metrics

#trying to build a model to predict sales volume based on the cleaned data

import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from xgboost import XGBRegressor

import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 1. Load cleaned data
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "cleaned-data", "cleaned_data.csv")

df = pd.read_csv(DATA_PATH)


# ------------------------------------------------------------
# 2. Remove all text/object columns (XGBoost can't use them)
# ------------------------------------------------------------

text_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()
df = df.drop(columns=text_cols)


# ------------------------------------------------------------
# 3. Encoding remaining categorical columns
# ------------------------------------------------------------

categorical_cols = []

# Only encode category — product_position is already one-hot encoded in cleaned data
if 'category' in df.columns:
    categorical_cols.append('category')

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


# ------------------------------------------------------------
# 4. Defining features and target
# ------------------------------------------------------------

TARGET_COL = 'sales_volume'
feature_cols = [col for col in df.columns if col != TARGET_COL]

X = df[feature_cols]
y = df[TARGET_COL]


# ------------------------------------------------------------
# 5. Train/test split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ------------------------------------------------------------
# 6. Train XGBoost model
# ------------------------------------------------------------

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    objective='reg:squarederror'
)

model.fit(X_train, y_train)


# ------------------------------------------------------------
# 7. Evaluation
# ------------------------------------------------------------

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model performance:")
print(f"RMSE: {rmse:.2f}")
print(f"MAE:  {mae:.2f}")
print(f"R²:   {r2:.3f}")

# ------------------------------------------------------------
# 8. Feature importance plot (saved to visuals)
# ------------------------------------------------------------

importance = model.feature_importances_
importance_df = pd.DataFrame({
    'feature': feature_cols,
    'importance': importance
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=importance_df.head(15),
    x='importance',
    y='feature',
    hue='feature',
    legend=False,
    palette='viridis'
)
plt.title("Feature Importances - XGBoost Sales Volume Model")
plt.tight_layout()

VISUALS_PATH = os.path.join(BASE_DIR, "..", "visuals", "xgboost_feature_importance.png")
plt.savefig(VISUALS_PATH)
plt.close()

print(f"Feature importance plot saved to: {VISUALS_PATH}")


#reviewing the feature importance plot, where promotion is dominating the chart i now want to drop promotion so i can see the other features and their importance.

importance_df_no_promo = importance_df[importance_df['feature'] != 'promotion']

plt.figure(figsize=(10, 6))
sns.barplot(
    data=importance_df_no_promo,
    x='importance',
    y='feature',
    hue='feature',
    legend=False,
    palette='viridis'
)
plt.title("Feature Importances (Excluding Promotion)")
plt.tight_layout()

path = os.path.join(BASE_DIR, "..", "visuals", "feature_importance_no_promo.png")
plt.savefig(path)
plt.close()

print(f"Saved: {path}")
