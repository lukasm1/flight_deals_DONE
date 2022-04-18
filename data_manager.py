# This class is responsible for talking to the Google Sheet.
import requests


class DataManager:
    def __init__(self):
        self.GET_SHEETS_API_PRICES = "https://api.sheety.co/76574eaca8ac30a2754a72ed27fe6a9c/flightDeals/prices"
        self.GET_SHEETS_API_USERS = "https://api.sheety.co/76574eaca8ac30a2754a72ed27fe6a9c/flightDeals/users"
        # this list is created for saving requests purposes>
        self.city_list = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco',
                          'Cape Town', 'Bali']
        self.price_list = [54, 42, 485, 551, 95, 414, 240, 260, 378, 501]
        self.email_list = ['pycharmtester1@gmail.com']

    # works but is not used for saving requests purposes>
    def get_cities_list(self):
        self.get_sheets_response = requests.get(url=self.GET_SHEETS_API_PRICES)
        sheet = self.get_sheets_response.json()["prices"]
        self.city_list = [sheet[_]["city"] for _ in range(len(sheet))]

    # works but is not used for saving requests purposes>
    def get_prices_list(self):
        self.get_sheets_response = requests.get(url=self.GET_SHEETS_API_PRICES)
        sheet = self.get_sheets_response.json()["prices"]
        self.price_list = [sheet[_]["price"] for _ in range(len(sheet))]

    def get_emails(self):
        self.get_sheets_response = requests.get(url=self.GET_SHEETS_API_USERS)
        sheet = self.get_sheets_response.json()["users"]
        self.email_list = [sheet[_]["email"] for _ in range(len(sheet))]

    # done>
    def update_sheet_with_iata_codes(self, iata_codes_list):
        index_of_iata_codes = 0
        self.IATA_LIST = iata_codes_list
        for number in range(2, 11):
            PUT_SHEETS_API = f"https://api.sheety.co/76574eaca8ac30a2754a72ed27fe6a9c/flightDeals/prices/{number}"
            put_params = {
                "price": {
                    "iata": self.IATA_LIST[index_of_iata_codes]
                }
            }
            self.put_sheets_response = requests.put(url=PUT_SHEETS_API, json=put_params)
            index_of_iata_codes += 1
