def quicsort(arr):
    if len(arr)<=1:
         return arr
    mid=arr[len[arr]//2]
    left=[x for x in arr if x<mid]
    middle=[x for x in arr if x==mid]
    right=[x for x in arr if x>mid]
    return quicsort(left)+quicsort(middle)+quicsort(right)


print(quicsort([1, 4, 6, 7, 5, 6, 4]))
