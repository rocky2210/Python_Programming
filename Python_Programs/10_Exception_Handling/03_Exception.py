import sys
a = 10
c = 2
def divide(a,b):
    if b == 0:
        raise Exception("Cannot divide by zero")
        return a/b

try:
    c = divide(5,0)
    print("Value of c is {}".format(c))
except NameError as e:
    print("Name error happend")
    print(e)
except IndexError as e:
    print("Index error happend")
    print(e)
except Exception as e:
    print("Someerror...{}".format(e))
    print("Error: {}".format(sys.exc_info()))
else:
    print("All good")
finally:
    print("Whatever the case is, I will work")