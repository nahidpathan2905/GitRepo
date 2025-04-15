a,b=20,30   #Global variable
class Sample6:
    c,d=10,20   #class variable
    def add(self):
        print(self.c+self.d)
    def mul(self,e,f):   #local variable
        print(e*f)
    def add1(self):
        t,y=30,40
        print(t+y)
        print(a+b)
        print(a*b)


a1=Sample6()
a1.add()
a1.mul(2,4)
a1.add1()

