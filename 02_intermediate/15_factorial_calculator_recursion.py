# Implement a function that returns the factorial of a given number using recursion.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter the number: "))
print("Factorial of", num, "is:", factorial(num))
