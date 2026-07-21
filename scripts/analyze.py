"""
Ngarkon data/apartments.csv, shton kolonën price_per_sqm,
printon çmimin mesatar sipas numrit të dhomave (bedrooms),
dhe printon 3 shpalljet me price_per_sqm më të ulët (ofertat më të mira).
"""

import pandas as pd

DATA_PATH = "data/apartments.csv"


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


if __name__ == "__main__":
    main()