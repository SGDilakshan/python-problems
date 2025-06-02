# Given a list of integers, find all the even numbers and store them in a new list.

numbers = [2, 23, 45, -12, 45, 2, 3, 7, -9, -2, 4, 6, 1, 3, 30]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)