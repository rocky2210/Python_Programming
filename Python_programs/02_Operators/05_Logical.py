# Define two boolean variables for logical operations
x = True
y = False

# Logical AND operator
print("x and y:", x and y)  # False

# Logical OR operator
print("x or y:", x or y)    # True

# Logical NOT operator
print("not x:", not x)      # False

# Logical XOR (exclusive OR) using not and or operators
print("x xor y:", (x or y) and not (x and y))  # True

"""
    Output:
        x and y: False
        x or y: True
        not x: False
        x xor y: True
"""