thisset = {"apple", "banana", "cherry"}
print(thisset)
print("-------------")

#True and 1 considered as same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print("-------------")

#length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("-------------")

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))
print("-------------")

#set constructor()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print("-------------")

#acessing sets
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("-------------")

#Adding set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
print("-------------")

#addting two sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("-------------")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
print("-------------")

#Removing items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
print("-------------")

#clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print("-------------")

#del()
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)
print("-------------")

#union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
"""
You can use the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another:
"""
print("-------------")

#Keep only the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
print("-------------")

#intersection()  method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print("-------------")

#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print("-------------")

#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print("-------------")

#copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
print("-------------")

#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
print("-------------")


set1 = {1, 2, 3, 4}
set2 = {2, 3}
is_subset = set2.issubset(set1)  # Checks if set2 is a subset of set1 (True)
is_superset = set1.issuperset(set2)  # Checks if set1 is a superset of set2 (True)
is_disjoint = set1.isdisjoint({5, 6})  # Checks if set1 and {5, 6} have no common elements (True)
print(is_subset)
print(is_superset)
print(is_disjoint)
print("-------------")

