class Father:
    def car(self):
        print("Running car method from super class")
    def home(self):
        print("running Home method from super class")
    def money(self):
        print("running money method from super class")
class Son(Father):
    def mobile(self):
        print("running mobile method from sub class")

A=Son()
A.car()
A.home()
A.money()
A.mobile()


