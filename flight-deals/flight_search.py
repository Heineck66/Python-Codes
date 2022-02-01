import requests
import pprint
from flight_data import FlightData
from datetime import datetime

# TEQUILA API KEY
TEQUILA_API_KEY = "[API_KEY]"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"

DEFAULT_CITY = "GRU"
CURRENCY = "BRL"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        module = "locations/query"

        headers = {"apikey": TEQUILA_API_KEY}
        params = {
            "term": city,
            "location_types": "city",
        }

        request = requests.get(f"{TEQUILA_ENDPOINT}{module}", params=params, headers=headers)
        request.raise_for_status()
        result = request.json()["locations"]
        code = result[0]["code"]
        # print(code)

        return code

    def get_flights(self, destination_city_code, from_time, to_time) -> FlightData:
        module = "search"

        headers = {"apikey": TEQUILA_API_KEY}

        params = {
            "fly_from": DEFAULT_CITY,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "flight_type": "oneway",
            "curr": CURRENCY,
            "adults": 2,
            "limit": 500,
        }

        response = requests.get(f"{TEQUILA_ENDPOINT}{module}", params=params, headers=headers)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            departure_date=datetime.utcfromtimestamp(data["route"][0]["dTimeUTC"]),
            arrivel_date=datetime.utcfromtimestamp(data["route"][0]["aTimeUTC"]),
        )

        return flight_data
