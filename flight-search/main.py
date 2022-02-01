# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
import datetime

f_search = FlightSearch()

# get flight info with sheet info
code = "MVD"

print(f"Looking for flights to {code}...")
flights = f_search.get_flights(
    destination_city_code=code,
    from_time=datetime.date(2022, 3, 1),
    to_time=datetime.date(2022, 3, 7),
    passager_number=1,
    result_limit=5,
)

with open("result.txt", "a", encoding="utf-8") as file:

    for flight in flights:
        message = (
            f"\n{code}:\nflight to {flight.destination_city}/{flight.destination_airport}\n\n"
            + f"from {flight.origin_city}/{flight.origin_airport} R${flight.price}\n"
            + f"Departure {flight.departure_date}\nArrival {flight.arrivel_date}\n\n"
            + f"Airlines: {flight.airlines}\n"
            + f"Conections: {flight.routes}\n"
        )

        print(message)
        file.write(message)
