"""
    Generators:
        Generators in Python are functions that enable you to create iterators. 
        They are defined using the yield keyword instead of return. Generators 
        allow you to iterate over a sequence of items one at a time without the 
        need to store the entire sequence in memory at once. This makes them memory 
        efficient, especially for large datasets or infinite sequences.
"""

def double_numbers(iterable):
    for i in iterable:
        print(f"[] double data gen {i}")
        yield i * 2  #Lazycoding
        
# def double_numbers(iterable):
#     l = []
#     for i in iterable:
#         print("[] double data gen ()".format(i))
#         l.append(i*2)
#     return l

def datagen():
    l = []
    for i in range(20):
        print("[] data gen")
        l.append(i)
    return l

# Generating the data on-demand
for i in double_numbers(range(20)):
    print(i)
    
# Iterating already available data
for i in datagen():
    print(i)
    
"""
    Output:
        [] double data gen 0
        0
        [] double data gen 1
        2
        [] double data gen 2
        4
        [] double data gen 3
        6
        [] double data gen 4
        8
        [] double data gen 5
        10
        [] double data gen 6
        12
        [] double data gen 7
        14
        [] double data gen 8
        16
        [] double data gen 9
        18
        [] double data gen 10
        20
        [] double data gen 11
        22
        [] double data gen 12
        24
        [] double data gen 13
        26
        [] double data gen 14
        28
        [] double data gen 15
        30
        [] double data gen 16
        32
        [] double data gen 17
        34
        [] double data gen 18
        36
        [] double data gen 19
        38
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        [] data gen
        0
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
        11
        12
        13
        14
        15
        16
        17
        18
        19
"""