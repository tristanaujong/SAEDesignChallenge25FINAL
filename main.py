from flask import Flask, request, jsonify, render_template
import requests # needed to connect to external apis
from dotenv import load_dotenv
import os


app = Flask(__name__)

# loads api key
load_dotenv()
api_key = os.getenv("MERCEDES_API_KEY")

# base api url
base_url = "https://api.mercedes-benz.com/configurator/v2/markets/en_DE/classes"

@app.route("/")
def get_model_info():
    
    # headers to attach to api for auth
    headers = {
        "accept": "application/json",
        "x-api-key": api_key
    }

    url = base_url
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        model_data = response.json()
        models = model_data

    else:
        models = []

    return render_template("index.html", models=models)

if __name__ == "__main__":
    app.run(debug=True)