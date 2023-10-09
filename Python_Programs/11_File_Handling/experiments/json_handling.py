import json

# Writing data to a JSON file
data = {
    "name": "Inu",
    "age": 23,
    "Status": "Mental 🤪"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading data from a JSON file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)  # Output: {'name': 'John', 'age': 28, 'city': 'San Francisco'}
