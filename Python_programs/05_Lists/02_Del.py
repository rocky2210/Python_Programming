#del keyword

"""
    del:
        It deletes an items inside a list or it can delete an entire variable 
"""

u = [1, 2, [1, 2, 3, [5, 6, 7]], 4, 5, 6,7]
u.remove(1)
print(u)
del u[3]
print(u)

#in keyword
"""
    The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
    The in keyword is also used to iterate through a sequence in a for loop.
"""
print(2 in u) #true
print("hello" in u) #false

"""
    Output:
        [2, [1, 2, 3, [5, 6, 7]], 4, 5, 6, 7]
        [2, [1, 2, 3, [5, 6, 7]], 4, 6, 7]
        True
        False
"""