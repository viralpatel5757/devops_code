# convert .csv data in to list formate
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

#### but there is much better way then this  ############
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

