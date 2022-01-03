class stack:
    def __init__(self):
        self.item=[]

    def size(self):
        print( "stack size is:",len(self.item))

    def is_empty(self):
        if(self.item==[]):
          print("Stack is emty")
        else:
            print("Not empty")

    def push(self,items):
        self.item.insert(0,items)

    def pop(self):
         return self.item.pop()

s=stack()
s.push(1)
s.push(3)
s.push(7)
s.size()

while not s.is_empty():
    ele=s.pop(5)
    print(ele)







