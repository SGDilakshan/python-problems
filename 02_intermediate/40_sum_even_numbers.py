# Write a program that takes a list of numbers as input (comma-separated) and prints the sum of all even numbers in the list.

numbers = input("Enter numbers separated by commas: ")
num_list = [int(num.strip()) for num in numbers.split(",")]
even_sum = sum(num for num in num_list if num % 2 == 0)
print("Sum of even numbers:", even_sum)