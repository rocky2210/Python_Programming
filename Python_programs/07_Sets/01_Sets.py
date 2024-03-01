thisset = {"apple", "banana", "cherry"}
print(thisset)  
# Output: {'apple', 'cherry', 'banana'}
print("---------------------------------")


# True and 1 considered as same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  
# Output: {'apple', 2, True, 'banana', 'cherry'}
print("---------------------------------")


# Length of the set
print(len(thisset)) 
# Output: 5
print("---------------------------------")


# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))  
# Output: <class 'set'>
print("---------------------------------")


#set constructor()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)  
# Output: {'banana', 'cherry', 'apple'}
print("---------------------------------")


# Accessing sets
one_piece = {"Luffy", "Zoro", "Sanji"}
print("Zoro" in one_piece)  
# Output: True
print("---------------------------------")


# Adding set items
one_piece.add("Nami")
print(one_piece)    
# Output: {'Luffy', 'Zoro', 'Sanji', 'Nami'}
print("---------------------------------")


# Adding two sets
anime = {"goku", "vegeta", "ichigo"}
anime.update(one_piece)
black_clover = ["asta", "yuno"]
anime.update(black_clover)
print(anime) 
# Output: {'Luffy', 'ichigo', 'Nami', 'asta', 'yuno', 'goku', 'Zoro', 'vegeta', 'Sanji'}
print("---------------------------------")


# Removing items
# remove method removes the specified element from the set if it is present. If the element is not found, 
# it raises a KeyError
anime.remove("asta")
print(anime) 
# Output: {'Zoro', 'yuno', 'Sanji', 'Luffy', 'ichigo', 'vegeta', 'goku', 'Nami'}

# discard method removes the specified element from the set if it is present. If the element is not found, 
# it does nothing and does not raise an error
anime.discard("ichigo") # {'Zoro', 'yuno', 'Sanji', 'Luffy', 'vegeta', 'goku', 'Nami'}
print(anime)
print("---------------------------------")


# Clear
anime.clear()
print(anime)  
# Output: set()
print("---------------------------------")


# del()
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)
# print("---------------------------------")


#union()
"""
    You can use the union() method that returns a new set containing all items from both sets,
    or the update() method that inserts all the items from one set into another
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  
# Output: {1, 2, 3, 'a', 'c', 'b'}
print("---------------------------------")


#intersection()  method will return a new set, that only contains the items that are present in both sets.
x = {"facebook", "instagram", "whatsapp"}
y = {"google", "microsoft", "whatsapp"}
z = x.intersection(y)
print(z)    
# Output: {'whatsapp'}
print("---------------------------------")


# Keep only the duplicates
x = {"facebook", "instagram", "whatsapp"}
y = {"google", "microsoft", "whatsapp"}
x.intersection_update(y)
print(x)    
# Output: {'whatsapp'}
print("---------------------------------")


# Keep all, but not the duplicates
x = {"facebook", "instagram", "whatsapp"}
y = {"google", "microsoft", "whatsapp"}
x.symmetric_difference_update(y)
print(x)    
# Output: {'instagram', 'google', 'microsoft', 'facebook'}
print("---------------------------------")


# symmetric_difference
x = {"facebook", "instagram", "whatsapp"}
y = {"google", "microsoft", "whatsapp"}
z = x.symmetric_difference(y)
print(z)    
# Output: {'facebook', 'instagram', 'microsoft', 'google'}
print("---------------------------------")


# copy()
anime = {"dragonball", "onepiece", "naruto", "bleach"}
x = anime.copy()
print(x)    
# Output: {'onepiece', 'dragonball', 'bleach', 'naruto'}
print("---------------------------------")


# difference 
x = {"facebook", "instagram", "whatsapp"}
y = {"google", "microsoft", "whatsapp"}
z = x.difference(y)
print(z)    
# Output: {'facebook', 'instagram'}
print("---------------------------------")


set1 = {1, 2, 3, 4}
set2 = {2, 3}
is_subset = set2.issubset(set1)  # Checks if set2 is a subset of set1 (True)
is_superset = set1.issuperset(set2)  # Checks if set1 is a superset of set2 (True)
is_disjoint = set1.isdisjoint({5, 6})  # Checks if set1 and {5, 6} have no common elements (True)
print(is_subset)    
# Output:  True
print(is_superset)  
# Output:  True
print(is_disjoint)  
# Output:  True
print("---------------------------------")
