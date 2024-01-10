#sets are not iterable
#sets are a value less dictionary, so duplicate items are not possible
#these are just sets from maths
#sets are mutable

"""
value immutable data type
"""

es = {1,1,2,2,3,3} 
#duplicates not allowed
print(es)   # {1, 2, 3}
print("---------------------------------")

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
print(s)    # {1, 3, 4, 5, 6, 9}
print(d)    # {1, 3, 6, 7, 8, 9}
print("---------------------------------")

print(f"Intersection: {s & d}") # Intersection: {1, 3, 6, 9}
print(f"Union: {s - d}")    # Union: {4, 5}
print(f"Difference: {s | d}")   # Difference: {1, 3, 4, 5, 6, 7, 8, 9}
print(f"Symmetric difference: {s ^ d}") # Symmetric difference: {4, 5, 7, 8}
print("---------------------------------")

# Is superset
print({1,2} >= {1,2,3})     # False
print({1,2,3} >= {1,2,3})   # True
print({1,2,3,4} >= {1,2,3}) # True
# Is subset
print({1,2} <= {1,2,3})     # True
print({1,2,3} <= {1,2,3})   # True



