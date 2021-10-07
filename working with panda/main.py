# import csv
# with open("working_sheet.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("working_sheet.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

from pandas import pandas

data = pandas.read_csv("working_sheet.csv")
print(data.temp == data.temp.max())  # return true or false
print(data[data.temp == data.temp.max()])  # returns the row with highest temp
# we can as well get a particular value of a row
tuesday = data[data.day == "Tuesday"]
print(tuesday.condition)  # would return the condition string

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)
# ''' to get hold of a row'''
# data[data.temp == 24]
# ''' to get hold of a row'''
# data["condition"] #or
# data.condition
# print(data["temp"].max())
# temp = data["temp"]
# list = temp.tolist()
#
# a = sum(list) / len(list)
# print(a)

''' we can as well create a pandas data frame from scratch  just by creatin ga dictionary and calling th function below'''
#
# data_dict = {
#     "student": ["Anini", "Jamisi", "Angela"],
#     "scores": [56, 60, 79]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# # we can as well get pandas to create a new csv file for us
# new_data.to_csv("new_data.csv")
