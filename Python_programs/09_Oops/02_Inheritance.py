# Inheritance

"""
    Inheritance:
        Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass or derived class) 
        to inherit attributes and methods from an existing class (superclass or base class). This enables code reusability and promotes 
        the creation of hierarchical relationships between classes. Inheritance is represented as an "is-a" relationship, where a subclass 
        "is-a" type of its superclass.
"""

# Parent class (base class)

class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        pass   # This method is defined in child classes

# Child classes (derived class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow meoww!"
    
# create instances of child classes
dog = Dog("Rado")
cat = Cat("Leo")

# call the speak method of each object
print(dog.speak())  # Output: Rado says Woof woof!
print(cat.speak())  # Output: Leo says Meow meoww!

