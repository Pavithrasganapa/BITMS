class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class professor(person):
    def isprofessor(self):
        return f"{self.name} is a professor"
sir=professor('balaji',30)
print(sir.isprofessor())
print()
class a:
    num1=2
class b:
    num2=3
class c(a,b):
    def sum(self):
        return self.num1+self.num2
c1=c()
print(c1.sum())
print()
class a:
    num1=2
    def home(self,x,y):
        self.x=x
        self.y=y
        print("property value=",self.x+self.y)
class b:
    num2=3
    def jewel(self,x):
        self.x=2000
        print("jewel value=",self.x)
class c(a,b):
    def sum(self):
        return self.num1+self.num2
c1=c()
c1.sum()
c1.home(1000000,4000000)
c1.jewel(10000)