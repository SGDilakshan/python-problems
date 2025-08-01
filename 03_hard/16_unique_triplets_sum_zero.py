# Find All Unique Triplets That Sum to Zero

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

nums = [-1, 0, 1, 2, -1, -4,5,2,7,-9,-5]
print(three_sum(nums))
