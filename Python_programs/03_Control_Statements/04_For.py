text = "Hello world!"
for char in text:
    print(char)
#-------------------------------

print("----------------------")
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
#-------------------------------

print("-----------------------------")
for num in range(1,6): # Range from 1 to 5 (inclusive)
    print(num)  
print("-----------------------------")

for x in range(2,6):
    print(x)
print("-----------------------------")

for x in range(2,30,3):
    print(x)
    
# Use for loop for iterable datatypes

for i in [1,2,3,4,5]:
    print(i)
print("-----------------------------")

s = {1,2,3,4,5}
for i in list(s): # Changed set into list using higher order function
    print(i)
print("-----------------------------")

l = ['apple','banana','orange']
for v in l:
    print(f"I am eating {v}")
print("-----------------------------")

l = [
    {
        "name":"rocky",
        "pass":"abcd"
    },
    {
        "name":"thiri",
        "pass":"asdf"
    },
    {
        "name":"vaisu",
        "pass":"sadf"
    },
    {
        "name":"inu",
        "pass":"sadf"
    },
        {
        "name":"dora",
        "pass":"zcxv"
    },
]

for user in l:
    # print(type(user))
    print(user["name"])