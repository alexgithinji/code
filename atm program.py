class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

def main():
    atm = ATM()

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            balance = atm.check_balance()
            print(f"Your balance is ksh 4{balance}")
        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            message = atm.deposit(amount)
            print(message)
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            message = atm.withdraw(amount)
            print(message)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
