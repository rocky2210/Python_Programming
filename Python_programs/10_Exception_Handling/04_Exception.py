import sys
a = 10
b = [1,2,3,4]
c = 7

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
        return a/b

try:
    c = divide(5,b[c])
    print(f"Value of c is {c}")
except (NameError,KeyError,IndexError) as e:
    print(f"Name error happend: {e}")
except ZeroDivisionError as e:
    print(f"Zerodivision error: {e}")
else:
    print("All good")
finally:
    print("Whatever the case is, I will work")
    
"""
    Output:
        Name error happend: list index out of range
        Whatever the case is, I will work
"""