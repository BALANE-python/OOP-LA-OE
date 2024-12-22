#OE6

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
            print(f"Balance updated to: P{self._balance}.")
        else:
            print("Error: Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: P{amount}. New balance: P{self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: P{amount}. New balance: P{self._balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def display_account_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Current Balance: P{self._balance}.")  



account = BankAccount("10202004", 1000.0)
account.display_account_info()
account.deposit(200)
account.withdraw(150)
account.set_balance(-500)
account.set_balance(1200)  
account.display_account_info()