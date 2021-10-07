file = open("../../my_file.txt")
content = file.read()
print(content)
with open("my_file.txt", mode="w") as File:
    File.write("hi i am fideh whats up with you?")
    File.write("\n and whats up with the team?")

with open("that+file.txt", mode="w") as doc:
    doc.write("that is the house")
