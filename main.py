# important links:
# Sheet copy> https://docs.google.com/spreadsheets/d/1nRw6JCBe2pmFGtNL1oZImKbk4wa-eVjOR-Cgf8IDX1c/edit#gid=0
# Sheety> https://dashboard.sheety.co/
# Tequila Kiwi API> https://docs.google.com/spreadsheets/d/1nRw6JCBe2pmFGtNL1oZImKbk4wa-eVjOR-Cgf8IDX1c/edit#gid=0
# Twilio> https://www.twilio.com/docs/sms

from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_data = FlightData()
notification_manager = NotificationManager()
flight_search = FlightSearch()

# WORKS>
# data_manager.get_cities_list()
# print(data_manager.city_list)

# ALSO WORKS>
# data_manager.get_prices_list()
# print(data_manager.prices_list)

# BUT FOR SAVING REQUESTS PURPOSES I CREATED THESE 2 LISTS LIKE THIS>
# data_manager.city_list=['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town', 'Bali']
# data_manager.prices_list=[54, 42, 485, 551, 95, 414, 240, 260, 378, 501,]


flight_data.get_iata_codes(data_manager.city_list)

# DONE>
# data_manager.update_sheet_with_iata_codes(flight_data.iata_list)

# creates dict of city/price:
city_lowest_price_dict = dict(zip(flight_data.iata_list, data_manager.price_list))

flight_search.search_flights(city_lowest_price_dict)

# DONE>
# data_manager.get_emails()
# and FOR SAVING REQUESTS PURPOSES I CREATED another LIST LIKE THIS>
# data_manager.email_list = ['pycharmtester1@gmail.com']


for item in flight_search.search_result_list:

    flight_data.formate_search_results(item)
    if flight_data.number_of_results > 0:
        # saving credit so not sending sms here, just printing>
        # notification_manager.send_sms(flight_data.sms_text)
        print(flight_data.sms_text, flight_data.url_text)
        notification_manager.send_emails(data_manager.email_list, flight_data.sms_text, flight_data.url_text)











