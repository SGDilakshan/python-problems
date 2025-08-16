# Write a Python program that takes a list of numbers and counts how many numbers are multiples of 13.

def count_multiples_of_13(numbers):
    count = 0
    for num in numbers:
        if num % 13 == 0:
            count += 1
    return count

# Example usage
numbers = [13, 26, 39, 40, 52, 65, 70]
print("Number of multiples of 13:", count_multiples_of_13(numbers))
