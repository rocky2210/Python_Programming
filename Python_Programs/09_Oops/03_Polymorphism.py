"""
Polymorphism allows objects of different classes to be treated as objects of a common base class. 
This enables you to write more flexible and generic code.
"""

class Shape:
    def area(self):
        pass  # This method is defined in child classes

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Create instances of different shapes
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calculate and print their areas
print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 20
print(f"Circle area: {circle.area()}")        # Output: Circle area: 28.274333882308138
