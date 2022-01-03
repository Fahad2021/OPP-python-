def print_n(s,n):
    if n>=0:
     return
    print(n,s)
    print_n(s,n-1)
print_n(3,20)
