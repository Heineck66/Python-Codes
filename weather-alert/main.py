import requests
import datetime as dt
import os


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "[API_KEY]"


MY_LAT = -23.56
MY_LON = -46.59


# MY_LAT = -21.39
# MY_LON = -42.53

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
    "units": "metric",
}

response = requests.get(OWM_endpoint, params=params, timeout=2)
response.raise_for_status()

print(response)
data = response.json()
hour_data = data["hourly"]

bring_umbrela = False

for hour in hour_data[:12]:
    weather_condition = hour["weather"][0]["id"]
    print(weather_condition)
    if weather_condition < 700:
        bring_umbrela = True


from twilio.rest import Client

# +5511989848422

bring_umbrela = True

if bring_umbrela:
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring your Umbrella",
        from_="[FROM_NUMBER]",
        to="[TO_NUMBER]",
    )

    print(message.status)
    print(message.price)
    print(message.body)

    print("Bring Umbrella. 😘")
