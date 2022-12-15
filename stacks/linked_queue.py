class Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next

class LinkedQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def __len__(self):
        return (self.size)
    
    def isEmpty(self):
        return self.size==0

    def enqueue(self,e):
        newest=Node(e,None)
        if self.isEmpty():
            self.head=newest
        else:
            self.tail._next=newest
        self.tail=newest 
        self.size+=1
    
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return 
        else:
            # print("first out is :",self.head._element)
            e=self.head._element
            self.head=self.head._next
        self.size-=1
        return e
    def display(self):
        p=self.head
        while p:
            print(p._element,end="-->")
            p=p._next
        print()


# lq=LinkedQueue()
# lq.enqueue(1)
# lq.enqueue(2)
# lq.enqueue(3)
# lq.enqueue(4)
# lq.dequeue()
# lq.display()
