class Node:
    def __init__(self,item=None,priority=None,next= None):
        self.item=item
        self.priority=priority
        self.next=next
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.s_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.s_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty")
        data=self.start.item
        self.start=self.start.next
        self.s_count -= 1
        return data
    def size(self):
        return self.s_count

pr_queue=PriorityQueue()
pr_queue.push(801,1)
pr_queue.push(205,5)
pr_queue.push(603,3)
pr_queue.push(904,4)
pr_queue.push(102,2)
while not pr_queue.is_empty():
    print(pr_queue.pop())
