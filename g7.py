import os
import requests

api_key = os.getenv("RESTCOUNTRIES_API_KEY")
headers = {"Authorization": api_key} if api_key else {}
url = "https://api.restcountries.com/countries/v5?memberships.g7=1"
response = requests.get(url, headers=headers, timeout=15)

if response.status_code == 200:
    data = response.json()
    if isinstance(data, list):
        countries = [country["name"]["common"] for country in data if "name" in country and "common" in country["name"]]
        print(f"Found {len(countries)} G7 countries.")
        for name in countries:
            print(name)
    else:
        print("Unexpected response format:")
        print(data)
else:
    print("Request failed. Status code:", response.status_code)
    print(response.text)
