# Write a Python program that takes a decimal number as input and converts it to its binary representation without using the built-in bin() function.

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

num = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(num))
