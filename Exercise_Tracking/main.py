import json
import ast
import requests
from datetime import datetime

APP_ID = "b00a340d"
APP_KEY = "9d94274396f3373a053cfa5033d61892"
NU_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END_POINT = "https://api.sheety.co/6db2eccc66b7d0928f25fb3daed946ee/workouts/workouts"

NU_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

activities = input("Tell me which exercises you did: ").title()

body = {
    "query": activities
}

NU_response = requests.post(url=NU_END_POINT, data=json.dumps(body), headers=NU_header)

data = NU_response.json()

# Extracting specific information using list comprehension
exercises_info = [
    {
        'name': exercise['name'],
        'duration_min': exercise['duration_min'],
        'nf_calories': exercise['nf_calories']
    }
    for exercise in data.get('exercises', [])
]

TODAY = datetime.now()
date = TODAY.strftime("%Y/%m/%d")
time = TODAY.strftime("%H:%M:%S")

for each in exercises_info:
    updating_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise":each["name"],
            "duration":each["duration_min"],
            "calories":each["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_END_POINT, json=updating_parameters)

response = requests.get(url=SHEETY_END_POINT)
print(response.json())
