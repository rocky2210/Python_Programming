#functions
"""
Group of instructions given to a computer to do a meaning task.
use "def" to create a new function
"""

def add(x,y):
    z = x + y
    print(f"result is {z}")
    return z

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 1: "))

print(f"Addition of {a} and {b} is {add(a,b)}")

"""
Output: 
    Enter the number 1: 10
    Enter the number 1: 20
    result is 30
    Addition of 10 and 20 is 30
"""