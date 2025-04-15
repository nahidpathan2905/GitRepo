class Father:
    def home(self):
        print("running home method from Super class")

class Son1(Father):
    def car(self):
        print("running car method from Base class")

class Son2(Father):
    def laptop(self):
        print("running laptop method from Base class")

s1=Son1()
s1.car()
s1.home()

s2=Son2()
s2.laptop()
s2.home()
