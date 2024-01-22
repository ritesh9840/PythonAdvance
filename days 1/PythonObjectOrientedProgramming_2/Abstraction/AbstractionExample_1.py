from abc import ABC, abstractmethod

# Define an abstract class (interface) representing a shape


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Implement concrete classes based on the abstract class


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Create instances of concrete classes
circle = Circle(5)
square = Square(4)

# Use the abstraction to calculate area and perimeter without worrying about implementation details
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")
