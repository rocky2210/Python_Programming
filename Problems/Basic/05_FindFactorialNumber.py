# Write a C program to find the factorial of a number. 

number = int(input("Enter a number: "))
if(number == 1 or number == 0):
    print(f"Factorial of {number} is : 1")
else:
    fact = 1
    for i in range(2,number + 1):
        fact = fact * i
    
print(f"Factorial of {number} is : {fact}")
    