"""
Ngarkon modelin e trajnuar nga models/price_model.joblib
dhe parashikon çmimin për një apartament të trilluar:
sqm=75, bedrooms=2, bathrooms=1, floor=3.
"""

import joblib
import pandas as pd

MODEL_PATH = "models/price_model.joblib"

sample_apartment = {
    "sqm": 75,
    "bedrooms": 2,
    "bathrooms": 1,
    "floor": 3,
}


def main():
    model = joblib.load(MODEL_PATH)

    # Përdorim DataFrame me emrat e kolonave, që të përputhet me trajnimin
    X_new = pd.DataFrame([sample_apartment])
    predicted_price = model.predict(X_new)[0]

    print("=" * 60)
    print("PARASHIKIM ÇMIMI")
    print("=" * 60)
    print(f"Apartamenti: {sample_apartment}")
    print(f"Çmimi i parashikuar: {predicted_price:,.2f} EUR")


if __name__ == "__main__":
    main()