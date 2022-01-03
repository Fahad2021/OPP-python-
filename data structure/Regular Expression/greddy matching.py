import re
x='From:Using character'
y=re.findall('^F.+?:',x)
print(y)