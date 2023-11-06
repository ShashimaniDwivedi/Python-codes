from abc import ABC, abstractmethod


# Define an abstract class (shape) with abstract method (area)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)

# Use the abstract method to calculate areas
print("Area of the circle:", circle.area())  # Outputs "Area of the circle: 78.5"
print("Area of the rectangle:", rectangle.area())  # Outputs "Area of the rectangle: 24"
