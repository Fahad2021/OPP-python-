class Stack:
    def __init__(self):
        self.stack=[]
    
    def add(self,val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:False

    def remove(self):
        if len(self.stack)<=0:
            return "No elements in stack"
        else:
            return self.stack.pop()

objstc=Stack()
objstc.add(4)
objstc.add(4)
objstc.add(9)

print(objstc.remove())
