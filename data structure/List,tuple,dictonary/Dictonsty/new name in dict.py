counts=dict()
names=['fahad','rahat','karim','burcha','fahad']
for name in names:
    if name is not counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)