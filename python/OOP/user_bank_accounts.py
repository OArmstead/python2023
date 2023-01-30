class Bank_Account:
    accounts = []
    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >=0:
            self.balance -= amount
        else:
            print('Insufficient Funds: Charging a $5 fee')
            self.balance -= 5
            return self 
    def show_account_info(self):
        print('Balance: {}'.format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    bank_name = 'Brooklyn National Bank'
    def __init__(self,name):
        self.name = name
        # self.amount = 0
        self.account = {'Checking': Bank_Account(.04,300),
                        'Savings': Bank_Account(.06,500)}
        
def show_user_balance(self):
    
        print('User: {}, Checking Balance:{}'.format(self.name, self.account['checking'].show_account_info()))
        print('User: {}, Saving Balance:{}'.format(self.name, self.account['savings']))
        
def transfer_money(self,amount,user):
    self.amount -= amount
    user.amount += amount
    self.show_user_balance()
    user.show_user_balance()


brian = User ('Brian McNight')


steve = User ('Steve Nash')
steve.bank_name = ("New York City Bank")


amare = User ("Amar'e Stoudamire")
amare.bank_name = ("Pheonix Bank of America")

amare.account['Checking'].deposit(100)
amare.show_user_balance()