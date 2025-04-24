# Given a list of numbers, find the sum and average.

numbers = [2, 5, 7, -4, 3, 6, 4, 8, 8, 1]
total = 0

for i in numbers:
    total += i

print("Sum:", total)
print("Average:", total / len(numbers))

# Method - 2
# numbers = [2, 5, 7, -4, 3, 6, 4, 8, 8, 1]
#
# total = sum(numbers)
# average = total / len(numbers)
#
# print("Sum:", total)
# print("Average:", average)