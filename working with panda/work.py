############ My Method #############

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_data = gray_squirrels["Primary Fur Color"]
gray = gray_data.tolist()
g = len(gray)
Cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_data = Cinnamon_squirrels["Primary Fur Color"]
cinnamon = cinnamon_data.tolist()
c = len(cinnamon)
white_squirrels = data[data["Primary Fur Color"] == "Black"]
white_data = white_squirrels["Primary Fur Color"]
black = white_data.tolist()
w = len(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [g, c, w]
}
Squirrel_stat = pandas.DataFrame(data_dict)
print(Squirrel_stat)
Squirrel_stat.to_csv("Squirrel_stat.csv")


############## Angela's Method ##################

#### This three lines does all ######
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

squirrel_dict = {
    "primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
dic = pandas.DataFrame(squirrel_dict)
dic.to_csv("ShortDIct.csv")




