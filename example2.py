'''num1=int(input("enetr the num1"))
num2=int(input("enetr the num2"))
if(num1>num2):
    print('num1 is greater',num1)
elif(num2>num1):
    print('num2 is greater',num2)
else:
    print("num1=num2 is equal")

num1=int(input("enetr the num1"))
num2=int(input("enetr the num2"))
print('num1 is greater' if num1>num2 else 'both are equal' if num1==num2 else 'num2 is greater')

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print('a' if a>b and a>c and a>d and a>e else 'b' if b>c and b>d and b>e else 'c' if c>d and c>e else 'd' if d>e else 'e')'''
'''print(chr(3242)+chr(3253)+chr(3263)+chr(3236)+chr(3262))
for i in range(65,91):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()
for i in range(1,11):
    print(i/10,end=' ')'''
a=-5
print(abs(a))
print(pow(2,3))
import math
a=math.sqrt(5)
print(a)
b=math.ceil(a)
print(b)
c=math.floor(a)
print(c)
print(math.ceil(5.00))
import keyword
print(keyword.kwlist)
def pavi():
    for i in range(1,11):
        print(i,'* 10=',i*10)
pavi()
def pra():
    n=int(input("enter a leap year"))
    if(n%400==0):
        print('leap year')
    else:
        print('its not a leap year')
pra()
