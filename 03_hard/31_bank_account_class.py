# Create a Bank Account Class with Basic Operations
#
# Design a BankAccount class in Python with the following features:
# Attributes:
# account_holder(string)
# balance(float, default is 0)

# Methods:
# deposit(amount) → adds amount to balance
#
# withdraw(amount) → subtracts amount if enough balance exists
#
# display_balance() → prints current balance

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Balance for {self.account_holder}: ${self.balance:.2f}")

account = BankAccount("Alice")
account.deposit(1000)
account.withdraw(300)
account.display_balance()
