import json

# Läs in JSON-filen
filename = "sweden_temperatures.json"

def read_file(file_name):
    with open(file_name, "r") as f:
        return json.load(f)

def write_file(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, ensure_ascii=False)

def update_temperature(temperatures):
    month = input("temperature: ").capitalize()
    new_temp = int(input("temperature: "))

    if month not in temperatures:
        print("Invalid month name!")
        return temperatures

    if new_temp > temperatures[month]:
        temperatures[month] = new_temp
        print("Record updated successfully!")
    else:
        print("No update needed.")
    return temperatures

# Huvudprogrammet
temperatures = read_file(filename)
temperatures = update_temperature(temperatures)
write_file(filename, temperatures)