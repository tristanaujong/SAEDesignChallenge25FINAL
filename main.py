from flask import Flask, request, render_template
import requests # needed to connect to external apis
from dotenv import load_dotenv
import os


app = Flask(__name__)

# loads api key
load_dotenv()
api_key = os.getenv("MERCEDES_API_KEY")

# base api url
base_url = "https://api.mercedes-benz.com/configurator/v2/markets/en_DE"
# headers to attach to api for auth
headers = {
    "accept": "application/json",
    "x-api-key": api_key
}


@app.route("/")
def get_class_info():

    # url to call api for car classes
    url = f"{base_url}/classes"

    # reponse from api
    response = requests.get(url, headers=headers)
    
    # if response is good, append json to class_data and classes
    if response.status_code == 200:
        class_data = response.json()
        classes = class_data

    else:
        classes = []

    return render_template("index.html", classes=classes)

@app.route("/models")
def get_model_info():

    # url to call api for car classes
    url = f"{base_url}/classes"
    response = requests.get(url, headers=headers)

    # get form submission answer from html
    curr_class = request.args.get("classId")

    # url to call api for car models
    model_url = f"{base_url}/models?classId={curr_class}"
    model_response = requests.get(model_url, headers=headers)

    # populate data if response is good
    if model_response.status_code == 200:
        model_data = model_response.json()
        models = model_data
    else:
        models = []

    if response.status_code == 200:
        class_data = response.json()
        classes = class_data
    else:
        classes = []

    return render_template("index.html", models=models, classes=classes)

@app.route("/models/<model_id>/configurations/initial")
def show_model(model_id):

    # url to call api for car classes
    url = f"{base_url}/classes"
    response = requests.get(url, headers=headers)

    # get form submission answer from html
    curr_class = request.args.get("classId")

    model_url = f"{base_url}/models?classId={curr_class}"
    model_response = requests.get(model_url, headers=headers)

    # populate data if response is good
    if model_response.status_code == 200:
        model_data = model_response.json()
        models = model_data

    else:
        models = []

    if response.status_code == 200:
        class_data = response.json()
        classes = class_data

    else:
        classes = []

    # get current model image
    # model_id = request.args.get("modelId")
    # curr_model_url = f"{base_url}/models/{model_id}/configurations/initial"

    # test url for model picture
    curr_model_url = "https://api.mercedes-benz.com/configurator/v2/markets/de_DE/models/2239791/configurations/AJ-055_AU-511_GC-421_LE-L_LU-197_MJ-805_PC-P07-P09-P20-P21-P34-P47-P64-PBG_PS-953%23_SA-01U-02B-14U-16U-17U-223-233-235-243-249-266-275-276-282-292-297-302-321-325-32U-33U-351-355-365-367-382-401-402-413-432-438-439-447-452-453-475-489-49U-501-513-524-534-537-540-543-546-561-562-581-582-587-596-61U-628-642-679-70B-726-727-72B-735-79B-810-840-854-868-871-874-881-883-889-88B-891-896-897-898-8U0-902-903-916-927-942-969-986-B05-H29-K32-K33-K34-L2B-R01-R39-U01-U10-U14-U19-U25-U35-U58-U60_SC-0K4-0S3-0U1-1B3-2S0-2U8-3S6-3V2-4S7-502-51B-5X5-6P5-7B4-7S8-8P3-8S8-8U1-8U8-998-B10-K15-K27-K37-K40-K41-K46-LS0-R7K/images/vehicle"
    curr_car_response = requests.get(curr_model_url, headers=headers)

    if curr_car_response.status_code == 200:
        curr_car_data = curr_car_response.json()
        curr_car = curr_car_data
    else:
        curr_car = []
    
    return render_template("index.html", models=models, classes=classes, curr_car=curr_car)
if __name__ == "__main__":
    app.run(debug=True)