# Given a list of numbers, create a function to find the sum of all positive numbers.

def sum_of_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

numbers = [1, -2, 3, 4, -5, 6, 5, 1]
print("The sum of all positive numbers is:", sum_of_positive_numbers(numbers))