class Honor7s:
    def phonename(self):    #method phonename
        print("Honor 7s")
    def call(self): #method call
        print("call in system Well")

    def message(self):      #method message
        print("Hi")

class Honor8s(Honor7s): #(Honor7s) is inheritence
    def phonename(self):  #phonename is method
        print("Honor 8s")
    def flash(self):        #flash is method
        print("Flash is Good")
    def music(self):        #music is method
        print("Also Good")



h=Honor8s()
h.phonename()
h.call()
h.message()
h.flash()
h.music()
print(issubclass(Honor8s,Honor7s))      #Honor7s is super/sub class of Honor8s  (super/sub class is Honor7s)
