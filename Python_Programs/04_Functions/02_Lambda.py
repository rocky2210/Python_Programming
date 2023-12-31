#simple lambda function
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

#lambda funnction with multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytriple = myfunc(3)

print(mydoubler(11))
print(mytriple(11))
