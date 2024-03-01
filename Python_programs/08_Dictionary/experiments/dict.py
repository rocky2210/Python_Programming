#dictionary are mutable
"""
d = {
    key : "value",
    key1 : "value",
}
Key : Immutable datatype(int,float,string,other immutable object)

To do all dictionary operations, a key must be hashed. Regardless of the
datatype of the key, it has be hashed.

"""
#Not iterative , no enumurated index.

#in keyword in dict

#in keyword in dict
"""
in is applied for the key by can be used to check if a key is present in dictionary
"""
d = {
    "one" : 1,
    "two" : 2
}
print("two" in d)   
# Output: True
print("three" in d) 
# Output: False

#del keyword in dict
del d["one"] #deletes the pair
print(f"del : {d}") 
# Output: del : {'two': 2}

#unpacking 
d = {'a':1,'b':2}
c = {'c' : 3}
print(d) 
# Output: {'a': 1, 'b': 2}
print(c) 
# Output: {'c': 3}
d = {'a':1,'b':2, **c} 
print(d) # it also update if index already exicts
# Output: {'a': 1, 'b': 2, 'c': 3}
