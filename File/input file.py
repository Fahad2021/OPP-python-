fahad=input('Enter your file name: ')
file=open(fahad)
count=0
for line in file:
    if line.startswith(""):
        count=count+1
print('there were count',count,'subject in line',fahad)