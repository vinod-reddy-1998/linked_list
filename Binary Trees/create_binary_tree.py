import sys
sys.path.append("..")
from stacks.linked_queue import LinkedQueue

class Node:
    __slots__="_left","_element","_right"
    def __init__(self,element,left=None,right=None):
        self._left=left
        self._element=element
        self._right=right
    
class BinaryTree:
    def __init__(self):
        self._root=None

    def makeTree(self,e,left,right):
        self._root=Node(e,left._root,right._root)
    
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=" ")
            self.inorder(troot._right)
    
    def preorder(self,troot):
        if troot:
            print(troot._element,end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)
    
    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element,end=" ")

    def levelOrder(self):
        Q=LinkedQueue()
        t=self._root
        print(t._element,end=" ")
        Q.enqueue(t)
        while not Q.isEmpty():
            t=Q.dequeue()
            if t._left:
                print(t._left._element,end=" ")
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element,end=" ")
                Q.enqueue(t._right)
            
            
    def count(self,troot):
        if troot:
            x=self.count(troot._left)
            y=self.count(troot._right)
            return x+y+1
        return 0
    
    def height(self,troot):
        if troot:
            x=self.height(troot._left)
            y=self.height(troot._right)
            if x>y:
                return x+1
            else:
                return y+1
        return 0

    



x=BinaryTree()
y=BinaryTree()
z=BinaryTree()
a=BinaryTree()
r=BinaryTree()
s=BinaryTree()
t=BinaryTree()
# x.makeTree(20,a,a)
# y.makeTree(30,a,a)
# z.makeTree(10,x,y)
# print("\n inorder transversal")
# z.inorder(z._root)
# print("\n preorder transversal")
# z.preorder(z._root)
# print("\n postorder transversal")
# z.postorder(z._root)
x.makeTree(40,a,a)
y.makeTree(60,a,a)
z.makeTree(20,x,a)
r.makeTree(50,a,y)
s.makeTree(30,r,a)
t.makeTree(10,z,s)
print("\n inorder transversal")
t.inorder(t._root)
print("\n preorder transversal")
t.preorder(t._root)
print("\n postorder transversal")
t.postorder(t._root)
print()
print("\n level order")
t.levelOrder()
c=t.count(t._root)
print("\n the count is ",c)
print(".........",t.height(t._root))
