# Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def info(self):
        return f"The area of the rectangle is {self.area()} and the perimeter of the rectangle is {self.perimeter()}."

# Create and display rectangle1
rectangle1 = Rectangle(3, 4)
print(rectangle1.info())

# Create and display rectangle2
rectangle2 = Rectangle(5, 6)
print(rectangle2.info())
