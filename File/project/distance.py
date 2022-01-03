import math
def destence(x1,x2,y1,y2):
    dx=x2-x1
    dy=y2-y2
    dsquare=dx**2+dy**2
    result=math.sqrt(dsquare)
    return result
print("Distance is:",destence(3,34,5,56))