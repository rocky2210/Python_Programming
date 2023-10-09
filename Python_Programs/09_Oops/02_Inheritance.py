# Parent class (base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method is defined in child classes

# Child classes (derived classes)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of each object
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
