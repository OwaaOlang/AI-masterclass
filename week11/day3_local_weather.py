import os
import requests
from dotenv import load_dotenv
from collections import defaultdict
from datetime import datetime

load_dotenv()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=15)
    return r.json() if r.status_code == 200 else None

def get_forecast(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    r = requests.get(url, timeout=15)
    return r.json() if r.status_code == 200 else None

def get_country_info(code):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        url = f"https://api.worldbank.org/v2/country/{code}?format=json"
        r = requests.get(url, headers=headers, timeout=15)
        j = r.json()
        if len(j) > 1 and j[1]:
            info = j[1][0]
            currency_map = {"UG":"UGX","KE":"KES","TZ":"TZS","RW":"RWF","US":"USD","GB":"GBP","NG":"NGN","ZA":"ZAR"}
            return {
                "region": info.get("region",{}).get("value"),
                "capital": info.get("capitalCity"),
                "currency": currency_map.get(code, "N/A")
            }
    except: pass
    return None

def run_tool():
    city = input("Enter city/district (e.g. Kampala, Gulu, Mbarara): ").strip() or "Kampala"
    
    weather = get_weather(city)
    if not weather:
        print(f"Could not find '{city}' - try district name like Gulu")
        return

    country_code = weather["sys"]["country"]
    country = get_country_info(country_code)
    forecast = get_forecast(city)

    print(f"\n=== CURRENT: {city.title()}, {country_code} ===")
    print(f"Temperature : {weather['main']['temp']}C (feels like {weather['main']['feels_like']}C)")
    print(f"Condition : {weather['weather'][0]['description'].title()}")
    print(f"Humidity : {weather['main']['humidity']}%")
    print(f"Wind : {weather['wind']['speed']} m/s")

    if country:
        print(f"\n=== Country Info ===")
        print(f"Region : {country['region']}")
        print(f"Capital : {country['capital']}")
        print(f"Currency: {country['currency']}")

    if forecast:
        print(f"\n=== 5-DAY PREDICTION for {city.title()} ===")
        daily = defaultdict(list)
        for item in forecast["list"]:
            day = datetime.fromtimestamp(item["dt"]).strftime("%a %d %b")
            daily[day].append(item)

        for day, items in list(daily.items())[:5]:
            temps = [i["main"]["temp"] for i in items]
            cond = items[len(items)//2]["weather"][0]["description"].title()
            print(f"{day}: {min(temps):.0f}C - {max(temps):.0f}C | {cond}")

run_tool()
