class Node:
    __slots__='_element','_next'
    def __init__(self,element,next):
        self._element=element
        self._next=next


class LinkedList:
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
        if self.isEmpty():
            self._head=newest
            # print("head",newest)
        else:
            self._tail._next=newest
            # print("tail",self._tail._next)
        self._tail=newest
        self._size+=1
    
    def display(self):
        p=self._head
        while p:
            print(p._element,end="--->")
            p=p._next
        print()
# searching a element in the linked list....
    def Search(self,key):
        p=self._head
        i=0
        while p:
            if p._element==key:
                return i
            else:
                i=i+1
                p=p._next
        return "element not found..."

# insert the element at the first.
    def addFirst(self,val):
        newest=Node(val,None)
        if self.isEmpty():
            self._head=newest
            self._tail=newest
            
        else:
            newest._next=self._head
            self._head=newest
        self._size+=1

    
# insert element at any where in the list........
    def insertElement(self,e,pos):
        newest=Node(e,None)
        p=self._head
        i=0
        while i<(pos-1):
            p=p._next
            i=i+1
        newest._next=p._next
        p._next=newest
        self._size+=1

    # delete the element at the starting.
    def delFirst(self):
        self._head=self._head._next
    
    # delete the element in any where.
    def removeany(self, position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i = i + 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e


L=LinkedList()
L.addLast(4)
L.addLast(7)
L.addLast(72)
L.addLast(75)
L.addLast(71)
L.display()
L.addFirst(44)
L.display()
print(len(L))
L.insertElement(99,3)
L.display()
print(L.Search(88))
print(len(L))
# L.delFirst()
# L.delFirst()

print(L.removeany(3))
L.display()
