# Reduce a Number to a Single Digit by Summing its Digits Repeatedly

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

num = int(input("Enter a number: "))
print("Single digit sum:", digital_root(num))
