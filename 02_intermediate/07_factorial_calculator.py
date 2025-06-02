# Write a program that calculates the factorial of a given number

def factorial(n):
    if n < 0:
        return "Invalid Number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter the Number to find factorial: "))
print(f"Factorial of {num} is:", factorial(num))