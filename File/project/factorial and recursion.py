def fact(n):
    if n==0:
     return 1
    else:
        recur=fact(n-1)
        result=n*recur
        return result
print(fact(16))
