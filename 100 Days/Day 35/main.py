import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
PARAMETER = {
    "lat": 1.352083,
    "lon": 103.819839,
    "cnt": 4,
    "appid": os.environ.get("appid"),
}

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

data = requests.get(OWM_ENDPOINT, params=PARAMETER)
data.raise_for_status()
weather_data = data.json()

will_rain = False
for item in weather_data["list"]:
    condition_code = int(item["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="bring umbrella, it wil rain today",
        from_="+19033547972",
        to="+6593622594"
    )

    print(message.status)
