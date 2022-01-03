import math
def area(radius):
    temp = math.pi * radius**2
    return temp
print(area(45))

import math
radius=30
radians=45
e = math.exp(1.0)
height = radius * math.sin(radians)
print(height)

def absolute_value(x):
    if x <= 0:
        return
        -x
    else:
        return x
print(absolute_value(11))

def absolute_value(x):
    if x < 0:
        return -x
    if x>0:
        return x
print(absolute_value(0))

