import sys
a = 10
c = 2

def divide(a,b):
    if b == 0:
        raise Exception("Cannot divide by zero")
        return a/b

try:
    c = divide(5,0)
    print(f"Value of c is {c}")
except NameError as e:
    print("Name error happed")
    print(e)
except IndexError as e:
    print("Index error happend")
    print(e)
except Exception as e:
    print(f"Someerror...{e}")
    print(f"Error: {sys.exc_info()}")
else:
    print("All good")
finally:
    print("Whatever the case is, I will work")
    
"""
    Output:
        Someerror...Cannot divide by zero
        Error: (<class 'Exception'>, Exception('Cannot divide by zero'), <traceback object at 0x7f54f139a440>)
        Whatever the case is, I will work
"""