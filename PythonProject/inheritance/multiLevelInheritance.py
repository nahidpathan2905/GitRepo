class WA1:
    def sms(self):
        print("SMS")
class WA2(WA1):
    def ac(self):
        print("Audio Calling")
class WA3(WA2):
    def vc(self):
        print("Video Calling")

w=WA3()
w.sms()
w.ac()
w.vc()
