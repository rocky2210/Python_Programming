text = "    Hello, World!   "

# 1. strip(): Removes leading and trailing whitespace
stripped_text = text.strip()
print("1. Stripped Text:", stripped_text)
"""
    Output:
        Stripped Text: Hello, World!
"""
print("---------")



# 2. lower(): Converts the string to lowercase
lowercase_text = text.lower()
print("2. Lowercase Text:", lowercase_text)
"""
    Output: 
        Lowercase Text:     hello, world!
"""
print("---------")



# 3. upper(): Converts the string to uppercase
uppercase_text = text.upper()
print("3. Uppercase Text:", uppercase_text)
"""
    Output: 
        Uppercase Text:     HELLO, WORLD! 
"""
print("---------")



# 4. replace(): Replaces a substring with another substring
replaced_text = text.replace("World", "Universe")
print("4. Replaced Text:", replaced_text)
"""
    Output: 
        Replaced Text:     Hello, Universe! 
"""
print("---------")



# 5. split(): Splits the string into a list of substrings based on a delimiter
split_text = text.split(',')
print("5. Split Text:", split_text)
"""
    Output: 
        Split Text: ['    Hello', ' World!   ']
"""
print("---------")



# 6. join(): Joins a list of strings into a single string using a delimiter
joined_text = '-'.join(split_text)
print("6. Joined Text:", joined_text)
"""
    Output: 
        Joined Text:     Hello- World!
"""
print("---------")


text = "Python is a versatile programming language"

# 7. find(): Searches for a substring and returns the index of the first occurrence
index = text.find("programming")
print("7. Index of 'programming':", index)
"""
    Output: 
        Index of 'programming': 16
"""
print("---------")



# 8. count(): Counts the number of non-overlapping occurrences of a substring
count = text.count("a")
print("8. Count of 'a':", count)
"""
    Output:
        Count of 'a': 3
"""
print("---------")

# 9. startswith(): Checks if the string starts with a specified prefix
startsWith = text.startswith("Python")
print("9. Starts with 'Python':", startsWith)
"""
    Output:
        Starts with 'Python': True
"""
print("---------")



# 10. endswith(): Checks if the string ends with a specified suffix
endsWith = text.endswith("language")
print("10. Ends with 'language':", endsWith)
"""
    Output: 
        Ends with 'language': True
"""
print("---------")



# 11. isalpha(): Checks if the string consists of alphabetic characters only
alpha_check = text.isalpha()
print("11. Is the string alphabetic?", alpha_check)
"""
    Output: 
        Is the string alphabetic? False
"""
print("---------")



# 12. isdigit(): Checks if the string consists of digits only
number = "12345"
digit_check = number.isdigit()
print("12. Is the string a digit?", digit_check)
"""
    Output: 
        Is the string a digit? True
"""
print("---------")



# 13. splitlines(): Splits the string at line breaks and returns a list
multiline_text = "Line 1\nLine 2\nLine 3"
lines = multiline_text.splitlines()
print("13. Split lines:", lines)
"""
    Output: 
        Split lines: ['Line 1', 'Line 2', 'Line 3']
"""
print("---------")



# 14. center(): Centers the string within a specified width with padding
centered_text = text.center(40, "-")
print("14. Centered Text:", centered_text)
"""
    Output: 
        Centered Text: Python is a versatile programming language
"""
print("---------")



# 15. isupper(): Checks if the string is in uppercase
uppercase_check = text.isupper()
print("15. Is the string in uppercase?", uppercase_check)
"""
    Output: 
        Is the string in uppercase? False
"""
print("---------")



# 16. islower(): Checks if the string is in lowercase
lowercase_check = text.islower()
print("16. Is the string in lowercase?", lowercase_check)
"""
    Output: 
        Is the string in lowercase? False
"""
print("---------")



# 17. rstrip(): Removes trailing whitespace
right_stripped_text = text.rstrip()
print("17. Right Stripped Text:", right_stripped_text)
"""
    Output: 
        Right Stripped Text: Python is a versatile programming language
"""
print("---------")



# 18. lstrip(): Removes leading whitespace
left_stripped_text = text.lstrip()
print("18. Left Stripped Text:", left_stripped_text)
"""
    Output: 
        Left Stripped Text: Python is a versatile programming language
"""
print("---------")



# 19. capitalize(): Converts the first character to uppercase and the rest to lowercase
capitalized_text = text.capitalize()
print("19. Capitalized Text:", capitalized_text)
"""
    Output: 
        Capitalized Text: Python is a versatile programming language
"""
print("---------")



# 20. swapcase(): Swaps the case of each character in the string
swapped_case_text = text.swapcase()
print("20. Swapped Case Text:", swapped_case_text)
"""
    Output: 
        Swapped Case Text: pYTHON IS A VERSATILE PROGRAMMING LANGUAGE
"""
print("---------")



# 21. title(): Converts the string to title case (each word starts with an uppercase letter)
title_text = text.title()
print("21. Title Case Text:", title_text)
"""
    Output: 
        Title Case Text: Python Is A Versatile Programming Language
"""
print("---------")



# 22. isalnum(): Checks if the string consists of alphanumeric characters only
alphanumeric_check = text.isalnum()
print("22. Is the string alphanumeric?", alphanumeric_check)
"""
    Output: 
        Is the string alphanumeric? False
"""
print("---------")



# 23. isspace(): Checks if the string consists of whitespace characters only
whitespace_check = text.isspace()
print("23. Is the string whitespace?", whitespace_check)
"""
    Output: 
        Is the string whitespace? False
"""
print("---------")



# 24. zfill(): Pads the string with zeros to a specified width
padded_text = "42".zfill(5)
print("24. Padded Text:", padded_text)
"""
    Output: 
        Padded Text: 00042
"""
print("---------")



# 25. partition(): Splits the string into three parts based on the first occurrence of a specified substring
partitioned_text = text.partition("a")
print("25. Partitioned Text:", partitioned_text)
"""
    Output: 
        Partitioned Text: ('Python is ', 'a', ' versatile programming language')
"""
print("---------")



# 26. rjust(): Right-justifies the string within a specified width with padding
right_justified_text = text.rjust(40, "#")
print("26. Right Justified Text:", right_justified_text)
"""
    Output: 
        Right Justified Text: ####Python is a versatile programming language
"""
print("---------")



# 27. ljust(): Left-justifies the string within a specified width with padding
left_justified_text = text.ljust(40, "*")
print("27. Left Justified Text:", left_justified_text)
"""
    Output: 
        Left Justified Text: Python is a versatile programming language*********
"""
print("---------")



# 28. find(): Searches for a substring and returns the index of the first occurrence
index = text.find("programming")
print("28. Index of 'programming':", index)
"""
    Output: 
        Index of 'programming': 16
"""
print("---------")



# 29. rfind(): Searches for a substring and returns the index of the last occurrence
last_index = text.rfind("a")
print("29. Last Index of 'a':", last_index)

"""
    Output: 
        Last Index of 'a': 35
"""
print("---------")



# 30. expandtabs(): Replaces tab characters with spaces
tabbed_text = "Tab\tSeparated\tText"
expanded_text = tabbed_text.expandtabs(4)
print("30. Expanded Tabs Text:", expanded_text)
"""
    Output: 
        Expanded Tabs Text: Tab Separated  Text
"""
print("---------")
