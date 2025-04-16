# Write a program that converts a given number of days into years, weeks, and month.

days = int(input("Enter the number of days: "))

year = days // 365
remaining_days = days % 365
month = remaining_days // 30
remaining_days %= 30
week = remaining_days // 7
remaining_days %= 7


print(f"{days} days contains {year} years, {month} months, {week} weeks, and {remaining_days} days.")