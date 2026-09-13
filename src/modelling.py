# --------------------------------------------------------
# MODELLING MODULE (MODULAR VERSION WITH XGBOOST)
# --------------------------------------------------------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from xgboost import XGBRegressor
import joblib

sns.set(style="whitegrid")

# --------------------------------------------------------
# SAVE PLOT
# --------------------------------------------------------

def save_plot(fig, filename):
    visuals_path = os.path.join(os.path.dirname(__file__), "..", "visuals", "model")
    os.makedirs(visuals_path, exist_ok=True)

    full_path = os.path.join(visuals_path, filename)
    fig.savefig(full_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {os.path.normpath(full_path)}")

# --------------------------------------------------------
# MAIN MODELLING FUNCTION
# --------------------------------------------------------

def train_models(df):

    target_col = "sales_volume"
    if target_col not in df.columns:
        raise ValueError(f"Required target column '{target_col}' was not found.")

    # ------------------------------------------------------------
    # 1. Data Preprocessing
    # ------------------------------------------------------------
    df = df[["price", "promotion", target_col]]

    # Ensure promotion is numeric
    if df["promotion"].dtype == "object":
        df["promotion"] = df["promotion"].map({"Yes": 1, "No": 0})

    # ------------------------------------------------------------
    # 2. Define features and target
    # ------------------------------------------------------------
    X = df[["price", "promotion"]]
    y = df[target_col]

    feature_cols = ["price", "promotion"]

    # ------------------------------------------------------------
    # 3. Train/test split
    # ------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ------------------------------------------------------------
    # 4. Train XGBoost model
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
    # 5. Evaluation
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
    # 6. Save metrics
    # ------------------------------------------------------------
    metrics = pd.DataFrame({
        "RMSE": [rmse],
        "MAE": [mae],
        "R2": [r2]
    })

    metrics_path = os.path.join(os.path.dirname(__file__), "..", "data", "model-metrics")
    os.makedirs(metrics_path, exist_ok=True)
    metrics.to_csv(os.path.join(metrics_path, "xgboost_metrics.csv"), index=False)

    # ------------------------------------------------------------
    # 7. Feature importance plot
    # ------------------------------------------------------------
    importance = model.feature_importances_
    importance_df = pd.DataFrame({
        'feature': feature_cols,
        'importance': importance
    }).sort_values('importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=importance_df,
        x='importance',
        y='feature',
        hue='feature',
        legend=False,
        palette='viridis'
    )
    plt.title("Feature Importances - XGBoost Sales Volume Model")
    plt.tight_layout()

    save_plot(plt.gcf(), "xgboost_feature_importance.png")

    # ------------------------------------------------------------
    # 8. Predicted vs Actual
    # ------------------------------------------------------------
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Sales Volume")
    plt.ylabel("Predicted Sales Volume")
    plt.title("Predicted vs Actual Sales Volume")
    plt.tight_layout()

    save_plot(plt.gcf(), "predicted_vs_actual.png")

    # ------------------------------------------------------------
    # 9. Residuals plot
    # ------------------------------------------------------------
    residuals = y_test - y_pred

    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel("Predicted Sales Volume")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.title("Residuals Plot")
    plt.tight_layout()

    save_plot(plt.gcf(), "residuals_plot.png")

    # ------------------------------------------------------------
    # 10. Save trained model
    # ------------------------------------------------------------
    model_path = os.path.join(os.path.dirname(__file__), "..", "data", "model")
    os.makedirs(model_path, exist_ok=True)
    joblib.dump(model, os.path.join(model_path, "xgboost_model.pkl"))

    print("\n--- XGBoost modelling complete ---")
    print("Metrics saved to data/model-metrics/xgboost_metrics.csv")
    print("Model saved to data/model/xgboost_model.pkl")
    print("Visuals saved to visuals/model/")

    return model


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        base_dir, "..", "data", "cleaned-data", "cleaned_data.csv"
    )
    data = pd.read_csv(data_path)
    train_models(data)
