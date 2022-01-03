class partyAni:
    x=0

    def __init__(self):
     print("I am const")

    def cat(self):
        self.x = self.x + 1
        print("hi", self.x)

    def __del__(self):
        print("i'm construsted", self.x)



an = partyAni()
an.cat()
an.cat()
an = 23
print('an contains', an)

