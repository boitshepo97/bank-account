class BankAccount:
    def __init__(self,balance,interest,monthly_fee):
        self.balance = balance
        self.interest = interest
        self.monthly_fee = monthly_fee

    def finish_month(self):
        """ This function will update the balance accordingly."""
        interest = (self.balance*self.interest)/12
        self.balance = self.balance + interest - self.monthly_fee
        return self.balance 
    
    def deposit(self):
        amount = float(input("Depositing amount: "))
        self.balance += amount
        return self.balance
        
    def withdraw(self): 
        amount = float(input("Withdrawing Amount: ")) 
        if self.balance <= amount: 
            self.balance -= amount 
            print("\n Insufficient balance") 
        else: 
            return self.balance 