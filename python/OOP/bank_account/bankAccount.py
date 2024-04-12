



class BankAccount:
    def __init__(self, account_type, int_rate=0.0, balance=0):
        self.account_type = account_type
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ${amount} into {self.account_type} account.')
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Withdrawn ${amount} from {self.account_type} account.')
        else:
            print("Insufficient funds")

        return self

    def display_account_info(self):
        print(f"{self.account_type} account balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"{self.account_type} account balance plus interest: ${self.balance}")
        return self


class CheckingAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__("Checking", int_rate=0.02, balance=balance)

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, minimum_deposit_required=300):
        super().__init__("Savings", int_rate=0.05, balance=balance)
        self.minimum_deposit_required = minimum_deposit_required

    def open_account(self, initial_deposit):
        if initial_deposit >= self.minimum_deposit_required:
            self.deposit(initial_deposit)
            print(f"{self.account_type} account opened with an initial deposit of ${initial_deposit}.")
        else:
            print(f"Insufficient funds to open a {self.account_type} account. Minimum deposit required: ${self.minimum_deposit_required}.")

class User:
    def __init__(self, first_name, last_name, email, checking_balance=0, savings_balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.checking_account = CheckingAccount(balance=checking_balance)
        self.savings_account = SavingsAccount(balance=savings_balance)

    def open_savings_account(self, initial_deposit):
        self.savings_account.open_account(initial_deposit)
        return self

    def show_user(self):
        print(f"User: {self.first_name}, {self.last_name}")
        self.checking_account.display_account_info()
        self.savings_account.display_account_info()
        return self

# Example usage:
John = User("John", "Doe", "JDoe@gmail.com")
John.show_user()

# Open a free checking account
John.checking_account.deposit(1000)
John.show_user()

# Attempt to open a savings account with insufficient funds
John.open_savings_account(200)
John.show_user()

# Open a savings account with the required minimum deposit
John.open_savings_account(500)
John.show_user()