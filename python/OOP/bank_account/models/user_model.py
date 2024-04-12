# models/user_model.py
# from models.bank_account_model import CheckingAccount, SavingsAccount
from bank_account.models.bank_account_model import CheckingAccount, SavingsAccount


class User:
    def __init__(self, first_name, last_name, email, checking_balance=0, savings_balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.checking_account = CheckingAccount(balance=checking_balance)
        self.savings_account = SavingsAccount(balance=savings_balance)
        self.initial_transactions_made = False

    def open_savings_account(self, initial_deposit):
        self.savings_account.open_account(initial_deposit)
        return self

    def show_user(self):
        print(f"User: {self.first_name}, {self.last_name}")
        self.checking_account.display_account_info()
        self.savings_account.display_account_info()
        return self


    def make_transactions(self):
        if not self.initial_transactions_made:
            # John Doe opens a checking account with an initial deposit of $1000
            self.checking_account.deposit(1000)

            # John Doe attempts to open a savings account with an insufficient initial deposit
            self.open_savings_account(200)

            # John Doe opens a savings account with the required minimum deposit of $300
            self.open_savings_account(375)

            # John Doe deposits $500 into his savings account
            self.savings_account.deposit(500)
            # Set flag to True to indicate that initial transactions were made
            self.initial_transactions_made = True
        return self
