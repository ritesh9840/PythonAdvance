class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


# Creating an instance of the Circle class
my_circle = Circle(radius=5)
area = my_circle.calculate_area()
print(area);
