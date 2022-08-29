# Weather App
# Get Your Free API : http://openweathermap.org/appid
# API docs: https://openweathermap.org/api
# pip3 install requests
# pip3 install beautifulsoup4?
# Weather in St. Petersburg https://openweathermap.org/city/498817
import requests as req
import api_keys  # define API key in api_keys.py - api_keys.API_KEY_OPENWEATHER


def get_weather(loc):
    # Set API
    api_url = "https://api.openweathermap.org/data/2.5/weather?"
    params = f"q={loc}&appid={api_keys.API_KEY_OPENWEATHER}"  # insert your API key here

    # Get the response from the API
    url = api_url + params
    response = req.get(url)
    # TODO: check response before continuing

    weather = response.json()

    # Fetch Weather
    print(f"Weather for {loc}:")
    temp = weather['main']['temp']
    print("Temperature:", "{:.1f}".format(temp - 273.15), "Celsius")
    humidity = weather['main']['humidity']
    print("Humidity:", humidity, "%")
    wind = weather['wind']['speed']
    print("Wind speed:", wind, "m/s")


# main
get_weather('St. Petersburg')
