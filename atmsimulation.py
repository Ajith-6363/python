class Atm:

    # Constructor
    def __init__(self):
        print("===================================")
        print("   Welcome to the ATM Machine")
        print("===================================")

        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):

    # If PIN is not created
      if self.pin == "":
        print("\n========== ATM MENU ==========")
        print("1. Create PIN")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.create_pin()

        elif choice == "2":
            print("Thank you for using our ATM.")
            exit()

        else:
            print("Invalid Choice")
            self.menu()

    # After PIN is created
      else:
        print("\n========== ATM MENU ==========")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.deposit_amount()

        elif choice == "2":
            self.withdraw()

        elif choice == "3":
            self.checkbalance()

        elif choice == "4":
            print("Thank you for using our ATM.")
            exit()

        else:
            print("Invalid Choice")
            self.menu()
    def create_pin(self):
        self.pin = input("Create your 4-digit PIN: ")
        print("PIN created successfully.")
        self.continue_in()
    # Deposit
    def deposit_amount(self):

        if self.pin == "":
            print("Please create your PIN first.")
            self.menu()
            return

        pin = input("Enter your PIN: ")

        if pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Amount deposited successfully.")
            print("Current Balance:", self.balance)
        else:
            print("Incorrect PIN.")

        self.continue_in()

    # Withdraw
    def withdraw(self):

        if self.pin == "":
            print("Please create your PIN first.")
            self.menu()
            return

        pin = input("Enter your PIN: ")

        if pin == self.pin:

            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", self.balance)
            else:
                print("Insufficient Balance.")

        else:
            print("Incorrect PIN.")

        self.continue_in()

    # Check Balance
    def checkbalance(self):

        if self.pin == "":
            print("Please create your PIN first.")
            self.menu()
            return

        pin = input("Enter your PIN: ")

        if pin == self.pin:
            print("Available Balance:", self.balance)
        else:
            print("Incorrect PIN.")

        self.continue_in()

    # Continue
    def continue_in(self):

        choice = input("\nPress 9 to continue or any other key to Exit: ")

        if choice == "9":
            self.menu()
        else:
            print("Thank you for using our ATM.")
            exit()


# Create Object
a = Atm()