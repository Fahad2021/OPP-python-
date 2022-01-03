d={'a':30,'b':20,'c':50}
t=sorted(d.items())
print(t)

[('a',30),('b',20),('c',50)]
for k,v in sorted(d.items()):
    print(k,v)