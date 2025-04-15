#instance method
class Sample1:
    def m1(self):
        print("without parameter")
    def m2(self,name):
        print("My name is", name)

s1=Sample1()
s1.m1()
s1.m2("Nahid")
#Static Method
class Sample2:
    @staticmethod
    def m3():
        print("without parameter")
    @staticmethod
    def m4(name):
        print("My name is", name)
Sample2.m3()
Sample2.m4("imran")


