class stackedArray:
    def __init__(self):
        self._data=[]
    
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)
    
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        return self._data.pop()

    def top(self):
        if self.isEmpty():
           print("stack is empty")
           return
        return self._data[-1]


s=stackedArray()
s.push(4)
s.push(5)
s.push(6)
s.pop()
print(s._data)
print(len(s))

