
x1=input("enter the vale x1:")
x2=input("enter the vale x2:")
y1=input("enter the vale y1:")
y2=input("enter the vale y2:")
dx=abs(x2-x1)
dy=abs(y2-y1)
if (dx>=dy):
    step=dx
else:
    step=dy
    dx=dx/step
    dy=dy/step

    x=x1;
    y=y1;
    i=1
while(i<=step):
    putpixel(x,y,5)
    x=x+dx
    y=y+dx
    i=i+1





