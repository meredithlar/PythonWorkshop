import json

# Option 1:
# Get cities in a list using list comprehension and print the list
def print_list_comp(weather_dict):
    cities = [city for city in weather_dict.keys()]
    print(cities)

# Option 2:
# Print each dictionary key on its own line
def print_keys(weather_dict):
    for city in weather_dict.keys():
        print(city)

def main():
    file = open("weather.json")
    text = file.read()
    weather_dict = json.loads(text)
    print_list_comp(weather_dict)
    print()
    print_keys(weather_dict)

main()
