class BankAccount:
    def __init__(self,balance,interest_rate,monthly_fee,customer):
        self.balance =balance
        self.interest_rate = interest_rate
        self.monthly_fee = monthly_fee
        self.customer = customer

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self,amount):
        if self.balance <= 0:
            return 'insufficient funds'
        else:
            self.balance -= amount
    def transfer(self,amount):
        self.balance -= amount
        return self.balance

    def finish_month(self):
        self.balance = self.balance + self.balance*self.interest_rate/12 - self.monthly_fee
        return self.balance