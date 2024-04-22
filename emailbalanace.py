'''email="pavi@gmail.com"
em=input("enter ur email")
if email==em:
    print("it is eligible for transaction")
else:
    print("it not")
def withdraw(account,amount):
    if amount>account['balance']:
        print("insufficient amount")
    else:
        account['balance']-=amount
        account['transaction'].append(f"withdrawal:${amount}")#f is a format specifier
        print(f"withdrawal successful.remaing balance:${account['balance']}")
def deposit(account,amount):
    account['balance']+=amount
    account['transaction'].append(f"Deposit: ${amount}")
    print(f"deposit successful.remaining balance:${account['balance']}")
def get_balance(account):
    return account['balance']
def get_transcation_history(account):
    return account['transaction']
account={
    'balance':1000,
    'transaction':[]
    }
choices={
    '1':deposit,
    '2':withdraw,
    '3':get_balance,
    '4':get_transcation_history,
    '5':exit
    }
while True:
    if email!=em:
        break
    else:
        print("1.deposit")
        print("2.withdraw")
        print("3.get_balance")
        print("4.get_transcation_history")
        print("5.exit")
        choice=input("enetr ur choice")
        if choice==5:
            print("exiting program")
            break
        if choice in choices:
            if choice=='1' or choice=='2':
                amount=float(input("enter amount:"))
                choices[choice](account,amount)
            else:
                print(choices[choice](account))
        else:
            print("invalid choice. please try again.")'''
password=1234
def withdraw(account,amount):
    if amount>account['balance']:
        print("insufficient amount")
    else:
        pw=int(input('enter password'))
        if password==pw:
            account['balance']-=amount
            account['transaction'].append(f"withdrawal:${amount}")#f is a format specifier
            print(f"withdrawal successful.remaing balance:${account['balance']}")
def deposit(account,amount):
     pw=int(input('enter password'))
     if password==pw:
        account['balance']+=amount
        account['transaction'].append(f"Deposit: ${amount}")
        print(f"deposit successful.remaining balance:${account['balance']}")
def get_balance(account):
     pw=int(input('enter password'))
     if password==pw:
         return account['balance']
def get_transcation_history(account):
     pw=int(input('enter password'))
     if password==pw:
        return account['transaction']
account={
    'balance':1000,
    'transaction':[]
    }
choices={
    '1':deposit,
    '2':withdraw,
    '3':get_balance,
    '4':get_transcation_history,
    '5':exit
    }
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.get_balance")
    print("4.get_transcation_history")
    print("5.exit")
    choice=input("enetr ur choice")
    if choice==5:
        print("exiting program")
        break
    if choice in choices:
        if choice=='1' or choice=='2':
            amount=float(input("enter amount:"))
            choices[choice](account,amount)
        else:
            print(choices[choice](account))
    else:
        print("invalid choice. please try again.")
