from flask import Flask, request, jsonify, render_template
import requests # needed to connect to external apis
from dotenv import load_dotenv
import os


app = Flask(__name__)

# loads api key
load_dotenv()
api_key = os.getenv("MERCEDES_API_KEY")

base_url = "https://api.mercedes-benz.com/configurator/v2/markets/us_US/models"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)