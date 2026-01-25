class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")

    def display_details(self):
        super().display_details()
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def display_details(self):
        super().display_details()
        print(f"Overdraft Limit: {self.overdraft_limit}")

# Create instances of BankAccount and its subclasses
account1 = BankAccount("12345", "John Doe", 1000)
account2 = SavingsAccount("67890", "Jane Smith", 2000)
account3 = CheckingAccount("34567", "Alice Johnson", 1500)

# Perform operations on the accounts
account1.deposit(500)
account1.withdraw(200)
account1.display_details()

account2.deposit(1000)
account2.apply_interest()
account2.display_details()

account3.deposit(500)
account3.withdraw(2000)  # This will use the overdraft limit
account3.display_details()