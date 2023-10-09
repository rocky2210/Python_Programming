import sys

a = 10
b = [1,2,3,4]
c = 2

try:
    c = a + b[c]
    raise IOError("This is a sample error")
    print("Value of c is {}".format(c))
except NameError as e:
    print("Name error happend")
    print(e)
except IndexError as e:
    print("Index error happend")
    print(e)
except Exception as e:
    print("Someerror...{}".format(e))
    print("Error: {}".format(sys.exc_info()[0]))
else:
    print("All good")
finally:
    print("Whatever the case is, I will work")