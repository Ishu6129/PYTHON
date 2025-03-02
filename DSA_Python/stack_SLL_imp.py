from SLL import *
class STACK:
    def __init__(self):
        self.mylist=SLL()
        self.s_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.s_count+=1
    def pop(self):
        if self.mylist.start!=None:
            data=self.mylist.start.item
            self.mylist.delete_first()
            self.s_count -= 1
            return data
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if self.mylist.start!=None:
            return self.mylist.start.item
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