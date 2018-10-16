import json

def print_sd_highs(weather_dict):
    sd_dict = weather_dict["San Diego, CA"]
    july_list = sd_dict["6"]

    for day_dict in july_list:
        high = str(day_dict["high"])
        day = str(day_dict["date"])
        print("July " + day + ": High of " + high)

def main():
    file = open("weather.json")
    text = file.read()
    weather_dict = json.loads(text)
    print_sd_highs(weather_dict)

main()