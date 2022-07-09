class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


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
        print(f"Balance {self.balance}")
        return self



    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

savings = BankAccount(.05, 3000)
checking = BankAccount(.02, 796)

savings.deposit(100).deposit(500).deposit(140).withdraw(280).yeild_interest().display_account_info()
checking.deposit(302).deposit(302).withdraw(100).withdraw(40).withdraw(130).withdraw(386).yeild_interest().display_account_info()