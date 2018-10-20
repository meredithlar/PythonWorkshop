import json
import statistics

def main():
    file = open("weather.json")
    text = file.read()
    weather_dict = json.loads(text)
    find_highest_average(weather_dict)
    print()
    find_lowest_average(weather_dict)

def find_highest_average(weather_dict):
    # list of average high temp for each city
    averages = []

    for city in weather_dict:
        highs_list = [day["high"] for month in weather_dict[city].keys() \
                      for day in weather_dict[city][str(month)]]
        high_mean = statistics.mean(highs_list)
        averages.append((city, high_mean))

    # Sort on 2nd element in tuple with lambda function
    averages.sort(key=lambda elem: elem[1])
    print("Highest average high")
    print(averages[-1][0] + ":", str(averages[-1][1]))

    
def find_lowest_average(weather_dict):
    averages = []

    for city in weather_dict:
        lows_list = [day["low"] for month in weather_dict[city].keys() \
                     for day in weather_dict[city][str(month)]]
        low_mean = statistics.mean(lows_list)
        averages.append((low_mean, city))

    # Default is to sort on 1st element in tuple
    averages.sort()
    print("Lowest average low")
    print(averages[0][1] + ":", str(averages[0][0]))

main()
