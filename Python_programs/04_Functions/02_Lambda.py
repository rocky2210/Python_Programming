# Lambda function

"""
    Lambda function:
        Lambda functions, also known as anonymous functions or lambda expressions, are small, 
        inline functions defined using the lambda keyword in Python. They are typically used for short, 
        one-time operations where defining a full function using the def keyword would be unnecessary or cumbersome.
"""

# Simple lambda function
add = lambda x,y : x + y
result = add(3,5)
print(result) #Output : 8

# Lambda function with multiple arguments
x = lambda a,b,c : a + b + c
print(x(5, 6, 3))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytriple = myfunc(3)

print(mydoubler(11))
print(mytriple(11))

"""
    Output:
        8
        14
        22
        33
"""