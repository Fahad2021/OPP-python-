from  abc import ABC,abstractmethod             #modiule abc
class Shape(ABC):                           #shape(ABC) is abstarctbase class
    def __init__(self,d1,d2):
        self.d1 = d1
        self.d2 = d2

    @abstractmethod                                                 #it is abstract method ,Abstarct base class creat in shape(ABC) top
    def area(self):
        # print("Shape Has no Area")
        pass          #it does not work beacause i can not creat it's body
class Triangle(Shape):
    def area(self):
        area=0.5* self.d1*self.d2
        print("Area of triangle is:",area)

class Rectangle(Shape):
    def area(self):
        area=self.d1*self.d2
        print("Area of Rectangle is:",area)

t1=Triangle(20,30)
t1.area()
r=Rectangle(50,50)
r.area()
