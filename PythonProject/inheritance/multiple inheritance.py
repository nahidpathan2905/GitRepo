class parent1:
    def mobile(self):
        print("running superclass")
class parent2:
    def home(self):
        print("running second super class")
class child(parent1,parent2):
    def car(self):
        print("running subclass")

c1=child()
c1.mobile()
c1.home()
c1.car()