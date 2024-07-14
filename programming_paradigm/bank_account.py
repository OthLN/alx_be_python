class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to account_balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the amount from account_balance if funds are sufficient.
        Returns True if successful, otherwise returns False.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")

if __name__ == "__main__":
    account = BankAccount(100)  
    account.deposit(50)
    account.withdraw(20)
    account.display_balance()
