# Bank Management System 

# Import necessary libraries
import random

# Define a class to represent customer accounts
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_number = random.randint(10000, 99999)  # Generate a random account number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"${amount} withdrawn successfully."
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return f"Account balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history

# Create a dictionary to store customer accounts
accounts = {}

# Function to create a new account
def create_account():
    account_holder = input("Enter the account holder's name: ")
    new_account = BankAccount(account_holder)
    accounts[new_account.account_number] = new_account
    print(f"Account created successfully. Your account number is: {new_account.account_number}")

# Function to perform transactions
def perform_transaction(account_number):
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Account holder: {account.account_holder}")
        print(account.get_balance())
        while True:
            print("\nTransaction Options:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Transaction History")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the amount to deposit: "))
                print(account.deposit(amount))
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                print(account.withdraw(amount))
            elif choice == '3':
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Account not found.")

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Create a New Account")
    print("2. Access an Existing Account")
    print("3. Exit")
    option = input("Enter your choice: ")

    if option == '1':
        create_account()
    elif option == '2':
        account_number = int(input("Enter your account number: "))
        perform_transaction(account_number)
    elif option == '3':
        print("Thank you for using our bank management system.")
        break
    else:
        print("Invalid choice. Please try again.")
