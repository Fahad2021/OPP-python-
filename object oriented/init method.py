class Rectangle:
    def __init__(self):
        print("I am serve the constructor,i'm not a constructor")

rect1=Rectangle()   #print("I am serve the constructor,i'm not a constructor")
rect2=Rectangle()   #print("I am serve the constructor,i'm not a constructor")

rect1.height=20
rect2.height=30

rect1.width=20
rect2.width=30

print("Rect1:",rect1.height*rect1.width)
print("Rect2:",rect2.height*rect2.width)

#.................................................................................................
class Car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        print("this is init")

audi=Car(300,"red")

class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color





