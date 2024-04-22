class BankAccount:
    def __init__(self,initial_balance):
        self.balance=initial_balance
        self.transaction= []
    def withdraw(shetty,amount):
        if amount>shetty.balance:
            print("insufficient amount")
        else:
            shetty.balance-=amount
            shetty.transaction.append(f"withdrawal:${amount}")#f is a format specifier
            print(f"withdrawal successful.remaing balance:${shetty.balance}")
    def deposit(self,amount):
        self.balance+=amount
        self.transaction.append(f"Deposit: ${amount}")
        print(f"deposit successful.remaining balance:${self.balance}")
    def get_balance(self):
        return self.balance
    def get_transaction_history(self):
        return self.transaction
account = BankAccount(1000)
print("balance",account.get_balance())
account.withdraw(200)
account.withdraw(500)
account.deposit(300)
print("balance",account.get_balance())
print("transaction",account.get_transaction_history())


#f=k+[(13*m-1)/5]+D+[D/4+[C/4]-2*C
