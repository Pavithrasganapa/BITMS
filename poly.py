#method overloading does not support in python
#repr is a built-in function represntation of  object or class
class A:
     def magicalprime():
          n=int(input("enter num"))
          rev=0
          flag=0
          digit=n%10
          rev=(rev*10)+digit
          for i in range(2,rev):
              if rev%i==0:
                  flag=1;
                  break
          if(flag==1):
              print("it is not magicalprime")
          else:
              print("it is magicalprime")   
class B(A):
    def is_neon_number(num):
        square = num ** 2
        digits_sum = sum(int(digit) for digit in str(square))
        return digits_sum == num
        num = int(input("Enter a number: "))
        if is_neon_number(num):
            print(num, "is a neon number.")
        else:
            print(num, "is not a neon number.")
class C(A):
    def pattern():
        n=input('enter name')
        length=len(n)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(self.n[i],end=' ')
                else:
                    print(' ',end=' ')
            print()
class D(A):
    def reverse_string(input_string):
        return input_string[::-1]
    original_string=input('enetr the name')
    reversed_string=reverse_string(original_string)
    print(reversed_string)
d=D()
d.magicalprime()
class E(B,C):
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
e= E(1000)
print("balance",e.get_balance())
e.withdraw(200)
e.withdraw(500)
e.deposit(300)
print("balance",e.get_balance())
print("transaction",e.get_transaction_history())
e.is_neon_number()
e.pattern()