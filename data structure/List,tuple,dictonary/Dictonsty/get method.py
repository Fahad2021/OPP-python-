counts=dict()
x=input('some name:')
for name in x:
  counts[name]=counts.get(name,0)+1
print(counts)