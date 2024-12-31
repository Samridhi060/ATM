# Author : Samridhi Gupta
# Date   : 30/12/2024
# Project : ATM

class Atm:
    # Constructor
    def __init__(self):
        # Private Attributes
        self.__pin = ""
        self.__balance = 0
        self.__menu()

    def __menu(self):
        user_choice = input("""
        Hello, How would you like to proceed?
        1. Set Pin
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Change Pin
        6. Get Pin
        7. Exit
        """)
        if user_choice == "1":
            self.set_pin()
        elif user_choice == "2":
            self.check_balance()
        elif user_choice == "3":
            self.deposit()
        elif user_choice == "4":
            self.withdraw()
        elif user_choice == "5":
            self.change_pin()
        elif user_choice == "6":
            self.get_pin()
        elif user_choice == "7":
            print("Goodbye!")
            exit()
        else:
            print("Invalid Choice. Please try again.")
            self.__menu()

    def set_pin(self):
        new_pin = input("Enter your new pin (4 digits): ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("Pin set successfully.")
        else:
            print("Invalid pin. Please enter a 4-digit pin.")
        self.__menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your balance is ${self.__balance:.2f}")
        else:
            print("Incorrect Pin.")
        self.__menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.__balance += amount
                    print("Deposit successful.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Incorrect Pin.")
        self.__menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            try:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= self.__balance:
                    self.__balance -= withdraw_amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Incorrect Pin.")
        self.__menu()

    def change_pin(self):
        self.set_pin()  # Reuse the set_pin method

    def get_pin(self):
        print("Warning: Displaying your PIN is not secure.")
        print(f"Your pin is {self.__pin}")
        self.__menu()

# Object instantiation
sbi = Atm()
