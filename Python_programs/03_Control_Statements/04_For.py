# For Loop

"""
    For Loop:
        a for loop is used to iterate over a sequence (such as a list, tuple, string, or range) 
        and execute a block of code for each item in the sequence. 
"""

text = "Hello world!"
for char in text:
    print(char)
"""
    Output:
            H
            e
            l
            l
            o
            
            w
            o
            r
            l
            d
            !
"""

print("----------------------")
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
#-------------------------------
"""
    Output:
        apple
        banana
        cherry
"""
print("-----------------------------")


for num in range(1,6): # Range from 1 to 5 (inclusive)
    print(num)  

"""
    Output:
        1
        2
        3
        4
        5
"""
print("-----------------------------")



for x in range(2,6):
    print(x)
"""
    Output:
        2
        3
        4
        5
"""
print("-----------------------------")



for x in range(2,30,3):
    print(x)
"""
    Output:
        2
        5
        8
        11
        14
        17
        20
        23
        26
        29
"""
    
    
# Use for loop for iterable datatypes

for i in [1,2,3,4,5]:
    print(i)
"""
Output:
        1
        2
        3
        4
        5
"""
print("-----------------------------")



s = {1,2,3,4,5}
for i in list(s): # Changed set into list using higher order function
    print(i)
"""
    Output:
        1
        2
        3
        4
        5
"""
print("-----------------------------")



l = ['apple','banana','orange']
for v in l:
    print(f"I am eating {v}")
"""
    Output:
        I am eating apple
        I am eating banana
        I am eating orange
"""
print("-----------------------------")



l = [
    {
        "name":"rocky",
        "pass":"abcd"
    },
    {
        "name":"gayu",
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
        "name":"radoo",
        "pass":"zcxv"
    },
]

for user in l:
    # print(type(user))
    print(user["name"])
"""
    Output:
        rocky
        gayu
        vaisu
        inu
        radoo
"""