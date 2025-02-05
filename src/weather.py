import asyncio
import requests
import json

from data.token import api_token

city = 'moscow'
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + city + '?'

params = {
    'unitGroup': 'metric',
    'key': api_token,
    'contentType': 'json',
    'include': 'current',
}

# TODO: Добавить функцию смены города

async def get_today_weather() -> dict:
    print("="*30)
    response = requests.get(url=url, params=params)
    print('Get data')

    if (response.status_code != 200):
        print('Error. Code is ' + response.status_code)
        return None

    weather_data_buf = response.json()['days'][0]
    weather_data_cur = {}
    weather_data_cur['tempmax'] = weather_data_buf['tempmax']
    weather_data_cur['tempmin'] = weather_data_buf['tempmin']
    weather_data_cur['precipprob'] = weather_data_buf['precipprob']
    weather_data_cur['preciptype'] = weather_data_buf['preciptype']
    weather_data_cur['snow'] = weather_data_buf['snow']
    weather_data_cur['snowdepth'] = weather_data_buf['snowdepth']
    weather_data_cur['windgust'] = weather_data_buf['windgust']
    weather_data_cur['windspeed'] = weather_data_buf['windspeed']
    weather_data_cur['pressure'] = weather_data_buf['pressure']
    weather_data_cur['cloudcover'] = weather_data_buf['cloudcover']
    weather_data_cur['uvindex'] = weather_data_buf['uvindex']
    weather_data_cur['conditions'] = weather_data_buf['conditions']
    weather_data_cur['description'] = weather_data_buf['description']

    print("="*30)
    print(weather_data_cur)
    return weather_data_cur





# {
#  "days": [
#   {
#    "tempmax": 19.2,
#    "tempmin": 14.6,
#    "precipprob": 100,
#    "preciptype": [
#     "rain"
#    ],
#    "snow": 0,
#    "snowdepth": 0,
#    "windgust": 42.5,
#    "windspeed": 18.7,
#    "pressure": 1011.6,
#    "cloudcover": 98.6,
#    "uvindex": 4,
#    "conditions": "Rain, Overcast",
#    "description": "Cloudy skies throughout the day with rain.",
#   }
#  ],
#  "currentConditions": {
#   "temp": 15.7,
#   "precipprob": 0,
#   "snow": 0,
#   "snowdepth": 0,
#   "preciptype": null,
#   "windgust": null,
#   "windspeed": 18.8,
#   "pressure": 1015.8,
#   "cloudcover": 91.8,
#   "uvindex": 0,
#   "conditions": "Overcast",
#  }
# }