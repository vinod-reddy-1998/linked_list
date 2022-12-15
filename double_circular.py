class Node:
    __slots__='_element',"_prev","_next"
    def __init__(self,element,prev,next):
        self._element=element
        self._prev=prev
        self._next=next
    
class DoubleCircular:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def addLast(self,element):
        newest=Node(element,None,None)
        if self.isEmpty():
            newest._next=self.head
            self.head=newest
            self.head._prev=self.tail
            
        else:
            newest._next=self.tail._next
            self.tail._next=newest
            newest._prev=self.tail
        self.tail=newest
        self.size+=1
    def addFirst(self,element):
        newest=Node(element,None,None)
        if self.isEmpty():
            newest._next=self.head
            self.head=newest
            newest._prev=self.head
        else:
            newest._next=self.head
            self.head=newest
            self.head._prev=self.tail._next
        self.tail=newest
        self.size+=1
    

    def delFirst(self):
        self.tail._next=self.head._next
        self.head=self.head._next
        self.head._prev=self.tail
        self.size-=1

    def delLast(self):
        p=self.head
        i=1
        while i<len(self):
            # print(p._element)
            p=p._next
            i+=1
        self.head._prev=p._next
        p._next=self.head
        self.size-=1
    
    def insertAt(self,element,pos):
        newest=Node(element,None,None)
        if pos>len(self):
            print("please lower the position")
        else:
            p=self.head
            i=1
            while i<(pos-1):
                print(p._element)
                p=p._next
                i+=1
            newest._next=p._next
            p._next=newest
            newest._prev=p
            self.size+=1
    def deleteAny(self,pos):
        p=self.head
        i=1
        while i<(pos-1):
            p=p._next
            i+=1
        p._next=p._next._next
        p._next._prev=p
        self.size-=1

    def display(self):
        p=self.head
        i=0
        while i<len(self):
            print(p._element,end="--->>")
            p=p._next
            i+=1
        print()


dc=DoubleCircular()
dc.addLast(1)
dc.addLast(2)
dc.addLast(3)
dc.addLast(4)
dc.addLast(5)
dc.display()
print("*"*20)
dc.delFirst()
dc.display()
dc.delLast()
dc.display()
dc.insertAt(23,2)
dc.display()
dc.deleteAny(2)
dc.display()
    


