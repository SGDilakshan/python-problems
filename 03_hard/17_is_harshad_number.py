# Write a Python program to check whether a number is a Harshad number (a number divisible by the sum of its digits).

def is_harshad_number(n):
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0

# Example usage
number = 18
print("Is Harshad Number?", is_harshad_number(number))
