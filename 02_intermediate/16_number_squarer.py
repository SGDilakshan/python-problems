# Create a function to find the square of each element in a given list.

def square_numbers(numbers):
    return [i * i for i in numbers]

number_list = [-2, -3, 1, 2, 3, 5]
print("Squares:", square_numbers(number_list))
