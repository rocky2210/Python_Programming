#functions
"""
Group of instructions given to a computer to do a meaningful task.
use "def" to create new functions

"""
def add(x,y):
    z = x + y
    print(f"result is {z}")
    return z

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

print(f"Addition of {a} and {b} is {add(a,b)}")
