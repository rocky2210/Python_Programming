"""
datatypes in python : 
            1. Text Type 		: str
	        2. Numeric Type 	: int,float,complex
	        3. Sequence Type 	: list,tuple,range
            4. Mapping Type 	: dict
            5. Set Types 		: set, frozenset
            6. Boolean Type 	: bool
            7. Binary Types 	: bytes,bytearray,memoryview
            8. None Types 		: NoneType
"""

#Text Type - String are identified as a contiguous set of characters represented in the quotation mark
text = "Monkey 🐒 123"

#Numeric Types - Stores the numberic values
number = 10 			#type(int)
decimal = 3.1 			#type(float)
complex_num = 2+ 4j		#type(complex)

#Sequence Types  
my_list = [1,2,3,4,5]	#type(list)
my_tuple = (1,2,3,4,5)  #type(tuple)
my_range = range(1,6)

#Mapping Type
my_dict = {
	'name':'Monkey D Luffy',
	'age' : 18
}						#type(dict)

#Set Types
my_set = {1,2,3,4,5}	#type(set)
my_frozenset = frozenset({1,2,3,4,5})	#type(frozenset)

#Boolean Types
is_valid = True			#type(bool)

#Binary Types
my_bytes = b'Hello'		#type(bytes)
my_bytearray = bytearray(b'Hello')	#type(bytesarray)
my_memoryview = memoryview(b'Hello') #type(memoryview)

#None Type
my_variable = None		#type(NoneType)


print("<-----Printing the values of all variables----->")
print("Text Type: (str):",text)

print("Numeric Types:")
print("		int: ",number)
print("		float:",decimal)
print("		compelx:",complex_num)

print("Sequence Types:")
print("		list:",my_list)
print("		tuple:",my_tuple)
print("		range:",my_range)

print("Mapping Type (dict):",my_dict)

print("Set Types:")
print("		set:",my_set)
print("		frozenset:",my_frozenset)

print("Boolean Type (bool):",is_valid)
print("bool(\'hi\')",bool('hi'))
print("bool(\'\')",bool(''))
print("bool(0)",bool(0))

print("Binary Types:")
print("		bytes:",my_bytes)
print("		bytearray",my_bytearray)
print("		bytearray",my_memoryview)

print("None Type (NoneType):",my_variable)
print("----------------------------------------------------")

#-------python memory management-----------
#integer
a = 10
b = 10
print(a is b) #is keyword used for identity comparison
#both gives same address
print(id(a))
print(id(b)) #id show address of the variable
# integer is immutable
a = 257
print(id(a))
b = 257
print(id(b))#different address (id will change after 256)

#list
b = [1,2,3,4]
print(id(b))
b.append(5) #append 5 in the list b
print(id(b))
#list is mutable b is same after modifiying b

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(id(a))
print(id(b))
#value of the lists are same but not stored in same address 

#float
a = 1.3
b = 1.3
print(a is b)
print(id(a))
print(id(b))

#string
a = "this is string"
b = "this is string"
print(a is b)
print(id(a))
print(id(b))
#id is changed because of space

a = "this_is_string"
b = "this_is_string"
print(id(a))
print(id(b))
#id is not changed
#string is immutable

#tuple 
a = (1,2,3)
b = (1,2,3)
print(a is b)
print(id(a))
print(id(b))

#list,dictionaries and sets are mutable
#int,float,string,tubles are immutable

#type
print(type(a)) #type gets the datatype of variable 