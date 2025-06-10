# Implement a program that uses a Circle class to calculate the area and circumference of multiple circles.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def info(self):
        return f"The area of the circle is {self.area()} and the perimeter of the circle is {self.perimeter()}."

# Create Circle instances
circle1 = Circle(7)
circle2 = Circle(14)

# Display results
print(circle1.info())
print(circle2.info())
