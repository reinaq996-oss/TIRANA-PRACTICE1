"""
Ngarkon data/apartments.csv, ndan të dhënat në train/test,
trajnon një model LinearRegression dhe një RandomForestRegressor
për të parashikuar price nga sqm, bedrooms, bathrooms dhe floor,
printon R² dhe Mean Absolute Error (MAE) mbi test set për krahasim,
dhe ruan modelin LinearRegression te models/price_model.joblib.
"""

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

DATA_PATH = "data/apartments.csv"
FEATURES = ["sqm", "bedrooms", "bathrooms", "floor"]
TARGET = "price"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "price_model.joblib")


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    lr_pred = lr_model.predict(X_test)

    lr_r2 = r2_score(y_test, lr_pred)
    lr_mae = mean_absolute_error(y_test, lr_pred)

    print("=" * 60)
    print("REZULTATET E MODELIT (LinearRegression)")
    print("=" * 60)
    print(f"Numri i shembujve trajnues: {len(X_train)}")
    print(f"Numri i shembujve testues:  {len(X_test)}")
    print(f"R² score: {lr_r2:.4f}")
    print(f"Mean Absolute Error (MAE): {lr_mae:,.2f} EUR")

    print("\nKoeficientët e modelit:")
    for feature, coef in zip(FEATURES, lr_model.coef_):
        print(f"  {feature}: {coef:,.2f}")
    print(f"  intercept: {lr_model.intercept_:,.2f}")

    # --- RandomForestRegressor, për krahasim ---
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    rf_pred = rf_model.predict(X_test)

    rf_r2 = r2_score(y_test, rf_pred)
    rf_mae = mean_absolute_error(y_test, rf_pred)

    print("\n" + "=" * 60)
    print("REZULTATET E MODELIT (RandomForestRegressor)")
    print("=" * 60)
    print(f"R² score: {rf_r2:.4f}")
    print(f"Mean Absolute Error (MAE): {rf_mae:,.2f} EUR")

    # --- Krahasim ---
    print("\n" + "=" * 60)
    print("KRAHASIMI I MODELEVE")
    print("=" * 60)
    print(f"{'Modeli':<22}{'R²':>10}{'MAE (EUR)':>16}")
    print(f"{'LinearRegression':<22}{lr_r2:>10.4f}{lr_mae:>16,.2f}")
    print(f"{'RandomForestRegressor':<22}{rf_r2:>10.4f}{rf_mae:>16,.2f}")

    # --- Ruajmë modelin LinearRegression të trajnuar ---
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(lr_model, MODEL_PATH)
    print(f"\nU ruajt modeli i trajnuar (LinearRegression) te '{MODEL_PATH}'")


if __name__ == "__main__":
    main()