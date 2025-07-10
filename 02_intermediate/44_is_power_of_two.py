# Write a function to check if a number is a power of 2.

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example Usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_power_of_two(num):
        print(f"{num} is a power of 2.")
    else:
        print(f"{num} is NOT a power of 2.")
