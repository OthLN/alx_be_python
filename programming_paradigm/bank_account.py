import sys
from bank_account import create_bank_account

def main():
    deposit, withdraw, display_balance = create_bank_account(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        print(deposit(amount))
    elif command == "withdraw" and amount is not None:
        print(withdraw(amount))
    elif command == "display":
        print(display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()