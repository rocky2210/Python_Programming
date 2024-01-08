# abs() - 	Returns the absolute value of a number
num = -42.7
abs_num = abs(num)
print("abs(): Absolute value of", num, "is", abs_num)
print("----------")

# all() - Returns True if all items in an iterable object are true
iterable1 = [True, True, False]
iterable2 = [True, True, True]
print("all(): All elements in iterable1 are true:", all(iterable1))
print("all(): All elements in iterable2 are true:", all(iterable2))
print("----------")

# any() - Returns True if any item in an iterable object is true
print("any(): Any element in iterable1 is true:", any(iterable1))
print("any(): Any element in iterable2 is true:", any(iterable2))
print("----------")

# ascii() - Returns a readable version of an object. Replaces none-ascii characters with escape character
unicode_str = "Björn"
ascii_str = ascii(unicode_str)
print("ascii(): ASCII representation of", unicode_str, "is", ascii_str)
print("----------")

# bin() - Returns the binary version of a number
number = 42
binary_num = bin(number)
print("bin(): Binary representation of", number, "is", binary_num)
print("----------")

# bool() - Returns the boolean value of the specified object
empty_list = []
non_empty_list = [1, 2, 3]
print("bool(): Is the list empty?", bool(empty_list))
print("bool(): Is the list non-empty?", bool(non_empty_list))
print("----------")

# bytearray() - Returns an array of bytes
byte_array = bytearray([65, 66, 67])
print("bytearray(): Byte array:", byte_array)
print("----------")

# callable() - Returns True if the specified object is callable, otherwise False
def my_function(): 
    return "Hello, World!"

class MyClass:
    def my_method(self):
        return "Goodbye, World!"
print("callable(): Is my_function callable?", callable(my_function))
print("callable(): Is MyClass.my_method callable?", callable(MyClass.my_method))
print("----------")


# chr() - 	Returns a character from the specified Unicode code.
unicode_code = 65
character = chr(unicode_code)
print("chr(): Character with Unicode code", unicode_code, "is", character)
print("----------")

# complex() - Returns a complex number
complex_num = complex(3, 4)
print("complex(): Complex number:", complex_num)
print("----------")

# dict() - Returns a dictionary (Array)
my_dict = dict(name="Alice", age=30, city="New York")
print("dict(): Dictionary:", my_dict)
print("----------")

# dir() - Returns a list of the specified object's properties and methods
print("dir(): Properties and methods of list:", dir([]))
print("----------")

# divmod()- Returns the quotient and the remainder when argument1 is divided by argument2
result = divmod(10, 3)
print("divmod(): Quotient and remainder of 10 divided by 3:", result)
print("----------")

# enumerate() - Takes a collection (e.g. a tuple) and returns it as an enumerate object
fruits = ["apple", "banana", "cherry"]
enumerated_fruits = enumerate(fruits)
print("enumerate(): Enumerated fruits:", list(enumerated_fruits))
print("----------")

# globals() - Returns the current global symbol table as a dictionary
print("globals(): Global symbol table as a dictionary:", globals())
print("----------")

# hasattr() - 	Returns True if the specified object has the specified attribute (property/method)
class MyClass:
    my_attribute = 42

print("hasattr(): MyClass has 'my_attribute'?", hasattr(MyClass, "my_attribute"))
print("----------")

# hash() - Returns the hash value of a specified object
hash_value = hash("Hello, World!")
print("hash(): Hash value of 'Hello, World!':", hash_value)
print("----------")

# # help() - Executes the built-in help system
# help(list)
print("----------")

# hex() - 	Converts a number into a hexadecimal value
number = 255
hex_value = hex(number)
print("hex(): Hexadecimal representation of", number, "is", hex_value)
print("----------")

# max() - Returns the largest item in an iterable
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_num = max(numbers)
print("max(): Maximum number:", max_num)
print("----------")

# min() - Returns the smallest item in an iterable
min_num = min(numbers)
print("min(): Minimum number:", min_num)
print("----------")

# memoryview()- 	Returns a memory view object
data = bytes("Hello, World!", "utf-8")
memory_view = memoryview(data)
print("memoryview(): Memory view:", memory_view)
print("----------")

# oct() - Converts a number into an octal
number = 42
oct_value = oct(number)
print("oct(): Octal representation of", number, "is", oct_value)
print("----------")

# zip() - Returns an iterator, from two or more iterators
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 91]
zipped_data = list(zip(names, scores))
print("zip(): Zipped data:", zipped_data)
print("----------")
