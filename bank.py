from bank_account import BankAccount

class Bank:
    def __init__(self,accounts):
        self.__accounts = accounts
        
    def withdraw(self,bank_account_number,amount,password):
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            if account is None:
                raise Exception("Account does not exist.")

            if account.customer.check_password(password) is False:
                raise Exception("wrong password")
        else:
            raise Exception("invalid account number")


        account.withdraw(amount)
        return account.balance

    
    def deposit(self,bank_account_number,amount):
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            if account is None:
                raise Exception("Account does not exist.")

        else:
            raise Exception("invalid account number")

        account.deposit(amount)
        return account.balance



    def transfer(self,bank_account_number,amount,password):


        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            if account is None:
                raise Exception("Account does not exist.")

            if account.customer.check_password(password) is False:
                raise Exception("wrong password")
        else:
            raise Exception("invalid account number")


        account.transfer(amount)
        return account.balance

     