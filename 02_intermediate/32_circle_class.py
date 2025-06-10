# Define a class for a Circle with methods to calculate its area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

# Create Circle instances
circle = Circle(7)
circle1 = Circle(10)

# Print results
print("Circle with radius 7:")
print("Area:", circle.area())
print("Circumference:", circle.circumference())

print("\nCircle with radius 10:")
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())
