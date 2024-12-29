import json

with open ("employees.json") as f:
    my_data = json.load(f)

new_data={}
for key, value in my_data.items():
    new_data[key] = sum(value)

print(new_data)