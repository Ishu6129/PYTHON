class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class STACK:
    def __init__(self,top=None):
        self.top=top
        self.s_count=0
    def is_empty(self):
        return self.top is None
    def push(self,data):
        n=Node(data,self.top)
        self.top=n
        self.s_count+=1
    def pop(self):
        if self.top !=None:
            data=self.top.item
            self.top=self.top.next
            self.s_count-=1
            return data
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if self.pop!=None:
            return self.top.item
        else:
            raise IndexError("Stack Underflow")
    def size(self):
        return self.s_count
stk=STACK()
print(stk.is_empty())
stk.push(30)
stk.push(20)
print(stk.peek())
print(stk.size())