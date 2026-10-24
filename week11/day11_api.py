import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 2.2499,
    "longitude": 32.8998,
    "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
    "timezone": "Africa/Kampala"
}

response = requests.get(url, params=params)
data = response.json()

# If error, print what API said
if "current" not in data:
    print("API returned:", data)
else:
    current = data["current"]
    print("--- Live Weather Report: Lira, Uganda ---")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Time: {current['time']}")
 