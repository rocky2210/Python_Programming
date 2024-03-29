# If elif statement

"""
    If elif statement:
        the elif statement (short for "else if") allows you to check multiple conditions sequentially 
        after an initial if statement. It is used when you have more than two possible conditions to check.
"""

z = 7
if z < 5:
    print("z is less than 5")
elif z == 5:
    print("z is equal to 5")
else:
    print("z is greater than 5") # This block will be executed
    
a = 33
b = 200

if b > a:
    pass

"""
    pass:
        if statements cannot be empty, but if you for some reason have an if statement with no content, 
        put in the pass statement to avoid getting an error.
"""

""" 
    Output:
        z is greater than 5
"""