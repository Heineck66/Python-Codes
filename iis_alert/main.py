import requests
import datetime as td
import smtplib
import os
import time

MY_LAT = -23.550520
MY_LONG = -46.633308

iis_pos = (0, 0)

#  Get IIS position  #
def is_iis_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iis_longitude = float(data["iss_position"]["longitude"])
    iis_latitude = float(data["iss_position"]["latitude"])
    global iis_pos
    iis_pos = (iis_latitude, iis_longitude)

    print(iis_latitude, " ", iis_longitude)
    print(MY_LAT, " ", MY_LONG)
    print(f"proximity: {MY_LAT + 5 > iis_latitude > MY_LAT -5} : {MY_LONG + 5 > iis_longitude > MY_LONG -5}")

    return True if MY_LAT + 5 > iis_latitude > -5 and MY_LONG + 5 > iis_longitude > MY_LONG - 5 else False


#  Get my position and day light time #
def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()["results"]
    sunrise_hour = data["sunrise"].split("T")[1].split(":")[0]
    # sunset_hour = data['sunset'].split("T")[1].split(':')[0]
    sunset_hour = 18

    time_now = td.datetime.now().hour

    print("Is dark: ", time_now >= int(sunset_hour))
    return True if time_now >= int(sunset_hour) or time_now <= int(sunrise_hour) else False


user = "[EMAIL]"
password = os.getenv("email_key")

# compare my pos with iis pos
while True:
    print("Checking...\n")
    if is_iis_overhead() and is_dark():
        print("look up!")

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(
                from_addr=user,
                to_addrs="regith@pm.me",
                msg=f'Subject:ISS Alert\n\n Look up!\nyour pos{MY_LAT, " - " ,MY_LONG} \nIIS pos: {iis_pos}',
            )
    else:
        print("Nothing for now.\n")
    time.sleep(120)
