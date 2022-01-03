#(2)#multi level inheritence)
class A:
    def Display1(self):
        print("i am inside in a")

class B(A):
    def Display2(self):
        print("i am inside in a,b")

class C(B):
    def Display3(self):
        super().Display1()                  #inherit display1
        super().Display2()                  #inherit display2
        print("i am inside in a,b,c")

c=C()
c.Display3()
print(issubclass(C,B))