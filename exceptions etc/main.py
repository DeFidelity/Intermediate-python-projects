# try:
#     file = open("a_file.txt")
#     directory = {"key": "content"}
#     print(directory["asjklfh"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("adeyemi")
# except KeyError:
#     print("There is no such key")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#
#
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
# print(make_pie(4))


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
#
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         post['Likes'] = 0
#
# print(total_likes)
#
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict ={row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    to_check = input("what do you want to discover? ").upper()
    try:
        answer = [data_dict[letter] for letter in to_check]
    except KeyError:
        print("Sorry letter inputs alone")
        generate_phonetic()
    else:
        print(answer)

generate_phonetic()