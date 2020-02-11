class BankAcount:
    def __init__(self,balance = 1000,interest = 0.12,fee = 50):
        self.balance = 1000
        self.interest = 12
        self.fee = 50

    def finish_month(self):
        """ This function will update the balance accordingly."""
        self.balance = self.balance + ((self.balance * 0.12)/ 12) - self.fee
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


M1 = BankAcount(1000)

print(f"R{M1.finish_month()}")

print(f"R{M1.deposit(300)}")
# class Bank:
#     def __init__(self):
      
      
#     def withdraw(bank_account_number,amount):
        
#     def deposit(bank_account_number,amount):
        
#     def transfer(from_bank_account_number,to_bank_account_number, amount):

# class Customer:
#     def __init__(self):
        
#     def set_password(self):