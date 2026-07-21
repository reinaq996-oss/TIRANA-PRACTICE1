"""
Ngarkon data/apartments.csv dhe printon një eksplorim bazë:
head(), info(), describe()
"""

import pandas as pd

DATA_PATH = "data/apartments.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    print("=" * 60)
    print("PARË TË PARË (df.head())")
    print("=" * 60)
    print(df.head())

    print("\n" + "=" * 60)
    print("INFORMACION MBI KOLONAT (df.info())")
    print("=" * 60)
    df.info()

    print("\n" + "=" * 60)
    print("STATISTIKA PËRSHKRUESE (df.describe())")
    print("=" * 60)
    print(df.describe())


if __name__ == "__main__":
    main()