import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)   # Read the header row
    
    for row in csv_reader:
        name, age, location = row
        print(f"Name: {name}, Age: {age}, Location: {location}")
        