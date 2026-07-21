"""
Ngarkon data/apartments.csv dhe krijon dy grafikë me matplotlib:
1. Histogram i çmimeve -> output/price_distribution.png
2. Bar chart i çmimit mesatar sipas numrit të dhomave -> output/avg_price_by_bedrooms.png
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # backend pa GUI, i sigurt për terminal/skript
import matplotlib.pyplot as plt

DATA_PATH = "data/apartments.csv"
OUTPUT_DIR = "output"


def main():
    df = pd.read_csv(DATA_PATH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- 1. Histogram i çmimeve ---
    plt.figure(figsize=(8, 5))
    plt.hist(df["price"], bins=10, color="#7B5EA7", edgecolor="black")
    plt.title("Shpërndarja e Çmimeve të Apartamenteve në Tiranë")
    plt.xlabel("Çmimi (EUR)")
    plt.ylabel("Numri i shpalljeve")
    plt.tight_layout()
    hist_path = os.path.join(OUTPUT_DIR, "price_distribution.png")
    plt.savefig(hist_path)
    plt.close()

    # --- 2. Bar chart: çmimi mesatar sipas numrit të dhomave ---
    avg_by_bedrooms = df.groupby("bedrooms")["price"].mean().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(
        avg_by_bedrooms.index.astype(str),
        avg_by_bedrooms.values,
        color="#A084CA",
        edgecolor="black",
    )
    plt.title("Çmimi Mesatar sipas Numrit të Dhomave")
    plt.xlabel("Numri i dhomave (bedrooms)")
    plt.ylabel("Çmimi mesatar (EUR)")
    plt.tight_layout()
    bar_path = os.path.join(OUTPUT_DIR, "avg_price_by_bedrooms.png")
    plt.savefig(bar_path)
    plt.close()

    print(f"U ruajt histogrami i çmimeve te '{hist_path}'")
    print(f"U ruajt bar chart-i i çmimit mesatar sipas dhomave te '{bar_path}'")


if __name__ == "__main__":
    main()