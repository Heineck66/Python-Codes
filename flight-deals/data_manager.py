from pprint import pprint
import requests
from flight_search import FlightSearch

SHEETY_ENDPOINT = "[SHEETY_ENDPOINT]"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheet_url = SHEETY_ENDPOINT

    def get_sheet_data(self) -> list:
        request = requests.get(self.sheet_url)
        request.raise_for_status()
        sheet_data = request.json()["prices"]

        return sheet_data

    def update_code(self):
        data = self.get_sheet_data()
        for index, city in enumerate(data):
            if city["iataCode"] == "":
                print("sheet code updated.")
                search = FlightSearch()
                body = {"price": {"iataCode": search.get_destination_code(city["city"])}}

                request_put = requests.put(url=(f"{self.sheet_url}/{index+2}"), json=body)
                request_put.raise_for_status()
