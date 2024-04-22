def magicalprime():
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if(flag==1):
        print("it is not prime")
    else:
        print("it is prime")
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
magicalprime()

    