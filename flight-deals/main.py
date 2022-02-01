# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

data_mang = DataManager()
f_search = FlightSearch()
sms_sender = NotificationManager()

# get data from the sheet
data_mang.update_code()
sheet_data = data_mang.get_sheet_data()

# get date
from_date = datetime.date.today()
to_date = from_date + datetime.timedelta(days=30)

# get flight info with sheet info
for city in sheet_data:
    code = city["iataCode"]
    dest = f_search.get_flights(code, datetime.date(2021, 12, 1), datetime.date(2022, 1, 15))
    code = city["iataCode"]
    print(f"{code}: R${dest.price} {dest.departure_date} {dest.arrivel_date}")

    # Check if prices from flight info match or lower than "Lowest price"
    if city["lowestPrice"] >= dest.price:
        print("\nGood Deal!\n")
        # if match send sms to number
        message = (
            f"Good deal!\n flight to {dest.destination_city}/{dest.destination_airport}\n "
            + f"from {dest.origin_city}/{dest.origin_airport} only R${dest.price}"
            + f"Departure {dest.departure_date} Arrival {dest.arrivel_date}"
        )
        sms_sender.send_sms(message)
