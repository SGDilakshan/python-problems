# Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

nums = [1, 2, 3, 4]
print("Product of array except self:", product_except_self(nums))
