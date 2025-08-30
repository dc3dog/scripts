import requests

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=a62ed952d08dc1f709b6cc3430194a57")

        except:
            print("No internet access :(")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.humidity = self.response_json["main"]["humidity"]
        self.feels_like = self.response_json["main"]["feels_like"]
#        self.dew_point = self.response_json["main"]["dew_point"]
#        self.temp_min = self.response_json["main"]["temp_min"]
#        self.temp_max = self.response_json["main"]["temp_max"]
#        self.wind_speed = self.response_json["main"]["wind_speed"]
#        self.wind_gust = self.response_json["main"]["wind_gust"]

    def temp_print(self):
        units_symbol = "F"
        if self.units == "metric":
            units_symbol = "C"
        print(f"In {self.name} it is currently {self.temp}° {units_symbol}")
        print(f"Humidity: {self.humidity}%")
        print(f"It feels like {self.feels_like}° {units_symbol}")
#        print(f"Dew Point: {self.dew_point}° {units_symbol}")
#        print(f"Today's High: {self.temp_max}° {units_symbol}")
#        print(f"Today's Low: {self.temp_min}° {units_symbol}")
#        print(f"Wind speed: {self.wind_speed}")
#        print(f"Gusting to: {self.wind_gust}")

my_city = City("Cincinnati", 39.162, -84.4569)
my_city.temp_print()

other_city1 = City("Lexington", 37.98869, -84.47772, units="imperial")
other_city1.temp_print()
#print(other_city1.response_json)

other_city2 = City("Indianapolis", 39.76838, -86.15804, units="imperial")
other_city2.temp_print()
#print(other_city2.response_json)