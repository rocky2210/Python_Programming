a = 5

a += 5
print("addition assignment : ",a)

a -= 5
print("subtraction assignment : ",a)

a *= 5
print("Multiplication assignment: ",a)

a /= 5
print("Division assignment: ",a)

a %= 3
print("Modulus assignment: ",a)

a = 5
a //= 3
print("Floor division: ",a)

a = 5
a **= 3
print("Exponential: ",a)

b = 5
b <<= 3
print("Left assignment: ",b)

z = 5
z >>= 3
print("Right assignment: ",z)

c = 5
c &= 3
print("BITWISE AND Assignment",c)

d = 5
d ^= 3
print("BITWISE XOR Assignment",d)

e = 5
e |= 3
print("BITWISE OR Assignment: ",e)


"""
    Output:
        addition assignment :  10
        subtraction assignment :  5
        Multiplication assignment:  25
        Division assignment:  5.0
        Modulus assignment:  2.0
        Floor division:  1
        Exponential:  125
        Left assignment:  40
        Right assignment:  0
        BITWISE AND Assignment 1
        BITWISE XOR Assignment 6
        BITWISE OR Assignment:  7
"""