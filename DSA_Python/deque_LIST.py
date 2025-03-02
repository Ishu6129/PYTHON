class DEQUE:
    def __init__(self):
        self.mylist=[]
    def is_empty(self):
        return self.mylist==[]
    def insert_front(self,data):
        self.mylist.insert(0,data)
    def insert_rear(self,data):
        self.mylist.append(data)
    def delete_front(self):
        if self.mylist:
            data = self.mylist[0]
            self.mylist.pop(0)
            return data
        else:
            raise IndexError("Deque Empty")
    def delete_rear(self):
        if self.mylist:
            data = self.mylist[-1]
            self.mylist.pop()
            return data
        else:
            raise IndexError("Deque Empty")
    def get_front(self):
        if self.mylist:
            return self.mylist[0]
        else:
            raise IndexError("Deque Empty")
    def get_rear(self):
        if self.mylist:
            return self.mylist[-1]
        else:
            raise IndexError("Deque Empty")
    def size(self):
        return len(self.mylist)
dq=DEQUE()
print(dq.is_empty())
dq.insert_rear(20)
dq.insert_front(10)
dq.delete_front()
dq.delete_rear()
print(dq.get_front())