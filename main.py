from flask import Flask, request, jsonify, render_template
import requests # needed to connect to external apis

app = Flask(__name__)

base_url = "https://api.mercedes-benz.com/configurator/v2"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)