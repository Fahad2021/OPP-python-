class Fahad:
    def Name(self):
        print("Name is Fahad")
    def eye(self):
        print("eye is Brown")
    def hair(self):
        print("Hair is Black")

class Akib(Fahad):  #inherit
    def Name(self):
        print("Name is akib")
    def eye(self):
        print("Eye is Black")
    def hair(self):
        print("hair is Curley")
f=Akib()
f.Name()
f.eye()
f.hair()
h=Fahad()
h.Name()
h.hair()
h.eye()


