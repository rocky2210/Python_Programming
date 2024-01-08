def basic_math(x,y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    return {
        "Addition":a,
        "Subtraction":s,
        "Multiplication":m,
        "Division":d
    }

a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))

d = basic_math( y = a, x = b) # Keyword arguments
print(f"basic math results {a} and {b} ")

for i in d.keys():  # way to iterate dictionary
    print(f"{i}: {d[i]}")
    
"""
    Output:
        Enter the number 1:10
        Enter the number 2:20
        basic math results 10 and 20
        Addition: 30
        Subtraction: 10
        Multiplication: 200
        Division: 2.0
"""