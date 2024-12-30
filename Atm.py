# Author : Samridhi Gupta
# Date   : 30/12/2024
# Project : ATM

class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_choice = input("""
        Hello, How would you like to proceed?
        1. Insert Pin
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        """)
        if user_choice == "1":
            self.insert_pin()
        elif user_choice == "2":
            self.check_balance()
        elif user_choice == "3":
            self.deposit()
        elif user_choice == "4":
            self.withdraw()
        elif user_choice == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid Choice. Please try again.")
            self.menu()
            

    def insert_pin(self):
        self.pin = input("Enter your new pin (4 digits): ")
        if len(self.pin) == 4 and self.pin.isdigit():
            print("Pin set successfully.")
        else:
            print("Invalid pin. Please enter a 4-digit pin.")
            self.insert_pin()
        self.menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is ${self.balance:.2f}")
        else:
            print("Incorrect Pin.")
        self.menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print("Deposit successful.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Incorrect Pin.")
        self.menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            try:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= self.balance:
                    self.balance -= withdraw_amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Incorrect Pin.")
        self.menu()

# Object instantiation
sbi = Atm()
