import json
import statistics

def print_monthly_averages(weather_dict):
    for city in weather_dict:
        months = [int(i) for i in weather_dict[city].keys()]
        months.sort()
        for month in months:
            highs_list = [day["high"] for day in weather_dict[city][str(month)]]
            lows_list = [day["low"] for day in weather_dict[city][str(month)]]
            high_mean = str(statistics.mean(highs_list))
            low_mean = str(statistics.mean(lows_list))
            print(city + ", " + str(month) + ": High of " + high_mean)
            print(city + ", " + str(month) + ": Low of " + low_mean)


def main():
    file = open("weather.json")
    text = file.read()
    weather_dict = json.loads(text)
    print_monthly_averages(weather_dict)


main()