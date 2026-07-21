"""
Ngarkon data/apartments.csv dhe krijon katër grafikë me matplotlib:
1. Histogram i çmimeve -> output/price_distribution.png
2. Bar chart i çmimit mesatar sipas numrit të dhomave -> output/avg_price_by_bedrooms.png
3. Scatter plot i çmimit kundrejt sipërfaqes (sqm) -> output/price_vs_sqm.png
4. Boxplot i çmimit sipas numrit të dhomave -> output/price_by_bedrooms_boxplot.png
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

    # --- 3. Scatter plot: çmimi kundrejt sqm ---
    plt.figure(figsize=(8, 5))
    plt.scatter(df["sqm"], df["price"], color="#6A4C93", edgecolor="black", alpha=0.7)
    plt.title("Çmimi vs Sipërfaqja (sqm)")
    plt.xlabel("Sipërfaqja (m²)")
    plt.ylabel("Çmimi (EUR)")
    plt.tight_layout()
    scatter_path = os.path.join(OUTPUT_DIR, "price_vs_sqm.png")
    plt.savefig(scatter_path)
    plt.close()

    # --- 4. Boxplot: çmimi sipas numrit të dhomave ---
    bedroom_groups = sorted(df["bedrooms"].unique())
    data_by_bedrooms = [df.loc[df["bedrooms"] == b, "price"] for b in bedroom_groups]

    plt.figure(figsize=(8, 5))
    plt.boxplot(data_by_bedrooms, tick_labels=[str(b) for b in bedroom_groups])
    plt.title("Shpërndarja e Çmimit sipas Numrit të Dhomave")
    plt.xlabel("Numri i dhomave (bedrooms)")
    plt.ylabel("Çmimi (EUR)")
    plt.tight_layout()
    boxplot_path = os.path.join(OUTPUT_DIR, "price_by_bedrooms_boxplot.png")
    plt.savefig(boxplot_path)
    plt.close()

    print(f"U ruajt histogrami i çmimeve te '{hist_path}'")
    print(f"U ruajt bar chart-i i çmimit mesatar sipas dhomave te '{bar_path}'")
    print(f"U ruajt scatter plot-i çmimi vs sqm te '{scatter_path}'")
    print(f"U ruajt boxplot-i çmimit sipas dhomave te '{boxplot_path}'")


if __name__ == "__main__":
    main()