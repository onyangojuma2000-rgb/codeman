import json

with open("nairobi_weather.json", "r") as f:
    data = json.load(f)

print(f"{data['main']['temp']}°C")