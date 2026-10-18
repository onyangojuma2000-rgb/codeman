import os
import requests

api_key = os.getenv("RESTCOUNTRIES_API_KEY")
headers = {"Authorization": api_key} if api_key else {}
url = "https://api.restcountries.com/countries/v5?q=Kenya"
response = requests.get(url, headers=headers, timeout=15)

if response.status_code == 200:
    data = response.json()
    if isinstance(data, list) and data:
        country = data[0]
        name = country["name"]["common"]
        capital = country["capital"][0]
        population = country["population"]
        currency = list(country["currencies"].keys())[0]

        print("Country:", name)
        print("Capital:", capital)
        print("Population:", population)
        print("Currency:", currency)
    else:
        print("Unexpected response format:")
        print(data)
else:
    print(f"Request failed. Status:", response.status_code)
    print(response.text)
