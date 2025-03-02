class Node:
    def __init__(self, item=None,prev=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DEQUE:
    def __init__(self):
        self.front=None
        self.rear=None
        self.s_count=0

    def is_empty(self):
        return self.front == None

    def insert_front(self, data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front = n
        self.s_count+=1

    def insert_rear(self, data):
        n = Node(data, self.rear,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.s_count += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque empty")
        if self.s_count==1:
            self.front=None
            self.rear=None
        else:
            self.front = self.front.next
            self.front.prev=None
        self.s_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque empty")
        if self.s_count == 1:
            self.front = None
            self.rear = None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.s_count -= 1
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque empty")
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque empty")
        return self.rear.item
    def size(self):
        return self.s_count
dq=DEQUE()
dq.insert_front(10)
dq.insert_rear(20)
print(dq.size())
print(dq.get_front())
dq.delete_front()
print(dq.get_front())