#!/usr/bin/env python3
"""BAsic Flask App"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home() -> str:
    """Renders the main page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    """Runs the program if its not imported"""
    app.run(debug=True)
