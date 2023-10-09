#sets are not iterable
#sets are a value less dictionary, so duplicate items are not possible
#these are just sets from maths
#sets are mutable


"""
value immutable data type
"""

es = {1,1,2,2,3,3} 
print(es) #duplicates not allowed

#add a new items
es.add(4)
print(es)

"""
set operations are done by the following operators
    & -> Intersection
    | -> Union
    - -> difference
    ^ -> symmetric difference
take 2 operand sets and return a set
    >= -> Is superset
    <= -> Is subset
take 2 operand sets and return a boolean
"""

s = {1,3,4,5,6}
d = {3,6,7,8,9}
s.add(9)
d.add(1)
print(s)
print(d)

print(s & d)
print(s - d)
print(s | d)
print(s ^ d)

print({1,2} >= {1,2,3})
print({1,2,3} >= {1,2,3})
print({1,2,3,4} >= {1,2,3})

print({1,2} <= {1,2,3})
print({1,2,3} <= {1,2,3})