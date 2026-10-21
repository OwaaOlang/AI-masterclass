import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWSAPI_KEY")
url = f"https://newsapi.org/v2/everything?q=AI&apiKey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Success! Found {data['totalResults']} articles")
    for article in data['articles'][:3]:
        print(f"- {article['title']}")
elif response.status_code == 401:
    print("401 Error - Invalid API Key")
elif response.status_code == 429:
    print("429 Error - Too many requests")
else:
    print(f"Error {response.status_code}: {response.text}")