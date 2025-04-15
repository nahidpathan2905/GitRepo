#single level
class Super:
    num1=10
    num=20
    def m1(self):
        print("method1 of super class")
    def m2(self):
        print("method2 of super class")
class Sub(Super):
    num2=20
    num=40
    def m3(self):
        print("method of sub class")
    def add(self):
        print(self.num1+self.num2)
    def add1(self):
        print(self.num+super().num)

s2=Sub()
s2.m1()
s2.m2()
s2.m3()
s2.add()
s2.add1()
#multi level
class insta:
    def story(self):
        print("instagram story")
class insta1(insta):
    def chat(self):
        print("direct messages")
class insta2(insta1):
    def vc(self):
        print("video calling")
i=insta2()
i.story()
i.chat()
i.vc()
#heirarchi inheritance
class Imran:
    def mobile(self):
        print("running mob method")
class Umayr(Imran):
    def car(self):
        print("running car method")
class Nahid(Imran):
    def laptop(self):
        print("running laptop method")
n=Nahid()
n.mobile()
n.laptop()

n1=Umayr()
n1.mobile()
n1.car()
#multiple inheritance
class Father:
    def mob(self):
        print("mob")
class father1:
    def home(self):
        print("home")
class son(father1,Father):
    def laptop(self):
        print("laptop")

s1=son()
s1.mob()
s1.home()
s1.laptop()






