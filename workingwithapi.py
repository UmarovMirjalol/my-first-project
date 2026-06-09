import requests 

def getweather(lat , lon):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    current_weather = data.get('current_weather', {})
    temperature = current_weather.get('temperature')
    return temperature

tashkent = getweather(41.2995, 69.2401)
print(f"Current temperature in Tashkent: {tashkent}°C")


paris = getweather(48.8566, 2.3522)
print(f"Current temperature in Paris: {paris}°C")

city = input("Press Enter your city: " \
      "and get the current temperature: ")

if city.lower() == "tashkent":
    print(f"Current temperature in Tashkent: {tashkent}°C")

elif city.lower() == "paris":
    print(f"Current temperature in Paris: {paris}°C")

else:    print("Sorry, we don't have data for that city.") 
