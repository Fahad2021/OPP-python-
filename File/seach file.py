fahad=open("file.txt")
for line in fahad:
    line=line.rstrip()
    if not  'uct.ac.za' in line:
       continue
print(line)