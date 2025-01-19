import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")  # Format the deposit message

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current Balance: ${self.account_balance:.2f}")  # Format the balance to 2 decimal places


def main():
    # Initialize the bank account with a starting balance of 100
    account = BankAccount(100)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Execute the appropriate banking operation based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")  # Format the withdraw message
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Valid commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()
