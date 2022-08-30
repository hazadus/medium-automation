# https://github.com/csparpa/pyowm
# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
#
# pip3 install pyowm
#
from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import api_keys


# ---------- FREE API KEY examples ---------------------
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM(api_keys.API_KEY_OPENWEATHER, config_dict)
mgr = owm.weather_manager()


# Search for current weather in St. Petersburg,RU and get details
observation = mgr.weather_at_place('St. Petersburg,RU')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

# Will it be clear tomorrow at this time in St. Petersburg,RU?
forecast = mgr.forecast_at_place('St. Petersburg,RU',
                                 '3h')  # '3h' because 'Daily' from GitHub examples is not supported with free API
answer = forecast.will_be_clear_at(timestamps.tomorrow())

# Get weather forecast for tomorrow, 06:00 (+00:00 GMT?)
weather = forecast.get_weather_at(timestamps.tomorrow(6, 0))
