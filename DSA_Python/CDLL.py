class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev = prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.start==None:
            n.prev=n
            n.next=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n = Node(data)
        if self.start == None:
            n.prev = n
            n.next = n
            self.start=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n

    def search_item(self,data):
        if self.start==None:
            return None
        temp=self.start
        if temp.item==data:
            return temp
        temp=temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_item(self,temp,data):
        n=Node(data)
        temp=self.search_item(temp)
        if temp:
            if temp == self.start.prev:
                self.insert_at_last(data)
            else:
                n.prev=temp
                n.next=temp.next
                temp.next.prev=n
                temp.next=n
    def delete_first(self):
        if self.start:
            if self.start==self.start.next:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next

    def delete_last(self):
        if self.start:
            if self.start == self.start.next:
                self.start = None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

    def delete_item(self,data):
        temp=self.search_item(data)
        if temp:
            if temp.next==self.start:
                self.delete_last()
            elif temp==self.start:
                self.delete_first()
            else:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
    def print_item(self):
        if self.start!=None:
            temp=self.start
            print(temp.item,end=" ")
            temp=temp.next
            while temp != self.start:
                print(temp.item,end=" ")
                temp=temp.next
            print()
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.cnt=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        elif self.current == self.start and self.cnt==1:
            raise StopIteration
        self.cnt=1
        data = self.current.item
        self.current = self.current.next
        return data

mylist=CDLL()
mylist.print_item()
for i in mylist:
    print(i)
