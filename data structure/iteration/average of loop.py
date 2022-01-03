sum=0
count=0
for value in[49,92,30,13]:
    count=count+1
    sum=sum+value
    print(count,sum,value)

print("After count:",count,"sum:",sum,"average:",sum//count)