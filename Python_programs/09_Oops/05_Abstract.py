"""
    Abstract:
        Abstract Base Classes (ABCs) in Python are a way of enforcing certain methods to be 
        implemented by subclasses. They are used to define a blueprint for classes and ensure 
        that all subclasses adhere to a common interface. ABCs cannot be instantiated themselves; 
        instead, they are designed to be subclassed.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
# You cannot create an instance of an abstract class:
# shape = Shape() # This will raise a TypeError

# Create instances of a concreate subclass
rectangle = Rectangle(5,4)
print(f"Rectangle area: {rectangle.area()}") 
# Output: Rectangle area: 20