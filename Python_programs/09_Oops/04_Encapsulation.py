"""
    Public: No special naming convention (e.g., self.name)
    Protected: Prefix with a single underscore (e.g., _protected_attribute)
    Private: Prefix with a double underscore (e.g., __private_attribute)
"""

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.__roll_number = roll_number  # Private attribute

    def get_roll_number(self):
        return self.__roll_number  # Getter method

    def set_roll_number(self, roll_number):
        if roll_number > 0:
            self.__roll_number = roll_number  # Setter method

# Create a Student Object
student = Student("Alice",101)

# Access and modify attributes using getter and setter methods
print(student.get_roll_number())    # Output: 101
student.set_roll_number(102)
print(student.get_roll_number())   # Output : 102