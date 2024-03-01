# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10,20,30,40,50]
mixed_list = [1,"hello",3.14]


# accessing the list

print(fruits[0])    
#  Output : "apple"

print(fruits[-1])   
#  Output : "cherry"

print(numbers[3])   
#  Output : "40"

print(mixed_list)   
#  Output : "hello"
print("------------------------------------")


# slicing the list
numbers = [1,2,3,4,5]
subset = numbers[1:4]
print(subset)
"""
    Output:
        [2,3,4]
"""
print("------------------------------------")


# List operations
list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2  
repeated = [1] * 3   
print(result)
# Output: [1,2,3,4,5,6]
print(repeated)
# Output: [1,1,1]
print("------------------------------------")


# Modifying list
one_piece = ["luffy", "goku", "zoro"]
one_piece[1] = "ussop"
print(one_piece)
# Output :  ["luffy", "ussop", "zoro"]
print("------------------------------------")


# List methods
print("\n\t list methods \t\n")
#append() = Adds an element at the end of the list
dragon_ball = ["goku", "vegeta"]
dragon_ball.append("gohan")  # Adds "gohan" to the end: ["goku", "vegeta", "gohan"]
print(f"append: {dragon_ball}")
# Output: append: ["goku", "vegeta", "gohan"]
print("------------------------------------")



# remove() = Removes all the elements from the list
dragon_ball.remove("goku")  # Removes "goku": ["vegeta", "gohan"]
print(f"remove: {dragon_ball}")
# Output: remove: ["vegeta", "gohan"]
print("------------------------------------")


# extend() = Returns a copy of the list
dragon_ball.extend(["goku","roshi"]) # adds multiple elements
print(f"extend(): {dragon_ball}")
# Output: extend(): ["vegeta", "gohan", "goku", "roshi"]
print("------------------------------------")


# insert() = Returns the index of the first element with the specified value
black_clover = ["asta","yuno","yami"]
black_clover.insert(2,"Noelle")
print(f"insert(): {black_clover}")
# Output: insert(): ["asta", "yuno", "Noelle", "yami"]
print("------------------------------------")



# pop() = Removes the element at the specified position
black_clover.pop(1)
print(f"pop(): {black_clover}")
# Output: pop(): ["asta", "Noelle", "yami"]
print("------------------------------------")



# clear() = Removes all the elements from the list
black_clover.clear()
print(f"clear(): {black_clover}") 
# Output: clear(): []
print("------------------------------------")



#! del() keyword also removes the specific index
# del black_clover[0]
# print(black_clover)


# List Operations
print("\n\t list operations \t\n")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Length: {len(numbers)}")
# Output: Length: 11
print(f"sum: {sum(numbers)}")
# Output: sum: 44
print(f"minimum value: {min(numbers)}")
# Output: minimum value: 1
print(f"maximum value: {max(numbers)}")
# Output: maximum value: 9
print(f"Type: {type(numbers)}") 
# Output: Type: <class 'list'> 
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
# Output: [1, 2, 3, 4]
print(original)
# Output: [1, 2, 3, 6]
print(new_list)
# Output: [1, 2, 3, 5]
print("------------------------------------")


# List comprehension
straw_hats = ["Luffy","Zoro","Sanji","ussop","nami","brook","robin","chopper","jinbe","franky"]
new_list = []

for x in straw_hats:
    if "a" in x:
        new_list.append(x)

print(f"List comprehension:  {new_list}")
# Output: List comprehension: ['Sanji', 'nami', 'brook', 'chopper', 'franky']
print("------------------------------------")


# List sort
sort_list = [100,50,65,82.23]
sort_list.sort()
print(sort_list)
# Output: [50, 65, 82.23, 100]


sort_list.sort(reverse = True)
print(sort_list)
# Output: [100, 82.23, 65, 50]
naruto = ["naruto","sasuke","hinata","kakashi"]
naruto.reverse()
print(naruto)
# Output: ['kakashi', 'hinata', 'sasuke', 'naruto']
print("------------------------------------")



""" 
    List methods
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