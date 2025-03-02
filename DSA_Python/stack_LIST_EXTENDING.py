class STACK(list):
    def is_empty(self):
        return self == []
    def push(self,data):
        self.append(data)
    def pop(self):
        if self!=[]:
            return super().pop()
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if self != []:
            return self[-1]
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No 'insert' attribute in Stack")
stk=STACK()
print(stk.size())
print(stk.is_empty())
stk.push(20)
stk.push(10)
print(stk.peek())
print(stk.size())
print(stk.is_empty())
stk.insert(1,20)