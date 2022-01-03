# class area:
#     def __init__(self,h,w):
#         self.h=h
#         self.w=w
# rect=area(10,20)
# tri=area(20,30)
#
# print(rect.h*rect.w)
# print(0.5*(tri.h*tri.w))

class grav:
    def __init__(self,m,g):

        self.m=m
        self.g=g

gravi=grav(150,9.8)

print("F:",gravi.m*gravi.g)
