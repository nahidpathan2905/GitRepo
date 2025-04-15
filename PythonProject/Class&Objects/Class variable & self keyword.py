
class Sample:
    num3=30
    num4=40
    def n1(self):
        print(self.num3+self.num4)
    def n2(self):
        num5=55    #local variable
        print(self.num3+self.num4+num5)
    def n3(self,num6):
        print(self.num3+num6)   #value of local variable should be pass in final calling statement with object

d1=Sample()
d1.n1()
d1.n2()
d1.n3(60)
print("------------------------------------")
class Demo:
    a,b=10,20
    def d1(self):
        print(self.a+self.b)
    def d2(self,c):
        print(self.a+c)
    def d3(self):
        d=44
        print(d)
a1=Demo()
a1.d1()
a1.d2(50)
a1.d3()


