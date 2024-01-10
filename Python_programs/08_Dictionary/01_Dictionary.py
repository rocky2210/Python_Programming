thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print("---------------------------------")



thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])    # Ford
print("---------------------------------")


#Duplicates not allowed
thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict1)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print("---------------------------------")


# length of dictonary
print(len(thisdict)) # 3
# type of dictionart
print(type(thisdict)) # <class 'dict'>
# dict constructer
thisdict = dict(name = "Rocky",aget = "22", planet = "Earth")
print(thisdict) # {'name': 'Rocky', 'aget': '22', 'planet': 'Earth'}
print("---------------------------------")


#Accessing items
cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = cars.get("brand")
print(x)    # Ford
print("---------------------------------")


# Keys() - method will return a list of all the keys in the dictonary.
x = cars.keys() # dict_keys(['brand', 'model', 'year'])
# before the change
print(x)  
cars["color"] = "red"
# after the change
print(x)    # dict_keys(['brand', 'model', 'year', 'color'])
print("---------------------------------")

#values() - method will return a list of all the values in the dictionary.
x = cars.values()
# before the change
print(x) # dict_values(['Ford', 'Mustang', 1964, 'red'])
cars['year'] = 2020
# after the change
print(x) # dict_values(['Ford', 'Mustang', 2020, 'red'])
print("---------------------------------")

#items() - method will return each item in a dictionary, as tuples in a list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
# before the change
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
# after the change
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
print("---------------------------------")

# Check if key exist
if "brand" in car:
    print("yes, 'model' is one of the keys in the car dictonary")
print("---------------------------------")
    
#update - method will update the dictionary with the items from the given argument.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print("---------------------------------")

