class Mango:
    def _init_(self):#init is a constructor,self is a default self parameter can be changed if we accesing the class variable we should access it with self param ex self.balance
        print("this is what?")
    def balaji(self):
        print("this is without para")
    def shetty(self,a,b):
        print(a+b,"this is with para")
    def magicalprime(self,a):
        prinf("check it magical prime or not")
    def neon(self,a):#5^2==5(25=2+5=7==5 not a neon)
        print("check neon or not")
man=Mango()#object created as man
man.balaji()
man.sheety(10,20)
man.magicalprime(10)
man.neon(5)