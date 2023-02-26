##### but the best way to deal with data and CSV file is to use pandas library #######
# pandas is super helpful data analysis library
# and you can see how with just 3 lines of code we are doing similar stuff as above

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])  # pandas is intelligent enough to know the heading of the colum and return the data underneath it
#
data_dict = data.to_dict()  # to convert it to dictionary
print(data_dict)

temp_list = data["temp"].to_list()  # getting the temp column data and converting it to list
print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

avg_temp = data["temp"].mean()
print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

# get data in column
condition = data["condition"]

# get data in row
data_row = data[data["day"] == "Monday"]  # fetch data (row) of Monday
print(data_row)

max_temp_row = data[data["temp"] == data["temp"].max()]  # fetch a row with max temp.
print(max_temp_row)

# get specific value out of row
monday = data[data.day == "Monday"]
print(monday.condition)

# get Mondays temp and convert it in to fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32

# creating dataframe from scratch
data_dict = {
    "students": ["Viral", "Mikin", "Panth"],
    "scores": [100, 76, 66]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("new_data_frame.csv")

