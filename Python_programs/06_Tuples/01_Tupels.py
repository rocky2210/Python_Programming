thistuple = ("vaisu", "gayu", "rocky")
print(f"tuples(): {thistuple}")
# Output: ("vaisu", "gayu", "rocky")
print("------------------------------------")

# Len() of the tuple
one_piece = ("Luffy", "Zoro", "sanji")
print(f"Length of one_piece: {one_piece}")
# Output: Length of one_piece: 3
print("------------------------------------")


# Tuple and not tuple
tup = ("Inu",)
print(type(tup))
# Output : <class 'tuple'>
tup = ("fire")
print(type(tup))
# Output : <class 'str'>
print("------------------------------------")


# Tuple constructor 
"""
    the tuple() class constructor to create tuple objects from an iterable, 
such as a list, set, dictionary, or string. If you call the constructor 
without arguments, then it will build an empty tuple.
"""
tupcon = tuple(("lion", "cheeta", "elephant"))  # not the double round-brackets
print(f"Tuple constructor : {tupcon}")
# Output: Tuple constructor : ('lion', 'cheeta', 'elephant')
print("------------------------------------")


#Access tuple
dragon_ball = ("goku", "vegeta", "goten")
print(dragon_ball[1])
# Output: vegeta
print(dragon_ball[-1])
# Output: goten
print("------------------------------------")


#Ranges of index
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
# Output: ('cherry', 'orange', 'kiwi')
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[:4])
# Output: ('apple', 'banana', 'cherry', 'orange')
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:])
# Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print("------------------------------------")


#Check items from the list
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
# Output: Yes, 'apple' is in the fruits tuple
print("------------------------------------")


#Change Tuple Values
"""
    Once a tuple is created, you cannot change its values. 
    Tuples are unchangeable.You can convert the tuple into a list, 
    change the list, and convert the list back into a tuple.
"""
x = ("baby", "gayu", "vaisu")
y = list(x)
y[1] = "sri"
x = tuple(y)
print(x)
# Output: ('baby', 'sri', 'vaisu')
print("------------------------------------")


# Adding tuple to tuple
black_clover = ("asta", "yuno", "yami")
y = ("Noelle",)
black_clover += y
print(black_clover)
# Output: ('asta', 'yuno', 'yami', 'Noelle')
print("------------------------------------")


# Removing items
y = list(black_clover)
y.remove("Noelle")
black_clover = tuple(y)
print(black_clover)
# Output: ('asta', 'yuno', 'yami')
print("------------------------------------")


# unpacking tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
# Output: apple
print(yellow)
# Output: banana
print(red)
# Output: cherry
print("------------------------------------")


# Using *Asterisk 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
# Output: apple
print(yellow)
# Output: banana
print(red)
# Output: ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
# Output: apple
print(tropic)
# Output: ['mango', 'papaya', 'pineapple']
print(red)
# Output: cherry
print("------------------------------------")


#joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# Output: ('a', 'b', 'c', 1, 2, 3)
#multiplying two tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print("------------------------------------")


#tuples methods
#count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
# Output: 2

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
# Output: 3
print("------------------------------------")