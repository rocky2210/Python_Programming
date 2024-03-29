# Polymorphism

"""
    Polymorphism:
        Polymorphism is another fundamental concept in object-oriented programming (OOP) 
        that allows objects of different classes to be treated as objects of a common superclass. 
        It enables a single interface to represent multiple underlying data types and behaviors. 
        Polymorphism is often described as "one interface, multiple implementations."
"""

class Shape:
    def area(self):
        pass    # This method is defined in child classes
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
# Create instances of different shapes
rectangle = Rectangle(5,4)
circle = Circle(3)

# Calculate and print their areas
print(f"Rectangle area: {rectangle.area()}") 
print(f"Circle area: {circle.area()}")

"""
    Rectangle area: 20
    Circle area: 28.26
"""