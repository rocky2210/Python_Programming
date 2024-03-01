# Filter()

"""
    filter():
        The filter() function in Python is used to construct an iterator from elements of an iterable 
        (such as lists, tuples, or sets) for which a specified function returns true. In other words, 
        it filters the elements of the iterable based on the condition provided in the function.
"""

l  = [100,120,1000,1120]
print(list(filter((lambda x : x >= 1000 ),l)))

def fil(x):
    return x >= 1000
print(list(filter(fil,l)))

"""
    Output:
        [1000, 1120]
        [1000, 1120]
"""
