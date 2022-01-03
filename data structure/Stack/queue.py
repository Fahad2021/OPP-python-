class queue:
    def __init__(self):
         self.que=[]
        
    def is_empty(self):
        if self.que==[]:
            print("no items here")
        else:
            print("here some items")

    def enqueue(self,item):
        return self.que.append(item)
    
    def dequeue(self):
        return self.que.pop(0)
    
q=queue()
q.enqueue(2)
q.enqueue("fahad")

while not q.is_empty():
    item=q.dequeue()
    print(item)





   