# Creating function
def fun(): # a function is defined using the def keyword
    print("Hello world")
    
# calling a function
fun()
print("--------------------------")


# passing arguments
def my_function(fname):
    print(fname + " Welcome")
    
my_function("Inu")
my_function("Vaisu")
print("---------------------------------")

# Passing 2 arguments
def my_function(fname, lname):
    print(fname+lname)

my_function("Gaya","thri")
print("-----------------------")

# keyword arguments
"""
send arguments with the key = value syntax
"""
def my_function(child3, child2,child1):
    print("The biggest child is "+ child3)

my_function(child1="baby",child2= "pappu", child3="rocky")
print("-----------------------")

# Arbitrary keywords arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed 
into your function, add two asterisk: ** before the parameter name 
in the function definition.
"""
def my_function(**kw):
    print("Her last name is "+kw["lname"])
my_function(fname = "selvi", lname = "dora")
print("----------------------------")

# Default parametr value
def my_func(planet = "Earth"):
    print(" I am from "+ planet)

my_func("Mars")
my_func("Venus")
my_func()
my_func("Jupiter")
print("----------------------------")

# Return values
def myreturn(x):
    return 5 * x

print(myreturn(3))
print(myreturn(5))
print(myreturn(9))

# Pass
def mypass():
    pass