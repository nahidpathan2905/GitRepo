a,b=20,30   #Global variable
class Sample6:
    a,b=10,20   #class variable
    def add(self):
        a,b=40,50   #local variable
        print(self.a+self.b)
        print(a+b)
        print(globals()['a']+globals()['b'])

a1=Sample6()
a1.add()