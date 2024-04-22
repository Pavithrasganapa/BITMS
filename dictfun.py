def pavi():
    return "this is my bank balance"
test_dict={"fname":pavi,"age":50,"address":"salem"}
print("the original dictionary is:"+str(test_dict))
res=test_dict['fname']()
print("the reqiured call result:"+str(res))
print()
def pavi(a,b):
    print("this is my bank balance",a+b)
test_dict={"fname":pavi,"age":50,"address":"salem"}
print("the original dictionary is:"+str(test_dict))
test_dict['fname'](10,20)
print()
#in python there is no switch case
for rollno in range(1,101):
    if rollno>50:
        break
    else:
        print("allowed to fest:",rollno)
print()
for rollno in range(1,101):
    if rollno==25 or rollno==50 or rollno==75:
        continue
    else:
        print("allowed to fest:",rollno)
print()
