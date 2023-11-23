# Create a program to find the maximum of three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a > b and a > c):
    print(f"{a} is greater than {b} and {c}")
elif(b > a and b > c):
    print(f"{b} is greater than {c} and {a}")
else:
    print(f"{c} is greater than {a} and {b}")

