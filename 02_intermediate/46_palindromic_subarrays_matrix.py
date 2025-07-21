# You are given a 2D matrix of integers. Your task is to find the number of palindromic subarrays in all possible rows and columns of the matrix.
# A subarray is palindromic if the sequence of elements is the same when reversed.

def count_palindromic_subarrays(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub = arr[i:j+1]
            if sub == sub[::-1]:
                count += 1
    return count

def total_palindromic_subarrays(matrix):
    total = 0

    # Count row-wise
    for row in matrix:
        total += count_palindromic_subarrays(row)

    # Count column-wise
    for col in zip(*matrix):
        total += count_palindromic_subarrays(list(col))

    return total

# Example usage
matrix = [
    [1, 2, 1],
    [3, 4, 3],
    [1, 2, 1]
]

print("Total palindromic subarrays:", total_palindromic_subarrays(matrix))
