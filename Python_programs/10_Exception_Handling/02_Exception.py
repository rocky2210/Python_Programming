import sys

a = 10
b = [1,2,3,4]
c = 2

try:
    c = a + b[c]
    raise IOError("This is a sample error")
    print(f"Value of c is {c}")
except NameError as e:
    print("Name error happed")
    print(e)
except IndexError as e:
    print("Index error happed")
    print(e)
except Exception as e:
    print(f"Someerror....{e}")
    print(f"Error: {sys.exc_info()[0]}")
else:
    print("All good")
finally:
    print("Whatever the case is, i will work")
    
"""
    Output:
        Someerror....This is a sample error
        Error: <class 'OSError'>
        Whatever the case is, i will work
"""