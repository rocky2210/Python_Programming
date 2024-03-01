# Iter

"""
    Iter():
        the iter() function is used to create an iterator from an iterable object. 
        An iterable object is any object that can be looped over, such as lists, 
        tuples, strings, dictionaries, and more. Iterators are objects that implement 
        the iterator protocol, which includes the __iter__() method (to return the 
        iterator object itself) and the __next__() method (to retrieve the next element 
        from the iterator).
"""

l = [1,2,3,4,5,6,7,8,9,10]
d = {'a':'b','c':'d','e':'f'}
for i in iter(d):
    print(i, d[i])
    
"""
    Output:
        a b
        c d
        e f
"""