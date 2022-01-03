class Shape:
    def __init__(self,d1,d2):
        self.d1 = d1
        self.d2 = d2

    def __init__area(self):
        print("I am Area")

class Triangle(Shape):
    def area(self):
        area=0.5* self.d1*self.d2
        print("Area of triangle is:",area)

class Rectangle(Shape):         #method overrithing
    def area(self):
        area=self.d1*self.d2
        print("Area of Rectangle is:",area)


t1=Triangle(20,30)
t1.area()
r=Rectangle(50,50)
r.area()
