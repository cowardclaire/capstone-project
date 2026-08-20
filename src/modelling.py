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

    # ------------------------------------------------------------
    # 1. Remove text/object columns (XGBoost cannot use them)
    # ------------------------------------------------------------
    text_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()
    df = df.drop(columns=text_cols)

    # ------------------------------------------------------------
    # 2. Encode remaining categorical columns
    # ------------------------------------------------------------
    categorical_cols = []

    if 'category' in df.columns:
        categorical_cols.append('category')

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # ------------------------------------------------------------
    # 3. Define features and target
    # ------------------------------------------------------------
    TARGET_COL = 'sales_volume'
    feature_cols = [col for col in df.columns if col != TARGET_COL]

    X = df[feature_cols]
    y = df[TARGET_COL]

    # ------------------------------------------------------------
    # 4. Train/test split
    # ------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ------------------------------------------------------------
    # 5. Train XGBoost model
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
    # 6. Evaluation
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
    # 7. Save metrics
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
    # 8. Feature importance plot
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

    save_plot(plt.gcf(), "xgboost_feature_importance.png")

    # ------------------------------------------------------------
    # 9. Feature importance without promotion
    # ------------------------------------------------------------
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

    save_plot(plt.gcf(), "feature_importance_no_promo.png")

    # ------------------------------------------------------------
    # 10. Predicted vs Actual
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
    # 11. Residuals plot
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
    # 12. Save trained model
    # ------------------------------------------------------------
    model_path = os.path.join(os.path.dirname(__file__), "..", "data", "model")
    os.makedirs(model_path, exist_ok=True)
    joblib.dump(model, os.path.join(model_path, "xgboost_model.pkl"))

    print("\n--- XGBoost modelling complete ---")
    print("Metrics saved to /data/model-metrics/")
    print("Model saved to /data/model/")
    print("Visuals saved to /visuals/model/")

    return model


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        base_dir, "..", "data", "cleaned-data", "cleaned_data.csv"
    )
    data = pd.read_csv(data_path)
    train_models(data)
