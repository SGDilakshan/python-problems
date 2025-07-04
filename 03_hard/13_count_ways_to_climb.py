# Write a Python function count_ways_to_climb(n, steps) that returns the number of distinct ways to climb a staircase with n steps, where you can climb any number of steps from the list steps at a time.

def count_ways_to_climb(n, steps, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n < 0:
        return 0

    total = 0
    for step in steps:
        total += count_ways_to_climb(n - step, steps, memo)

    memo[n] = total
    return total

# Example usage:
n = 5
steps = [1, 3, 5]
print("Number of ways to climb:", count_ways_to_climb(n, steps))
