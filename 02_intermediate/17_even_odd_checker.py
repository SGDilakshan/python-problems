# Write a function to check if a number is even or odd and return “Even” or “Odd” accordingly.

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_or_odd(3))
print(even_or_odd(6))
