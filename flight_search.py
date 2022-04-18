import requests
from datetime import datetime, timedelta


class FlightSearch:
    def __init__(self):
        today = datetime.now()
        tomorrow = (today + timedelta(1)).strftime("%d/%m/%Y")
        half_year = (today + timedelta(181)).strftime("%d/%m/%Y")
        self.search_result_list = []
        self.search_result = ""
        self.KIWI_API_END = "https://tequila-api.kiwi.com/v2/search"
        self.API_KEY = "XX""
        self.AffilID = "lukasminsterflightsearch"
        self.FLY_FROM = "LON"
        self.CURR = "GBP"
        self.DATE_FROM = tomorrow
        self.DATE_TO = half_year
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.max_stopovers = 0
        self.headers = {
            "apikey": self.API_KEY,
        }

    def search_flights(self, cities_prices_dict):
        for (key, value) in cities_prices_dict.items():

            self.kiwi_params = {
                "fly_from": self.FLY_FROM,
                "fly_to": key,
                "date_from": self.DATE_FROM,
                "date_to": self.DATE_TO,
                "nights_in_dst_from": self.nights_in_dst_from,
                "nights_in_dst_to": self.nights_in_dst_to,
                "curr": self.CURR,
                "price_to": value - 1,
                "limit": 1,
                "max_stopovers": self.max_stopovers,
            }

            self.response = requests.get(url=self.KIWI_API_END, params=self.kiwi_params, headers=self.headers)
            results = self.response.json()["_results"]

            if results == 0:
                self.kiwi_params = {
                    "fly_from": self.FLY_FROM,
                    "fly_to": key,
                    "date_from": self.DATE_FROM,
                    "date_to": self.DATE_TO,
                    "nights_in_dst_from": self.nights_in_dst_from,
                    "nights_in_dst_to": self.nights_in_dst_to,
                    "curr": self.CURR,
                    "price_to": value - 1,
                    "limit": 1,
                    "max_stopovers": 1,  # this changed. can we put it behind params, somehow?? dime.
                }
                self.response = requests.get(url=self.KIWI_API_END, params=self.kiwi_params, headers=self.headers)

            self.search_result_list.append(self.response.json())
