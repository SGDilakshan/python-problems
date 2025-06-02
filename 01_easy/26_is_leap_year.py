# Create a program that takes a year as input and checks if it is a leap year or not.

year = int(input("Enter your year: "))

if (year%4==0 and year%100 !=0) or (year%400 ==0):
    print(year,"Leap Year...")
else:
    print(year,"Not a Leap Year...")