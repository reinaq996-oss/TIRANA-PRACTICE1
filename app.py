import pandas as pd
from flask import Flask, render_template, abort

app = Flask(__name__)

DATA_PATH = "data/apartments.csv"


@app.route("/")
def home():
    df = pd.read_csv(DATA_PATH)
    df = df.reset_index().rename(columns={"index": "id"})
    listings = df.to_dict(orient="records")
    return render_template("index.html", city="Tirana", listings=listings)


@app.route("/listing/<int:listing_id>")
def listing_detail(listing_id):
    df = pd.read_csv(DATA_PATH)

    if listing_id < 0 or listing_id >= len(df):
        abort(404)

    listing = df.iloc[listing_id].to_dict()
    listing["id"] = listing_id
    return render_template("listing.html", city="Tirana", listing=listing)


if __name__ == "__main__":
    app.run(debug=True)