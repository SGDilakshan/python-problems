# Calculate the compound interest for a given principal amount, interest rate, and time period.

# Note
# A = P(1 + r/n)^(nt)
# A is the amount of money accumulated after n years, including interest.
# P is the principal amount (the initial amount of money).
# r is the annual interest rate (in decimal).
# n is the number of times that interest is compounded per year.
# t is the time the money is invested for, in years.

def compound_interest(principal_amount, rate, time, compounded_per_year):
    rate = rate / 100
    amount = principal_amount * (1 + rate / compounded_per_year) ** (compounded_per_year * time)
    interest = amount - principal_amount
    return interest

principal_amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period in years: "))
compounded_per_year = float(input("Enter the number of times interest is compounded per year: "))

print("Compound interest:", round(compound_interest(principal_amount, rate, time, compounded_per_year), 2))
