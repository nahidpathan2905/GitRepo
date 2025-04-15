#function without parameters
def addition():
    num1=20
    num2=45
    print(num1+num2)
addition()
print("---------------------------------------")
def demo():
    print("hi")
    print("hello")
demo()
demo()
print("-------fun with one int parameter--------------")
def squareOfNumber(num1):
    print(num1*num1)
squareOfNumber(7)
squareOfNumber(12)
print("-------fun with two int parameters--------------")
def addition(num1,num2):
    print(num1+num2)
addition(10,20)
addition(200,450)
addition(45,50)
print("-------fun with string parameter--------------")
def Stdname(name):
    print(name)
Stdname("Umayr")
Stdname("Nahid")

print("-------fun with multipe parameters of diff types--------------")
def StdInfo(name,rollNo,percentage,grade):
    print("Stdname:", name)
    print(rollNo)
    print(percentage)
    print(grade)
StdInfo("nahid",1,80,"A")
StdInfo("Imran",2,45.8,"A")
print("-------fun with positionals parameters--------------")
def greet(name,age):
    print("my name is:", name)
    print("age:",age)
greet("nahid",27)
greet(32,"Imran")

print("-------fun with keywords parameters--------------")
def greet(name,age):
    print("my name is:", name)
    print("age:",age)
greet(name="UMayr",age=2)       #order doesnt matter,provide keywords at time of passing values when calling fun
greet(age=3,name="IMran")


print("-------fun with default/optional parameters--------------")
def greet(name="Nahid",age=27):
    print("my name is:",name)
    print("age is:",age)
greet()
greet("abc",20)
greet("wer",34)