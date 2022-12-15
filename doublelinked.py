class Node:
    __slots__="_element","_next","_prev"
    def __init__(self,element,next,prev):
        self._element=element
        self._next=next
        self._prev=prev


class Double:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size==0
    

    def addLast(self,e):
        newest=Node(e,None,None)
        if self.isEmpty():
            self._head=newest
        else:
            self._tail._next=newest
            newest._prev=self._tail 
        self._tail=newest
        self._size+=1
    
    def display(self):
        p=self._head
        while p:
            print(p._element,end=".....>")
            p=p._next
        print()


    def addFirst(self,e):
        newest=Node(e,None,None)
        if self.isEmpty():
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head._next
            self._head._prev=newest
            self._head=newest
        self._size+=1

    def insertElement(self,e,pos):
        newest=Node(e,None,None)
        p=self._head
        i=1
        while i<(pos -1):
            p=p._next
            i+=1
        newest._next=p._next
        p._next._prev=newest
        p._next=newest
        newest._prev=p
        self._size+=1
    
    def delFirst(self):
        self._head=self._head._next
        self._head._prev=None
        self._size-=1
    
    def delEnd(self):
        i=0
        p=self._head
        while i<self._size:
            p=p._next
            i+=1
        self._tail=self._tail._prev
        self._tail._next=None
        self._size-=1


    def delAny(self,pos):
        i=0
        p=self._head
        while i<(pos-1):
            p=p._next
            i+=1
        p._next=p._next._next
        p._next._prev=p
        self._size-=1



            
d=Double()
d.addLast(1)
d.addLast(2)
d.addLast(3)
d.addLast(4)
d.addLast(5)
d.display()