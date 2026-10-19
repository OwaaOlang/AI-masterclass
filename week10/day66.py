


def service_offer(skill, price, delivery):
        return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"

print(service_offer("Python Automation", 15000,3))
print(service_offer("Data Report", 8000, 2))
import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

if response.status_code==200:
    data = response.json()
    country = data[0]

    name =country["name"]["common"]
    capital= country["capital"][0]
    population = country["population"]
    currency = list(country["currencies"].keys())[0]

    print(f"Country: {country}")
    print(f"Capital: {capital}")
    print(f"population: {population}")
    print(f"Currency: {currency}")
else:
    print("status failed.status:", response.status_code)