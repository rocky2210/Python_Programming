# variable scopes

"""
    Variable scope:
        Variable scope refers to the region of code where a variable is accessible and can be referenced. 
        In Python, the scope of a variable is determined by where it is defined within the code. 
        Understanding variable scope is crucial for writing clear and maintainable code, as it helps 
        prevent unintended side effects and conflicts between variables with the same name.
        
        Global scope: Variables defined at the outermost level of a Python script or module have global scope. 
        They can be accessed from anywhere within the script or module, including inside functions.
        
        Local scope: Variables defined within a function have local scope. They can only be accessed from within 
        the function where they are defined.
"""
x = 5
def set_x(num):
    x = num
    print(x)

    
def set_global_x(num):
    global x
    print(x) # Output: 5
    x = num
    print(x) # Output: 6
    
print(x)
# Output: 5
set_x(50)
# Output: 50
print(x)
# Output: 5
set_global_x(6)
# Output: 6
print(x)
# Output: 6
set_x(40)
# Output: 40
print(x)
# Output:6