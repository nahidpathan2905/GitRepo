# class Demo:
#     def __init__(self,name,Rollno):
#         print(name,Rollno)
#
# a1=Demo("Umayr",5)
class Sample2:
    def __init__(self,num1,num2):
        self.a=num1    #converting local variable into class variable
        self.b=num2
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

S1=Sample2(10,20)
S1.add()
S1.mul()

