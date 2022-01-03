def bad_fibonce(n):
    if n<=1:
        return n
    else:
        return bad_fibonce(n-2)+bad_fibonce(n-1)
print(bad_fibonce(7))


