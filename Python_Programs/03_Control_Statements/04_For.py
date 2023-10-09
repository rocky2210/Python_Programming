text = "Hello World!"
for char in text:
    print(char)
#--------------------------------------------
print ("-------------------------------------")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#--------------------------------------------
print ("-------------------------------------")
for num in range(1, 6):  # Range from 1 to 5 (inclusive)
    print(num)

print ("-------------------------------------")
for x in range(2, 6):
  print(x)

print ("-------------------------------------")
for x in range(2, 30, 3):
  print(x)

"""
use for loop for iterable datatypes
"""
for i in [1,2,3,4,5]:
  print(i)

s = {1,2,3,4,5}
for i in list(s): #changed set into list using higher order function
  print(i)

l = ['apple','banana','orange']
for v in l:
  print("I am eating {}".format(v))


l = [
  {
    "username":"rocky",
    "password":"sadf"
  },
    {
    "username":"sree",
    "password":"sadf"
  },
    {
    "username":"vaisu",
    "password":"sadf"
  },
    {
    "username":"inu",
    "password":"sadf"
  },
]

for user in l:
  # print(type(user))
  print(user["username"])

