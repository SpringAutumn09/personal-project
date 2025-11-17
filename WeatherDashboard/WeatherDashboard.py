import DataCleaner


STATE_CITY_DIR = 'ListOfStatesAndCities.txt'
STATE_CODE_DIR = 'StateCodes.txt'
WEATHER_API = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={apikey}"
GEOCODING_API = "http://api.openweathermap.org/geo/1.0/direct?q={cityname},{statecode},{countrycode}&limit={limit}&appid={apikey}"




statesandcity = DataCleaner.cleaningstateandcity(STATE_CITY_DIR)
statesandcodes = DataCleaner.cleaningstatecodes(STATE_CODE_DIR)

print(statesandcity)
print(statesandcodes)