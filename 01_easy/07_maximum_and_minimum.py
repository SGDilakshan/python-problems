# Given a list of numbers, find the maximum and minimum values.

numbers = [-5, 2, 4, 6, 7, 2, 4, 9, 6, 13, 1]

min_val = numbers[0]
max_val = numbers[0]

for i in numbers:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
