class QUEUE:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return self.queue == []
    def enqueue(self,data):
        self.queue.insert(-1,data)
    def dequeue(self):
        if self.queue!=[]:
            return self.queue.pop()
        else:
            raise IndexError("Queue underflow")
    def get_front(self):
        if self.queue != []:
            return self.queue[0]
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if self.queue != []:
            return self.queue[-1]
        else:
            raise IndexError("Queue underflow")
    def size(self):
        return len(self.queue)
que=QUEUE()
print(que.is_empty())
que.enqueue(10)
que.enqueue(20)
print(que.is_empty())
print(que.get_front())
print(que.get_rear())
print(que.size())
print(que.dequeue())
print(que.is_empty())
print(que.size())
print(que.dequeue())
print(que.is_empty())
print(que.size())
