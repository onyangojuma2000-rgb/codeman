import requests

response = requests.get(
    'https://api.restcountries.com/countries/v5?q=Kenya',
    headers={'Authorization': 'Bearer rc_live_373575f97ad64d3cabf4a116daa0cc8d'}
)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    currency = list(country["currencies"].keys())[0]

    print("Status code:", response.status_code)
    print("Response data:", data)
    print("Country:", name)
    print("Capital:", capital)
    print("Population:", population)
    print("Currency:", currency)
else:
    print("Request failed. Status code:", response.status_code)