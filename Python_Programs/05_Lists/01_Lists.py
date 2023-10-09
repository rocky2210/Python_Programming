#creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed_list = [1, "hello", 3.14]

#asscessing the list
print(fruits[0])     # Output: "apple"
print(fruits[-1])    # Output: "cherry"
print(numbers[3])    # Output: "40"
print(mixed_list[1])    # Output: "hello"

#slicing the list
numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]  # [2, 3, 4]
print(subset)

#List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  # [1, 2, 3, 4, 5, 6]
repeated = [1] * 3  # [1, 1, 1]
print(result)
print(repeated)

#Modifying list
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # Now 'fruits' is ["apple", "orange", "cherry"]
print(fruits)

#List methods
#append()
fruits = ["apple", "cherry"]
fruits.append("banana")  # Adds "banana" to the end: ["apple", "cherry", "banana"]
print(fruits)
#remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # Removes "banana": ["apple", "cherry"]
print(fruits)
#extend()
fruits = ["apple", "cherry"]
fruits.extend(["grape", "kiwi"])  # Adds multiple elements
print("extend(): ",fruits)
#insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
#pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#del() keyword also removes the specific index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#List Operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
length = len(numbers)
total = sum(numbers)
min_value = min(numbers)
max_value = max(numbers)
print(length)
print(total)
print(min_value)
print(max_value)
print(type(numbers)) #type

#Copy List
original = [1, 2, 3]
shallow_copy = original[:]  # Create a shallow copy of the list
new_list = list(original)   # Create a new list with the same elements
shallow_copy.append(4)
new_list.append(5)
print(shallow_copy)
print(original)


#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#List sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

""" List methods
append()    Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""