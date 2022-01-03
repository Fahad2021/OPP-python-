smallest=None
for value in[1,2,3,4,5,6]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print("after smallestr",smallest)