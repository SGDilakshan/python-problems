# Calculate the area and circumference of a circle given its radius

import math

def calculate_area(r):
    return math.pi * (r ** 2)

def calculate_circumference(r):
    return 2 * math.pi * r

radius = float(input("Enter the radius: "))
print(f"Area of the circle: {calculate_area(radius):.2f}")
print(f"Circumference of the circle: {calculate_circumference(radius):.2f}")
