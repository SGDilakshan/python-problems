# Implement a program that simulates a basic bank account using a BankAccount class.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs{amount} successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs{amount} successful.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: Rs{self.balance}")

# Example usage
bank_account = BankAccount("123456789", "Dilakshan", 1000)

bank_account.deposit(500)
bank_account.display_balance()

bank_account.withdraw(200)
bank_account.display_balance()
