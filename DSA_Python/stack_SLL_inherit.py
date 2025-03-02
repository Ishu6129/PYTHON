from SLL import *
class STACK(SLL): # class SLL is inherited
    def __init__(self):
        super().__init__() # calling parent __init__ method
        self.s_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.s_count+=1
    def pop(self):
        if self.start!=None:
            data=self.start.item
            self.delete_first()
            self.s_count -= 1
            return data
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if self.start!=None:
            return self.start.item
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return self.s_count
stk=STACK()
print(stk.is_empty())
stk.push(30)
stk.push(20)
stk.push(10)
print(stk.peek())
print(stk.size())