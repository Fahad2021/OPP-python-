pos=-1
def seacrch(L,n):
    i=0
    while i<len(L):
        if L[i]== n:
            globals()['pos']=i
            return True
        i=i+1
    return False
L=[1,2,3,7,6,9,10]
n=6
if seacrch(L,n):
    print("Found at",pos+1)
else:
    print("Not Found")

pos=-1
def seacrch(L,n):
    i=0
    j=len(L)
    for i in range (j):
        if L[i] == n:
            globals()['pos']=i
            return True
        i=i+1
    return False

    
L=[1,2,3,7,6,9,10]
n=8
if seacrch(L,n):
    print("Found at",pos+1)
else:
    print("Not Found")

L=[1,4,5,67,45,89,100]
n=int(input("Enter your searching value:"))

for i in range (len(L)):
    if L[i]==n:
        print("Found it position",i+1)
        break

    else:
        print("Not found")




