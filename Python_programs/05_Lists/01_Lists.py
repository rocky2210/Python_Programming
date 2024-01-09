# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10,20,30,40,50]
mixed_list = [1,"hello",3.14]


# accessing the list
print(fruits[0])    #  Output : "apple"
print(fruits[-1])   #  Output : "cherry"
print(numbers[3])   #  Output : "40"
print(mixed_list)   #  Output : "hello"
print("------------------------------------")


# slicing the list
numbers = [1,2,3,4,5]
subset = numbers[1:4] # [2,3,4]
print(subset)
print("------------------------------------")


# List operations
list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2  #[1,2,3,4,5,6]
repeated = [1] * 3   # [1,1,1]
print(result)
print(repeated)
print("------------------------------------")


# Modifying list
one_piece = ["luffy", "goku", "zoro"]
one_piece[1] = "ussop"  # Now 'fruits' is ["apple", "orange", "cherry"]
print(one_piece)
print("------------------------------------")


# List methods
print("\n\t list methods \t\n")
#append() = Adds an element at the end of the list
dragon_ball = ["goku", "vegeta"]
dragon_ball.append("gohan")  # Adds "gohan" to the end: ["goku", "vegeta", "gohan"]
print(f"append: {dragon_ball}")

# remove() = Removes all the elements from the list
dragon_ball.remove("goku")  # Removes "goku": ["vegeta", "gohan"]
print(f"remove: {dragon_ball}")

# extend() = Returns a copy of the list
dragon_ball.extend(["goku","roshi"]) # adds multiple elements
print(f"extend(): {dragon_ball}")

# insert() = Returns the index of the first element with the specified value
black_clover = ["asta","yuno","yami"]
black_clover.insert(2,"Noelle")
print(f"insert(): {black_clover}")

# pop() = Removes the element at the specified position
black_clover.pop(1)
print(f"pop(): {black_clover}")

# clear() = Removes all the elements from the list
black_clover.clear()
print(f"clear(): {black_clover}") 
print("------------------------------------")

#! del() keyword also removes the specific index
# del black_clover[0]
# print(black_clover)


# List Operations
print("\n\t list operations \t\n")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Length: {len(numbers)}")
print(f"sum: {sum(numbers)}")
print(f"minimum value: {min(numbers)}")
print(f"maximum value: {max(numbers)}")
print(f"Type: {type(numbers)}") 
print("------------------------------------")


# Copy List
print("\n\t Copy List \t\n")
original = [1,2,3]
shallow_copy = original[:]  # Create a shallow copy of the list
new_list = list(original)  # Create a new list with same elements
shallow_copy.append(4)
new_list.append(5)
original.append(6)
print(shallow_copy)
print(original)
print(new_list)
print("------------------------------------")


# List comprehension
straw_hats = ["Luffy","Zoro","Sanji","ussop","nami","brook","robin","chopper","jinbe","franky"]
new_list = []

for x in straw_hats:
    if "a" in x:
        new_list.append(x)

print(f"List comprehension:  {new_list}")
print("------------------------------------")


# List sort
sort_list = [100,50,65,82.23]
sort_list.sort()
print(sort_list)

sort_list.sort(reverse = True)
print(sort_list)
naruto = ["naruto","sasuke","hinata","kakashi"]
naruto.reverse()
print(naruto)
print("------------------------------------")



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