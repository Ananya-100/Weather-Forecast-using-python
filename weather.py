import requests
import os
from datetime import datetime
user_api = os.environ["weather_data"]
location = input("enter city name : ")
weatherapi_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(weatherapi_link)
api_data = api_link.json()

if api_data['cod']=='404':
    print("Invalid city:{},please check your city name".format(location))
else:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y| %I:%M:%S:%p")
    print("------------------------------------------------------------------------------------")
    print("weather Stats for -{} || {}".format(location.upper(), date_time))
    print("------------------------------------------------------------------------------------")
    print("current temperature is : {:.2f} deg C".format(temp_city))
    print("Weather description : ", weather_desc)
    print("Wind speed : ", wind_spd, "kmph")
    print("humidity : ", hmdt, "%")
