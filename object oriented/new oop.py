class Student:
    pass            #empty class/empty method
beg=Student()       #instance of student class          (beg is object)
shirt=Student()     #instance
pant=Student()      #instance
section=Student()   #instance
year=Student()          #instance

beg.color="blue"            #attribute
shirt.color="white"     #.......
pant.color="black"      #......
year.part="third year"      #attribute

print(beg.color)        #call attribute
print(shirt.color)
print(pant.color)
print(year.part)



class Rectangle:
    pass
rect1=Rectangle()
rect2=Rectangle()

rect1.height=20
rect2.height=30

rect1.width=20
rect2.width=30

print("Rect1:",rect1.height*rect1.width)
print("Rect2:",rect2.height*rect2.width)






