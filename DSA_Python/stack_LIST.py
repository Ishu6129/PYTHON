class STACK:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return self.stack == []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.stack!=[]:
            return self.stack.pop()
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return len(self.stack)
stk=STACK()
print(stk.size())
print(stk.is_empty())
stk.push(20)
stk.push(10)
print(stk.peek())
print(stk.size())
print(stk.is_empty())
