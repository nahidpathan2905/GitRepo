class grandfather:
    def home(self):
        print("2bhk")
    def mobile(self):
        print("iphone")
    def car(self):
        print("kia")
class father(grandfather):
    def home(self):
        print("3bhk")
    def mobile(self):
        print("iplus")
    def car(self):
        print("thar")
class son(father):
    def home(self):
        print("1bhk")
    def mobile(self):
        print("moto")
    def car(self):
        print("brezza")
g=grandfather()
g.car()
g.home()
g.mobile()
f=father()
f.home()
f.mobile()
f.car()
s=son()
s.car()
s.mobile()
s.home()