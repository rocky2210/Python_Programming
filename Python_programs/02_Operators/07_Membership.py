#  Membership operators are used to test whether a value is a member of a sequence or not. The two membership operators are in and not in

# Define a list
my_list = [1, 2, 3, 4, 5]

# Membership operator 'in' checks if a value is present in the list
print("3 in my_list:", 3 in my_list)  # True
print("6 in my_list:", 6 in my_list)  # False

# Membership operator 'not in' checks if a value is not present in the list
print("3 not in my_list:", 3 not in my_list)  # False
print("6 not in my_list:", 6 not in my_list)  # True

# Define a string
my_string = "Hello, World!"

# Membership operator 'in' checks if a substring is present in the string
print("'Hello' in my_string:", 'Hello' in my_string)    # True
print("'Python' in my_string:", 'Python' in my_string)  # False

# Membership operator 'not in' checks if a substring is not present in the string
print("'Hello' not in my_string:", 'Hello' not in my_string)    # False
print("'Python' not in my_string:", 'Python' not in my_string)  # True

"""
    Output:
        3 in my_list: True
        6 in my_list: False
        3 not in my_list: False
        6 not in my_list: True
        'Hello' in my_string: True
        'Python' in my_string: False
        'Hello' not in my_string: False
        'Python' not in my_string: True
"""