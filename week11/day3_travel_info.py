import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city, country_code="South Sudan"):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=15)
    if r.status_code == 200:
        return r.json()
    return None

def get_country_info(country_code):
    headers = {"User-Agent": "Mozilla/5.0"}
    code = country_code.strip().upper()

    urls = [
        f"https://restcountries.com/v3.1/alpha/{code}",
        f"https://api.allorigins.win/raw?url=https://restcountries.com/v3.1/alpha/{code}",
    ]

    for url in urls:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code != 200:
                continue
            data = r.json()

            # FIX FOR YOUR ERROR - this is what I missed
            if isinstance(data, list):
                if len(data) > 0:
                    return data[0]
            elif isinstance(data, dict):
                # dict means it already IS the country (from proxy) or error
                if "region" in data or "population" in data:
                    return data
        except Exception:
            continue
    return None

def run_tool():
    print("Travel weather Tool")
    city = input("Enter city: ").strip() or "Kampala"

    weather_data = get_weather(city)
    if not weather_data:
        print(f"Could not find '{city}'")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}C")
    print(f"Condition : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity : {weather_data['main']['humidity']}%")
    print(f"Wind : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown")
        currencies = ", ".join(country_data.get("currencies", {}).keys())

        print(f"\n=== Country Info ===")
        print(f"Region : {region}")
        print(f"Population : {population:,}")
        print(f"Currency : {currencies if currencies else 'N/A'}")
    else:
        print("\nCountry info: API blocked, but weather works")

run_tool()