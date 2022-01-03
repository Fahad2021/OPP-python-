import re
x='my 2choice number 12 to 96'
y=re.findall('[12-96]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)