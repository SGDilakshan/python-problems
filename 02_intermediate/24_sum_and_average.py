# Given a list of numbers, find the sum and average using built-in functions.

def sum_and_average(num):
    total_sum = sum(num)
    print("Sum:", total_sum)

    if num:
        avg = total_sum / len(num)
    else:
        avg = 0
    print("Average:", avg)

numbers = [1, 2, 3, 4, 10, -2]
sum_and_average(numbers)
