import datetime
import requests
import os

APP_ID = os.environ.get("APP_ID", "APP_ID environment variable not found")
API_KEY = os.environ.get("API_KEY", "API_KEY environment variable not found")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN", "SHEET_TOKEN environment variable not found")

now = datetime.datetime.now()
current_time_12hr = now.strftime("%I:%M %p")
current_date = now.strftime("%d/%m/%Y")


def text_to_json():
    headers = {
        "Content-Type": "application/json",
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    param = {
        "query": input(f"Tell Me which exercises you did: "),
        "weight_kg": "61",
        "height_cm": "164.592",
        "age": "24",
    }
    # print(headers)

    res = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=param)
    res.raise_for_status()
    data = res.json()["exercises"]
    return data


def update_sheet():
    exersice_data = text_to_json()
    headers = {"Authorization": SHEET_TOKEN}
    for exersice in exersice_data:
        body = {
            "workout": {
                'date': current_date,
                'time': current_time_12hr,
                'exercise': exersice['user_input'],
                'duration': f"{exersice['duration_min']}min",
                'calories': exersice['nf_calories'],
            }
        }
        res = requests.post("https://api.sheety.co/134ec5674b7bd7440096f4dc6db1ffe8/myWorkouts/workouts", json=body,
                            headers=headers)
        res.raise_for_status()
        print(res.json())


if __name__ == "__main__":
    update_sheet()
