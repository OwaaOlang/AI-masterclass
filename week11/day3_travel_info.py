import os
import requests
from dotenv import load_dotenv, find_dotenv

# One .env in Ai masterclass folder
load_dotenv(find_dotenv())

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("API key not found! Check .env")
        return None
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=15)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"Weather error: {r.status_code}")
        return None

def get_air_pollution(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        return r.json()['list'][0]['main']['aqi']
    return None

def get_forecast(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        return r.json()
    return None

def get_country_info(country_code):
    try:
        url = f"https://api.worldbank.org/v2/country/{country_code}?format=json"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

def main():
    print("Travel Weather Tool")
    city = input("Enter city: ").strip()
    if not city:
        return

    weather = get_weather(city)
    if not weather:
        print("Could not get weather")
        return

    print(f"\n--- {weather['name']}, {weather['sys']['country']} ---")
    print(f"Temperature : {weather['main']['temp']}C")
    print(f"Condition : {weather['weather'][0]['description']}")
    print(f"Humidity : {weather['main']['humidity']}%")
    print(f"Wind : {weather['wind']['speed']} m/s")

    lat = weather['coord']['lat']
    lon = weather['coord']['lon']

    # Air Quality
    aqi = get_air_pollution(lat, lon)
    levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
    if aqi:
        print(f"Air Quality : {aqi}/5 ({levels.get(aqi)})")
        if aqi >= 4:
            print("⚠️ Air is alarming - wear mask if in Dakar / Beijing")
    else:
        print("Air Quality : unavailable")

    # 5-Day Forecast
    forecast = get_forecast(lat, lon)
    if forecast:
        print("\n--- 5-Day Forecast ---")
        for i in range(0, 40, 8): # 8 x 3h = 24h
            item = forecast['list'][i]
            date = item['dt_txt'].split(' ')[0]
            temp = item['main']['temp']
            desc = item['weather'][0]['description']
            print(f"{date} : {temp}C, {desc}")

    # Country info
    info = get_country_info(weather['sys']['country'])
    if not info:
        print("\nCountry info: API blocked, but weather works")

if __name__ == "__main__":
    main()
