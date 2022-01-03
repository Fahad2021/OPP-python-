class Queue:
    def __init__(self,size):
        self.items=[0]*size
        self.max_size=size
        self.head,self.tail,self.size=0,0,0
    
    def enqueue(self,item):
        if self.is_full():
            print("queue is full")
            return

        print("Inserting Item",item)
        self.items[self.tail]=item
        self.tail=(self.tail+1)%self.max_size
        self.size+=1
    
    def dqueue(self):
        item=self.items[self.head]
        self.head=(self.head+1)%self.max_size

        return item
    
    def is_empty(self):
        if self.size==0:
            return("Queue is empty")
        return("no empty")
    
    def is_full(self):
        if self.size==self.max_size:
            return True
        return False

    def remove(self):
        return self.items.pop(0)


q=Queue(10)
q.enqueue(9)
q.enqueue(8)
q.enqueue(5)
q.enqueue(4)
q.remove()
q.remove()

while not q.is_empty():
     itm=q.dequeue()
     print(itm)

print(q.items)
print("head",q.head)
print("tail",q.tail)


        
        