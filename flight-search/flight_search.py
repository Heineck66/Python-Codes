import requests
import pprint
from flight_data import FlightData
from datetime import datetime
import json

from pprint import pprint

TEQUILA_API_KEY = "[API_KEY]"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"

DEFAULT_CITY = "GRU"
CURRENCY = "BRL"

HEADERS = {"apikey": TEQUILA_API_KEY}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        module = "locations/query"

        params = {
            "term": city,
            "location_types": "city",
        }

        request = requests.get(f"{TEQUILA_ENDPOINT}{module}", params=params, headers=HEADERS)
        request.raise_for_status()
        result = request.json()["locations"]
        code = result[0]["code"]

        return code

    def get_flights(self, destination_city_code, from_time, to_time, passager_number, result_limit) -> FlightData:
        module = "search"

        params = {
            "fly_from": DEFAULT_CITY,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "curr": CURRENCY,
            "adults": passager_number,
            "limit": result_limit,
        }

        response = requests.get(f"{TEQUILA_ENDPOINT}{module}", params=params, headers=HEADERS)
        response.raise_for_status()

        try:
            data = response.json()["data"]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        # with open("result.json", "w") as file:
        #     json.dump(data, file)

        flights = []

        for flight in data:
            connections = len(flight["route"])
            price = flight["price"]
            if connections <= 4 and price < 130000:
                flight_data = FlightData(
                    price=price,
                    origin_airport=flight["flyFrom"],
                    origin_city=flight["cityFrom"],
                    destination_city=flight["flyTo"],
                    destination_airport=flight["cityTo"],
                    departure_date=datetime.utcfromtimestamp(flight["dTimeUTC"]),
                    arrivel_date=datetime.utcfromtimestamp(flight["aTimeUTC"]),
                    airlines=flight["airlines"],
                    connections_count=len(flight["route"]),
                    routes_raw=flight["route"],
                )
                flights.append(flight_data)

        return flights
