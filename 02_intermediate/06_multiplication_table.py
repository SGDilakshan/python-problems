# Implement a program that prints the multiplication table of a given number.

number = int(input("Enter the Number: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")