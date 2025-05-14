# Write a program that checks if a given number is positive, negative, or zero.

class NumberChecker:
    def check(self, num):
        if num > 0:
            print(num, "is a Positive Number.")
        elif num < 0:
            print(num, "is a Negative Number.")
        else:
            print(num, "is Zero.")

number = int(input("Enter a number: "))
checker = NumberChecker()
checker.check(number)
