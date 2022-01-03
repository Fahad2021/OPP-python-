
xfile=open('file.txt')
count=0
for sent in xfile:
   for line in xfile:
    count=count+1
print("line count:",len(sent),count)

