class Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next
        
class LinkedStack:
    def __init__(self):
        self._top=None
        self._size=0
    
    def __len__(self):
        return (self._size)
    
    def isEmpty(self):
        return (self._size)==0
    
    def push(self,e):
        newest=Node(e,None)
        if self.isEmpty():
            self._top=newest
        else:
            newest._next=self._top
            self._top=newest
        self._size+=1
    
    def pop(self):
        if self.isEmpty():
            print("list is empty..")
        else:
            print("top element is:",self._top._element)
            self._top=self._top._next
        self._size-=1
    
    def top(self):
        if self.isEmpty():
            print("list is empty..")
        print(self._top._element)
    

    def display(self):
        p=self._top
        while p:
            print(p._element,end="-->")
            p=p._next
        print()


ls=LinkedStack()
ls.push(2)
ls.push(3)
ls.push(4)
ls.push(5)
ls.pop()
ls.top()
ls.display()
print(len(ls))

