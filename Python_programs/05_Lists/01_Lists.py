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


#Modifying list
one_piece = ["luffy", "goku", "zoro"]
one_piece[1] = "ussop"  # Now 'fruits' is ["apple", "orange", "cherry"]
print(one_piece)
print("------------------------------------")


#List methods
print("\n\t Python list methods \t\n")
#append() = Adds an element at the end of the list
dragon_ball = ["goku", "vegeta"]
dragon_ball.append("gohan")  # Adds "gohan" to the end: ["goku", "vegeta", "gohan"]
print(f"append: {dragon_ball}")

#remove() = Removes all the elements from the list
dragon_ball.remove("goku")  # Removes "goku": ["vegeta", "gohan"]
print(f"remove: {dragon_ball}")

#extend() = Returns a copy of the list
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


#List Operations
print("\n\t Python list operations \t\n")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Length: {len(numbers)}")
print(f"sum: {sum(numbers)}")
print(f"minimum value: {min(numbers)}")
print(f"maximum value: {max(numbers)}")
print(f"Type: {type(numbers)}") 
print("------------------------------------")


