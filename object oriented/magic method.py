#__init__(self.other)
#__ lt__(self.other) less than<
#__le__(self.other)         less than equal<=
#__eq__(self.other)  equal==
#__ne__(self.other) not equal !=
#__gt__(self.other)       greater tahn>
#__ge__(self.other)  greater equal>=
#__add__(self.other)  +
#__sub__(self.other)  -
#__mul__(self.other)  *
#__div__(self.other)  /

#__str__(self) it is return,so we call return function

class Honda:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __str__(self):          #use magic method
        return (f"Name = {self.name},color={self.color}")       #__str__ for return function

    def show(self):
        print(f"Name = {self.name},color={self.color}")

b1=Honda("rtr","red")
b2=Honda("rtr","blue")
print(str(b1==b2))          #it can show false becaus it can compare object

#...........................................................................................................

class Honda:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __eq__(self, other):
        return self.name==other.name and self.color==other.color

    def __str__(self):          #use magic method
        return (f"Name = {self.name},color={self.color}")       #__str__ for return function

    def show(self):
        print(f"Name = {self.name},color={self.color}")

b1=Honda("rtr","red")
b2=Honda("rtr","red")
print(b1==b2)