# a=7/3
# print(a)
# b=7%3
# print(b)

def great(x,y):
 if(x>y):
    print("1,x is greater then y",x)
 elif(y>x):
    print("2,y is greater than x",y)

great(2,5)

def fun(x,y):
 if(x<=y)or(y>=x):
    print("Done")
fun(6,7)

count=0
for i in range(10):
    if(i%2==0):
        count=count+1
        print(count,i)
    else:
        False
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print (n,countdown(n-1))

countdown(8)