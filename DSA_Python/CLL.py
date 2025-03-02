class Node:
    def __init__(self, item=None, next = None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last is None
    def insert_at_start(self,data):
        n=Node(data)
        if self.last is None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n = Node(data)
        if self.last is None:
            n.next = n
            self.last = n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search_item(self,value):
        if self.last == None:
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == value:
                return temp
            temp = temp.next
        if temp.item==value:
            return temp
        return None

    def insert_item(self,value,data):
        value = self.search_item(value)
        if self.last!=None and value!=None:
            n = Node(data,value.next)
            value.next=n
            if value==self.last:
                self.last=n
    def delete_first(self):
        if self.last is not None:
            if self.last.next != self.last:
                self.last.next = self.last.next.next
            else:
                self.last=None
    def delete_last(self):
        if self.last is not None:
            if self.last.next != self.last:
                if self.last.next.next==self.last:
                    self.last.next.next=self.last.next
                    self.last=self.last.next
                else:
                    temp=self.last.next
                    while temp.next != self.last:
                        temp=temp.next
                    temp.next=self.last.next
                    self.last=temp
            else:
                self.last=None
    def delete_item(self,data):
        if self.last!=None:
            if self.last.next.item==data:
                self.delete_first()
            elif self.last.item==data:
                self.delete_last()
            else:
                temp=self.last.next
                if temp.next.next==self.last:
                    if temp.next.item == data:
                        temp.next=self.last
                else:
                    while temp != self.last:
                        if  temp.next.item == data:
                            break
                        temp=temp.next
                    temp.next=temp.next.next

    def print_item(self):
        if self.last!=None:
            temp=self.last.next
            while temp != self.last:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)
    def __iter__(self):
        if self.last!=None:
            return CLLIterator(self.last.next)
        else:
            return CLLIterator(None)

class CLLIterator:
    def __init__(self, last):
        self.lst = last
        self.current=last
        self.cnt=0
    def __iter__(self):
        return self

    def __next__(self):
        if self.lst == None:
            raise StopIteration
        if self.current==self.lst and self.cnt==1:
            raise StopIteration
        self.cnt=1
        data = self.current.item
        self.current = self.current.next
        return data

mylist=CLL()
mylist.insert_at_start(10)
mylist.insert_item(10,20)
mylist.insert_at_last(30)
mylist.delete_item(50)
mylist.print_item()
for i in mylist:
    print(i)