import requests

response = requests.get(
    'https://api.restcountries.com/countries/v5?memberships.g7=1',
    headers={'Authorization': 'Bearer rc_live_373575f97ad64d3cabf4a116daa0cc8d'}
)

data = response.json()
if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
print(type(data))

p
