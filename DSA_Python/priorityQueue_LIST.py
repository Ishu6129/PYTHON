class PriorityQueue:
    def __init__(self):
        self.mylist=[]
    def is_empty(self):
        return self.mylist==[]
    def push(self,data,priority):
        index=0
        while index < len(self.mylist) and self.mylist[index][1]<=priority:
            index+=1
        self.mylist.insert(index,(data,priority))
    def pop(self):
        if self.mylist:
            return self.mylist.pop(0)[0]
        else:
            raise IndexError("Empty")
    def size(self):
        return len(self.mylist)
pr_queue=PriorityQueue()
pr_queue.push(801,1)
pr_queue.push(205,5)
pr_queue.push(603,3)
pr_queue.push(904,4)
pr_queue.push(102,2)
while not pr_queue.is_empty():
    print(pr_queue.pop())