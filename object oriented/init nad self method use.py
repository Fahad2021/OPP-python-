class car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        print('I Am 1st')
CD=car(200,"red")

#....................................................
class car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color

CD=car(200,"red")
print(CD.speed,CD.color,"(I am 2nd)")