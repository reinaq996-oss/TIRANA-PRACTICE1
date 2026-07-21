""""
Ngarkon data/apartments.csv, ndan të dhënat në train/test,
trajnon një model LinearRegression për të parashikuar price
nga sqm, bedrooms, bathrooms dhe floor,
printon R² dhe Mean Absolute Error (MAE) mbi test set,
dhe ruan modelin e trajnuar te models/price_model.joblib.
"""

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print("=" * 60)
    print("REZULTATET E MODELIT (LinearRegression)")
    print("=" * 60)
    print(f"Numri i shembujve trajnues: {len(X_train)}")
    print(f"Numri i shembujve testues:  {len(X_test)}")
    print(f"R² score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:,.2f} EUR")

    print("\nKoeficientët e modelit:")
    for feature, coef in zip(FEATURES, model.coef_):
        print(f"  {feature}: {coef:,.2f}")
    print(f"  intercept: {model.intercept_:,.2f}")

    # --- Ruajmë modelin e trajnuar ---
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"\nU ruajt modeli i trajnuar te '{MODEL_PATH}'")


if __name__ == "__main__":
    main()