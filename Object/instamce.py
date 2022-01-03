class partyAnimal:
    x=0
    name=""             #instance variable
    def __init__(self,z):
      self.name=z          #insatnce
      print(self.name,"constructed")

    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)

    def __del__(self):
        print("my total count",self.x,self.name)

s=partyAnimal("fahad")
y=partyAnimal("rahad")
r=partyAnimal("Rahim")

s.party()
y.party()
y.party()
y.party()
r.party()
r.party()
r.party()
r.party()
r.party()
r.party()
r.party()
r.party()


