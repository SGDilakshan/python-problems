# Find the Missing Number in an Array

def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)

# Example usage
nums = [3, 0, 1]
print("Missing number:", find_missing_number(nums))
