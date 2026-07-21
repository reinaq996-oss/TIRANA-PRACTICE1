"""
Gjeneron 40 shpallje (listings) të rreme apartamentesh në Tiranë
dhe i ruan si CSV në data/apartments.csv
"""

import os
import random
import pandas as pd

# Për rezultate të përsëritshme (mund ta hiqësh nëse do random çdo herë)
random.seed(42)

NEIGHBORHOODS = [
    "Blloku",
    "Don Bosko",
    "Komuna e Parisit",
    "Njesia Bashkiake 5",
    "Ali Demi",
    "21 Dhjetori",
    "Fresk",
    "Kombinat",
    "Selitë",
    "Liqeni i Thatë",
    "Astir",
    "Yzberisht",
]

def generate_listing():
    sqm = random.randint(35, 180)
    bedrooms = random.randint(1, 4)
    bathrooms = random.randint(1, min(bedrooms, 3))
    floor = random.randint(0, 12)  # 0 = përdhesë
    neighborhood = random.choice(NEIGHBORHOODS)

    # Çmimi bazohet përafërsisht te sqm + zhurmë e rastësishme,
    # për të simuluar diferenca çmimi/m2 mes zonave
    price_per_sqm_base = random.uniform(900, 2200)
    price = round(sqm * price_per_sqm_base, -2)  # rrumbullakosur në 100 €

    return {
        "price": int(price),
        "sqm": sqm,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floor": floor,
        "neighborhood": neighborhood,
    }


def main():
    listings = [generate_listing() for _ in range(40)]
    df = pd.DataFrame(listings)

    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "apartments.csv")

    df.to_csv(output_path, index=False)

    print(f"U krijuan {len(df)} shpallje dhe u ruajtën në '{output_path}'")


if __name__ == "__main__":
    main()