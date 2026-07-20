"""
generate_fake_listings.py

Gjeneron 40 shpallje FALSE (fiktive) apartamentesh në Tiranë,
me kolonat: price, sqm, bedrooms, bathrooms, floor, neighborhood.
I ruan në data/apartments.csv duke përdorur pandas.
"""

import random
import pandas as pd
from pathlib import Path

random.seed(42)  # për rezultate të përsëritshme (të njëjtat çdo herë që e ekzekuton)

NEIGHBORHOODS = [
    "Blloku", "Kombinat", "Don Bosko", "21 Dhjetori",
    "Njesia 5", "Laprake", "Ysberisht", "Selite",
]

def generate_listing():
    sqm = random.randint(35, 180)
    price_per_sqm = random.randint(900, 2200)
    price = sqm * price_per_sqm

    return {
        "price": price,
        "sqm": sqm,
        "bedrooms": random.randint(1, 4),
        "bathrooms": random.randint(1, 2),
        "floor": random.randint(0, 10),
        "neighborhood": random.choice(NEIGHBORHOODS),
    }

def main():
    listings = [generate_listing() for _ in range(40)]
    df = pd.DataFrame(listings)

    out_path = Path("data/apartments.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print(f"U ruajtën {len(df)} rreshta në {out_path}")

if __name__ == "__main__":
    main()