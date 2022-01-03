class Tri:
    def __init__(self,base,height):   #constructor
        self.base=base          #object
        self.height=height      #object

    def calculate_area(self):           #Function
        Area=0.5*self.base*self.height
        print(f"Area is =",Area)

t1=Tri(10,30)       #object
#print(isinstance(t1,Tri))       #object check
t1.calculate_area() #function call
t2=Tri(60,70)       #object
t2.calculate_area() #functionn call