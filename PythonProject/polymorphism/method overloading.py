class Sample:
    def add(self,a=0,b=0,c=0,d=0):
       print(a+b+c+d)
s=Sample()
s.add()
s.add(10,20)
s.add(10,20,30)
s.add(10,20,30,40)

class Sample1:
    def studentName(self,name):
        print(name)

a=Sample1()
a.studentName("Nahid")
a.studentName("Imran")
