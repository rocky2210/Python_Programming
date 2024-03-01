# Enum

"""
    Enum:
        The enumerate() function is used to iterate over a sequence (such as a list, 
        tuple, or string) while keeping track of the index position of each item. 
        It returns an enumerate object, which yields pairs containing the index and
        the corresponding value from the iterable.
"""

l = ['apple','orange','banana','kiwi']
print(type(l))
print(type(enumerate(l)))
e = enumerate(l)
for i,v in e:
    print(f"#{i} {v}")
"""
    Output:
        <class 'list'>
        <class 'enumerate'>
        #0 apple
        #1 orange
        #2 banana
        #3 kiwi
"""


# __next__

"""
    __next__():
        __next__() is a special method used in the context of iterators. It allows an 
        iterator object to return the next element in the sequence it represents. This 
        method is automatically called when you use the built-in next() function to iterate 
        through an iterator.
"""
l = ['apple','orange','banana','kiwi']
k = enumerate(l)
for h in range(len(l)):
    print(k.__next__())
"""
    Output:
        (0, 'apple')
        (1, 'orange')
        (2, 'banana')
        (3, 'kiwi')
"""