import math

# Base Class - Shape
class Shape:
    def area(self):
        # This method is meant to be overridden by derived classes
        raise NotImplementedError("Subclasses must implement the area method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate area of rectangle (length * width)
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate area of circle (π * radius²)
        return math.pi * self.radius ** 2

def main():
    # Creating instances of Rectangle and Circle
    shapes = [
        Rectangle(10, 5),  # Rectangle with length=10 and width=5
        Circle(7)          # Circle with radius=7
    ]

    # Loop through each shape and print its area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
