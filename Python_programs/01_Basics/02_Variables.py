# Variables

""" 
    Variables:
        Variables are the containers for storing the data values.
        A variable is a symbolic name or identifier that is used to
        store and represent a value in memory
"""

# Declaring a variable
x = 10
print(x)

# Type() to get datatype of variable
print(type(x))

# Multiwords variable name
caseCaseName = "rocky"      # Commonly used for var and fun
PascalCaseName = "inu"      # Commonly used for class name
snake_case_name = "dora"    # Commonly used for var and fun
print(caseCaseName)
print(PascalCaseName)
print(snake_case_name)

# Many values to multiple variables
x,y,z = "red","yellow","blue"
print(x,y,z)
print(" + operator: "+x) #concatination

# One value to multiple variables
x = y = z = "orange"
print(x)
print(y)
print(z)


"""
    Output:
        10
        <class 'int'>
        rocky
        inu
        dora
        red yellow blue
        + operator: red
        orange
        orange
        orange
"""


# Single line comment

"""
Multi
Line
comment
"""
