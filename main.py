import requests

import datetime
today = datetime.datetime.now()
date_tod = today.strftime("%d/%m/%Y")
time_now = today.strftime("%X")
APP_id = "b2c5180a"
API_key = "8ad7d9ed6e3c325dde6ba705e01c412a"
headers = {
    "x-app-id": APP_id,
    "x-app-key": API_key,
    "Content-Type": "application/json"
}
query = input("What workouts did you do today?")
passing_details = {
     "query": f"{query}",
     "gender": "female",
     "weight_kg": 64,
     "height_cm": 163,
     "age": 23
}
response_nutri = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=passing_details)
print(response_nutri.text)
exercise_list = response_nutri.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/2aa6397ad00a979d8de863ad6fefe1cd/workoutsList/sheet1"
sheety_headers = {
    "Authorization": "Bearer secrettoken",
}

for exercise in exercise_list:
    duration_min = exercise["duration_min"]
    print(duration_min)
    sheet_inputs= {

    "sheet1" : {
        "date": date_tod,
        "time": time_now,
        "exercise": exercise["user_input"].title(),
        "duration": str(duration_min),
        "calories": exercise["nf_calories"],
    }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheety_response.text)

