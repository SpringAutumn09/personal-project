import DataCleaner as DataCleaner
import requests

STATE_CITY_DIR = 'ListOfStatesAndCities.txt'
STATE_CODE_DIR = 'StateCodes.txt'
WEATHER_API = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={apikey}"
GEOCODING_API = "http://api.openweathermap.org/geo/1.0/direct?q={cityname},{statecode},{countrycode}&limit={limit}&appid={apikey}"

 
cityandstatecodes = DataCleaner.StatecodeAndCity()

def FahrenheitToCelsius(f):
    c = (f)*5/9 -32

def round_float(num, decimals=0):
    # Shift the decimal point to the right
    multiplier = 10 ** decimals
    
    # Multiply the number by the multiplier, round it to the nearest integer, and then shift the decimal back
    rounded = int(num * multiplier + 0.5) if num > 0 else int(num * multiplier - 0.5)
    
    # Divide back to get the rounded value
    return rounded / multiplier

def getcityandstate():
    statecode = ''
    while True:
        cityname = input("Enter a city name: ").lower()
        if cityname.isdigit():
            print("Invalid input for city name")
            continue
        else:
            break
    for keyword, values in cityandstatecodes.items():
        for value in values:
            if cityname == value.lower():
                statecode = keyword
                break
    
    return cityname, statecode

def getgeocode(cityname, statecode, apikey):
    response = requests.get(GEOCODING_API.format(cityname= cityname, statecode= statecode, countrycode= "", limit= 5, apikey= apikey))
    data = response.json()
    if data == []:
        print("Invalid cityname entry.")
    else:
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon, response


def WeatherData(lat, lon, apikey):
    pass

