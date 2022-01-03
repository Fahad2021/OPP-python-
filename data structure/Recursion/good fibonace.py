def good_fibonce(n):
    if n<=1:
        return (n,0)
    else:
        (a,b)=good_fibonce(n-1)
        return (a+b,a)

print(good_fibonce(10))


