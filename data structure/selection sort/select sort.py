list=[1,3,5,0,2,34,13,45]
for i in range (len(list)):
    smallest_val=min(list[i:])
    samllest_index=list.index(smallest_val)
    list[i],list[samllest_index]=list[samllest_index],list[i]

print(list)
