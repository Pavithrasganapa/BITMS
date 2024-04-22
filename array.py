'''banana=[10,'pavi',25.00000,'p']
print(banana)

for i in banana:
    print(i,end="-")
print()
pine=[10,'pavi',25.00000,'p']
print(banana)
print(banana==pine)
banana[2]='sonu,pavi'
print(banana)
print(banana==pine)
pine[1:3]=(2,'pavi',345,466,'l')#value are dynamically added another word is appended
print(pine)
print(pine[4])
print()
clg=[10,20,30,40,50,60,70]
print(clg[1])
print(clg[-1])
print(clg[1:3])#traversing,n-1 concept for 3
print(clg[1:7])
#print(clg[7])#list index out of range
print(clg[:])#prints all the value
print(clg[-1:-3])#print empty
print(clg[-4:-1])#we should  assign always small value to large value
print(clg[3:-1])
print(clg[1:])
print(clg[:-1])
print(clg[0:4:2])#2 is step value increase by 2,4 is end index,0 is starting index
print(clg[0:4:3])
print(clg[0:6:3])

pavi=[1,2,3,4,5]#list variable
pra=[3,4,5,6]
sin=pavi+pra
print(sin)
print(type(pavi))
print(type(pra))
print(sin*2)
print(len(sin))
print(max(sin))
print(min(sin))

a=[10,2,3,4,6]
sum=0
for i in a:
    sum+=i
print(sum)'''

'''a=[10,25,37,40,57,65]
for i in a:
    if i%10==7:
        print(i)
        
a=[10,25,37,40,57,65]
for i in a:
    if i%10==5:
        print(i)'''
#remove duplicate value
p=[10,20,30,40,50,30,50]
s=[]
for i in p:
    if i not in s:
        s.append(i)
print(s)

p=[10,20,30]
s=[30,40,50]
for i in p:
    for j in s:
        if i==j:
            print(j)
p=tuple([1,2,3])
print(p)
print(type(p))

for i in range(-10,10,2):
    print(i+1)
print()
p=(10,20,30)#parenthisis tuple
s=tuple([30,40,50])
for i in p:
    for j in s:
        if i==j:
            print(j)
print()
a=tuple()
n=int(input("enetr n"))
for i in range(n):
    temp=int(input('enter ele'))
    a+=(temp,)
print('elementss')
'''for items in a:
    print(items,end=" ")'''
print(a)