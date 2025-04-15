class Father:
    num1=10
    def car(self):
        print("Running car method from super class")
    def home(self):
        print("running Home method from super class")
    def money(self):
        print("running money method from super class")
class Son(Father):
    num2=20
    def mobile(self):
        print("running mobile method from sub class")
    def add(self):
        print(self.num1+self.num2)

A=Son()
A.car()
A.home()
A.money()
A.mobile()
A.add()