"""
Ngarkon data/apartments.csv, shton kolonën price_per_sqm,
printon çmimin mesatar sipas numrit të dhomave (bedrooms),
printon 3 shpalljet me price_per_sqm më të ulët (ofertat më të mira),
dhe shkruan një raport të shkurtër përmbledhës te output/summary.txt.
"""

import os
import pandas as pd

DATA_PATH = "data/apartments.csv"
OUTPUT_DIR = "output"


def main():
    df = pd.read_csv(DATA_PATH)

    # Shtojmë kolonën price_per_sqm
    df["price_per_sqm"] = (df["price"] / df["sqm"]).round(2)

    print("=" * 60)
    print("ÇMIMI MESATAR SIPAS NUMRIT TË DHOMAVE (bedrooms)")
    print("=" * 60)
    avg_by_bedrooms = df.groupby("bedrooms")["price"].mean().round(2)
    print(avg_by_bedrooms)

    print("\n" + "=" * 60)
    print("3 OFERTAT MË TË MIRA (price_per_sqm më e ulët)")
    print("=" * 60)
    best_deals = df.nsmallest(3, "price_per_sqm")
    print(best_deals)

    # --- Raport përmbledhës -> output/summary.txt ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_listings = len(df)
    avg_price = df["price"].mean()
    avg_sqm = df["sqm"].mean()
    best_value = df.loc[df["price_per_sqm"].idxmin()]

    summary_lines = [
        "RAPORT PËRMBLEDHËS - TIRANA DEAL FINDER",
        "=" * 45,
        f"Numri total i shpalljeve: {total_listings}",
        f"Çmimi mesatar: {avg_price:,.2f} EUR",
        f"Sipërfaqja mesatare: {avg_sqm:,.2f} m²",
        "",
        "OFERTA MË E MIRË (price_per_sqm më e ulët):",
        f"  Çmimi: {best_value['price']:,.0f} EUR",
        f"  Sipërfaqja: {best_value['sqm']} m²",
        f"  Dhoma gjumi: {best_value['bedrooms']}",
        f"  Banjo: {best_value['bathrooms']}",
        f"  Kati: {best_value['floor']}",
        f"  Zona: {best_value['neighborhood']}",
        f"  Çmimi/m²: {best_value['price_per_sqm']:,.2f} EUR",
    ]

    summary_path = os.path.join(OUTPUT_DIR, "summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))

    print(f"\nU ruajt raporti përmbledhës te '{summary_path}'")


if __name__ == "__main__":
    main()