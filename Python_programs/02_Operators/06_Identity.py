# Identity operator

"""
    Identity Operator
        identity operators are used to compare the memory locations of two objects, 
        checking whether they refer to the same object in memory. 
"""

# Define two variables with the same value
a = [1, 2, 3]
b = [1, 2, 3]

# Identity operator 'is' checks if two objects have the same identity (memory location)
print("a is b:", a is b)  # False

# Identity operator 'is not' checks if two objects have different identities
print("a is not b:", a is not b)  # True

# Define a new variable that references the same object as 'a'
c = a

# Now, 'c' and 'a' point to the same object
print("a is c:", a is c)  # True

# 'c' and 'a' have the same identity, so 'c' is not a different object from 'a'
print("a is not c:", a is not c)  # False

"""
    Output:
        a is b: False
        a is not b: True
        a is c: True
        a is not c: False
"""