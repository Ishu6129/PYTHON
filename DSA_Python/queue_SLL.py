class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class QUEUE:
    def __init__(self, front=None,rear=None):
        self.front = front
        self.rear = rear
        self.s_count = 0

    def is_empty(self):
        return self.front==None

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.s_count+=1
        self.rear=n

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        elif self.rear==self.front:
            data=self.front.item
            self.front=None
            self.rear=None
        else:
            data=self.front.item
            self.front=self.front.next
        self.s_count-=1
        return data

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue underflow")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue underflow")

    def size(self):
        return self.s_count
que=QUEUE()
print(que.is_empty())
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
print(que.is_empty())
print(que.get_front())
print(que.get_rear())
print(que.dequeue())
print(que.get_front())
print(que.get_rear())
print(que.size())
print(que.dequeue())
print(que.get_front())
print(que.get_rear())
print(que.size())
print(que.dequeue())
try:
    print(que.get_front())
except IndexError as e:
    print(e.args[0])
try:
    print(que.get_rear())
except IndexError as e:
    print(e.args[0])
print(que.size())
print(que.is_empty())
print(que.rear)