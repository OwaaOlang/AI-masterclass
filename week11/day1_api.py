
import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    currency = list(country["currencies"].keys())[0]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)
          

import requests

# Lira, Uganda coordinates
url = "https://api.open-meteo.com/v1/forecast?latitude=2.2499&longitude=32.8998&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code&timezone=Africa/Kampala"

response = requests.get(url)
data = response.json()

current = data["current"]

print("--- Live Weather Report: Lira, Uganda ---")
print(f"Temperature: {current['temperature_2m']} °C")
print(f"Wind Speed: {current['wind_speed_10m']} km/h")
print(f"Humidity: {current['relative_humidity_2m']}%")
print(f"Time: {current['time']}")
print("-----------------------------------------")
