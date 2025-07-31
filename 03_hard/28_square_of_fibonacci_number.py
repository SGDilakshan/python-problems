# Find the Square of the Nth Fibonacci Number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def square_of_fibonacci(n):
    fib = fibonacci(n)
    return fib * fib

# Example usage
n = int(input("Enter a number: "))
print(f"Square of {n}th Fibonacci number is:", square_of_fibonacci(n))
