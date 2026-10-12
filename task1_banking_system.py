
import hashlib
import getpass
from decimal import Decimal, InvalidOperation


class BankAccount:
    """Represents a single bank account."""

    def __init__(self, account_number, holder_name, password):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = Decimal("0.00")
        self.password_hash = self._hash_password(password)

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def authenticate(self, password):
        return self.password_hash == self._hash_password(password)

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."

        self.balance += amount
        return True, f"Deposit successful. Balance: {self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."

        if amount > self.balance:
            return False, "Insufficient funds."

        self.balance -= amount
        return True, f"Withdrawal successful. Balance: {self.balance:.2f}"

    def get_details(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.holder_name}\n"
            f"Balance: {self.balance:.2f}"
        )


class Bank:
    """Manages multiple bank accounts."""

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, holder_name, password):
        if not holder_name.strip():
            raise ValueError("Account holder name cannot be empty.")

        if len(password) < 4:
            raise ValueError("Password must contain at least 4 characters.")

        account_number = str(self.next_account_number)
        self.next_account_number += 1

        account = BankAccount(account_number, holder_name, password)
        self.accounts[account_number] = account

        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        return list(self.accounts.values())


def read_amount():
    """Read a valid monetary amount from the user."""
    try:
        amount = Decimal(input("Enter amount: ").strip())

        if not amount.is_finite():
            raise ValueError("Amount must be a finite number.")

        if amount.as_tuple().exponent < -2:
            raise ValueError("Use no more than two decimal places.")

        return amount.quantize(Decimal("0.01"))

    except (InvalidOperation, ValueError) as error:
        print(f"Invalid amount: {error}")
        return None


def main():
    bank = Bank()

    while True:
        print("\n========== SIMPLE BANKING SYSTEM ==========")
        print("1. Open account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check account details")
        print("5. List all accounts")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter account holder's name: ").strip()
            password = getpass.getpass("Create a password: ")

            try:
                account = bank.create_account(name, password)
                print("\nAccount created successfully!")
                print(f"Account number: {account.account_number}")
            except ValueError as error:
                print(error)

        elif choice in ("2", "3", "4"):
            account_number = input("Enter account number: ").strip()
            account = bank.get_account(account_number)

            if account is None:
                print("Account not found.")
                continue

            password = getpass.getpass("Enter your password: ")

            if not account.authenticate(password):
                print("Incorrect password.")
                continue

            if choice == "2":
                amount = read_amount()
                if amount is not None:
                    success, message = account.deposit(amount)
                    print(message)

            elif choice == "3":
                amount = read_amount()
                if amount is not None:
                    success, message = account.withdraw(amount)
                    print(message)

            else:
                print(account.get_details())

        elif choice == "5":
            accounts = bank.list_accounts()

            if not accounts:
                print("No accounts have been created.")
            else:
                for account in accounts:
                    print(
                        f"{account.account_number} - "
                        f"{account.holder_name} - "
                        f"Balance: {account.balance:.2f}"
                    )

        elif choice == "6":
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()