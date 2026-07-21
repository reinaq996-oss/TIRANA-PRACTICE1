import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

DATA_PATH = "data/apartments.csv"


@app.route("/")
def home():
    df = pd.read_csv(DATA_PATH)
    listings = df.to_dict(orient="records")
    return render_template("index.html", city="Tirana", listings=listings)


if __name__ == "__main__":
    app.run(debug=True)