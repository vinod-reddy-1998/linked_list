class QueueArray:
    def __init__(self):
        self.data=[]
    
    def __len__(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data)==0
    
    def enqueue(self,e):
        self.data.append(e)
    
    def dequeue(self):
        if self.isEmpty():
            print("list is empty..")
        else:
            self.data.pop(0)
    
    def first(self):
        if self.isEmpty():
            print("list is empty..")
            return
        return self.data[0]

q=QueueArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.data)


    
