class BankAccount:
    accounts = [] 
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if (self.balance - amount) >=0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self

    def display_account_info(self):
        return f"{self.balance}"
        



    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

    @classmethod
    def print_all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()

savings = BankAccount(.05, 3000)
checking = BankAccount(.02, 796)

savings.deposit(100).deposit(500).deposit(140).withdraw(280).yeild_interest().display_account_info()
checking.deposit(302).deposit(302).withdraw(100).withdraw(40).withdraw(130).withdraw(386).yeild_interest().display_account_info()

class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            'savings' : BankAccount(.05, 3000),
            'checking' : BankAccount(.02, 796)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance
        user.display_user_balance

daniel = User("Daniel")

daniel.account['savings'].deposit(500)
daniel.display_user_balance()