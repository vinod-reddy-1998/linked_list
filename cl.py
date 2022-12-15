class Node:
    __slot__="_element","_next"
    def __init__(self,e,next):
        self._element=e
        self._next=next
    
class circularLinkedList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size
    

    def isEmpty(self):
        return self._size==0
    

    def addLast(self,e):
        newest=Node(e,None)
        p=self._head
        if self.isEmpty():
            newest._next=newest
            self._head=newest
        else:
            newest._next=self._tail._next
            self._tail._next=newest

        self._tail=newest
        self._size+=1
    
    def display(self):
        p=self._head
        i=0
        k=self._size
        print(k)
        while i<len(self):
            print(p._element,end="....>")
            i+=1
            p=p._next
        print()

    def addFirst(self,e):
        newest=Node(e,None)
        if self.isEmpty():
            self._head=newest
            self._head._next=newest
            # newest._next=newest
            # self._head=newest
            self._tail=newest

        else:
            self._tail._next=newest
            newest._next=self._head
            self._head=newest
        self._size+=1
            
    def insertElement(self,pos,e):
        newest=Node(e,None)
        p=self._head
        i=1
        while i<(pos-1):
            p=p._next
            i+=1
        newest._next=p._next
        p._next=newest
        self._size+=1

    def delFirst(self):
        self._tail._next=self._head._next
        self._head=self._head._next
        self._size-=1
    
    def delLast(self):
        l=self._size
        p=self._head
        i=1
        while i<l:
            p=p._next
            i+=1
        p._next=self._head
        self._tail=p
        self._size-=1

    def delany(self,pos):
        p=self._head
        i=1
        while i<(pos-1):
            # print("vinod")
            p=p._next
            # print(p)
            i+=1
        e=p._next._element
        p._next=p._next._next

        print("deleted value is ",e)
        self._size-=1 


c=circularLinkedList()
c.addLast(3)
c.addLast(4)
c.addLast(5)
c.addLast(57)
c.addLast(54)
c.addLast(7)
print("len is ",len(c))
c.addFirst(99)
c.display()
# c.delLast()
c.delany(4)
c.display()

            

