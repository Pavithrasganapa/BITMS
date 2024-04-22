'''x=5
y='john'
print(x)
print(y)

x,y,z='orangre','mango','cherry'
print(x,y,z)

x="pavi"
y="thra"
print(x+y)

a=b=c=d=55
print(c)

x="john"
x='John'
print(x,x)
a,b=10,20
c='balu'
#d=a+b+c error due to different datatype
#print(d)

a=50
print(a)

#print("my age="+a)
print("my age=",a)
x=~5
print(x)
#print(~x)
x+=10
print(x)
x-=10
print(x)
#x**=10
#print(x)
x//=10
print(x)
x=6//10
print(x)
a=25
#a<<=3
a<<=5
print(a)
n='pavi'
print('i' in n)
print('i' not in n)
a=[5,4,3]
#print(5 in 10)#single character cannot be execute
print(5 in a)
print(50 not in a)
a=5
b=5
print(a is b)
a=5
b=5.0
print(a is not b)
print(a is b)
if(5>10):
    print("yes")
else:
    print("no")
age1=int(input('age1='))
age2=int(input('age2='))
if(age1>age2):
    age3=age1+age2
    print('age3 added',age3)
else:
    age3=age1-age2
    print('age3 subtracted',age3)'''
email='Pavi@gmail.com'
password=4567
uemail=input('emailid=')
upassword=int(input('password='))
if(email==uemail):
    if(password==upassword):
        print("login succesful")
    else:
        print("login unsuccesful due to password")
else:
    print("login unsuccesful due to email")
email='Pavi@gmail.com'
password=4567
otp=6789
uemail=input('emailid=')
upassword=int(input('password='))
if(email==uemail and password==upassword):
     print("login succesful")
     uotp=int(input('otp='))
     if(otp==uotp):
          print('succesful transcation')
     else:
         print('unsuccesful transcation')
else:
    print("login unsuccesful")