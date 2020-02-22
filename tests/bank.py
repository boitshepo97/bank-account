from bank_account import BankAccount

class Bank:
    def __init__(self, accounts, balance):
        self.__accounts = accounts
        self.balance = balance
   
    def withdraw(self,bank_account_number,amount):
        self.amount = float(input("Withdrawing Amount: ")) 
        if self.balance >= self.amount: 
            self.balance -= self.amount 
            return self.balance  
        else: 
            return "Insufficient balance"
        
    def deposit(self,bank_account_number,amount):
        self.amount = float(input("Depositing amount: "))
        self.balance += self.amount
        return bank_account_number, self.balance
    
    def transfer(self,from_bank_account_number,to_bank_account_number, amount):
        self.amount = float(input("Transfer Amount: "))
        if self.balance >= self.amount:
            self.balance -= self.amount
            print(self.balance)
            return "Transfer Successful"  
        else: 
            return "Insufficient Funds"
     