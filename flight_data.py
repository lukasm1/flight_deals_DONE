import requests


class FlightData():
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.KIWI_LOCATION_END = "https://tequila-api.kiwi.com/locations/query"
        self.API_KEY = "XX"
        #   self.stop_overs=kw["stop_overs"]=0
        #   self.via_city=kw["via_city"]=""
        self.headers = {
            "apikey": self.API_KEY,
        }
        self.iata_list = []
        self.number_of_results = 0

    def get_iata_codes(self, cities_list):
        for city in cities_list:
            self.kiwi_params = {
                "term": city
            }
            self.response = requests.get(url=self.KIWI_LOCATION_END, params=self.kiwi_params, headers=self.headers)
            self.iata_list.append(self.response.json()["locations"][0]["code"])

    def formate_search_results(self, json_result_object):
        self.number_of_results = json_result_object["_results"]
        if self.number_of_results > 0:
            number_of_routes = len(json_result_object["data"][0]["route"])
            departure_airport_iata = json_result_object["data"][0]["flyFrom"]
            destination_airport_iata = json_result_object["data"][0]["flyTo"]
            departure_city = json_result_object["data"][0]["cityFrom"]
            destination_city = json_result_object["data"][0]["cityTo"]
            flight_price = json_result_object["data"][0]["price"]
            flight_date_from = json_result_object["data"][0]["route"][0]["local_departure"].split("T")[0]
            flight_date_to = json_result_object["data"][0]["route"][1]["local_arrival"].split("T")[0]
            self.sms_text = f"Low price alert! Only £{flight_price} to fly from " \
                            f"{departure_city}-{departure_airport_iata} to {destination_city}-{destination_airport_iata}, " \
                            f"from {flight_date_from} to {flight_date_to}."
            self.url_text = f"https://www.google.co.uk/flight?hl=en#flt={departure_airport_iata}.{destination_airport_iata}.{flight_date_from}*" \
                            f"{destination_airport_iata}.{departure_airport_iata}.{flight_date_to}"
            if number_of_routes > 2:
                potential_via_city1 = json_result_object["data"][0]["route"][1]["cityFrom"]
                potential_via_city2 = json_result_object["data"][0]["route"][1]["cityTo"]
                if potential_via_city1 != departure_city and potential_via_city1 != destination_city:
                    via_city = potential_via_city1
                else:
                    via_city = potential_via_city2
                stop_overs = 1
                self.sms_text += f"\nFlight has {stop_overs} stop over, via {via_city}."
