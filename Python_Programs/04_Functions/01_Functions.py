#creating functions
def fun(): #a function is defined using the def keyword
    print("Hello World")

#calling a function
fun()
print("----------------------------")


#passing arguments
def my_function(fname):
    print(fname + " SON")

my_function("Goku")
my_function("Gohan")
print("----------------------------")


#passing 2 arguments
def my_function(fname, lname):
  print(fname + " D " + lname)

my_function("Monkey", "Luffy")
print("----------------------------")


#arbitrary arguments *
"""
If you do not know how many arguments that will be passed into your function, 
    add a * before the parameter name in the function definition.
"""
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Luffy", "Ace", "Sabo")
print("----------------------------")


#keyword arguments
"""
send arguments with the key = value syntax.
"""
def my_function(child3, child2, child1):
    print("The Biggest child is " + child3)

my_function(child1 = "Luffy", child2 = "Sabo", child3 = "Ace")
print("----------------------------")


#Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function,
    add two asterisk: ** before the parameter name in the function definition.
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Izuku", lname = "Midoriya")
print("----------------------------")


#Default parameter value
def my_func(country = "Norway"):
  print("I am from " + country)

my_func("Sweden")
my_func("India")
my_func()
my_func("Brazil")
print("----------------------------")


#Return Values
def myreturn(x):
  return 5 * x

print(myreturn(3))
print(myreturn(5))
print(myreturn(9))


#Pass
def mypass():
  pass