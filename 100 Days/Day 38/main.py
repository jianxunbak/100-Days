import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

GENDER = "male"
WEIGHT = 84
HEIGHT = 188
AGE = 36

SHEETY_POST_API = os.environ["SHEETY_POST_API"]
SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_HEADER = {
    "Authorization": SHEETY_KEY
}
NUTRI_KEY = os.environ["NUTRI_KEY"]
NUTRI_ID = os.environ["NUTRI_ID"]
NUTRI_API = os.environ["NUTRI_API"]
USER_INPUT = input("What exercise did you do?:\n")
HEADER = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
}

DATA = {
    "query": USER_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

nutri_response = requests.post(NUTRI_API, headers=HEADER, json=DATA)
data = nutri_response.json()

for items in data["exercises"]:
    workout_data = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": items["name"].title(),
            "duration": items["duration_min"],
            "calories": items["nf_calories"]
        }
    }
    sheety_response = requests.post(SHEETY_POST_API, json=workout_data, headers=SHEETY_HEADER)
    print(sheety_response.text)
    print(sheety_response.status_code)
