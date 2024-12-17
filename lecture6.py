#DataBase searching for name training

with open("names.txt") as f:
    lines = f.readlines()

name_to_search = "Lee"
for line in lines:
    if name_to_search in line:
        print(line) 