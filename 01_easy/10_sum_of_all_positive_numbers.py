# Given a list of integers, find the sum of all positive numbers.

numbers = [3, 6, 8, -4, 2, -1, -5, 3, 4]
positive_sum = 0

for i in numbers:
    if i > 0:
        positive_sum += i

print("Sum of the positive numbers is", positive_sum)
