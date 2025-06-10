# Create a class to represent a basic calculator with add, subtract, multiply, and divide methods.

class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

# Create an instance of Calculator
calculator = Calculator()

# Take input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Addition:", calculator.add(num1, num2))
    print("Subtraction:", calculator.subtract(num1, num2))
    print("Multiplication:", calculator.multiply(num1, num2))
    print("Division:", calculator.divide(num1, num2))
except ValueError:
    print("Invalid input. Please enter numeric values.")
