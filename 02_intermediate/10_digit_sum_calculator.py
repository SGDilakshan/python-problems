# Calculate the sum of digits of a given number

num = int(input("Enter the Number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("Sum of digits:", sum_of_digits)