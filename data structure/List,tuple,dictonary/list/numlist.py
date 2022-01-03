numlist=list()
while True:
    inp=input("Enter some number in list:")
    if inp=='done':break
    value=float(inp)
    numlist.append(value)
avg=sum(numlist)/len(numlist)
print("average",avg)