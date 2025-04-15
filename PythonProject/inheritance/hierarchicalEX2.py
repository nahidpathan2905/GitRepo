class parent:
    def mobile(self):
        print("running mobile method")

class child1(parent):
    def car(self):
        print("running car method")

class child2(parent):
    def laptop(self):
        print("running laptop method")

s1=child1()
s1.mobile()
s1.car()

s2=child2()
s2.laptop()
s2.mobile()