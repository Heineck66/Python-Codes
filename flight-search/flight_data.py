class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
        self,
        price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        departure_date,
        arrivel_date,
        airlines,
        routes_raw,
        connections_count,
    ) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.arrivel_date = arrivel_date
        self.airlines = airlines
        self.connections_count = connections_count
        routes = []
        for route in routes_raw:
            routes.append([route["cityFrom"], route["cityTo"]])
        self.routes = routes
