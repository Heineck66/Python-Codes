import requests
from datetime import datetime as dt

# ---- get user exercise input -----

user_input = input("What exercise you did today? ")


# ---- get exercise info in nutrix API

header = {
    "x-app-id": "[API_ID]",
    "x-app-key": "[APP_KEY]",
}

user_data = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30,
}

nutri_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_exercise = requests.post(nutri_url, user_data, headers=header)
print(request_exercise.status_code)
print(request_exercise.text)

result = request_exercise.json()

# ---- ADD info into google sheet using sheety API -----

sheet_url = "[SHEETY_URL]"

bearer_token = "[TOKEN]"

print("\n\n\n")

exe = result["exercises"][0]

print(exe)
print("\n\n\n")

date = dt.now().strftime("%d/%m/%Y")
time = dt.now().strftime("%X")
exercise = exe["name"].title()
duration = exe["duration_min"]
calories = exe["nf_calories"]

body_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

header = {
    "Autorization": bearer_token,
}

request_sheet = requests.post(sheet_url, json=body_data, headers=header)
print(request_sheet.status_code)
request_sheet.raise_for_status()
