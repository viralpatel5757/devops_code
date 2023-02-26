# challange : from 2018_squirrel_census.csv fetch the total number of black, grey and cinnamon squirrels .
#  put this info in squirrel_count.csv


import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
fur_color_list = squirrel_data["Primary Fur Color"].to_list()

# gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

gray_squirrels_count = fur_color_list.count("Gray")
red_squirrels_count = fur_color_list.count("Cinnamon")
black_squirrels_count = fur_color_list.count("Black")

fur_color_dict = {
    "fur_color": ["Gray", "Cinnamon", "Black"],
    "squirrel_count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

fur_color_data = pandas.DataFrame(fur_color_dict)
fur_color_data.to_csv("squirrel_count.csv")
