# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number*number for number in numbers]
# print(squared_numbers)
# result = [number for number in numbers if number % 2 == 0]
# print(result)
# with open("file.txt") as file1:
#     l1 = file1.readlines()
# with open("file2.txt") as file2:
#     l2 = file2.readlines()
# result = [int(num) for num in l1 if num in l2]
# print(result)
# import random
# names = ["caroline", "grace", "elizbeth", "esther", "daniel", "donald", "wisdom", "godwin", "victor", "chidinma", "vincent"]
# student_score = {student:random.randint(1,100) for student in names}
# passed_student = {student:score for (student, score) in student_score.items() if score > 59}
# print(passed_student)

# sentence = "what is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# result = {word:len(word) for word in words}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 24,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "Score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)
# loop through a data frame with code like this:
pandas_student = pandas.DataFrame(student_dict)
# for (key, value) in pandas_student.items():
#     print(value == 98)
#loop through rows of data frame:
for (index, row) in  pandas_student.iterrows():
    # print(row)

    if row.student == "angela":
        print(row.score )


