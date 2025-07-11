# Given an N x M matrix of integers, count how many "peaks" are present. A cell is considered a peak if its value is strictly greater than all of its up/down/left/right neighbors.

def count_peaks(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            is_peak = True
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] >= matrix[i][j]:
                        is_peak = False
                        break
            if is_peak:
                count += 1

    return count


matrix = [
    [1, 4, 3],
    [6, 5, 2],
    [1, 8, 1]
]

print("Number of peaks:", count_peaks(matrix))
