import requests
import os


API_KEY = os.environ.get("OWM_API_KEY");
# in terminal export OWM_API_KEY=<api_key>

param = {
    # "lat": "24.871941",
    # "lon": "66.988060",
    "lat": "18.706064",
    "lon": "98.981712",
    "appid": API_KEY,
    "cnt": 4
}

res = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=param)
weather_data = res.json()
weathers = weather_data["list"]

will_rain = False
for hour_data in weathers:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring your umbrella")
    # twilio APi Code here 👇🏼
