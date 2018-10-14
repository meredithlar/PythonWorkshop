import json

file = open("weather.json")
text = file.read()
weather_dict = json.loads(text)


