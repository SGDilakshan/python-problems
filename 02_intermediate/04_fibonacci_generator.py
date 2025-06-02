# Create a program that generates the Fibonacci sequence up to a given number of terms.

number_of_terms = int(input("Enter the number limit: "))
first = 0
second = 1

for i in range(0,number_of_terms):
    if i<2:
        next = i
    else:
        next = first+second
        first = second
        second = next
    print(next,end=" ")