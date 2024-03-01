# next() 

"""
    next()
        The next() function in Python is used to retrieve the next item from an iterator. 
        It is typically called with an iterator as an argument, and it returns the next 
        element from that iterator.
"""

l = [1,2,3,4,5,6,7,8,9,10]
l = iter(l)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

"""
    Output:
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
"""