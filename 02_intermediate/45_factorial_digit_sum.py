# Write a Python program that takes a number n as input and returns the sum of all digits of n!

def factorial_digit_sum(n):
    from math import factorial
    fact = factorial(n)
    return sum(int(digit) for digit in str(fact))

# Example usage
n = int(input("Enter a number: "))
print("Sum of digits of", n, "factorial is:", factorial_digit_sum(n))
