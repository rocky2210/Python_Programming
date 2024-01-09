thistuple = ("vaisu", "gayu", "rocky")
print(f"tuples(): {thistuple}")
print("------------------------------------")

# Len() of the tuple
one_piece = ("Luffy", "Zoro", "sanji")
print(f"Length of one_piece: {one_piece}")
print("------------------------------------")


# Tuple and not tuple
tup = ("Inu",)
print(type(tup))    # Output : tuple
tup = ("fire")
print(type(tup))    # Output : str
print("------------------------------------")


# Tuple constructor 
"""
    the tuple() class constructor to create tuple objects from an iterable, 
such as a list, set, dictionary, or string. If you call the constructor 
without arguments, then it will build an empty tuple.
"""
tupcon = tuple(("lion", "cheeta", "elephant"))  # not the double round-brackets
print(f"Tuple constructor : {tupcon}")
print("------------------------------------")


#Access tuple
dragon_ball = ("goku", "vegeta", "goten")
print(dragon_ball[1])
print(dragon_ball[-1])
print("------------------------------------")


#Ranges of index
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[:4])
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:])
print("------------------------------------")


#Check items from the list
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
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
print("------------------------------------")


# Adding tuple to tuple
black_clover = ("asta", "yuno", "yami")
y = ("Noelle",)
black_clover += y
print(black_clover)
print("------------------------------------")


# Removing items
y = list(black_clover)
y.remove("Noelle")
black_clover = tuple(y)
print(black_clover)
print("------------------------------------")


# unpacking tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print("------------------------------------")


# Using *Asterisk 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
print("------------------------------------")


#joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#multiplying two tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
print("------------------------------------")


#tuples methods
#count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
print("------------------------------------")





