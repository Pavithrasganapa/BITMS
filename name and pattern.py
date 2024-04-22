name=input('enter name')
length=len(name)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(name[i],end=" ")
        else:
            print(" ",end=" ")
    print()
name=input('enter name')
length=len(name)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(name[i],end=" ")
        else:
            print(" ",end=" ")
    print()
 
 
 
 
 
 
 
 
 
 
 
'''from datetime import date,datetime
today=date.today()
print("today=",today)
print("today day=",today.strftime('%A'))
now=datetime.now()
print("today time=",now.strftime('%H:%M:%S'))'''

