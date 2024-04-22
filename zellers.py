#f=k+[(13*m-1)/5]+D+[D/4+[C/4]-2*C
date=int(input("enter date 1-31"))
month=int(input("enter month 1-12"))
year=int(input("enter year"))
#for i in range(1):
if date|month|year<0:
    exit()
if month<3:#month==1 or month==2
    year-=1
    month+=12
q=date
m=month-2
d=year%100
c=year//100
#month=month-2
f=int((q+((13*m-1)/5)+d+(d/4)+(c/4)-(2*c)))%7
print(f)
if f==0:
    print("sunday")
elif f==1:
    print("monday")
elif f==2:
    print("tuesday")
elif f==3:
    print("wednsday")
elif f==4:
    print("thursday")
elif f==5:
    print("friday")
elif f==6:
    print("saturday")
else:
    print("no week")
#days_of_week=['sat','sunday','mon','tues','wed','thur','fri']
#print( days_of_week[f])