# Write a Python program to rotate the digits of a number to the left by one position. For example, 12345 becomes 23451.
def rotate_left(number):
    number_str = str(number)
    if len(number_str) <= 1:
        return number
    rotated = number_str[1:] + number_str[0]
    return int(rotated)

# Example usage
num = 12345
print("Original number:", num)
print("After rotating left:", rotate_left(num))
