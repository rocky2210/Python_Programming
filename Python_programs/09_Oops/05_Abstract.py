"""
Abstract Base Classes provide a way to define abstract methods and 
enforce that derived classes implement these methods.
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
print(f"Rectangle area: {rectangle.area()}") # Output: Rectangle area: 20