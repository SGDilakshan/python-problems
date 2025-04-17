# Implement a program that swaps the values of two variables.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

print(f"Before Swap: Number 1 = {num1}, Number 2 = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After Swap: Number 1 = {num1}, Number 2 = {num2}")
